num1 = 4
num2 = 52
id1 = f"{num1}0{num2}"

print(type(id1))
list1 = [int(i) for i in id1]
print(list1)
new_id = id1.split('0')
print(new_id)