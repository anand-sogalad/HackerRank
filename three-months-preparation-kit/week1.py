# print the plus minus and zeros ration in a given array
def plus_minus(arr: list):
    plus_count = len(list(filter(lambda x: x > 0, arr)))
    minus_count = len(list(filter(lambda x: x < 0, arr)))
    zero_count = len(list(filter(lambda x: x == 0, arr)))
    total_count = len(arr)

    # print statements
    print(f"{plus_count/total_count:.5f}")
    print(f"{minus_count/total_count:.5f}")
    print(f"{zero_count/total_count:.5f}")


def mini_max_sum(arr: list):
    sums = []
    for i in arr:
        sums.append(sum(arr) - i)

    # print statements
    print(min(sums), max(sums), sep=" ")


def time_conversion(s: str):
    if s.endswith("PM"):
        if int(s[:2]) < 12:
            return str(int(s[:2]) + 12) + s[2:-2]
        elif int(s[:2]) == 12:
            return s[:-2]
    elif s.endswith("AM"):
        if int(s[:2]) < 12:
            return s[:-2]
        elif int(s[:2]) == 12:
            return "00" + s[2:-2]


def breaking_records(scores: list):
    first_score = scores[0]
    top_score = first_score
    low_score = first_score
    top_score_count = 0
    low_score_count = 0
    for i in list(dict.fromkeys(scores)):
        if i < low_score:
            low_score = i
            low_score_count += 1
        elif i > top_score:
            top_score = i
            top_score_count += 1
    return top_score_count, low_score_count


def main():
    # plus_minus
    plus_minus([-4, 3, -9, 0, 4, 1])
    mini_max_sum([1, 2, 3, 4, 5])
    print(time_conversion("12:01:00AM"))
    for i in [
        [12, 24, 10, 24],
        [10, 5, 20, 20, 4, 5, 2, 25, 1],
        [3, 4, 21, 36, 10, 28, 35, 5, 24, 42],
    ]:
        print(breaking_records(i))


if __name__ == "__main__":
    main()


# New learnings
"""
Use dict.fromkeys(list):
    when we need to remove the duplicates but keep the order
Use set(list):
    When we need to remove the duplicates but no need to keep the order
"""