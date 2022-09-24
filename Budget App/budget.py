class Category:
    def __init__(self, name):         # Constructor
        self.name = name
        self.ledger = []

    def deposit(self, amount, descr = None):
    # This method accepts an amount and description. If no description is given,
    # defaults to an empty string. The method appends an object to the ledger list
        if descr == None:
            self.ledger.append({"amount": amount, "description": ""})
        else:
            self.ledger.append({"amount": amount, "description": descr})

    def withdraw(self, amount, descr = None):
    # This method receives an amount that is stored in the ledger as a -(number),
        if self.check_funds(amount):
            if descr == None:
                self.ledger.append({"amount": -amount, "description": ""})
            else:
                self.ledger.append({"amount": -amount, "description": descr})
            return True
        else: return False

    def get_balance(self):
    # This method returns the sum of deposits & withdrawals
        current_balance = 0.0
        for line in self.ledger:
            current_balance += line["amount"]
        return current_balance

    def transfer(self, amount, category):
    # This method accepts an amount and another budget category as arguments. The
    # method adds a withdrawal to self.category and adds a deposit to the other
    # category with the amount and descriptions. Return False if not enough funds
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else: return False

    def check_funds(self, amount):
    # This method checks against balance It returns `False` if the amount > balance
        if amount > self.get_balance(): return False
        else: return True

    def __str__(self):
    # When the budget object is printed it displays:
    # * Title line of 30 characters with centered name with '*' characters
    # * list of items in ledger | Description (23 chars ljust()), amount:.2f (rjust)
    # * line displaying the category total.
        output_line = ""
        output_line += self.name.center(30, "*") + "\n"        # Load title line

        for line in self.ledger:                               # Load ledger lines
            output_line += line["description"][:23].ljust(23," ")\
            + "{:.2f}".format(line["amount"]).rjust(7, " ") + "\n"

        output_line += f"Total: {self.get_balance():.2f}"      # Load total line
        return output_line

def create_spend_chart(categories):
# This function receives a categories list and creates a spend chart with all
    spend_chart = "Percentage spent by category\n"             # load chart title
    total_spend = 0.0        # Var tracks the cummulative total of withdrawals
    max_height = 0           # Var stores the longest category name
    breakdown = []           # list stores (name, withdrawals, name_height, %)

    for category in categories:
    # Read through each ledger and store total_spend & self.total_spend amounts
        name_height = len(category.name)
        self_spend = 0.0                        # Reset self_spend for new category
        for line in category.ledger:
            if line["amount"] < 0 :
                self_spend += line["amount"]
                total_spend += line["amount"]
            else: continue
        breakdown.append({"category": category.name, "withdrawals": self_spend,\
        "name_height": name_height})

    for line in breakdown:
    # Calculate percentages | update breakdown with new "percentage":% pair
        percentage = round((line["withdrawals"] / total_spend) * 100)
        line['percentage'] = percentage

        if line['name_height'] > max_height:
            max_height = line['name_height']

    for line in breakdown:
    # Adjust name_height of all category names to be equal to max_height
        if len(line['category']) < max_height:
            line['category'] = line['category'].ljust(max_height, " ")
        else: continue

    count = 0; index = 0
    while count <= 10:
    # Print the chart bars
        spend_chart += str(100 - (10 * count)).rjust(3," ") + "| "
        while index < len(breakdown):
            if breakdown[index]['percentage'] >= (100 - (10 * count)):
                spend_chart += 'o  '
            else:
                spend_chart += '   '
            index += 1
        count += 1
        index = 0                       # Reset index for next item in breakdown
        spend_chart += '\n'

    # Add lines to spend_chart. 2 spaces beyond final bar
    spend_chart += "    " + str().center((len(breakdown)\
    + (2 * len(breakdown) + 1)), "-") + "\n   "

    count = 0
    while count < max_height:
    # Add category names (2 spaces between each category)
        index = 0
        while index < len(breakdown):
            if count == 0:
                spend_chart += "  " + f"{breakdown[index]['category'][count]}".capitalize()
            else:
                spend_chart += "  " + f"{breakdown[index]['category'][count]}"
            index += 1
        count += 1
        spend_chart += '  '
        if count == max_height:
            break
        else: spend_chart += '\n   '

    return spend_chart
