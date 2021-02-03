#7-8
print('-----Exercise 7-8-----')

sandwich_orders = ['BLT','Club','Pastrami','Chicken Parm','Pastrami','Turkey','PB&J','Pastrami']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Preparing Sandwich: {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches that have been made:")
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches)

#7-9
print("\n-----Exercise 7-9-----")

sandwich_orders = ['BLT','Club','Pastrami','Chicken Parm','Pastrami','Turkey','PB&J','Pastrami']
finished_sandwiches = []

print("Sorry! We are out of Pastrami sandwiches.\n")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Preparing Sandwich: {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches that have been made:")
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches)
