from models.Operation import Operation
from Interface import Interface
import os

print("### MY BUDGET ####")

option = Interface.options()
os.system('clear')
while(option != "4"):
    if option == '1':
        Interface.insertOperation()
    elif option == '2':
        Interface.StatisticMenu()
    os.system('clear')
    option = Interface.options()
    os.system('clear')

