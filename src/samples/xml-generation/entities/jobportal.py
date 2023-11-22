import xml.etree.ElementTree as ET
from entities.role import Role

class JobPortal:

    def __init__(self, jobPortal, jobDescription, jobTitle, experience, workType, qualifications, skills, preference, jobPostingDate, personId):
        JobPortal.counter += 1
        self._id = JobPortal.counter
        self._jobPortal = jobPortal
        self._jobDescription = jobDescription
        self._jobTitle = jobTitle
        self._experience = experience
        self._workType = workType
        self._qualifications = qualifications
        self._skills = skills
        self._preference = preference
        self._jobPostingDate = jobPostingDate
        self._personId = personId
        self._roles = []

    def add_role(self, role: Role):
        self._roles.append(role)

    def to_xml(self):
        el = ET.Element("JobPortal")
        el.set("id", str(self._id))
        el.set("jobPortal", self._jobPortal)
        el.set("jobDescription", self._jobDescription)
        el.set("jobTitle", self._jobTitle)
        el.set("experience", self._experience)
        el.set("workType", self._workType)
        el.set("qualifications", self._qualifications)
        el.set("skills", self._skills)
        el.set("preference", self._preference)
        el.set("jobPostingDate", self._jobPostingDate)
        el.set("person_ref", str(self._personId.get_id()))

        roles_el = ET.Element("roles")
        for role in self._roles:
            roles_el.append(role.to_xml())

        el.append(roles_el)
        

        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"person_ref: {self._personId}, jobPostingDate:{self._jobPostingDate}, preference: {self._preference}, skills:{self._skills}, qualifications: {self._qualifications}, workType: {self._workType}, experience: {self._experience}, jobTitle:{self._jobTitle}, jobDescription: {self._jobDescription}, jobPortal: {self._jobPortal}, id:{self._id}"


JobPortal.counter = 0
