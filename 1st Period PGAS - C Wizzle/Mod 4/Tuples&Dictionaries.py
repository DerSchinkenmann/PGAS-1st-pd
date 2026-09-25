#[list]
#(tuple) 
#{dictionary}

#these are the three main data structures

#tuples are essentially immutable lists. Tuples are typically used for 
#the attributes of a single entity, whereas a list is is typically a 
#collection of similar items
tuplevar = ('name', 'age', 'occupation')

listvar = ['alice', 'bob', 'charles']

#you can use them similarly, but a tuple is not meant to be changed
#(immutable), and can be used as keys in ditionaries or elements in sets


#A dictionary is a data type that assigns a value to a key. Dictionaries
#are one way(meaning a key goes to a value, not the other way around),
#mutable, and not indexed. Each key is unique, meaning you cant have more
#than one key per value. A key is immutable(this does not mean the dictionary is immutable,
#but the key is), and can be a number or 
#string, but not a list

#by default, dictionaires are unordered, but in newer versions (3.6.x) 
#dictionaries are ordered. For the test, they are not ordered

#the len() func works for dictionaries, but only counts the pairs

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

print(dictionary['cat'])
print(phone_numbers['Suzy'])

dictionary = {"cat": "chat", 
              "dog": "chien", 
              "horse": "cheval"
              }
#this is a more cromulent way of writing dictionaries, lengthy 
#expressions benefit from vertical allignment by increasing legibility

#the method keys() returns every key that the dictionary has.
print(dictionary.keys())

#the method items() returns every pair as a tuple
print(dictionary.items())

#the method values returns ever value assigned to a key
print(dictionary.values())

#while dictionary keys are immutable, the values themself are. 
#this means that you can change the value associated with a key
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)

#you can also add key pairs to dictionaries,
dictionary['swan'] = 'cygne'
print(dictionary)

#and there is a method to do so if you prefer
dictionary.update({"duck": "canard"})
print(dictionary)

#you can use the del() func to delete key pairs as well
del dictionary['dog']
print(dictionary)

#the popitem() method deletes the last item of an ordered dictionary,
#but in older versions of python, unordered dictionaries are the standard
#so this method would just delete a random item.

school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
#this is an example of dictionaries and tuples working together