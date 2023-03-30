import operator
print("Hello world")
operators = {"+":operator.add,
             "-":operator.sub,
             "*":operator.mul,
            "/":operator.truediv}
def calc(x1,x2,op):
    return[op](x1, x2)
