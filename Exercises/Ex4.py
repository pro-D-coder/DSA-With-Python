'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''


def small_sum(number):
    if number < 0:
        raise ValueError(str("Value Must Be Positive"))
    sum = 0
    counter = number-1
    while counter > 0:
        sum = sum + (counter*counter)
        counter -= 1
    return sum


if __name__ == '__main__':
    num = int(input("Enter A Number: "))
    print("Sum = {0}".format(small_sum(num)))
