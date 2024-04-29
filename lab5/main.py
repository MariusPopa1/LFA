class Grammar:
    def __init__(self):
        self.s = ['S']
        self.vn = ['A', 'B', 'C', 'S', 'D']
        self.vt = ['a', 'b', 'c', 'd']
        self.p = [
            ('S', '', 'AC'),
            ('S', 'b', 'A'),
            ('S', '', 'B'),
            ('S', 'a', 'A'),
            ('A', '', 'e'),
            ('A', 'a', 'S'),
            ('A', '', 'ABAb'),
            ('B', 'a', ''),
            ('B', '', 'AbSA'),
            ('C', '', 'abC'),
            ('D', '', 'AB'),

        ]
        self.dic = {

        }

    def show_grammar(self):
        print("VN = {", ', '.join(map(str, self.vn)), '}')
        print("VT = {", ', '.join(map(str, self.vt)), '}')
        print("P = { ")
        for el in self.p:
            print(el)
        print("}")

    def remove_useless(self):
        x = 0
        while x in range(len(self.p)):
            count = 0
            first_el = self.p[x]

            a = first_el[0]
            for third_el in self.p:
                c = third_el[2]
                if a in c:
                    count += 1

            if count == 0:
                del self.p[x]
            else:
                x += 1

        for el in self.p:
            a, b, c = el
            print(f"{a}-->{b}{c}")
        print(len(self.p))

    def remove_null(self):
        x = 0
        while x in range(len(self.p)):
            culprit = self.p[x]
            if culprit[2] == 'e':
                trigger = culprit[0]
                del self.p[x]
                el = 0
                while el in range(len(self.p)):
                    test = self.p[el]
                    if test[2].count(trigger) != 0:
                        string = test[2]
                        letter = 0
                        #
                        #
                        while letter in range(len(string)):
                            if string[letter] == trigger:
                                string1 = string[:letter] + string[letter + 1:]
                                ins = (test[0], test[1], string1)
                                el += 1
                                self.p.insert(el, ins)
                            letter += 1
                    if test[2].count(trigger) > 1:
                        self.p.insert(el, (test[0], test[1], test[2].replace(trigger, '')))
                        el += 1
                    el += 1
            x += 1

    def unit_production(self):
        replace = [
            (),
        ]
        for element in self.p:
            if element[0] in self.vn and element[2] in self.vn and len(element[2]+element[1]) == 1:
                replace.append((element[0], element[2]))

        replace.pop(0)
        copy = self.p
        addition = [
            (),
        ]
        for element in replace:
            for impostor in copy:
                if impostor[0] == element[1]:
                    addition.append((element[0], impostor[1], impostor[2]))
        addition.pop(0)
        impostor = 0

        while impostor in range(len(self.p)):
            if self.p[impostor][0] in self.vn and self.p[impostor][2] in self.vn and len(self.p[impostor][2]+self.p[
                    impostor][1]) == 1:
                del self.p[impostor]
            else:
                impostor += 1
        self.p.extend(addition)
        self.p.sort()
        for el in self.p:
            a, b, c = el
            print(f"{a}-->{b}{c}")
        print(len(self.p))

    def unproductive(self):
        trash = ["",]
        big_string = ""
        for element in self.p:
            big_string = big_string + element[0]
        for element in self.p:
            if element[0] in element[2] and big_string.count(element[0]) == 1:
                string = element[2]
                print(string)
                upper = 0
                lower = 0
                for letter in string:
                    if letter in "QWERTYUIOPASDFGHJKLZXCVBNM":
                        upper += 1
                    elif letter in "qwertyuiopasdfghjklzxcvbnm":
                        lower += 1
                if upper == 1 and lower > 0:
                    trash.append(element[0])
        element = 0
        trash.pop(0)
        if len(trash) != 0:
            while element in range(len(self.p)):
                for piece in trash:
                    if piece in self.p[element] or piece in self.p[element][2]:
                        del self.p[element]
                    else:
                        element += 1
        for el in self.p:
            a, b, c = el
            print(f"{a}-->{b}{c}")
        print(len(self.p))

    def convert_to_dic(self):
        temp_list = [self.p[0][1] + self.p[0][2]]
        tuple_list = [

        ]
        self.p.append(("", "", ""))
        element = 1
        while element in range(len(self.p)-1):
            if self.p[element][0] == self.p[element+1][0]:
                temp_list.append(self.p[element][1]+self.p[element][2])
                element += 1
            else:
                temp_list.append(self.p[element][1]+self.p[element][2])

                tuple_list.append((self.p[element][0], temp_list))
                element += 1
                temp_list = []

        self.dic = dict(tuple_list)
        print(self.dic)

    def chomsky_normal_form(self):
        # 5. Obtain CNF
        p5 = self.dic.copy()
        temp = {}
        vocabulary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        free_symbols = [v for v in vocabulary if v not in self.dic.keys()]
        for key, value in self.dic.items():
            for v in value:
                if (len(v) == 1 and v in self.vt) or (len(v) == 2 and v.isupper()):
                    continue
                else:
                    # split production into two parts
                    left = v[:len(v) // 2]
                    right = v[len(v) // 2:]
                    # get the new symbols for each half
                    if left in temp.values():
                        temp_key1 = ''.join([i for i in temp.keys() if temp[i] == left])
                    else:
                        temp_key1 = free_symbols.pop(0)
                        temp[temp_key1] = left
                    if right in temp.values():
                        temp_key2 = ''.join([i for i in temp.keys() if temp[i] == right])
                    else:
                        temp_key2 = free_symbols.pop(0)
                        temp[temp_key2] = right
                    # replace the production with the new symbols
                    p5[key] = [temp_key1 + temp_key2 if item == v else item for item in p5[key]]

        # add new productions
        for key, value in temp.items():
            p5[key] = [value]

        print(f"5. Final CNF:\n{p5}")


grammar = Grammar()
print("The grammar after removing the null productions is = {")
grammar.remove_null()
print("    }")
grammar.unit_production()
grammar.unproductive()
grammar.remove_useless()
grammar.convert_to_dic()
grammar.chomsky_normal_form()
