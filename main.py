from Madlibs import fisher,farmer,magical_adventure
import random 

user_name = input(" enter your Name  : ")
print(f"Hi {user_name}, we had a great time with you  :)")
if __name__ == "__main__":
    
    m = random.choice([farmer,fisher,magical_adventure])
    madlib = m()
    print(madlib)
    
print(f"\n\t The game has been ended {user_name}")