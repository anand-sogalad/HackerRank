#  Given an array of integers, where all elements but one occur twice, find the unique element.
def lonely_int(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num


# grade rounding based on the given condition
# condition:
# below 38 should not be rounded
# if the difference between grade and its next multiple of 5 is less thann 3,
# only then grade shoukld be rounded to its next multipole of 5
def grade_roundup(grades):
    rounded_grades = []
    for grade in grades:
        if grade > 37 and grade % 5 > 2:
            grade += 5 - grade % 5
        rounded_grades.append(grade)
    return rounded_grades


def flipping_bits(n):
    return n ^ 0xFFFFFFFF


def diagnal_difference(arr):
    left_to_right = 0
    right_to_left = 0
    for idx, row in enumerate(arr):
        left_to_right += row[idx]
        right_to_left += row[-(idx + 1)]
    return abs(left_to_right - right_to_left)


def main():
    arr = [1, 2, 3, 4, 3, 2, 1]
    result = lonely_int(arr)
    print(f"Lonely array: {result}")

    grades = [84, 29, 57]
    result = grade_roundup(grades)
    print(f"Rounded grades: {result}")

    number = 1
    result = flipping_bits(number)
    print(f"Result after flipping: {result}")

    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    result = diagnal_difference(arr)
    print(f"Diagnal difference: {result}")


if __name__ == "__main__":
    main()
