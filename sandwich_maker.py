
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients:
            if ingredients[ingredient] > self.machine_resources[ingredient]:
                print(f'Sorry there is not enough {ingredient}.')
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount_used in order_ingredients.items():
            self.machine_resources[ingredient] -= amount_used
        print(f'{sandwich_size} sandwich is ready. Bon appetit!')