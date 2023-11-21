import xml.etree.ElementTree as ET


class Role:

    def __init__(self, salaryRange, responsabilities, jobPortal):
        Role.counter += 1
        self._id = Role.counter
        self._salaryRange = salaryRange
        self._responsabilities = responsabilities
        self._jobPortal = jobPortal

    def to_xml(self):
        el = ET.Element("Role")
        el.set("id", str(self._id))
        el.set("salaryRanges", self._salaryRange)
        el.set("responsabilities", self._responsabilities)
        el.set("jobPortal_ref", str(self._jobPortal.getid()))

        
        return el

    def __str__(self):
        return f"salaryRange:{self._salaryRange}, responsabilities:{self._responsabilities}, jobPortal:{self._jobPortal}"


Role.counter = 0
