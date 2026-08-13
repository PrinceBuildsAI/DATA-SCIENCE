
num = [1, 2, 3, 4]

iter_object = iter(num)

while True:
    try:
        print(next(iter_object))
    except:
        break
    