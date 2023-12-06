#Create an empty tuple
empty_tuple = ()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Brothers = ('Lautai',  'Kabiru',  'Abdu')
Sisters = ('Ladi','Kande','Ikilima','Lantana')

#Join brothers and sisters tuples and assign it to siblings
siblings = Brothers + Sisters
print(siblings)

#How many siblings do you have?
No_of_siblings =len(siblings)
print(f'I have {No_of_siblings} siblings')

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Siblings = list(siblings)
Siblings.append('Abba')
Siblings.append('Umma')
family_members = tuple(Siblings)
print(f'My family members are : {family_members}')

#Unpack siblings and parents from family_members

Fam = list(family_members)

*scadic, Abba, Umma = Fam
print('siblings unpacked from family members', scadic)
idi, Dm, Auduwa, Ladidi, Kandala, iki, Lanto, *parents = Fam
print('Parents unpacked from family members',parents)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ('lemon', 'pear', 'apple', 'cashew')
vegetables = ('carrots', 'tomato', 'lettuce', 'potato')
animals_products = ('meat', 'eggs', 'hide','milk', 'cheese')
food_stuff_tp = fruits + vegetables + animals_products
print('Food stuff tuple is : ' , food_stuff_tp )

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print('Food stuff list is : ' , food_stuff_lt )

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
No_of_foodstuff = len(food_stuff_lt)
middle_item = No_of_foodstuff // 2
slicing_middle_item = food_stuff_lt[middle_item]
print('The middle item is ',slicing_middle_item)

#Slice out the first three items and the last three items from food_staff_lt list
first_3_items = food_stuff_lt[0:3]
print('the first three items are ', first_3_items)
last_3_items = food_stuff_lt[-4:-1]
print('the last three items are ', last_3_items)

#del food_stuff_tp
del food_stuff_tp

#Check if an item exists in tuple:
    #Check if 'Estonia' is a nordic country
    #Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('checking whether Estonia is a nordic country :', 'Estonia' in nordic_countries)
print('checking whether Iceland is a nordic country :', 'Iceland' in nordic_countries)