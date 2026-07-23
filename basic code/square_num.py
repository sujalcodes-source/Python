# squares = []
# for value in range(0,11):
#     square = value*value
#     squares.append(square)
# print(square)

squares = []
for value in range(1, 11):
 square = value ** 2
 squares.append(square)
print(squares)

print(max(squares))
print(min(squares))
print(sum(squares))