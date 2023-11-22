import xml.etree.ElementTree as ET


class Role:

    def __init__(self, role, salaryRange, responsabilities, company):
        Role.counter += 1
        self._id = Role.counter
        self._role = role
        self._salaryRange = salaryRange
        self._responsabilities = responsabilities
        self._company = company

    def to_xml(self):
        el = ET.Element("Role")
        el.set("id", str(self._id))
        el.set("role", self._role)
        el.set("salaryRanges", self._salaryRange)
        el.set("responsabilities", self._responsabilities)
        el.set("company_ref", str(self._company.get_id()))
        return el

    def __str__(self):
        return f"role:{self._role}, salaryRange:{self._salaryRange}, responsabilities:{self._responsabilities}, company:{self._company}"


Role.counter = 0
