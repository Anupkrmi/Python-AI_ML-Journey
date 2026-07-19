print("Dictionaries in Python are used to store data in key-value pairs.")
my_dict = {"name" : "Anup",
           "age" : 19,
           "city" : "Pune"}

print("The dictionary is:", my_dict)
print("The keys of the dictionary are:", my_dict.keys())
print("The values of the dictionary are:", my_dict.values())
print("type of the dictionary is:", type(my_dict))
print("The value of the key 'name' is:", my_dict["name"])
print("The value of the key 'age' is:", my_dict["age"])
print("The value of the key 'city' is:", my_dict["city"])
print("Dictionaries in Python are mutable, meaning you can change their content.")
print("The dictionary after adding a new key-value pair is:", my_dict)
my_dict["country"] = "India"

print("Dictionaries can hold variables of different data types, including lists and tuples.")
my_dict["hobbies"] = ["reading", "swimming"]
print("The dictionary after adding a list as a value is:", my_dict)

dict_with_different_types = {"name" : "Anup",
                             "age" : 19,
                             "is_student" : True,
                             "hobbies" : ["reading", "swimming"],
                             "address" : ("Pune", "Maharashtra")}
print("The dictionary with different data types is:", dict_with_different_types)

print("Nested Dictionaries are dictionaries within dictionaries.")
nested_dict = {"person1" : {"name" : "Anup", "age" : 19},
               "person2" : {"name" : "Rahul", "age" : 20}}
print("The nested dictionary is:", nested_dict)


print("Sets in Python are used to store multiple items in a single variable.")
my_set = {"apple", "banana", "cherry"}
print("The set is:", my_set)
print("Sets are unordered, meaning the items have no defined order.")
print("Sets are unindexed, meaning you cannot access items in a set by referring to an index or a key.")
print("Sets are mutable, meaning you can add or remove items from a set after its creation.")
my_set.add("orange")
print("The set after adding a new item is:", my_set)
my_set.remove("banana")
print("The set after removing an item is:", my_set)
print("Sets do not allow duplicate items. If you try to add a duplicate item, it will be ignored.")
my_set.add("apple")
print("The set after trying to add a duplicate item is:", my_set)
print("Sets can be used to perform mathematical set operations like union, intersection, difference, and symmetric difference.")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("The first set is:", set1)
print("The second set is:", set2)
print("The union of the two sets is:", set1.union(set2))
print("The intersection of the two sets is:", set1.intersection(set2))
print("The difference of the two sets is:", set1.difference(set2))
print("The symmetric difference of the two sets is:", set1.symmetric_difference(set2))
print("Sets can also be used to check for membership, meaning you can check if an item is present in a set or not.")
print("Is 3 present in set1?", 3 in set1)
print("Is 9 present in set1?", 9 in set1)
print("Empty sets can be created using the set() function, and they can be used to store unique items.")
empty_set = set()
print("The empty set is:", empty_set)
print("Type of the empty set is:", type(empty_set))
