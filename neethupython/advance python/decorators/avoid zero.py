
def revert_values(func):  #it always accept a function  sub()
    def inside(no1,no2):
        if no1<no2:
            (no1,no2)=(no2,no1)
        return func(no1,no2)
    return inside
def avoid_zero(func):  #it always accept a function  sub()
    def wrapper(num1,num2):
        if (num1==0)&(num2==0):
            raise Exception("zero is not divisible")
        else:
            return func(num1,num2)
    return wrapper
@revert_values
@avoid_zero
def div(num1,num2):
    return num1/num2
print(div(0,10))