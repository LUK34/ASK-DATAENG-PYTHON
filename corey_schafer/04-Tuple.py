print("-----------------------------------------------------")
print("TUPLES")
print("The main difference between List and tuples is that.")
print("LIST is MUTABLE")
print("TUPLE is IMMUTABLE")
print("-----------------------------------------------------")
print("count() method -> to count how many elements are present in the tuple")
tuple_1=(1,2,3,2,5,4,5,5,5,5,5,5,5)
print(tuple_1.count(2))
print(tuple_1.count(5))
print("-----------------------------------------------------")
print("index() method -> to extract the index value of the tuple")
print("this will take the index value of the first occurrence")
print(tuple_1.index(2))
print(tuple_1.index(5))
print("-----------------------------------------------------")
print ("min() method:")
print(min(tuple_1))
print ("max() method:")
print(max(tuple_1))
print ("sum() method:")
print(sum(tuple_1))
print("-----------------------------------------------------")
print("Tuple does not support item assignment -> IMMUTABLE")
tuple_1=('History','Math','Physics','CompSci')
tuple_2=tuple_1
print(tuple_1)
print(tuple_2)
#tuple_1[0]='Art'
#print(tuple_1)
#print(tuple_2)
print("-----------------------------------------------------")





