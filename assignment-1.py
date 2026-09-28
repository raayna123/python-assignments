print("LIST OPERATIONS")
names=["Raayna", "Dhriti", "Dishita", "Himanshu", "Aditya"]
print("Original List: ", names)
names.append("Arnav")
names.insert(3, "Kyra")
names.remove("Kyra")
names.pop(3)
print("Modified list: ", names)
print("")

print("TYPLE OPERATIONS")
num=(10,20,10, 50, 30, 10, 20, 40)
print(num.count(10))
print(num.index(20))
print(len(num))
print(sum(num))
print(sorted(num))
print("")

print("DICTIONARY OPERATIONS")
dict={"name": "Raayna", "age": 18}
print("Original Dictionary: ", dict)
print(dict.keys())
print(dict.values())
for key,value in dict.items():
    print(f"{key}:{value}")
print(dict.get("name"))
dict.update({"gender": "female"})
print("Modified Dictionary: ", dict)