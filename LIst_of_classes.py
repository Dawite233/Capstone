classes = []

class_name = input('Enter class name? Enter to quit! ')

while class_name:
    classes.append( class_name )
    class_name = input('Enter class name? enter to quit! ')

print(classes)


for index, c in enumerate (classes):
    print(f'{index+1}: {c} ')