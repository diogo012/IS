import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from csv_reader import CSVReader
from entities.country import Country
from entities.company import Company
from entities.role import Role
from entities.jobportal import JobPortal
from entities.person import Person
from entities.job import Job

from lxml import etree


class CSVtoXMLConverter:

    def __init__(self, path, schema_path):
        self._reader = CSVReader(path)
        self._schema_path = schema_path

    def to_xml(self):
        # read countries
        countries = self._reader.read_entities(
            attr="Country",
            builder=lambda row: Country(
                country = row["Country"],
                location = row["location"],
                latitude = row["latitude"],
                longitude = row["longitude"]
            )
        )

        # read person
        persons = self._reader.read_entities(
            attr="Contact Person",
            builder=lambda row: Person(
                contactPerson = row["Contact Person"],
                contact = row["Contact"]
            )
        )

        # read jobportal
        jobportals = self._reader.read_entities(
            attr="Job Portal",
            builder=lambda row: JobPortal(
                jobPortal = row["Job Portal"]
            )
        )


        # read company
        companies = self._reader.read_entities(
            attr="Company",
            builder=lambda row: Company(
                company = row["Company"],
                companySize = row["Company Size"],
                benefits = row["Benefits"],
                country = countries[row["Country"]]
            )
        )

        # read roles
        roles = self._reader.read_entities(
            attr="Role",
            builder=lambda row: Role(
                role=row["Role"],
                salaryRange=row["Salary Range"],
                responsabilities=row["Responsibilities"],
                company=companies[row["Company"]]
            )
        )

        # read role
        def after_creating_job(job, row):
            # add the role to the appropriate company
            jobportals[row["Job Portal"]].add_job(job)

        self._reader.read_entities(
            attr="Job Title",
            builder=lambda row: Job(
                jobTitle=row["Job Title"],
                jobDescription=row["Job Description"],
                experience=row["Experience"], 
                workType=row["Work Type"],    
                qualifications=row["Qualifications"],  
                skills=row["skills"],
                preference=row["Preference"],
                jobPostingDate=row["Job Posting Date"],
                personId=persons[row["Contact Person"]],
                role=roles[row["Role"]]
            ),
            after_create=after_creating_job
        )

        # generate the final xml
        root_el = ET.Element("Jobs")

        jobportals_el = ET.Element("JobPortals")
        for jobportal in jobportals.values():
            jobportals_el.append(jobportal.to_xml())

        companies_el = ET.Element("Companies")
        for company in companies.values():
            companies_el.append(company.to_xml())
        
        countries_el = ET.Element("Countries")
        for country in countries.values():
            countries_el.append(country.to_xml())

        roles_el = ET.Element("Roles")
        for role in roles.values():
            roles_el.append(role.to_xml()) 

        persons_el = ET.Element("Persons")
        for person in persons.values():
            persons_el.append(person.to_xml()) 

        root_el.append(jobportals_el)
        root_el.append(companies_el)
        root_el.append(countries_el)
        root_el.append(roles_el)
        root_el.append(persons_el) 

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode() 
        dom = md.parseString(xml_str)
        return dom.toprettyxml() 
    #Escrever para ficheiro xml
    def write_to_xml_file(self, output_file):
        xml_tree = self.to_xml()
        xml_str = ET.tostring(xml_tree, encoding='utf8', method='xml').decode()
        with open(output_file, 'w') as file:
            file.write(xml_str)
 
    # ------- Validar
    def validate_xml(self, xml_str, output_file):
        schema = etree.XMLSchema(file=self._schema_path)
        xml_parser = etree.XMLParser(schema=schema)

        try:
            etree.fromstring(xml_str, xml_parser)
            print("XML is valid against the schema.")
            self.write_to_xml_file(output_file)
        except etree.XMLSyntaxError as e:
            print("XML is not valid against the schema.")
            print(e)

    def to_xml_str_and_validate(self, output_file):
        xml_str = self.to_xml_str()
        self.validate_xml(xml_str, output_file)
        """ return xml_str """
