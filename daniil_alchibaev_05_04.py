src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

results = [src[index] for index in range(1, len(src)) if
           src[index-1] < src[index]]

print(results)
