# Defined list of that will be used to generate passwords

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "white", "gray", "silver", "gold", "maroon", "navy"]

CITIES = ["Paris", "New York", "London", "Tokyo", "Rome", "Shanghai", "Los Angeles", "Sydney", "Moscow", "Beijing", "Mumbai", "Toronto", "Seoul", "Madrid", "Berlin"]

FRUITS = ["apple", "banana", "orange", "lemon", "lime", "grapefruit", "peach", "plum", "mango", "pineapple", "strawberry", "blueberry", "blackberry", "raspberry", "pomegranate"]



def get_input():
    while True:
        try:
            num_pass = int(input("Number of passwords needed?: "))
            if 1 <= num_pass <= 500:
                return num_pass
            else:
                print("enter value between 1 to 500")
        except ValueError:
            print("Enter a  integer")
# Get number of passwords from the user and check it's valid input

def gen_pass(colors,cities,fruits):
    import random
    password = random.choice(colors)+random.choice(cities)+random.choice(fruits)
    return password
# generate password by randomly selecting a color, city, and fruit from the provided lists and concatenating them together

def main():
    num_pass = get_input()
    for i in range(1, num_pass+1):
        password = gen_pass(COLORS, CITIES, FRUITS)
        print(f'{i} --> {password}')
# main function that calls other functions to get number of passwords, and generate and print them

if __name__ == "__main__":
    print("Password generator")
    main()   #runs main function  