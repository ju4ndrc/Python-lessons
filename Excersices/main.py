from operator import length_hint
from types import new_class

code = "Z"
print(len(code))
def prueb(code):

    length = len(code)
    cont = 0

    for i in reversed(range(0, length)):
        if code[i].isalpha() and code[cont].isalpha():
            if code[i] != code[cont]:
                return False
            cont = cont + 1
    return True


result = prueb(code)
print(result)
# new_text = ""
# for char in code:
#     if char.isalpha():
#         new_text = new_text + char
#
# print(new_text)
#
# new_text = new_text.lower()
#
# new_text = new_text.replace(" ", "")
#
# length = len(new_text)
# reversed_text = new_text[::-1]
# if reversed_text == new_text:
#     print(1)
# else:
#     print(0)
#
# #
# Another solution
# letters = ''.join([char.lower() for char in code if char.isalpha()])
# return letters == letters[::-1]
# Two Pointer: Time Complexity - O(n); Space Complexity - O(1)

    # l, r = 0, len(code)-1
    # while l < r:
    #     if code[l].isalpha() and code[r].isalpha():
    #         if code[l].lower() != code[r].lower():
    #             return False
    #         else:
    #             l += 1
    #             r -= 1
    #     elif not code[l].isalpha():
    #         l += 1
    #     else:
    #         r -= 1
    # return True
# for i in range(0,len):
#     if new_text[i] != new_text[len(new_text)-1]:
#         print("1")
#     else:
#         print("0")
#     length = length - 1

#letter = list(code)

# code = code.lower()
# code = code.replace(" ", "")

# letter = list(code)
# print(letter)
# length = len(letter)
# for i in range(0,length+1):
#     print(letter[i],": Evaluating")
#     is_letter = letter[i].isalpha()
#     print(is_letter)
#     if not is_letter:
#         print(f"{letter[i]}: is not a letter")
#         letter.remove(letter[i])
#     else:
#         print(f"{letter[i]}: is a LETTER")
#     i = i + 1
#     print("Finish iteration")
# print(letter)


# def isAlphabeticPalindrome(code):
#
#     code = code.lower()
#     code = code.replace(" ", "")
#     alpha = code.isalpha()
#     if  not alpha:
#         letter = list(code)
#         length = len(letter)
#         for i in range(length):
#             if letter[i] != "a":
#
#
#
#
# result = isAlphabeticPalindrome(code)
# print(result)