a = 5
b = 4
try:
    print("Open")
    k = int(input("Enter the number: "))
    print(k)
    print(a / b)

except ZeroDivisionError as e:
    print("Hey you can't divide a number by 0", e)

except ValueError as e:
    print("Input invalid", e)

except Exception as e:
    print("Something went wrong...")

finally:
    print("Closed")
