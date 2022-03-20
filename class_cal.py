class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2 
    def add(self):
        return (self.num1+self.num2)
    def mul(self):
        return (self.num1*self.num2)
    def div(self):
        return (self.num1/self.num2)
    def sub(self):
        return (self.num1-self.num2)
num1=int(input("enter num1 :"))
num2=int(input("enter num2 :")) 
obj=calculator(num1,num2)
print(obj.add())
print(obj.sub())
print(obj.mul())
print(obj.div())  