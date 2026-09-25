#main purpose of a function is to reduce repeated code
#another purpose is to break down a large piece of code to make it 
#easier to read and test
#the third purpose is to decompose the problem to let the product be
#implemented as a set of different funcs packed tg in diff modules
#examples of built-in funcs are print(), input(), int(), and float()

def value(): #this is defining a function
    return input("Enter a value: ") #this returns whatever you input
a = value() #this is calling a function (and assigning its value to a)
b = value()
c = value()

#it's important to define functions before they are called(invoked), 
#otherwise it will throw an error b/c it doesn't know what the func is

def addition(num1, num2): #num1 and num2 are parameters
    return num1 + num2

varglobal = 4
print(addition(3,5))#3 and 5 are arguments
print(varglobal)
#parameters are called local variables, meaning they only exist in the 
#context of the function. varglobal is an example of a global var, 
#meaning it exists throughtout the entire program

#parameters are by default position based, but if you set the parameter
#name equal to the value, it will use that instead

print(addition(num2=5, num1=7))

#there are two main functions of the return instruction. The first 
#being without an expressions, which basically just exits the function
#the second(and arguably more important), is to return a value.
#the functions earlier in this program contain returns with value

#vars have scopes, meaning that depending on whether the var was 
#defined inside of the function or defined outside of it, it will 
#serve a different purpose. 
#a var defined within a function is a local var, meaning it is only 
#used in the context of the function and is disregarded when the func
#is finished
#global variables can be used anywhere, inside or outside funcs
#you can also turn local vars into global vars by adding the 
#keyword 'global' before the var, making the var modifiable and
#persistent to the outside var
#  
