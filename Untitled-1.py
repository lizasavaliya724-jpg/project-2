class payment:

    def pay (self, amount):
        print ("payment processing...")

# child class 1
 
class Cashpayment (payment):

    def pay(self, amount):
        print ("Cash Payment")
        print("Amount:", amount)
        print ("Please pay cash at counter.")

# child class 2

class Cardpayment (payment):

    def pay(self, amount):
        print ("Card Payment")
        print("Amount:", amount)
        print ("Payment done using Credet / Debit card.")

# child class 3

class UPIPayment (payment):

    def pay(self, amount):
        print ("UPI Payment")
        print("Amount", amount)
        print ("Payment using UPI")

amount = 2000

payment = [Cashpayment() , Cardpayment() , UPIPayment]

payment.pay(2000)
