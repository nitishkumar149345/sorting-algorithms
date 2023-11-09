order = []
size= int (input())
for i in range (size):
    a= int(input())
    order.append(a)

def selection_sort(a=[], s= int()):
    new_order=[]
    for i in range (s):
        min_value= min(a)
        print ("mi  {}".format(min_value))
        new_order.append(min_value)
        a.remove(min_value)
    print (new_order)
    
selection_sort(order,size)

