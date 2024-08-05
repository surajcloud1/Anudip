# ## Que 1 ==>print helllo
print("hello")

#### OutPut " hello "


### Ans===> Local variables are defined inside a function and can only be used within that function. They are not accessible outside of the function.
#### Global variables are defined outside of all functions and are accessible from any function within the same module.

####Q.2 describe local variable and global variable code
global_var = 24


def function():
    local_var = 30  # this is local variable
    print(f"i am a local variable: {local_var}")


function()

print(f"i am a gloabl variable : {global_var}")


## output i am a local variable:  30
## i am a gloabl variable : 24


#### Q.3 Write a code that describe Indentation error
def fun():
    print("This line is properly indented")


# print("This line is not properly indented")  # This will cause an IndentationError

fun()
#### output ====> "This line is not properly indented"


##### Q.4 write a code that describe local and global variable with same name

var = "i am global variable"


def function_lclglbl():
    var = "i am local variable"
    print(var)


function_lclglbl()
print(var)

#### output "i am local variable"
#### "i am global variable"


##### Q.5 Write a code for string, int and float input.
# Taking string input from the user
string_input = input("Enter a string: ")
print(f"You entered the string: {string_input}")

# Taking integer input from the user
int_input = int(input("Enter an integer: "))
print(f"You entered the integer: {int_input}")

# Taking float input from the user
float_input = float(input("Enter a float: "))
print(f"You entered the float: {float_input}")

###### output Enter a string: rahil
##### You entered the string: rahil
####  Enter an integer: 7
#### You entered the integer: 7
#### Enter a float: 2.6
##### You entered the float: 2.6