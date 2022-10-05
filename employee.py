"""Employee pay calculator."""

class Employee:
    def __init__(self, name, contract, salaryCal , hours = 0, isCommission = False, commissionType = "", commission = 0, contracts = 0):
        self.name = name
        self.contract = contract
        self.salaryCal = salaryCal
        
        

    def get_pay(self):
        totalPay = 0

        if contract == "monthly":
            if commission == False:
                totalPay = salaryCal

            elif commission & commissionType == "bonus":
                totalPay = salaryCal + commission

            else:
                totalPay = salaryCal +  (contracts * commission)

        elif contract == "hourly":
            if commission == False:
                totalPay = salaryCal * hours

            elif commission & commissionType == "bonus":
                totalPay = (salaryCal * hours) + commission

            else:
                totalPay = (salaryCal * hours) +  (contracts * commission)






    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly', 3000, True, 'contract', 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', 25, 150, True, "contract", 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', 2000, True, "bonus", 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', 30, 120, True, "bonus", 600)
