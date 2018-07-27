#making lists

friends = ["Beyonce", "Jay-Z", "Chrissy Teigen", "Barack Obama", "Stephen Colbert"]
weights = [153.4, 81.2, 1293.4, 432.6]
random_data = ["George", 8, 10.2]

womenInTech = ["Dorothy Vaughn", "Cindy Alvarez", "Amanda Randles"]
print(womenInTech)
print(len(womenInTech))
print("Dorothy Vaughn" in womenInTech)
# Output: True
print("Jane Doe" in womenInTech)
# Output: False

numbers = [1, 2, 3, 2, 1]
for num in numbers:
    print(num)

for i in range(len(numbers)):
    print(numbers[i])

anExample = "Ada!"
print(len(anExample))
# Output 4:
print("da" in anExample)
# Output: True
print(anExample[2])
# Output: a
print(anExample[2] + anExample[1])
# Output ad
for letter in anExample:
    print(letter)
# Output: A
# Output: d
# # Output: a
# # Output: !

amigos = ["Samia", "Thanni", "Mourie", 2]
print(amigos)
print(len(amigos))
print("Samia" in amigos)
print("Fabia" in amigos)

for letters in amigos:
    print(letters)

# list.append() vs list.extend()
list = ["larry", "curly", "moe"]
list.append("shemp")
print(list)

list.extend(["harry", "richard"])
print(list)

list2 = ["harry", "richard"]
list.extend(list2)
print(list)

#Finding the Average
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
#ages.sort() rearranges the numbers
total = sum(ages)
average = (total / len(ages))
print(average)

#Another Way to Find Average
total = 0
for item in ages:
        total+= item
#means total = total + item
average = total/len(age)
print(average)
