from faker import Faker 
import pandas as pd

faker = Faker()
num_employees = 50

def create_employees(num_employees):
  employees = []
  for _ in range(num_employees):
    employee = {}
    employee['First Name'] = faker.first_name()
    employee['Last Name'] = faker.last_name()
    employee['Company'] = faker.random_element(elements=("Brandon Consulting", "InteliClear LLC"))
    employee["Department"] = faker.random_element(elements=("Marketing", "Finance", "Asset Advisor", "Accounting", "Compliance", "Banking"))
    employee['Role'] = faker.random_element(elements=("CTO", "Stock Analyst", " Investment Banker ", "Consultant", "Intern", "IT Department", "Financial Advisors"))
    employee["Desk Number"] = faker.random_int(min = 0, max = 25, step = 1)
    employee['Salary($)'] = faker.random_int(min=50000, max=550000, step=2000)
    employee['SSN'] = faker.ssn()
    employee['Email'] = faker.email()
    employee['Phone'] = faker.phone_number()
    employee['Address'] = faker.address()
    employees.append(employee)
  return employees

employee_list = create_employees(num_employees)
df = pd.DataFrame(employee_list)
print(df)
