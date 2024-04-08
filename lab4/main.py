from Operations import *


expression_list = ["(S|T)(U|V)W*Y+24", "L(M|N)O^3P*Q(2|3)", "R*S(T|U|V)W(X|Y|Z)^2", "(a|b)(c|d)E*G?",
                   "P(Q|R|S)T(UV|W|X)*Z+", "1(0|1)*2(3|4)^536"]
for expression in expression_list:
    print("Given Expression: ", expression)
    separated = split(expression)
    codes_list, separated = assign(separated)
    final_result = output(codes_list, separated)
    print("\n")
