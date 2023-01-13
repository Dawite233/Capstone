
# Variables 

school = 'MCTC'
gpa = 3.7
student_in_class = 22

# If-statement 

if gpa == 4:
    print('WOW!!!')

elif gpa > 3:
    print('Asesome!')




else:
    print('Cool!')
# if-elif-else 

# lists

schools =['MCTC', 'DCTC', 'North Hennepin Technical COllge', 'Invert Hill Technical Collge']
if 'MCTC' in schools:
    print('MCTC is one of the schools in the list.')


schools.sort()
print(schools)
schools.append('Century College')
print(school)




schools.reverse() # returns None
print(schools)



# in operator


# Strings
class_name = 'Software Development Capstone'
print(class_name.upper())
print(len(class_name))
print(class_name.split())
print(class_name.split('o'))
print(class_name.expandtabs())

if 'Capstone' in class_name:
    print('This must be the capstone course.')


# loops - for loops over range 
# loops - for loops over sequence 
for D in range(12):
    print(D)


for s in schools:
    print(s.upper())

for letter in school:
    print(letter)

for d in schools:
    print(d)

for letter_num in school:
    print(letter_num * 13)


data = [0] * 10 
print(data)

name_multi = ['Dawit'] * 10 
print(name_multi)

for D_10  in name_multi:
    print(D_10)

more_data = [None] * 10
print(more_data)

more_datas = [' Dawite Gebrekerstos '] * 12
print(more_datas)

for DG_12 in more_datas:
    print(DG_12)


# while loops 

name = input('Enter your name: ')
while not name:
    print('Please enter at least one character ')
    name = input(' Enter your name: ')




# True and False and None

start_of_semster = True
winter = False


if winter: # if winter == True:
    print('brrrrrrr')
else:
    print('It is not winter')


# Dictionaries

class_codes = { 2905: 'Captone', 2560: 'Web', 2545: 'Java'}

print(class_codes[2560])

for code in class_codes:
    print(code)
    print(class_codes[code])


for code, name in class_codes.items():
    print('The class code is ' + str(code) +  ' and the name is ' + name + '.' )



for code, name in class_codes.items():
    print(f'The class code is  {code} and the name is {name}. ')


# Slicing string, lists

dishes = ['Doro', 'Cheese burger', 'Egg adn cheese burger', 'cheken with rice', 'cheese curt', 'Kitfo']





first_2 = dishes[0:3]  # first_2 = dishes[:2]
print(first_2)


for D2 in dishes:
    print(D2)

last_school = schools[-1]
print(last_school)

last_food = dishes[-1]
print(last_food)

school_name = 'Minneapolis Community and Technical College '
city = school_name[:11]
print(city)

last_two_school = schools[-2:]
print(last_two_school)



# file 10 

with open('data.txt') as f:
    print(f.read())

with open('schools.txt', 'w') as f:
    f.writelines(schools)


# Function 

def get_name():
    print('Hello, please enter your name!')
    name = input('Your name is: ')
    return name

name = get_name()





