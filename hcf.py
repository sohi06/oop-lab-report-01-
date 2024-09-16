def hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 48
num2 = 18
print(f"HCF of {num1} and {num2} is {hcf(num1, num2)}")