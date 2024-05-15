import datetime
from dataclasses import dataclass

@dataclass
class Person:
    firstname: str
    lastname: str
    birthday: datetime.date

    def __init__(self, firstname:str, lastname:str, birthday:str|datetime.date):
        self.firstname = firstname
        self.lastname = lastname
        if isinstance(birthday, datetime.date):
            self.birthday = birthday
        else:
            self.birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d').date()

    @property
    def name(self):
        "Return the full name of the person."
        return f"{self.lastname}, {self.firstname}"

    def get_age(self, day:datetime.date=datetime.date.today()):
        """Return the age of the person in years.

        If the optional argument `day` is given, the age is calculated at that day.
        """
        age = day - self.birthday
        # this is not 100% correct, but good enough for this example
        # for a more precise calculation you could install the `dateutil` package and use the `relativedelta` function
        return age.days // 365
    

