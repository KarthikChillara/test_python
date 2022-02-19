def MyFavoriteFood(Dish):
    print(type(Dish), id(Dish))
    for item in Dish:
        print(item)


MyFavoriteDishes = ["Mexican", "Italian", "Thai", "Indian"]
print(type(MyFavoriteDishes), id(MyFavoriteDishes))
MyFavoriteFood(MyFavoriteDishes)


def SomeFun():
    pass


SomeFun()


# Function calling itself is called as Recursion
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


result = factorial(5)
print("Factorial of 5 =",result)
