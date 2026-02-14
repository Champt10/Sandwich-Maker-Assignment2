class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        total = (large_dollars * 1.00) + (half_dollars * .50) + (quarters * .25) + (nickels * .05)

        return round(total, 2)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        coins = round(coins, 2)
        cost = round(cost, 2)

        if coins < cost:
            print("Sorry, that’s not enough money. Money refunded.")
            return False

        change = round(coins - cost, 2)
        print(f'Here is ${change:.2f} in change.')
        return True
