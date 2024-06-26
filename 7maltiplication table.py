def multiplication_table(number):
    i = 1
    while i <= 10:
        print(f"{number} x {i} = {number * i}")
        i += 1

number = int(input("enter number: "))
multiplication_table(number)
