# Type B
# print(bool(0),bool(str(0))) # 0 indicates false while str(0) is non-empty string

# print((6) == int((input("Enter value: ")))) #ValueError: invalid literal for int() with base 10: '5+4/2'

# print((6) == (input("Enter value: "))) # False

# a,b,c = 2,3,6
# d=a+b*c/b
# print(d)

# a=va=3
# b=va=3
# print(a,b) # 3,3

# a=3
# b=3.0
# print(a==b) # True
# print(a is b) # False

# a,b,c = 1,1,2
# d=a+b
# print(c == d) # True
# print(c is d) # True

# a = 5-4-3
# b = 3**2**3
# print(a) # -2
# print(b) # 6561

# a,b,c = 0.1 # TypeError: cannot unpack non-iterable float object
# d=0.3
# e= a+b+c-d
# print(e)

# a=12
# b=7.4
# c=1
# a -= b
# print(a,b) # 4.6 7.4
# a *= 2+c
# print(a) # 13.799999999999999
# b += a*c
# print(b) # 21.2

# x,y = 4,8
# z=x/y*y
# print(z) # 4.0

# x,y = 4,8
# z=int(x/(y*y))
# print(z) # 0

# print(10/0 or 3) # ZeroDivisionError: division by zero

# a,b = bool(0), bool(0.0)
# c,d = str(0), str(0.0)
# print(len(a),len(b)) # TypeError: object of type 'bool' has no len()
# print(len(c),len(d)) # 1 3

# s="12345"
# sum=0
# for i in s:
#     sum += int(i)
# print(sum) # 15

# a=True
# b=0<5
# print(a == b) # True
# print(a is b) # True
# c=str(a)
# d=str(b)
# print(c == d) # True
# print(c is d) # True
# e = input("Enter: ")
# print(e)
# print(c == e)
# print(c is e)

# name = 'HariT'
# name[2]='R'
# print(name) # TypeError: 'str' object does not support item assignment

# a = bool(0)
# b = bool(1)
# print(a == 'false') # False
# print(b == 'true') # False

# print(type(int('123'))) # <class 'int'>
# print(type(int('Hello'))) # ValueError: invalid literal for int() with base 10: 'Hello'
# print(type(str('123.0'))) # <class 'str'>

# print("Hello" + '2') # Hello2
# print("Hello"/2) # TypeError: unsupported operand type(s) for /: 'str' and 'int'
# print("Hello" / 2) # TypeError: unsupported operand type(s) for /: 'str' and 'int'

