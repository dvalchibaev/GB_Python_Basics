# lesson 05 task 01
def odd_nums(limit):
    # по ТЗ до n ВКЛЮЧИТЕЛЬНО, поэтому +1
    for odd in range(1, limit+1, 2):
        yield odd


odd_gen = odd_nums(15)
for _ in range(4):
    print(next(odd_gen))


# lesson 05 task 02
def odd_gnrtr(limit):
    # по ТЗ до n ВКЛЮЧИТЕЛЬНО, поэтому +1
    return (x for x in range(1, limit+1, 2))


odd_gen2 = odd_gnrtr(15)
for _ in range(4):
    print(next(odd_gen2))
