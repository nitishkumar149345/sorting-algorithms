size = int (input())
order= []
for i in range (size):
    a=int (input())
    order.append(a)
def bubble_sort(o=[],s=int ()):

    for i in range (s):
        for j in range (s):
            if o[j]>o[i]:
                o[i],o[j]= o[j],o[i]
bubble_sort(order,size)
print (order)

