# Your optional code here
# You can import some modules or create additional functions


# def checkio(data):
#     # Your code here
#     # It's main function. Don't remove this function
#     # It's used for auto-testing and must return a result for check.
#     # replace this for solution
#     # my
#     # res = []
#     # for item in data:
#     #     if data.count(item) > 1:
#     #         res.append(item)
#     # return res
#     # speedy
#     # 1
#     # from collections import Counter
#     # nonunique = Counter(data) - Counter(set(data))
#     # return [x for x in data if x in nonunique]




# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# Loop over original list


if __name__ == "__main__":
    # 2
    checkio = lambda d: [x for x in d if d.count(x) > 1]
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
