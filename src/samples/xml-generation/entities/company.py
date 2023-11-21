import xml.etree.ElementTree as ET

from entities.role import Role


class Company:

    def __init__(self, company, companyProfile, companySize, benefits):
        Company.counter += 1
        self._id = Company.counter
        self._company = company
        self._companyProfile = companyProfile
        self._companySize = companySize
        self._benefits = benefits
        self._roles = []

    def add_role(self, role: Role):
        self._roles.append(role)

    def to_xml(self):
        el = ET.Element("Company")
        el.set("id", str(self._id))
        el.set("company", self._company)
        el.set("companyProfile", self._companyProfile)
        el.set("companySize", self._companySize)
        el.set("benefits", self._benefits)

        roles_el = ET.Element("roles")
        for role in self._roles:
            roles_el.append(role.to_xml())

        el.append(roles_el)

        return el

    def __str__(self):
        return f"{self._benefits} {self._companySize} {self._companyProfile} {self._company} ({self._id})"


Company.counter = 0
