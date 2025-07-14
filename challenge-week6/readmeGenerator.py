from questions import i1
from questions import LicenseAnswer


""""---------- CREATING README ----------"""
class creatingReadme:
    def __init__ (self, title, description, installation, usage, author, license, email, phone):
        self.title = title
        self.description = description
        self.installation = installation
        self.usage = usage
        self.author = author
        self.license = license
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"""###{self.title}

##Description

{self.description}


##Installation Instructions

{self.installation}


##Usage Information

{self.usage}


##Author Name

{self.author}


##License Type

{self.license}


##Contact Information

#Email Address **<ins>{self.email}</ins>**
#Phone Number **<ins>{self.phone}</ins>**
  """
a = creatingReadme(i1.title, i1.description, i1.installation, i1.usage, i1.author, {LicenseAnswer}, i1.email, i1.phone)