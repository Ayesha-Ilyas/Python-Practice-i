list=[]
print("initial blank lists: ")

lists =['ay','ah','sh']
print('lists is here')
print(lists[0],lists[1])
list=[['hello','oola'],['gig',2],[3,4,[6,7]]]
print(list[0])
lists.append(3)#only one elemnet can be added at a time. append is used to add a elemnet at the end.
lists.append((3,3,3))
lists.append([3,4,5,5,5])
for y in range(0,10): #output ['ay', 'ah', 'sh', 3, (3, 3, 3), [3, 4, 5, 5, 5], 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lists.append(y)
#print(lists)
lists.insert(1,4)
print(lists)#output['ay', 4, 'ah', 'sh', 3, (3, 3, 3), [3, 4, 5, 5, 5], 0, 1, 2, 3, 4, 5, 6, 7, 8, 9] on 1st index there is 4. and the data of 1st is not overwriten.
lists.extend([999,4,00000,3333])#same as append but it's output is ['ay', 4, 'ah', 'sh', 3, (3, 3, 3), [3, 4, 5, 5, 5], 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999, 4, 0, 3333]
# but it is mutable.
print(lists)
lists.extend((3,4,00000,3333)) #output is ['ay', 4, 'ah', 'sh', 3, (3, 3, 3), [3, 4, 5, 5, 5], 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999, 4, 0, 3333] but is it is not mutable
# coz inside there is  tuple
print(lists)
print(list[0][0])
print(list[2][2][0],list[1][0])#multidimenal array
print(list[-3])
lists.remove(3)#it only removes the 1st searched mached item from the list not the item from that (written no. as arrgument) index. it takes only one no. as arrgument.
print(lists)
list.pop(2)#it removes the item from the index 2 (written no. as arrgument) in the list names as list. it takes only one no. as arrgument.
print(list)
#list sclicing
list1=[11,2,3,4,5,6,7,8,9,10]
slice_list=list1[0:2]
slice_list1=list1[:2]
slice_list2=list1[:-2]
slice_list3=list1[::-1]
slice_list4=list1[0:-2:5]# internet!!!!
slice_list5=list1[:-1:]
slice_list6=list1[-1::]
slice_list7=list1[:5]
print(slice_list)#output [11, 2]
print(slice_list1)#output [11, 2]
print(slice_list2)#output [11, 2, 3, 4, 5, 6, 7, 8]
print(slice_list3)#revise list output [10, 9, 8, 7, 6, 5, 4, 3, 2, 11]
print(slice_list4)
print(slice_list5)#output [11, 2, 3, 4, 5, 6, 7, 8, 9]
print(slice_list6)#output [10]
print(slice_list7)#output [11, 2, 3, 4, 5]
list.clear()#it remove all items from list.
print(list)
print(list1.index(2))#retturn the index of first matched item.
#lists=['ay', 4, 'ah', 'sh', (3, 3, 3), [3, 4, 5, 5, 5], 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999, 4, 0, 3333, 3, 4, 0, 3333]
print(lists.count(3))#output is 2 coz here the 3 exists 2 times.it returns count of no. of items passed as arrgument.
list2=[85,536373,34,5,1,5,4,3]
#internet!!!! all below threee
print(list2.sort())# sort the item in ascending order of the list.
print(list2.reverse())#reverse the order of the order of item.
print(list2.copy()) #returns a copy of the list.
#list Method
# append()
# extend()
# insert()
# remove()
# pop()
# clear()
# index()
# count()
# sort()
# reverse()
# copy()
