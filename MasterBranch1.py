def add(a,b):
    c = a+b
    return c

res = add(10,20)
print(res)

#eve or odd
def even_odd(*lis):
    even = []
    odd = []
    for i in lis:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

res1 = even_odd([10,5,6,8,7,1])
print(res1)