import xml.etree.ElementTree as ET


class JobPortal:

    def __init__(self, jobPortal, jobDescription, jobTitle, experience, workType, qualification, skills, preference, postingDate, personId):
        JobPortal.counter += 1
        self._id = JobPortal.counter
        self._jobPortal = jobPortal
        self._jobDescription = jobDescription
        self._jobTitle = jobTitle
        self._experience = experience
        self._workType = workType
        self._qualification = qualification
        self._skills = skills
        self._preference = preference
        self._postingDate = postingDate
        self._personId = personId

    def to_xml(self):
        el = ET.Element("JobPortal")
        el.set("id", str(self._id))
        el.set("jobPortal", self._jobPortal)
        el.set("jobDescription", self._jobDescription)
        el.set("jobTitle", self._jobTitle)
        el.set("experience", self._experience)
        el.set("workType", self._workType)
        el.set("qualification", self._qualification)
        el.set("skills", self._skills)
        el.set("preference", self._preference)
        el.set("postingDate", self._postingDate)
        el.set("person_ref", str(self._personId.getid()))

        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"person_ref: {self._personId}, postingDate:{self._postingDate}, preference: {self._preference}, skills:{self._skills}, qualifications: {self._qualification}, workType: {self._workType}, experience: {self._experience}, jobTitle:{self._jobTitle}, jobDescription: {self._jobDescription}, jobPortal: {self._jobPortal}, id:{self._id}"


JobPortal.counter = 0
