class food_item (object):
    def __init__(self,name,calories,protein,carbohydrates,fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat
def daily_nutrition_tracker(food_list):
    total_calories = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0
    
    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbohydrates += food.carbohydrates
        total_fat += food.fat

    print("Daily nutrition summary:")
    print(f"Total calories: {total_calories}")
    print(f"Total protein: {total_protein} g")
    print(f"Total carbohydrate: {total_carbohydrates} g")
    print(f"Total fat: {total_fat} g")

    if total_calories > 2500:
        print("Warning: calorie intake is above 2500.")
    if total_fat > 90:
        print("Warning: fat intake is above 90 g.")

#example
instant_noodles = food_item("Instant Noodles", 800, 10, 60, 25)
bubble_tea = food_item("Bubble Tea", 300, 2, 50, 5)
fried_chicken = food_item("Fried Chicken", 1500, 35, 20, 70)
cola = food_item("Cola", 150, 0, 40, 0)

foods_eaten = [instant_noodles, bubble_tea, fried_chicken, cola]

daily_nutrition_tracker(foods_eaten)