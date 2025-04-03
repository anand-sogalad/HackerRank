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


def camel_case(string: str):
    action, _type, text = string.split(";")

    if action.lower() == "s":
        if _type.lower() == "v":
            print(
                "".join([f" {s.lower()}" if s.isupper() else s.lower() for s in text])
            )
        elif _type.lower() == "m":
            text = text[:-2]
            print(
                "".join([f" {s.lower()}" if s.isupper() else s.lower() for s in text])
            )
        else:
            print(
                "".join(
                    [f" {s.lower()}" if s.isupper() else s.lower() for s in text]
                ).strip()
            )
    else:
        text = text.split()
        if _type.lower() == "v":
            print(text[0].lower() + "".join([s.capitalize() for s in text[1:]]))
        elif _type.lower() == "m":
            print(text[0].lower() + "".join([s.capitalize() for s in text[1:]]) + "()")
        else:
            print("".join([s.capitalize() for s in text]))


def sparse_array(string_list: list, query_list: list):
    return [
        sum(i)
        for i in [
            [query_word.count(string) for string in string_list]
            for query_word in query_list
        ]
    ]


def divisible_sum_pairs(int_list: list, k: int):
    print(
        len(
            [
                (i, j)
                for idx, i in enumerate(int_list)
                for j in int_list[idx + 1 :]
                if (i + j) % k == 0
            ]
        )
    )


def find_median(arr):
    return sorted(arr)[len(arr) // 2]


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
    camel_case("S;V;pictureFrame")
    sparse_array(
        [
            "abcde",
            "sdaklfj",
            "asdjf",
            "na",
            "basdn",
            "sdaklfj",
            "asdjf",
            "na",
            "asdjf",
            "na",
            "basdn",
            "sdaklfj",
            "asdjf",
        ],
        ["abcde", "sdaklfj", "asdjf", "na", "basdn"],
    )
    divisible_sum_pairs([1, 3, 2, 6, 1, 2], 3)


if __name__ == "__main__":
    main()


# New learnings
"""
Use dict.fromkeys(list):
    when we need to remove the duplicates but keep the order
Use set(list):
    When we need to remove the duplicates but no need to keep the order
"""
