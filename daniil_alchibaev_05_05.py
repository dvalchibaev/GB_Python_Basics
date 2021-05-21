src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result_01 = [element for element in src if src.count(element) == 1]
print(result_01)

# alternative solution
appeared = set()
result = []
