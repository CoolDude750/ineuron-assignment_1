#!/usr/bin/env python
# coding: utf-8

# 1. In the below elements which of them are values or an expression? eg:- values can be
# integer or string and expressions will be mathematical operators.
# *
# 'hello'
# -87.8
# -
# /
# +
# 6

# solution:- 1) values are 'hello',-87.8,6
#            2) expressions are *, -, / ,+

# 2. What is the difference between string and variable?

# solution:-1) strings is basically the inbuilt data type in python which is used to store the
#     sequence of characters in sigle quote and double quote.
#     
#      2) variable is just a name given to a memory space which acts as bucket to hold data inside that
#     bucket.

# 3. Describe three different data types.

# Solution:- 1)Lists- A collection of data enclosed within [], It is similar as array of other 
#     programing language, but it can cantain heterogenius type of data and it is Mutable which means 
#     we can perform insert, update etc. operations easily.
#     e.g:- lst = [1,2,3,4,5]
# 
#  2)Tuples - A collection of data enclosed within (), It just like list which also store data in 
# sequencial manner. But Tuples are immutable.Tuples can contain any number of elements and of any
# datatype like strings, integers, list, etc.
# e.g :- tupl = (1,2,3,4,5)
# 
#  3)Dictionaries - It is unordered collection of data values, enclosed within {} and used to store data values in key-value pair format . key and values are seperated by colon :, and elements are key with values are seperated by comma. dictionaries are mutable.
#  e.g :-dictionary = {"a":1, "b":2, "c":3}
# 

# 4. What is an expression made up of? What do all expressions do?

# solution:- Expression is basically made up of operands and operator .
#     Operand are nothing but values upon which we performs operations to get some desired result.
#     Operators are the mathematical symbols that convey some meaning to perform calculations and 
#     operations.
#     Expressions perform the operations on given values to get some desired values.

# 5. This assignment statements, like spam = 10. What is the difference between an
# expression and a statement?

# solution:- assignment statement like spam = 10 assigns the value 10 to the varible spam.
#     expression is special type of instruction which is evluated to give reduce value of an instruction
#     e.g = 1 + 2 
#         = 3
#         
# and in case of statement it is just excuted by interpreter to assign something or print
# something . It just command that is executed that does evaluated like expression.
# e.g =print("HELLO")
#     =HELLO

# 6. After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1

# solution:- 23

# 7. What should the values of the following two terms be?
# 'spam'+'spamspam'
# 'spam'*3

# Solution:- Both the statement will give
#     'spamspamspam'

# 8. Why is eggs a valid variable name while 100 is invalid?

# solution: - Rules for Python variables are it must start with a letter or the underscore character and 
# cannot start with a number and  can only contain alpha-numeric characters and underscores like
# A-z, 0-9, and _ 
# 
# so eggs is valid name according to rule and 100 is invalid
# 

# 9. What three functions can be used to get the integer, floating-point number, or string
# version of a value?

# solution:- The int() , float() , and str( ) functions can be used to get the integer, 
# floating-point number, or string version of a value.

# 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten'+ 99 +'burritos'.

# solution:-
#     concatination operations can only be perform among the string data type . concatination between 
#     integer is not possible as it is not iterable.
#     
#     solution to the error is below
#     'I have eaten'+ ' 99 ' +'burritos'
#     and we'll get output as :- 'I have eaten 99 burritos'
