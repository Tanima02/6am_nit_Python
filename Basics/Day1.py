
aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]
oneMoreList = [22, 34, 56,34, 34, 78, 98]
oneMoreList1 = [23, 35, 57,35, 35, 79, 99]
#count
print(aCoolList.count(22))

print(aCoolList.count('spiderman'))
#Delete
print(oneMoreList.count(34))
del(oneMoreList[2])
print(oneMoreList)
#Extend
print(aCoolList.extend(oneMoreList))
print (aCoolList)
 #index
print (aCoolList.index(78))
#insert
aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]

oneMoreList = [22, 34, 56,34, 34, 78, 98]
#Enumerate
print(aCoolList,tuple(enumerate(aCoolList)))
print("")
aCoolList.insert(0,"Guido Van Rossum")
print(aCoolList)
#print(aCoolList,list(enumerate(aCoolList)))
#print (oneMoreList,list(enumerate(oneMoreList)))
#print("")

a_list = [1, 2, 3]

print(a_list,type(a_list),id(a_list),len(a_list))
print(list(enumerate(a_list)))

a_list.append(4)

print(a_list,type(a_list),id(a_list),len(a_list))
print(list(enumerate(a_list)))

a_list.append([5, 6, 7])
print(a_list,type(a_list),id(a_list),len(a_list))
print(list(enumerate(a_list)))

a_list.append("Guido")
print(a_list,type(a_list),id(a_list),len(a_list))
print(list(enumerate(a_list)))


list1, list2 = ['123','!','a','abc', 'xyz', 'ABC'], [456, 700, 200]

print ("Min value element : ", min(list1))
print ("Max value element : ", max(list1))

print ("Min value element : ", min(list2))
print ("Max value element : ", max(list2))

aCoolList = ["superman", "spiderman", 1947,1987,1947,"Spiderman"]
oneMoreList = [22, 34, 56,34, 34, 78, 98]

print (list(enumerate(aCoolList)))

aCoolList.remove(1947)
aCoolList.pop()
aCoolList.pop(3)
print("")
print(list(enumerate(aCoolList)))

aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]
oneMoreList = [22, 34, 56, 34, 34, 78, 98]

# sorting and reversing
print (oneMoreList)
oneMoreList.reverse()
print ("After Reverse Method : ",oneMoreList)

print(aCoolList)
aCoolList.reverse()
print("After Reverse Method : ",aCoolList)

aCoolList = ["c","5","A","!","k"]
oneMoreList = [98, 34, 56,10, 34, 78, 2]

print(aCoolList)
aCoolList.sort()
print(aCoolList)

print (oneMoreList)
oneMoreList.sort()
print (oneMoreList)