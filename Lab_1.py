import operator
print("Hello world")
operators = {"+":operator.add,
             "-":operator.sub,
             "*":operator.mul,
            "/":operator.truediv}
def calc(x1,x2,op):
    return[op](x1, x2)
def evens(nums_list):
   for num in nums_list:
         if num % 2 == 0:
            print(num, end=' ')
evens([5, 20, 21, 58, 3])