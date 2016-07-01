#ex14

#removing duplicates

#using a loop
def removedupes(listSupplied):
    print(listSupplied)
    new_list=[]
    for x in listSupplied:
        if x not in new_list:
            new_list.append(x)
    print("List using loop:",new_list)



#using sets
def removedupes_2(listSupplied_2):
    new_set=set()
    for x in listSupplied_2:
        new_set.add(x)
    print("Set using sets:",new_set)



i=[1,2,3,1,2,3,4,5,2,3,4,8,10]
removedupes(i) #loop
removedupes_2(i) #sets




#ex05 using sets (items from both but no dupes)
def ex5(set1,set2):
    set_k=set()
    for i in set1:
        set_k.add(i)
    for j in set2:
        set_k.add(j)
    print("This is set k:",set_k)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
ex5(a,b)
