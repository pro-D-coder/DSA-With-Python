'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n
'''


def small_odd_sum(number):
    sum = 0
    if(number < 0):
        raise ValueError("Must be Positive")
    for i in range(number-1, 2, -1):
        if i % 2 != 0:
            sum += i*i
    return sum
    '''OR
    sum([i*i for i in range(int(input("Enter Number: ")),2,-1)  if i % 2 != 0])
    '''


if __name__ == '__main__':
    print(small_odd_sum(int(input("Enter A Number: "))))
