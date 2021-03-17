#Hands on #1

import matplotlib.pyplot as plt

# cubed = []
# inputVal = [1,2,3,4,5]
# for num in inputVal:
#     cubed.append(num*num*num)
# plt.plot(inputVal,cubed)
# plt.title("Cubed Numbers")
# plt.ylabel("Values Cubed")
# plt.xlabel("Input Values")
# plt.grid()
# plt.show()

#Hands on #2

# squared = []
# inputVal = [1,2,3,4,5]
# for num in inputVal:
#     squared.append(num*num)
# ax1 = plt.subplot(1,2,1)
# ax1.plot(inputVal,squared)
# plt.title("Squared Numbers")
# plt.ylabel("Values Squared")
# plt.xlabel("Input Values")
# plt.grid()

# cubed = []
# inputVal2 = [1,2,3,4,5]
# for num in inputVal2:
#     cubed.append(num*num*num)
# ax2 = plt.subplot(1,2,2)
# ax2.plot(inputVal,cubed)
# plt.title("Cubed Numbers")
# plt.ylabel("Values Cubed")
# plt.xlabel("Input Values")
# plt.grid()

# plt.suptitle("Fun with Numbers")
# plt.show()

#Hands on #3

# squared = []
# inputVal = [1,2,3,4,5]
# for num in inputVal:
#     squared.append(num*num)
# ax1 = plt.subplot(1,2,1)
# ax1.plot(inputVal,squared, marker="*",c="blue",lw="2.0",ls="--")
# plt.title("Squared Numbers")
# plt.ylabel("Values Squared")
# plt.xlabel("Input Values")
# plt.grid()

# cubed = []
# inputVal2 = [1,2,3,4,5]
# for num in inputVal2:
#     cubed.append(num*num*num)
# ax2 = plt.subplot(1,2,2)
# ax2.plot(inputVal,cubed, marker="p",c="red",lw="2.0",ls=":")
# plt.title("Cubed Numbers")
# plt.ylabel("Values Cubed")
# plt.xlabel("Input Values")
# plt.grid()

# plt.suptitle("Fun with Numbers",c="green",fontsize="18")
# plt.subplots_adjust(top=.8,wspace=1)
# plt.show()

#Hands on #4

squared = []
inputVal = [1,2,3,4,5]
for num in inputVal:
    squared.append(num*num)
ax1 = plt.subplot(1,2,1)
ax1.plot(inputVal,squared, marker="*",c="blue",lw="2.0",ls="--")
plt.title("Squared Numbers")
plt.ylabel("Values Squared")
plt.xlabel("Input Values")
plt.grid()

cubed = []
inputVal2 = [1,2,3,4,5]
for num in inputVal2:
    cubed.append(num*num*num)
ax2 = plt.subplot(1,2,2)
plt.style.use("seaborn-pastel")
ax2.plot(inputVal,cubed, marker="p",c="red",lw="2.0",ls=":")
plt.title("Cubed Numbers",color="red")
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")
plt.grid()

plt.suptitle("Fun with Numbers",c="green",fontsize="18")
plt.subplots_adjust(top=.8,wspace=1)
plt.show()