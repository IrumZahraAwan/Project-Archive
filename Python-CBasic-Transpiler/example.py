def isprime():
    prime = True
    for x in n ** 0.5:
        if n % x == 0:
            prime = False

def fizzbuzz():
    for x in range(100):
        if x % 3 == 0:
            if x % 5 == 0:
                print("Fizzbuzz")
            else:
                print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

fizzbuzz()
n = 11
isprime()
