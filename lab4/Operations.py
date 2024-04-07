import random


def split(expression):
    elements = []
    bracket_count = 0
    count = 0
    while count in range(len(expression)):
        if expression[count] == '(':
            bracket_count += 1
            end_index = expression.find(')', count)
            elements.append("|" + expression[count+1:end_index] + "|")
            count = end_index
        elif expression[count] in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890":
            elements.append(expression[count])
            count += 1
        elif expression[count] in "+*?":
            elements[-1] = elements[-1] + expression[count]
            count += 1
        else:
            count += 1
        if expression[count] == '^':
            elements[-1] = elements[-1] + expression[count:count+2]
            count += 2
    print(elements)
    return elements


def assign(elements):
    codes_list = []
    for count in range(len(elements)):
        codes_list.append("")

    for count in range(len(elements)):
        if len(elements[count]) == 1:
            codes_list[count] = 1  # Always Show
            continue
        if elements[count].count('|') != 0:
            codes_list[count] = 20  # Choose one
            if elements[count].count('*') != 0:
                codes_list[count] = 21  # 0 up to 5
            if elements[count].count('?') != 0:
                codes_list[count] = 22  # Maybe show
            if elements[count].count('+') != 0:
                codes_list[count] = 23  # 1 up to 5
            if elements[count].count('^') != 0:
                codes_list[count] = 24
        else:
            if elements[count].count('*') != 0:
                codes_list[count] = 3  # 0 up to 5
            if elements[count].count('?') != 0:
                codes_list[count] = 4  # Maybe show
            if elements[count].count('+') != 0:
                codes_list[count] = 5  # 1 up to 5
            if elements[count].count('^') != 0:
                codes_list[count] = 6
    return codes_list, elements


def output(codes_list, separated):
    final_string = ""
    for count in range(len(codes_list)):
        if codes_list[count] == 1:
            final_string += separated[count]

    return final_string
