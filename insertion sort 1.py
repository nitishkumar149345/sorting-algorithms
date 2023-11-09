order= []
size= int (input())
for i in range (size):
    a= int (input())
    order.append(a)

def insertion_sort(a=[],length= int()):
    for i in range (1,length):
        j=i-1
        temp= a[i]
        while  a[j]>temp and j>=0 :
            a[j+1]= a[j]
            j-=1
        a[j+1]= temp

insertion_sort(order, size)
print (order)