class Calculator:
    def add(self, x, y):
        return x+y
    
    def sub(self, x, y):
        return x-y

    def div(self, x, y):
        if y != 0 :
            return x/y
        else:
            return ("Cannot divide by 0")

    def mult(self, x, y):
        return x*y
    

calculator = Calculator()
x = 4
y = 24
z = 0

add = calculator.add(x,y)
sub = calculator.sub(x,y)
mult = calculator.mult(x,y)
div = calculator.div(y,x)
div0 = calculator.div(y,z)

print(str(x) + " + " + str(y) + " = " + str(add))
print(str(x) + " - " + str(y) + " = " + str(sub))
print(str(x) + " * " + str(y) + " = " + str(mult))
print(str(y) + " / " + str(x) + " = " + str(div))
print(str(y) + " / " + str(z) + " = " + str(div0))
