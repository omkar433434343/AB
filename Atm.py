class Atm:
	def __init__(self, cardnumber, pin):
		self.cardnumber = cardnumber
		self.pin = pin

	def balanceinquiry(self):
		print("Your balance is: 500$")

	def cashwidthdrawal(self, amount):
		new_amount = 500-amount
		print("You widthdrawed: " + str(amount) + ". Your remaining balance is: " + str(new_amount))

def main():
	name = input("Hi, what is your name?")
	print("Hey, " + name)
	cardnumber = input("input your card number: ")
	pin = input("Enter your pin: ")
	new_user = Atm(cardnumber, pin)

	print("choose your plan")
	print("1.Balance inquiry")
	print("2.Cash widthdrawal")
	activity = int(input("Enter plan choice '1 OR 2' : "))

	if (activity == 1):
		new_user.balanceinquiry()
	elif (activity == 2):
		amount = int(input("Enter the amount: "))
		new_user.cashwidthdrawal(amount)
	else:
		print("Enter a valid number")
main()


print("made by om :)")
