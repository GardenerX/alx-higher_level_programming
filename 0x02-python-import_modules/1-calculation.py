#!/usr/bin/python3
if __name__ == '__main__':
 from calculator_1.py import add, sub, mul, div
a = 10
b = 5

print("{}".format(a), "+", "{}".format(b), "=", "{}".format(add(a, b)), end='\n')
print("{}".format(a), "-", "{}".format(b), "=", "{}".format(sub(a, b)), end='\n')
print("{}".format(a), "*", "{}".format(b), "=", "{}".format(mul(a, b)), end='\n')
print("{}".format(a), "/", "{}".format(b), "=", "{}".format(div(a, b)), end='\n')
