# biuldin functions with python
# reduce()
# sum()
# ord()
# comp()
# max()
# min()
# all()
# any()
# len()
# enumerate()
# accumulate()
# filter()
# map()
# lambda()
#The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.
#Working :

#At first step, first two elements of sequence are picked and the result is obtained.
#Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
#This process continues till no more elements are left in the container.
#The final returned result is returned and printed on console.
#filter_none
import functools
lis= [1,3,5,6,2]
print(functools.reduce(lambda a,b: a+b, lis))#using the reduce to compute the sum of the list
#output is 17 of sum.
print(functools.reduce(lambda a,b:a if a>b else b, lis))#using reduce to compute the max no. from the list.
import operator
print(functools.reduce(operator.add,lis))#using reduce to compute the sum, using operator
#output is 17 of sum.
print(functools.reduce(operator.mul,lis))#using reduce to compute the product, using operatpr
print(functools.reduce(operator.add,['h','e','l','l','o']))#using reduce to concatenate the string
#reduce() vs accumulate()

#Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. But there are differences in the implementation aspects in both of these.
#reduce() is defined in “functools” module, accumulate() in “itertools” module.
#reduce() stores the intermediate result and only returns the final summation value. Whereas, accumulate() returns a list containing the intermediate results.
# The last number of the list returned is summation value of the list.
#reduce(fun,seq) takes function as 1st and sequence as 2nd argument. In contrast accumulate(seq,fun) takes sequence as 1st argument and function as 2nd argument.
import itertools
print(list(itertools.accumulate(lis,lambda x,y: x+y)))
print(functools.reduce(lambda x,y:x+y,lis))
#sum() function in Python
#Sum of numbers in the list is required everywhere. Python provide an inbuilt function sum() which sums up the numbers in the list.



