import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from csv_reader import CSVReader
from entities.country import Country
from entities.team import Team
from entities.player import Player

from lxml import etree


class CSVtoXMLConverter:

    def __init__(self, path, schema_path):
        self._reader = CSVReader(path)
        self._schema_path = schema_path

    def to_xml(self):
        # read countries
        countries = self._reader.read_entities(
            attr="nationality",
            builder=lambda row: Country(row["nationality"])
        )

        # read teams
        teams = self._reader.read_entities(
            attr="Current Club",
            builder=lambda row: Team(row["Current Club"])
        )

        # read players

        def after_creating_player(player, row):
            # add the player to the appropriate team
            teams[row["Current Club"]].add_player(player)

        self._reader.read_entities(
            attr="full_name",
            builder=lambda row: Player(
                name=row["full_name"],
                age=row["age"],
                country=countries[row["nationality"]]
            ),
            after_create=after_creating_player
        )

        # generate the final xml
        root_el = ET.Element("Football")

        teams_el = ET.Element("Teams")
        for team in teams.values():
            teams_el.append(team.to_xml())

        countries_el = ET.Element("Countries")
        for country in countries.values():
            countries_el.append(country.to_xml())

        root_el.append(teams_el)
        root_el.append(countries_el)

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()

    # ------- Validar
    def validate_xml(self, xml_str):
        schema = etree.XMLSchema(file=self._schema_path)
        xml_parser = etree.XMLParser(schema=schema)

        try:
            etree.fromstring(xml_str, xml_parser)
            print("XML is valid against the schema.")
        except etree.XMLSyntaxError as e:
            print("XML is not valid against the schema.")
            print(e)

    def to_xml_str_and_validate(self):
        xml_str = self.to_xml_str()
        self.validate_xml(xml_str)
        return xml_str
