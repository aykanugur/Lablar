import string


def reverse_string(string):
    return string[::-1]
def capitalize_words(s):
    return s.upper()
def remove_punctuation(s):
    for x in s:
        if x in string.punctuation:
            s = s.replace(x, "")
    return s