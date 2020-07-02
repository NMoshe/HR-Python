'''You are given two non-empty linked lists representing two non-negative integers.
   The digits are stored in reverse order and each of their nodes contain a single digit.
   Add the two numbers and return it as a linked list.

   You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''


def addTwoNumbers(l1, l2):
    se1, se2 = '', ''
    for x in l1[::-1]:
        se1 += str(x)
    for x in l2[::-1]:
        se2 += str(x)
    return print(int(se1) + int(se2))


addTwoNumbers([3, 4, 2], [4, 6, 5])
