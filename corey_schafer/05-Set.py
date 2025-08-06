print("-----------------------------------------------------")
print("SET")
print("A set is an unordered, unindexed and mutable collection of unique elements.")
print("-----------------------------------------------------")
print("Duplicate elements are removed automatically in a set.")
print("Set containing without duplicates:")
print("RESULT:")
my_set = {1, 2, 3, 4}
print(my_set)
print("Set containing with duplicates:")
print("RESULT:")
dup_set = {1, 2, 2, 3, 4}
print(dup_set)  # Output: {1, 2, 3, 4}
print("-----------------------------------------------------")
print("Indexing is not allowed.")
print("-----------------------------------------------------")
print("Set is more optimized when compared to tuples/list")
fruits = {"apple", "banana", "apple", "mango"}
print('kiwi' in fruits)
print('apple' in fruits)
print("-----------------------------------------------------")
print("SCENARIO 1: Intersection between 2 sets")
cs_courses={'History','Math','Physics','CompSci'}
art_courses={'History','Math','Art','Design'}

print(cs_courses.intersection(art_courses))
print("-----------------------------------------------------")
print("SCENARIO 2: Union between 2 sets")
cs_courses={'History','Math','Physics','CompSci'}
art_courses={'History','Math','Art','Design'}

print(cs_courses.union(art_courses))
print("-----------------------------------------------------")
print("SCENARIO 3: Empty List, Empty Tuple, Empty Set")
print("Empty List")
empty_list=[]
empty_list=list()
print("Empty Tuple")
empty_tuple=[]
empty_tuple=tuple()
print("Empty Sets")
print("This is not right -> We cannot create empty set. If we do the below -> this will create an empty dictionary")
empty_set={}
print("The only way to create empty set is through -> `set()`. The below code is the correct way to create empty set.")
empty_set=set()
print("-----------------------------------------------------")


print("-----------------------------------------------------")







