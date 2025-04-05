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


def main():
    arr = [1, 2, 3, 4, 3, 2, 1]
    result = lonely_int(arr)
    print(f"Lonely array: {result}")

    grades = [84, 29, 57]
    result = grade_roundup(grades)
    print(f"Rounded grades: {result}")


if __name__ == "__main__":
    main()
