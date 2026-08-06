# Read how many numbers will be entered
n = int(input())

# Initialize the counters and total
zero = 0
pos = 0
neg = 0
total = 0

# Read and process each number
for i in range(n):
    value = int(input())
    total = total + value

    if value == 0:
        zero = zero + 1
    elif value > 0:
        pos = pos + 1
    else:
        neg = neg + 1

# Display the results
print("Positive Count:", pos)
print("Negative Count:", neg)
print("Zero Count:", zero)
print("Total:", total)