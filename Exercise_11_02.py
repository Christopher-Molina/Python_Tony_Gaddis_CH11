class Person:

    # The __init__ method initializes the data attributes
    def __init__(self, name, address, tel):
        self.__name = name
        self.__address = address
        self.__tel = tel

    # The following are mutator methods for the data attributes
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_tel(self, tel):
        self.__tel = tel

    # The following are accessor methods for the data attributes
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_tel(self):
        return self.__tel


class Customer(Person):

    # The __init__ method initializes the data attributes
    def __init__(self, name, address, tel, cust_number, mailing_list):

        Person.__init__(self, name, address, tel)

        self.__cust_number = cust_number
        self.__mailing_list = mailing_list

    # The following is a mutator and accessor method for the customer_number attribute
    def set_cust_number(self, cust_number):
        self.__cust_number = cust_number

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

    def get_cust_number(self):
        return self.__cust_number

    def get_mailing_list(self):
        return self.__mailing_list


def main():
    try:
        name = input('Enter customer\'s name: ')
        tel = input('Enter customer\'s telephone number: ')
        address = input('Enter customer\'s address: ')
        cust_number = int(input('Enter customer number: '))
        mail = input('Include in Mailing List? (Y/N): ').upper()
        mailing_list = None

        if mail in {'Y', 'N', 'YES', 'NO'}:
            if mail == 'Y' or mail == 'YES':
                mailing_list = True
            else:
                mailing_list = False

        # Create instance of customer
        customer = Customer(name, tel, address, cust_number, mailing_list)

        # Display customer information
        print('----------------------------')
        print(f'Name: {customer.get_name()}')
        print(f'Tel: {customer.get_tel()}')
        print(f'Address: {customer.get_address()}')
        print(f'Customer Number: {customer.get_cust_number()}')
        print(f'On Mailing List: {customer.get_mailing_list()}')
    except (IOError, TypeError, ValueError, Exception) as e:
        print(e)


# Call the main function
if __name__ == '__main__':
    main()
