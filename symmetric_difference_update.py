cities={"tokyo","madrid","barlin","delhi"}
cities2={"tokyo","madrid","seoul","kabul"}
cities3=cities.symmetric_difference(cities2)
print(cities3)
cities.symmetric_difference_update(cities2)
print(cities)