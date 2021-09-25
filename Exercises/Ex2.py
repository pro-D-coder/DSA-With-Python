'''
Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
'''


def is_even(number):
    unit_digit = ['0', '2', '4', '6', '8']
    last_digit = number[len(number) - 1]
    if last_digit in unit_digit:
        return True
    return False


if __name__ == '__main__':
    num = input('Enter A Number: ')
    print(is_even(num))
