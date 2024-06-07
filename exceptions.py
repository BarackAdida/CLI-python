numerator = 10
denominator = 2

try:
    result = numerator / denominator
    result = numerator * denominator
except ZeroDivisionError as e:
    print(f"Exception: {e}")
finally:
    print("Finally we're done")
# print(result)
print("End of execution")

def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18!")
    return "Access granted!!"


print(check_age(19))
