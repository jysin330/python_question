def isalnum(str):
    for i in str:
        if i.isalnum():
            return True

    return False


def isalpha(str):
    for i in str:
        if i.isalpha():
            return True

    return False


def isdigit(str):
    for i in str:
        if i.isdigit():
            return True

    return False


def islower(str):
    for i in str:
        if i.islower():
            return True

    return False


def isupper(str):
    for i in str:
        if i.isupper():
            return True

    return False


if __name__ == '__main__':
    s = input()

    print(isalnum(s))
    print(isalpha(s))
    print(isdigit(s))
    print(islower(s))
    print(isupper(s))
