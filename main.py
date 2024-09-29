from services import register_user,authenticate_user,add_cars,delete_car,get_all_cars,update_cars
from utils import get_user_choice, print_menu, get_user_input, print_cars

def main_menu():
    while True:
        options = ['Login', 'Register', 'Exit']
        print_menu(options)
        choice = get_user_choice(len(options))

        if choice == 1:
            login()
        if choice == 2:
            register()
        if choice == 3:
            break

def login():
    username = get_user_input('Enter username: ')
    password = get_user_input('Enter password: ')
    if authenticate_user(username, password):
        print("Welcome")
        car_menu()
    else:
        print("Enter correct username anda password!")


def register():
    first_name = get_user_input('Enter first name: ')
    last_name = get_user_input('Enter last name: ')
    username = get_user_input('Enter username: ')
    password = get_user_input('Enter password: ')

    register_user(first_name,last_name,username,password)
    print("succes!!!")

def car_menu():
    while True:
        print("--Car Menu--")
        options = ["show all car", "add car", "update car", "delete car", "exit"]
        print_menu(options)
        choice = get_user_choice(len(options))

        if choice == 1:
            show_all_cars()
        elif choice == 2:
            add_new_car()
        elif choice == 3:
            update_car()
        elif choice == 4:
            ...
        elif choice == 5:
            break

def show_all_cars():
    cars = get_all_cars()
    if cars:
        print_cars(cars)
    else:
        print_cars("You have not any car!")

def add_new_car():
    name = get_user_input("Enter car's name:")
    color = get_user_input("Enter car's color:")
    rental_price = get_user_input("Enter car's rental price:")
    add_cars(name, color, rental_price,)

def update_car():
    show_all_cars()
    car_id = get_user_input("Enter car's new id:")
    name = get_user_input("Enter car's new name:")
    color = get_user_input("Enter car's new color:")
    rental_price = get_user_input("Enter car's new rental price:")
    update_cars(car_id,name, color, rental_price,)   

def hi():
    print("hi!")

if __name__ == "__main__":
    main_menu()


    