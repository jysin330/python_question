def reverse_data(data):
    reversed_data = int(str(data)[::-1])
    return reversed_data

# Example usage
data = input("enter: ")
reversed_data = reverse_data(data)
print(reversed_data)