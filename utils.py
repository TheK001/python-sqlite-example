def print_menu(options):
    for id, option in enumerate(options, 1):
        print(f"{id}. {option}")

def get_user_choice(max_choice):
    while True:
        try:
            choice = int(input("Enter the choice: "))
            if 1 <= choice <= max_choice:
                return choice
            else:
                print(f"Enter menu between 1 and {max_choice}")
        except:
            print("enter valid menu")

def print_cars(cars):
    for car in cars:
        print(f"id:{car[0]} name: {car[1]} color: {car[2]} price: {car[3]} ", sep="\n")

def get_user_input(data):
    return input(data)