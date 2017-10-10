# my solution
def checkio(text):
    # replace this for solution
    alist = []
    for i in range(26):
        alist.append(0)
    str = text.lower()
    for i in str:
        if i.isalpha():
            alist[ord(i)-97] += 1
    return chr(97 + alist.index(max(alist)))



# https://py.checkio.org/mission/most-wanted-letter/publications/category/clear/
# Speedy
# from string import ascii_lowercase as letters
# checkio = lambda text: max(letters, key=text.lower().count)

# Clear
# import string
# def checkio(text):
#     """
#     We iterate through latyn alphabet and count each letter in the text.
#     Then 'max' selects the most frequent letter.
#     For the case when we have several equal letter,
#     'max' selects the first from they.
#     """
#     text = text.lower()
#     return max(string.ascii_lowercase, key=text.count)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

