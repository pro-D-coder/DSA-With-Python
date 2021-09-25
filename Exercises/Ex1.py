'''
Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise
'''


def is_multiple(n, m):
    for i in range(1, m):
        product = i * n
        if(product == m):
            return True
    return False


if __name__ == "__main__":
    n = int(input("Enter Number: "))
    m = int(input("Enter Another Number: "))
    print(is_multiple(n, m))
