'''
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution
'''


def minmax(data):
    min = data[0]
    max = data[0]
    if len(data) == 1:
        return (data[0], data[0])
    for i, j in enumerate(data):
        if(i == 0):
            continue
        if(j >= max):
            max = j
        if(j <= min):
            min = j

    return (min, max)


if __name__ == "__main__":
    try:
        input_seq = list()
        print("Press q for stopping the input")
        while(True):
            value = input("Enter Number: ")
            if value != 'q':
                input_seq.append(int(value))
            else:
                break
        print(minmax(input_seq))
    except(ValueError):
        print("Passing Value to MinMax")
        print(minmax(input_seq))
