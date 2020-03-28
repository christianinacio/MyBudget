import sqlite3
from models.Operation import Operation

class Data:

    @classmethod
    def connect(self):
        self.conn = sqlite3.connect('budget.db')
        self.c = self.conn.cursor()

    @classmethod
    def create_tables(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS Operations(id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE, type INTEGER, descr VARCHAR(40), amount DOUBLE)')
        self.c.execute('CREATE TABLE IF NOT EXISTS TypeOperations(id INTEGER PRIMARY KEY,desc VARCHAR(20))')

    @classmethod
    def insertType(self):
        self.c.execute("INSERT INTO TypeOperations (id, desc) VALUES (1,'DEBIT')")
        self.c.execute("INSERT INTO TypeOperations (id, desc) VALUES (2,'CREDIT')")
        self.c.execute("INSERT INTO TypeOperations (id, desc) VALUES (3,'CASH')")
        self.conn.commit()
    
    @classmethod
    def insertOperation(self,operation):
        self.c.execute('INSERT INTO Operations (date, type, descr, amount) VALUES (?,?,?,?)',(operation.date, operation.type, operation.desc, operation.amount))
        self.conn.commit()

    @classmethod
    def close(self):
        self.c.close()
        self.conn.close()
    
    @classmethod
    def getOperation(self):
        operations = []
        self.c.execute('SELECT * FROM Operations')
        for row in self.c.fetchall():
            operations.append(Operation(row[0],row[1],row[2],row[3]))
        return operations

    @classmethod
    def getOperationMonthly(self):
        print("Operation Monthly: \n")
        self.c.execute("SELECT date, t.desc, descr, amount FROM Operations o JOIN TypeOperations t on o.type = t.id WHERE date between date('now','start of month') AND date('now','start of month','+1 month')")
        for row in self.c.fetchall():
            print(row)
    
    @classmethod
    def getOperationForType(self, type):
        self.c.execute("SELECT date, descr, amount FROM Operations WHERE type = ? AND date between date('now','start of month') AND date('now','start of month','+1 month')",(type,))
        for row in self.c.fetchall():
            print(row)
    
    @classmethod
    def getStatistic(self):
        DateCredit = input("Last billing cycle (YYYY-MM-DD)")
        self.c.execute("SELECT sum(amount) FROM Operations WHERE type = 3")
        sumCash = self.c.fetchone()[0]
        self.c.execute("SELECT sum(amount) FROM Operations WHERE type = 2 AND date > ?",(DateCredit,))
        sumCredit = self.c.fetchone()[0]
        self.c.execute("SELECT sum(amount) FROM Operations WHERE type = 1")
        sumDebit = self.c.fetchone()[0]
        print(" Total Debit     Total Credit      Total Cash ")
        print("   " + str(sumDebit) + "             " + str(sumCredit) + "           " + str(sumCash))
