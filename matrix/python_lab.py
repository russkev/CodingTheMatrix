# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.





## 1: (Task 0.5.1) Minutes in a Week
minutes_in_week = 60*24*6


## 2: (Task 0.5.2) Remainder
#For this task, your expression must use //
remainder_without_mod = 2304811 - 47*(2304811//47)



## 3: (Task 0.5.3) Divisibility
divisible_by_3 = 673+900%3==0



## 4: (Task 0.5.4) Conditional Expression
# Replace the ... with the expression 
x = -9
y = 1/2
expression_val = 2**(y+1/2) if x+10<0 else 2**(y-1/2)



## 5: (Task 0.5.5) Squares Set Comprehension
first_five_squares = { x**2 for x in {1,2,3,4,5} }



## 6: (Task 0.5.6) Powers-of-2 Set Comprehension
first_five_pows_two = { 2**x for x in {0,1,2,3,4} }



## 7: (Task 0.5.7) Double comprehension evaluating to nine-element set
# Assign three-element sets to X1 and Y1 so that
# {x*y for x in X1 for y in Y1} evaluates to a nine-element set.

X1 = { 1, 2, 3 }
Y1 = { 5, 6, 7 }



## 8: (Task 0.5.8) Double comprehension evaluating to five-element set
# Assign disjoint three-element sets to X1 and Y1 so that
# {x*y for x in X1 for y in Y1} evaluates to a five-element set.

X2 = { 1, 1, 2 }
Y2 = { 2, 3, 4 }



## 9: (Task 0.5.9) Set intersection as a comprehension
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
# Replace { ... } with a one-line set comprehension that evaluates to the intersection of S and T
S_intersect_T = {y for x in S for y in T if x == y}



## 10: (Task 0.5.10) Average
list_of_numbers = [20, 10, 15, 75]
# Replace ... with a one-line expression that evaluates to the average of list_of_numbers.
# Your expression should refer to the variable list_of_numbers, and should work
# for a list of any length greater than zero.
list_average = sum([20,10,15,75])/4



## 11: (Task 0.5.11) Cartesian-product comprehension
# Replace ... with a double list comprehension over ['A','B','C'] and [1,2,3]
cartesian_product = [[x,y] for x in ['A','B','C'] for y in [1,2,3]]



## 12: (Task 0.5.12) Sum of numbers in list of list of numbers
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
# Replace ... with a one-line expression of the form sum([sum(...) ... ]) that
# includes a comprehension and evaluates to the sum of all numbers in all the lists.
LofL_sum = sum([sum(x) for x in LofL])



## 13: (Task 0.5.14) Three-element tuples summing to zero
S = {-4, -2, 1, 2, 5, 0}
# Replace [ ... ] with a one-line list comprehension in which S appears
zero_sum_list = [ (x,y,z) for x in S for y in S for z in S if sum([x,y,z])==0]



## 14: (Task 0.5.15) Nontrivial three-element tuples summing to zero
S = {-4, -2, 1, 2, 5, 0}
# Replace [ ... ] with a one-line list comprehension in which S appears
exclude_zero_list = [ (x,y,z) for x in S for y in S for z in S if (sum([x,y,z])==0 and ((x,y,z) != (0,0,0))) ]


## 15: (Task 0.5.16) One nontrivial three-element tuple summing to zero
S = {-4, -2, 1, 2, 5, 0}
# Replace ... with a one-line expression that uses a list comprehension in which S appears
first_of_tuples_list = [ (x,y,z) for x in S for y in S for z in S if (sum([x,y,z])==0 and ((x,y,z) != (0,0,0))) ][0]



## 16: (Task 0.5.17) List and set differ
# Assign to example_L a list such that len(example_L) != len(list(set(example_L)))
example_L = [1,1,2,3]



## 17: (Task 0.5.18) Odd numbers
# Replace {...} with a one-line set comprehension over a range of the form range(n)
odd_num_list_range = {x for x in list(range(100)) if x%2 != 0}



## 18: (Task 0.5.19) Using range and zip
# In the line below, replace ... with an expression that does not include a comprehension.
# Instead, it should use zip and range.
# Note: zip() does not return a list. It returns an 'iterator of tuples'
range_and_zip = list(zip(list(range(5)),['A','B','C','D','E']))



## 19: (Task 0.5.20) Using zip to find elementwise sums
A = [10, 25, 40]
B = [1, 15, 20]
# Replace [...] with a one-line comprehension that uses zip together with the variables A and B.
# The comprehension should evaluate to a list whose ith element is the ith element of
# A plus the ith element of B.
list_sum_zip = [sum(x) for x in list(zip(A,B))]



## 20: (Task 0.5.21) Extracting the value corresponding to key k from each dictionary in a list
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
# Replace [...] with a one-line comprehension that uses dlist and k
# and that evaluates to ['Sean','Roger','Pierce']
value_list = [x[k] for x in dlist]



## 21: (Task 0.5.22) Extracting the value corresponding to k when it exists
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
#Replace [...] with a one-line comprehension 
value_list_modified_1 = [x[k] if k in x else 'NOT PRESENT' for x in dlist ] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [x[k] if k in x else 'NOT PRESENT' for x in dlist ] # <-- as you do here



## 22: (Task 0.5.23) A dictionary mapping integers to their squares
# Replace {...} with a one-line dictionary comprehension
square_dict = {x:x*x for x in range(100)}



## 23: (Task 0.5.24) Making the identity function
D = {'red','white','blue'}
# Replace {...} with a one-line dictionary comprehension
identity_dict = {x:x for x in D}



## 24: (Task 0.5.25) Mapping integers to their representation over a given base
base = 10
digits = set(range(base))
# Replace { ... } with a one-line dictionary comprehension
# Your comprehension should use the variables 'base' and 'digits' so it will work correctly if these
# are assigned different values (e.g. base = 2 and digits = {0,1})
representation_dict = {u:(u//base**2,(u%base**2)//base,u%base) for u in range(base**3)}


## 25: (Task 0.5.26) A dictionary mapping names to salaries
id2salary = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
# Replace { ... } with a one-line dictionary comprehension that uses id2salary and names.
listdict2dict = {x:y for x,y in zip(names, id2salary.values())}



## 26: (Task 0.5.28) Procedure nextInts
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def nextInts(L): return [ x+1 for x in L ]



## 27: (Task 0.5.29) Procedure cubes
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def cubes(L): return [ x*x*x for x in L ] 



## 28: (Task 0.5.30) Procedure dict2list
# Input: a dictionary dct and a list keylist consisting of the keys of dct
# Output: the list L such that L[i] is the value associated in dct with keylist[i]
# Example: dict2list({'a':'A', 'b':'B', 'c':'C'},['b','c','a']) should equal ['B','C','A']
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def dict2list(dct, keylist): return [ dct[x] for x in keylist ]



## 29: (Task 0.5.31) Procedure list2dict
# Input: a list L and a list keylist of the same length
# Output: the dictionary that maps keylist[i] to L[i] for i=0,1,...len(L)-1
# Example: list2dict(['A','B','C'],['a','b','c']) should equal {'a':'A', 'b':'B', 'c':'C'}
# Complete the procedure definition by replacing { ... } with a one-line dictionary comprehension
def list2dict(L, keylist): return { x:y for x,y in zip(keylist, L) }



## 30: (Task 0.5.32) Generating all three-digit numbers over a given base
# Complete the procedure definition by replacing { ... } with a one-line set comprehension
def all_3_digit_numbers(base, digits): return {x for x in range(base**3)}

