from InquirerPy import inquirer
from rich.console import Console
from InquirerPy import prompt

console = Console()

""""----------QUESTIONS----------"""
questions = [
    {"type": "input", "name": "title", "message": "What is the title of your project?"},
    {"type": "input", "name": "description", "message": "Give me a description of your project:"},
    {"type": "input", "name": "installation", "message": "Give me step-by-step instructions on installation to run your project:"},
    {"type": "input", "name": "usage", "message": "Give me all relevant usage information for your project:"},
    {"type": "input", "name": "author", "message": "Who is the author of the project?:"},
    {"type": "input", "name": "email", "message": "Contact Info: Your Email Address?"},
    {"type": "input", "name": "phone", "message": "Contact Info: Your Phone Number?"},
]

LicenseAnswer = inquirer.select(message="Select one:", choices=[
    "MIT License", "Apache License 2.0", "GNU GPL v3", "BSD 3-Clause License", "Unlicensed"
    ]).execute()
answers = prompt(questions)

""""----------PROCESSING ANSWERS----------"""
class inputQuestions:
    def __init__(self, title, description, installation, usage, author, email, phone):
        self.title = title
        self.description = description
        self.installation = installation
        self.usage = usage
        self.author = author
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.title}, {self.description}, {self.installation}, {self.usage}, {self.author}, {self.email}, {self.phone}"

i1 = inputQuestions(answers["title"], answers["description"], answers["installation"], answers["usage"], answers["author"], answers["email"], answers["phone"])
