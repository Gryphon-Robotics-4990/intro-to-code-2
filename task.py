# This is a comment. Comments are where you put human-readable text (such as an explanation of how your code works) in
# your code. Basically, how it works is the computer reads your code normally, until it finds the '#' symbol. It then
# ignores everything that comes after the '#' on that line. For example, see the following line.

print("#like, comment, and subscribe!") #Prints "#like, comment, and subscribe!"

# So that may be a little confusing. Let's break down which '#' does what. The first # (the one before the "like")
# is part of a 'string' (more on that later). '#'s inside strings are ignored. The 2nd # (After the end parentheses)
# denotes the start of the comment. This is because it is the first # outside of a string. The 3rd #, before the
# second 'like', is ignored. Once a # is found on a line, it ignores everything after it, including the 3rd #.

def operations():
    # Now that we have that out of the way, let's start with actual code. The first concept is the variable. A
    # variable is like a container. It stores an arbitrary value that you can assign as well as retrieve.
    
    teamNumber = 4991
    
    # The line above creates a new variable, called teamNumber. Variables can be called anything you want,
    # with a few exceptions. Almost all languages have "keywords", which are basically words or phrases that 
    # the language reserves for its own use. For example 'def', 'return', and 'class' are examples of Python keywords.
    # A keyword is not a valid name for a variable. There's a few more rules for variables:
    # 1. They can only consist of the letters of the English alphabet (A-Z or its lowercase variants), numbers (1-9),
    #     and underscores ('_')
    # 2. They must include at least one letter
    # 3. They must start with a letter or underscore
    
    # Now for the next part of the line above.  The '=' operator is called the assignment operator. It is different
    # from the equality operator, which uses the '=' symbol in math. The assignment operator essentially gives the variable
    # on the left the value on the right. In the line above, it 'assign' the value 4991 to the variable teamNumber.
    
    print(teamNumber)
    
    # print() is a function that is built-in to Python. It basically displays whatever is inside the parentheses to the
    # console (basically output). The line above would print 4991, as that is the value given to the variable teamNumber.
    # You can get the values you have stored inside variables by using its name.
    
    # But wait. Our team number isn't 4991. So now, you will learn how to modify the values of variables. The first
    # option is to use reassignment. Reassignment is when you give a variable a new value. For example:
    teamNumber = 4990
    # Now, the teamNumber variable has the value 4990. The old value, 4991, is forever banished into the void. You will
    # not be able to get it back. Be careful when you reassign variable values!
    
    # To modify variable values, Python, like most languages, supports the 4 basic operations and respects order of operations.
    # In the line of code below, Python will calculate 3 * 5 before adding 2, which results in 17.
    value1 = 2 + 3 * 5
    
    # You can also add parentheses to expressions, which Python will follow.
    value2 = (2 + 3) * 5
    # In the line of code, Python will calculate 2 + 3 first, and multiply that result by 5. You can also use variables in
    # expressions.
    value1 = value1 + teamNumber
    # This may be a little confusing, if you're reading it like math. What the line of code above, I basically told Python
    # to reassign the variable 'value1'. The new value for that variable would be the expression on the right of the '='.
    # In this case, that would be the old value1 (which if you look above, is 17) plus the teamNumber (which is also
    # defined above, as 4990). The new value of value1 is 5007.
    
    # Now, as an exercise: Modify the line of code below so that a new variable called 'value3' is the product of value1 and the
    # team number.
    value2 = value1 * 2
    
    # There's one more concept to go over: functions. We will not get in to the details in this task, but you should still understand
    # what is going on. Functions are similar to functions in math. They have inputs, often called "parameters" or "arguments",
    # and outputs (called "return values"). In most languages, you can name functions anything you want, much like variables.
    # However, unlike variables, you can't rename a function.
    
    value4 = function1(value3, value1)
    
    # In the line of code above, we create a new variable called value4. We then run (or "call", as some people call it) a
    # function with the very creative name "function1". function1 takes two parameters (which are the two values inside the
    # parentheses) and returns the first parameter squared times the second parameter (you can see the code for the function
    # below, but you don't need to fully understand it. You will learn specifics in the next task). In this case, what the line
    # of code above does is equivalent to "value4 = value3 * value3 * value1". What functions do is allow us to reuse code.
    # If, for example, we wanted to do a complex calculation on a number, we would use functions. That way, we don't have to write
    # out the calculation every time we want to use it.
    
    # Exercise 2: Modify the function below so that the two parameters are value4 and value1. You don't need to calculate the
    # answer, or fully understand what's going on. More function stuff will come in the next task.
    ans = function2(value4, value1)
    
    return value1, ans

def function1(a, b):
    return a * a * b

def function2(a, b):
    return (a + b) * 2
