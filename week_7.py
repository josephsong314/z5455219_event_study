"""
variable

<target> = <expression>

1. evaluate <target>
- if not valid raise an expression

2. evaluate <expression>


3. python will assign the expression to target.


"""



lst =[1,2,]
lst = -99
print(lst)

x = -99
y = x
print(y)

lst = [1,2,3]
lst[0]

print(lst[0])

print(id(lst))

lst0 =[1,2]
lst1 = [1,2]
lst2 = lst0

lst2[0] = -99

print(lst2[0])

"""
pandas
"""

dic = {'a':1,2: 3}
print(dic['a'])
print(dic[2])

# tuple/list

lst = [1,2,3]
print(lst[0])


# pandas

# Seeries

"""
one demnsional series
 ser[indexer]
 
 ser.loc: selection by lablel (in the index)
 ser.iloc: selection by index (in array)
"""

