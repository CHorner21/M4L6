class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Number of Customers Served: {self.number_served}")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("Sample Restaurant", "Italian")

print(f"Initial Number of Customers Served: {restaurant.number_served}")

restaurant.number_served = 30
print(f"Updated Number of Customers Served: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Updated Number of Customers Served using set_number_served(): {restaurant.number_served}")

restaurant.increment_number_served(20)
print(f"Updated Number of Customers Served using increment_number_served(): {restaurant.number_served}")
