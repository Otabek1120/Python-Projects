def str_info(my_str):    """    :param my_str: the string given by the use    :return: None    prints out a bunch of info about the str    """    str_len = len(my_str)    print(str_len)    # 2. 2 char in the str    try:        print(my_str[1])    except IndexError:        print("need a longer str")    # 3. 10 chars or all    print(my_str[:10])    # 4. -5 chars    print(my_str[-5:])    # 5. all-cap    print(my_str.upper())    # 6. check the first char    first_char = my_str[0]    if first_char.isalpha():        if first_char.lower() in "qwerty":            print("QWERTY")        elif first_char in "uiop":            print("UIOP")        else:            print("LETTER")    elif first_char.isdigit():        print("DIGIT")    else:        print("OTHER")def nums(num1, num2):    """    :param num1: an int given by the user    :param num2: another one    :return: the product of them    """    result = int(num1) * int(num2)    return resultdef main():    my_str = input("input string: ")    str_info(my_str)    num1 = input()    num2 = input()    print(nums(num1, num2))main()