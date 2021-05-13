from math import floor

class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        header = "*" * (15 - int(len(self.category)/2)) + self.category + "*" * (14 - int(len(self.category)/2))
        if len(header) < 30 :
            header += "*"
        output = header
        for item in self.ledger:
            width = 30 - len(item["description"][0:23])
            output += f"\n{item['description'][0:23]}" + "{amount:.2f}".format(amount=item['amount']).rjust(width)
        output += f"\nTotal: {self.get_balance()}"
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # check if funds are enought, then:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        # returns the current balance based of the deposits and withdrawals.
        return self.check_funds()

    def transfer(self, amount, to_category):
        # withdraw from current category and transfer to destination category
        # need to check funds
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": f"Transfer to {(to_category.category)}"})
            to_category.ledger.append({"amount": amount, "description": f"Transfer from {self.category}"})
            return True
        return False

    def check_funds(self, amount=None):
        # returns False if the amount is greater than the balance, else returns True
        self.total = 0
        for item in self.ledger:
            self.total += item['amount']
        if amount:
            return amount <= self.total
        else:
            return self.total

    


# percentage spend by category
def create_spend_chart(categories):
    # first, get each category spend in a list
    amount_spend = []
    for category in categories:
        expenses = 0
        for item in category.ledger:
            print(item["amount"])
            if item["amount"] < 0:
                expenses += -item["amount"]
        amount_spend.append(expenses)
    total_spend = sum(amount_spend)
    print(amount_spend)

    percentage_spend = [floor(amount/total_spend*10)*10 for amount in amount_spend]
    number_of_dots = [int(amount/10) for amount in percentage_spend]
    print(percentage_spend)
    print(number_of_dots)

    output_str = "Percentage spent by category"
    left = 10
    while left >= 0:
        if left == 10:
            output_str += f"\n{left*10}|"
        elif left > 0:
            output_str += f"\n {left*10}|"
        else:
            output_str += f"\n  {left*10}|"
        for bar in number_of_dots:
            if bar >= left:
                output_str += " o "
            else:
                output_str += "   "
        left -= 1
    output_str += "\n   "
    output_str += ("-"*(len(number_of_dots)*3+1)).rjust(len(number_of_dots)*3+2)

    # x axis
    category_names = [category.category for category in categories]
    biggest_string = max(category_names, key=len)
    print(biggest_string)
    i = 0
    while i < len(biggest_string):
        output_str += "\n     "
        for category in category_names:
            if i < len(category):
                output_str += category[i]
            else:
                output_str += " "
            output_str += "  "
        i += 1
                

    print(number_of_dots)

    return output_str


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])
print(actual)

