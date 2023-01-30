import Exercise_11_01


class ShiftSupervisor(Exercise_11_01.Employee):

    def __init__(self, employee_name, employee_number, annual_salary, bonus):

        Exercise_11_01.Employee.__init__(self, employee_name, employee_number)
        self.__annual_salary = annual_salary
        self.__bonus = bonus

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def get_bonus(self):
        return self.__bonus


def main():
    print('Shift Supervisor Employee Data:')
    employee_name = input('Employee Name: ')
    employee_number = int(input('Employee Number: '))
    annual_salary = input('Annual Salary: $')
    bonus = input('Yearly Bonus: $')

    shift_supervisor = ShiftSupervisor(employee_name, employee_number, annual_salary, bonus)

    print('\nHere is the data you entered for the shift supervisor:')
    print(f'Name: {shift_supervisor.get_employee_name()}')
    print(f'Employee Number: {shift_supervisor.get_employee_number()}')
    print(f'Annual Salary: ${shift_supervisor.get_annual_salary():}')
    print(f'Yearly Bonus: ${shift_supervisor.get_bonus():}')


if __name__ == '__main__':
    main()
