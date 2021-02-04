#Hands On #1
#Exercise 8-3
print("-----Exercise 8-3-----\n")

def make_shirt(shirt_size, shirt_message):
    print(f"The size of the shirt is '{shirt_size}'.")
    print(f"The message on the shirt is '{shirt_message}'.\n")

make_shirt('small','hello, world')
make_shirt(shirt_size='large', shirt_message='keep it real')

#Exercise 8-4
print("-----Exercise 8-4-----")

def make_shirt2(shirt_size='large', shirt_message='I love Python'):
    print(f"The size of the shirt is '{shirt_size}'.")
    print(f"The message on the shirt is '{shirt_message}'.\n")

make_shirt2(shirt_size='large')
make_shirt2(shirt_size='medium')
make_shirt2(shirt_message='Python is OK.')