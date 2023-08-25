# --------->isdisjoint()
# cities={"tokyo","madrid","barlin","delhi"}
# cities2={"tokyo","madrid","seoul","kabul"}
# cities3={"barlin","delhi"}
# print(cities.isdisjoint(cities2))
# print(cities2.isdisjoint(cities3))

# --------->issuperset()
# cities={"tokyo","madrid","barlin","delhi"}
# cities2={"tokyo","madrid"}
# print(cities.issuperset(cities2))

# ---------->issubset()
# cities={"tokyo","madrid","barlin","delhi"}
# cities2={"tokyo","madrid"}
# print(cities2.issubset(cities))

# ----------->add() 
# cities={"tokyo","madrid","barlin","delhi"}
# cities.add("ydygwg7q6")
# print(cities)

# --------->update()
# cities2={"tokyo","madrid","seoul","kabul"}
# cities3={"barlin","delhi"}
# cities2.update(cities3)
# print(cities2)

# ---------->remove() and discard()
# cities2={"tokyo","madrid","seoul","kabul"}
# cities2.remove("tokyo")
# print(cities2)
# cities2.remove("delhi") #throw an error
# print(cities2)
# cities2.discard("delhi") #not throwing any error
# print(cities2)

# ---------->pop()
# cities2={"tokyo","madrid","seoul","kabul"}
# item=cities2.pop()
# print(cities2)
# print(item)

# --------->del
# cities2={"tokyo","madrid","seoul","kabul"}
# del cities2
# print(cities2)

# ---------->clear()
cities2={"tokyo","madrid","seoul","kabul"}
cities2.clear()
print(cities2)