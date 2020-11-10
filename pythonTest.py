##################REFERENCE ON HOW TO USE PYTHON ON EMACS


##in order to run the contents of this buffer simply use C-c C-c
##no main function? does order not matter?
##shell in a way acts as "Main" function
##once i send the contents of the buffer to the shell, i can then use the
##functions in the shell
##example: we have function greet and addNums. Once I send the contents
##I can then type "greet()" in shell and it will run the functions as defined
##in the buffer
##Similarly with addNums, i can also run the function, although it requires
##parameters. I can either hardcode (i.e. addNums(8, 3)) or create variables
##within the buffer(where I write the functions or the shell(where the buffer
##is sent to)

##Note: probably not the best way to develop but will research how to improve 
def greet():
    print("Enter your name")
    name = input()
    print("Hello, " + name + ". Good morning!")

def addNums(num1, num2):
    print(num1 + num2)

