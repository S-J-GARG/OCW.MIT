class solve():
    def __init__(self):
        pass
    def cube(self):
        input_number=float(input("Enter any number\n"))     
        x=float(input_number)
        y=x*x*x
        print(y)  

# Find factorial of a number
def factorial(n):
        if n < 0:
            raise ValueError("factorial: input must not be negative")
        elif n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n+1 ):
                result *= i
            return result

''' count the pattern in count_pattern(pattern lst), which counts the number of times a certain pattern of
# symbols appears in a list, including overlaps. So count_pattern( ('a', 'b'), ('a',
# 'b', 'c', 'e', 'b', 'a', 'b', 'f')) should return 2      '''
# x=('a','b')
# y=('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f')
# x=0
# def count_pattern(a,b):
  
#     k=0
#     for x in y:
#         if x==y:
#             k=k+1
#         return k

# print(count_pattern(x,y)) 
def count_pattern(pattern, lst):
    count = 0
    pattern_length = len(pattern)
    lst_length = len(lst)
    k=lst_length - pattern_length + 1
    print(pattern_length)
    print(lst_length)
    print(k)
    print(range(k))
    print(lst[0:2])
    print(lst[1:3])
    print(lst[2:4])
    print(pattern)
    for i in range(k):
        if lst[i:i+pattern_length] == pattern:
            count += 1

    return count
# pattern1 = ('a', 'b')
# lst1 = ('a', 'b', 'a', 'b', 'b', 'a', 'b', 'f')
# print(count_pattern(pattern1, lst1))  # Output: 2

'''Expression depth
 One way to measure the complexity of a mathematical expression is the depth of the expression
 describing it in Python lists. Write a program that finds the depth of an expression.
e.g  
depth('x') => 0
depth(('expt', 'x', 2)) => 1
depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))) => 2'''
# def depth(pattern):
#     count=0
#     count_pattern=len(pattern)
#     print(count_pattern)
#     print(pattern[1])
#     print(range(count_pattern-1))
#     for i in range(count_pattern-1):
        
#         # print(pattern[i])
#         check_pattern=pattern[i]

#         print(check_pattern[i])
#         # if isinstance(check_pattern[i],tuple):
#         #     count+=1
#         # return count
    
    

# x=depth(('expt', '2'))
# print(x)
def depth(expression):
    if not isinstance(expression, tuple):  # Base case: expression is not a tuple
        return 0
    else:
        max_depth = 0
        for sub_expr in expression: #it checking every sub-expression in given expression 
            if isinstance(sub_expr, tuple):
                sub_depth = depth(sub_expr)
                max_depth = max(max_depth, sub_depth)
        return max_depth + 1

# Examples:
print(depth('x'))  # Output: 0
print(depth(('expt', 'x', 2)))  # Output: 1
print(depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))))  # Output: 2
