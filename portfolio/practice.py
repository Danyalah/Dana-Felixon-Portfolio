#Write a program that computes the sum of the first 20 positives integers
def sumInts():
    sum = 0
    for i in range(0, 20):
        sum = i + sum
    return sum

print(sumInts())
