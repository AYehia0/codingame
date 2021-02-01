w, h, count_x, count_y = [int(i) for i in input().split()]

x_counts = [0]
y_counts = [0]

all_x = []
all_y = []

ans = 0

for i in input().split():
    x = int(i)
    x_counts.append(x)

x_counts.append(w)
for i in input().split():
    y = int(i)
    y_counts.append(y)

y_counts.append(h)

# print(x_counts)
# print(y_counts)

for i in range(len(x_counts) -1):
    for j in x_counts:
        if j-x_counts[i] > 0:
            all_x.append(j-x_counts[i])

for i in range(len(y_counts) -1):
    for j in y_counts:
        if j-y_counts[i] > 0:
            all_y.append(j-y_counts[i])


# print(all_x)
# print(all_y)

# Slow way to do it
# for i in all_x:
#     for j in all_y:
#         if i == j:
#             ans += 1

# Optimized way to do it 
print(sum([all_y.count(i) for i in all_x]))

