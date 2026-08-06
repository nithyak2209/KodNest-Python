limit = int(input())
target = int(input())

count_values = []
count = 0
total = 0
found = False

for i in range(1, limit):
    if i % 3 == 0:
        count = count + 1
        count_values.append(i)

for i in count_values:
    total = total + i

for i in count_values:
    if i == target:
        found = True

print("Count:", count)
print("Sum:", total)

if found:
    print("Target Found: Yes")
else:
    print("Target Found: No")