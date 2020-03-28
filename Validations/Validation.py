
def validation_date(date):
    if date[0:2] != '20':
        raise ValueError("Error Year")
    if date[4:5] != '-' or date[7:8] != '-':
        raise ValueError("Error format date")

def valitdation_typeOperation(number):
    if number < 1 or number > 3:
        raise ValueError("Invalid Type Operation")


