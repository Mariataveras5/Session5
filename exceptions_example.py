name = input("What is your name? ")
#lets write this in a simpler way
age2 = input(f"How old are you {name}? ")
try:
    age2 = int(age2)
    print(f"{name}, you were born in {2024-age2}")
except ValueError:
    print("Please enter a valid value for age")
    print("I can also print this in case of error that I prevented")
except ZeroDivisionError:
    print("you can not divide by 0!")
except:
    print("this is another type of error")
else: #this is for no exception
    print("thank you for playing as expected")
finally: #This eill be executed no matter what, at the very end
    print("Thanks for playing the game.")
