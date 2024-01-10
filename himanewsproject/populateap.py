import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','himanewsproject.settings')
import django
django.setup()

from testapp.models import Apjobs
from faker import Faker
from random import *
fake=Faker()

def phonenumber():
    d1 = randint(6,9)
    num = '' + str(d1)
    for i in range(9):
        num += str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project manager','Team leader','Software engineer','Associate engeneer','Python web developer'))
        feligibility = fake.random_element(elements=('Btech','Mtech','Mca','Phd','Mahesh sir'))
        faddress = fake.address()
        femail = fake.email()
        fnumber = phonenumber()
        Apjobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            number=fnumber,
        )
n=int(input('Enter number of records:'))
populate(n)
print(f'{n}records inserted successfully ....')