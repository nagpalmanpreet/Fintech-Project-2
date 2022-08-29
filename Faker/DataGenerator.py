from faker import Faker
from faker.providers import BaseProvider
from datetime import datetime
import random
import csv

class IndustryProvider(BaseProvider):
    def industry(self):
        return random.choice(['IT', 'Finance', 'Health'])

class ZipCodeProvider(BaseProvider):
    def zipCode(self):
        return random.choice(['3000', '3185', '3021', '2000'])

class BooleanProvider(BaseProvider):
    def booleanGenerate(self):
        #return random.choice(['0', '1'])
        return (1)


fake = Faker('en_AU')

fake.add_provider(IndustryProvider)
fake.add_provider(ZipCodeProvider)
fake.add_provider(BooleanProvider)


def get_monthly_revenue():
    return random.randrange(0, 8000)


def min_operating_period():
    return random.randrange(1, 15)

def loanAmt():
    return random.randrange(10000, 20000)

def businessHistory():
    return random.randrange(0, 1)

def isDefault():
    return (1)

def hasProperty():
    return random.randrange(0,1)

def hasOtherLoan():
    return random.randrange(0,1)

def cash():
    return random.randrange(10000,200000)

def directorAge():
    return random.randrange(25,40)

def taxReturn():
    return random.randrange(0,100000)

def generate_loanData():
    return [get_monthly_revenue(), min_operating_period(), loanAmt(),businessHistory(), fake.industry(),fake.postcode(),fake.booleanGenerate(),fake.booleanGenerate(),cash(),directorAge(),taxReturn(),fake.booleanGenerate()]

with open('../Resources/loan_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['monthly_revenue', 'min_operating_period', 'loanAmt', 'businessHistory', 'industry', 'zipCode','hasProperty','otherLoan','cash','directorAge','taxReturn','isDefault'])
    for n in range(1, 20):
        writer.writerow(generate_loanData())
