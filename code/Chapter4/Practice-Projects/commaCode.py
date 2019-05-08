spam = ['apples', 'bananas', 'tofu', 'cats']


def commaCode(spam):
    str = ''
    for index in range(len(spam)):
        if index == len(spam) - 1:
            str = str + 'and ' + spam[index]
        else:
            str  = str + spam[index] + ', '
    return str

print(spam)
str = commaCode(spam)
print(str)
