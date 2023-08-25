countries=("spain","italy","india","england","germany")
temp=list(countries)
temp.append("russiA");
temp.pop(3)
temp[2]="finland"
countries=tuple(temp)
print(countries)