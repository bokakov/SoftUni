company_employees = {}

while True:
    command = input()
    if command == "End":
        break
    arguments = command.split(" -> ")
    name_of_company = arguments[0]
    employee_id = arguments[1]

    if name_of_company not in company_employees:
        company_employees[name_of_company] = []

    if employee_id not in company_employees[name_of_company]:
        company_employees[name_of_company].append(employee_id)

for company, employees in company_employees.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
