import xml.etree.ElementTree as ET

from entities.player import Player


class Company:

    def __init__(self, companyProfile, companySize):
        Company.counter += 1
        self._id = Company.counter
        self._companyProfile = companyProfile
        self._companySize = companySize

    def add_player(self, player: Player):
        self._players.append(player)

    def to_xml(self):
        el = ET.Element("Company")
        el.set("id", str(self._id))
        el.set("companyProfile", self._companyProfile)
        el.set("companySize", self._companySize)

        players_el = ET.Element("Players")
        for player in self._players:
            players_el.append(player.to_xml())

        el.append(players_el)

        return el

    def __str__(self):
        return f"{self._name} ({self._id})"


Company.counter = 0
