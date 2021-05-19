def revert_values(func):  #it always accept a function  sub()
    def inside(num1,num2):
        if num1<num2:
            (num1,num2)=(num2,num1)
        return func(num1,num2)
    return inside

@revert_values
def sub(num1,num2):
    return num1-num2

@revert_values
def div(num1,num2):
    return num1/num2
print(sub(2,10))
print(div(5,10))




# def sub(num1,num2):
#     if num1<num2:
#         (num1,num2)=(num2,num1)
#     return num1-num2
# def div(num1,num2):
#     if num1 < num2:
#         (num1, num2) = (num2, num1)
#     return num1/num2
# print(sub(2,10))
# print(div(2,8))