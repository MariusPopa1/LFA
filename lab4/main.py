from Operations import *


expression = "O(P|Q|R)+2(3|4)^2Q+Q*Q^2"
separated = split(expression)
codes_list, separated = assign(separated)
print(codes_list)
print(separated)
print(output(codes_list, separated))
