
def greet_wit_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")
    print(f"Isn't the weather nice today, {name}?")



def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with(location="Nepal",name = "Keshab")

test_h = int (input("What's the height of the wall: "))
test_w = int (input("What's the width of the wall: "))
coverage = 5
def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    round_of_cans = round(number_of_cans)
    print(f"You'll need {round_of_cans} cans of paint.")

paint_calc(height=test_h, width= test_w, cover= coverage)