# loan calculator
# 04/06/2023 MWC

# Loan amount (A)
# Number of periodic payments (n) = payments per year * number of years
# Periodic interest rate (i) = annual rate / number of payment periods
#
# Discount Factor (D) = ((( 1 + i ) ^n ) - 1 ) / ( i ( 1+ i) ^n)
#
#
# A = $100,000
# n = 360 (30 years * 12 monthly payments)
# i = .005 (.06 / 12 monthly payments)
# D = 166.7916 (((1+.005)^360)-1)/(.005(1+.005)^360))
# Loan payment (P) = A / D = $599.55 (in this case monthly payment)

class Loan:
    def __init__(self, loanAmount, numberYears, annualRate):
        self.loanAmount = loanAmount
        self.annualRate = annualRate
        self.numberOfPmts = numberYears * 12 #monthly pmts
        self.periodicIntRate = self.annualRate / 12
        self.discountFactor = 0.0
        self.loanPmt = 0
        
    def getDiscountFactor(self):
        return self.discountFactor
    
    def calculateDiscountFactor(self):
        self.discountFactor = (((1.0 + self.periodicIntRate) ** self.numberOfPmts) - 1.0) / (self.periodicIntRate * (1.0 + self.periodicIntRate) ** self.numberOfPmts)
        
    def calculateLoanPmt(self):
        self.calculateDiscountFactor()
        self.loanPmt = self.loanAmount / self.getDiscountFactor()
        
    def getLoanPmt(self):
        return self.loanPmt
        
        

def collectLoanDetails():
    loanAmount = input("What is the loan amount?")
    while not loanAmount.isnumeric():
        loanAmount = input("Please enter a valid loan amount:")
    loanAmount = float(loanAmount)

    numberYears = input("How many years is the loan?")
    while not numberYears.isnumeric():
        numberYears = input("Please enter a valid number of years:")
    numberYears = float(numberYears)

    annualRate = input("What is the annual interest rate for the loan - entered as a decimal?")
    while not all(c.isdigit() or c == '.' for c in annualRate):
        annualRate = input("Please enter a valid annual interest rate:")
    annualRate = float(annualRate)

    return Loan(loanAmount, numberYears, annualRate)
    
 
def main():
    
    loan = collectLoanDetails() #set the variable equal to the return value (making an object)
    
    loan.calculateLoanPmt() #run the method to calculate the loan payment
    
    print("Your monthly payment is: ${0:6.2f}".format (loan.getLoanPmt()))
    
    
if __name__ == "__main__":
    main()