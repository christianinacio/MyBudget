from Data import Data
from Validations import Validation
from models.Operation import Operation
import datetime
import os

class Interface:

    @classmethod
    def options(self):
        print("### MY BUDGET #### \n")
        Data.connect()
        Data.create_tables()
        print("1. Add operation")
        print("2. Statistic")
        print("4. Exit \n ")
        return input("Enter option: ")
    
    @classmethod
    def StatisticMenu(self):
        print("2. Statistic:")
        print("   |->  1. Monthly Operation")
        print("   |->  2. Totals")
        print("   |->  3. Cash Operation")
        print("   |->  4. Monthly Expenses")
        print("   |->  5. Back \n ")
        option = input("Enter option: ")
        if option == '1':
            Data.getOperationMonthly()
        elif option == '2':
            Data.getStatistic()
        elif option == '3':
            Data.getOperationForType(3)
        elif option == '4':
            #TODO: show mothly Expenses
            print("Comming soon ...")
        if option != '5':   
            input("Press enter")
        os.system('clear')
                

    @classmethod
    def selectType(self):
        print("    Type:")
        print("      1. DEBITO")
        print("      2. CREDITO")
        print("      3. EFECTIVOS \n ")
        return input("Enter option: ")

    @classmethod
    def insertOperation(self):
        try:
            print("New operation:")
            date = input("    Date (YYYY-MM-DD): ")
            Validation.validation_date(date)
            typeOp = int(self.selectType())
            Validation.valitdation_typeOperation(typeOp)
            desc = input("    Description: ")
            amount = input("    Amount: ")
            save = input("Do you want save it ? (Y/n)")
            if save=='y' or save=='Y':
                operation = Operation(date, typeOp, desc, amount)
                Data.insertOperation(operation)
        except Exception as e:
            print(e)
            input("Press enter for continue")
    


