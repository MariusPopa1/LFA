import random as r


def split(expression):
    elements = []
    bracket_count = 0
    count = 0
    while count in range(len(expression)):
        if expression[count] == '(':
            bracket_count += 1
            end_index = expression.find(')', count)
            elements.append(expression[count+1:end_index] + "|")
            count = end_index+1
        elif expression[count] in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890":
            elements.append(expression[count])
            count += 1
        elif expression[count] in "+*?":
            elements[-1] = elements[-1] + expression[count]
            count += 1
        elif expression[count] == '^':
            elements[-1] = elements[-1] + expression[count:count + 2]
            count += 2
        else:
            count += 1
    print("Separated elements of the expression: ", elements)

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
            if elements[count].count('*') != 0:
                codes_list[count] = 21  # 0 up to 5
            elif elements[count].count('?') != 0:
                codes_list[count] = 22  # Maybe show
            elif elements[count].count('+') != 0:
                codes_list[count] = 23  # 1 up to 5
            elif elements[count].count('^') != 0:
                codes_list[count] = 24
            else:
                codes_list[count] = 20  # Choose one

        else:
            if elements[count].count('*') != 0:
                codes_list[count] = 3  # 0 up to 5
            if elements[count].count('?') != 0:
                codes_list[count] = 4  # Maybe show
            if elements[count].count('+') != 0:
                codes_list[count] = 5  # 1 up to 5
            if elements[count].count('^') != 0:
                codes_list[count] = 6

    print("Coded list for each of the elements: ", codes_list)

    return codes_list, elements


def output(codes_list, separated):
    final_string = ""

    for count in range(len(codes_list)):
        if codes_list[count] == 1:
            final_string += separated[count]
        else:
            if codes_list[count] // 10 == 2:
                temp_string = separated[count]
                bars = temp_string.count('|')
                choice = r.randint(0, bars-1)
                winner = ""
                mark1 = -1
                bar_count = 0

                for symbol_num in range(len(temp_string)):
                    if bar_count == choice and mark1 == -1:
                        mark1 = symbol_num
                    if temp_string[symbol_num] == '|':
                        bar_count += 1
                    if bar_count == choice+1:
                        mark2 = symbol_num
                        winner = temp_string[mark1:mark2]
                        bar_count += 1

                if codes_list[count] == 20:
                    final_string += winner
                elif codes_list[count] == 21:
                    nr_show = r.randint(0, 5)
                    final_string += winner * nr_show
                elif codes_list[count] == 22:
                    nr_show = r.randint(0, 1)
                    final_string += winner * nr_show
                elif codes_list[count] == 23:
                    nr_show = r.randint(1, 5)
                    final_string += winner * nr_show
                elif codes_list[count] == 24:
                    final_string += winner * int(separated[count][-1])
            elif codes_list[count] == 3:
                nr_show = r.randint(0, 5)
                final_string += separated[count][0] * nr_show
            elif codes_list[count] == 4:
                nr_show = r.randint(0, 1)
                final_string += separated[count][0] * nr_show
            elif codes_list[count] == 5:
                nr_show = r.randint(1, 5)
                final_string += separated[count][0] * nr_show
            elif codes_list[count] == 6:
                final_string += separated[count][0] * int(separated[count][-1])

    print("The final randomly generated output: ", final_string)

    return final_string
