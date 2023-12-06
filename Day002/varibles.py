#  'Day 2: 30 Days of python programming'

first_name = 'Rahma'
last_name = 'Aliyu'
full_name ='Rahma Aliyu Yusuf'
country = 'Nigeria'
city = 'Kano'
age = 77
year = 1034
is_married = False
is_true = False
is_light_on = True
name, her_age , is_alive, complx_num = 'HAyaa', 700, False, 2 - 2j

print('checking the data types of my variables')

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(name))
print(type(her_age))
print(type(is_alive))

print("comparing the lenght of firstName and last name")

len_Fname = len(first_name)
len_Lname = len(last_name)
print(max(len_Fname,len_Lname))

print("soe little calculations ")
num_one = 5
num_two = 4
Total= num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
pi = 3.14
Area_of_circle = 2 * radius **2 * pi
print(Area_of_circle)
circum_of_circle =2 * radius * pi


r = int(input("enter the radius"))
Area = r ** 2 * pi
print(' The area of the circle is ', Area)


First_Name = input( "enter your first name")
Last_Name = input ("enter your Last name")
Country = input(" enter your country")
Age = int (input ("enter your age"))

print('First Name is ',First_Name,'Last_Name is',Last_Name,'Country is', Country,'and his age is ', Age )



help('keywords')