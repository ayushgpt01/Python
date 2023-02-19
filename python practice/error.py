# error handling

while True:
    try:
        age = int(input("Enter Your Age :"))
        print(2/age)
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Zero not accepted")
    else:
        print(f"Your age is : {age}")
        break
    finally:
        print("This ALWAYS runs")


# def func(num1,num2):
#     try:
#         return num1/num2
#     except (TypeError,ZeroDivisionError) as err:
#         print(err)

# print(func(1,0))