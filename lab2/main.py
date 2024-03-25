class FiniteAutomaton:
    def __init__(self):
        self.Q = ['q0', 'q1', 'q2', 'q3']
        self.Sigma = ['a', 'b', 'c']
        self.Delta = {
            ('q0', 'a'): ['q0', 'q1'],
            ('q1', 'b'): ['q2'],
            ('q2', 'a'): ['q2'],
            ('q3', 'c'): ['q3'],
            ('q2', 'c'): ['q3']
        }
        self.q0 = 'q0'
        self.F = ['q3']

    def convert_to_grammar(self):
        s = self.q0
        vn = self.Q
        vt = self.Sigma
        p = []
        for state in self.Q:
            for symbol in self.Sigma:
                if (state, symbol) in self.Delta:
                    next_states = self.Delta[(state, symbol)]
                    for next_state in next_states:
                        p.append((state, symbol, next_state))
        for final_state in self.F:
            p.append((final_state, '', 'e'))
        return Grammar(s, vn, vt, p)

    def nfa_to_dfa(self):
        input_symbols = self.Sigma
        initial_state = self.q0
        final_states = self.F
        transitions = {}
        new_states = [initial_state]
        while new_states:
            state = new_states.pop()
            if state not in transitions:
                transitions[state] = {}
                for el in input_symbols:
                    next_states = set()
                    for s in state.split(','):
                        if (s, el) in self.Delta:
                            next_states.update(self.Delta[(s, el)])
                    next_states = ','.join(sorted(list(next_states)))
                    transitions[state][el] = next_states
                    if next_states not in transitions and next_states != '':
                        new_states.append(next_states)

        states = list(transitions.keys())
        print(f"Q = {states}")
        print(f"Sigma = {input_symbols}")
        print(f"Delta = {transitions}")
        print(f"q0 = {initial_state}")
        print(f"F = {final_states}")


class Grammar:
    def __init__(self, s, vn, vt, p):
        self.s = s
        self.vn = vn
        self.vt = vt
        self.p = p

    def show_grammar(self):
        print("VN = {", ', '.join(map(str, self.vn)), '}')
        print("VT = {", ', '.join(map(str, self.vt)), '}')
        print("P = { ")
        for el in self.p:
            a, b, c = el
            print(f"    {a} -> {b}{c}")
        print("}")

    def classify_grammar(self):
        for lhs, rhs_list in self.p.items():
            for rhs in rhs_list:
                if len(lhs) > len(rhs) or (len(lhs) > 1 and any(char in self.vn for char in lhs)):
                    return "Unrestricted"

                if len(lhs) != 1 or lhs not in self.vn:
                    return "Context Sensitive"

        is_right_linear = any(all(symbol in self.vt for symbol in rhs[:-1]) and rhs[-1] in self.vn for rhs_list in
                              self.p.values() for rhs in rhs_list)
        is_left_linear = any(rhs[0] in self.vn and all(symbol in self.vt for symbol in rhs[1:]) for rhs_list in
                             self.p.values() for rhs in rhs_list)

        if is_right_linear or is_left_linear:
            return "Regular Linear"

        return "Context Free"


# main
finite_automaton = FiniteAutomaton()
grammar = finite_automaton.convert_to_grammar()
print("Grammar:")
grammar.show_grammar()
print()

print("Deterministic Finite Automaton:")
finite_automaton.nfa_to_dfa()
