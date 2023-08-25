cities={"tokyo","madrid","barlin","delhi"}
cities2={"tokyo","madrid","seoul","kabul"}
cities3=cities.difference(cities2)
print(cities3)
cities.difference_update(cities2)
print(cities)