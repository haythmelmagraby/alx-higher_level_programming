#!/usr/bin/python3
def uppercase(str):
    for i in str:
        print("{:c}".format(
            ord(i) - 32 if ord(i) >= ord('a') and ord(i) <= ord('z')
            else ord(i)
            ), end="")
    print()
