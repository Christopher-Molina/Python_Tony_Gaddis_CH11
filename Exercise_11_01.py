class Employee:

    # The __init__ method initializes the data attributes
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    # The following are mutator methods for the data attributes
    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

    # The following are accessor methods for the data attributes
    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number


class ProductionWorker(Employee):
    # The __init__ method initializes the data attributes
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):

        # Call the superclass __init__ method
        Employee.__init__(self, employee_name, employee_number)

        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    # The following are mutator methods for the data attributes
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    # The following are accessor methods for the data attributes
    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate


def main():
    print('Production Worker Employee:')
    employee_name = input('Name: ')
    employee_number = int(input('Employee Number: '))
    shift_number = int(input('Shift Number (1 = Day, 2 = Night): '))
    hourly_pay_rate = input('Hourly Pay Rate: $')

    # Create an object of the ProductionWorker class
    production_worker = ProductionWorker(employee_name, employee_number, shift_number, hourly_pay_rate)

    # Display data
    print('\nHere is the data you entered for the production worker:')
    print(f'Name: {production_worker.get_employee_name()}')
    print(f'Employee Number: {production_worker.get_employee_number()}')
    print(f'Shift Number (1 = Day, 2 = Night): {production_worker.get_shift_number()}')
    print(f'Hourly Pay Rate: ${production_worker.get_hourly_pay_rate()}')


# Call the main function
if __name__ == '__main__':
    main()
