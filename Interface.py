from Data import Data
from models.Operation import Operation
import datetime
import os

class Interface:

    @classmethod
    def options(self):
        Data.connect()
        Data.create_tables()
        #Data.insertType()
        print("1. Add operation")
        print("2. Statistic")
        print("4. Exit \n ")
        return input("Enter option: ")
    
    @classmethod
    def StatisticMenu(self):
        print("1. Monthly Operation")
        print("2. Totals")
        print("3. Cash Operation")
        print("4. Back \n ")
        option = input("Enter option: ")
        if option == '1':
            Data.getOperationMonthly()
        elif option == '2':
            Data.getStatistic()
        elif option == '3':
            Data.getOperationForType(3)
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
        print("New operation:")
        date = input("    Date (YYYY-MM-DD): ")
        typeOp = int(self.selectType())
        desc = input("    Description: ")
        amount = input("    Amount: ")
        save = input("Do you want save it ? (Y/n)")
        if save=='y' or save=='Y':
            operation = Operation(date, typeOp, desc, amount)
            Data.insertOperation(operation)
    


