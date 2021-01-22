print("------Exercise 3-10------")
lakes = ["Superior","Michigan","Torch","Elk"]

print(f"Original List:  {lakes}")

lakes.append("Boardman")
print(f"List with append: {lakes}")

lakes.insert(0,"Glen")
print(f"List with insert: {lakes}")

del lakes[0]
print(f"List with delete: {lakes}")

removedLake = lakes.pop()
print(f"Lakes with pop: {lakes}")

lakes.remove("Torch")
print(f"Lakes with remove: {lakes}")

print(f"Lakes using sorted: {sorted(lakes)}")

lakes.reverse()
print(f"Lakes using reverse: {lakes}")

lakes.sort()
print(f"Lakes using sort: {lakes}")

print(f"There are {len(lakes)} lakes in the final list.")
