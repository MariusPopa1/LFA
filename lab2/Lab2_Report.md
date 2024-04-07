# Report for the Second Laboratory Work

<br><br>
<br><br>

## Contents

- [Objectives](#objectives)
- [Overview](#overview)
- [Implementation](#implementation)
  - [Checking the type](#checking-the-type)
  - [Grammar](#Grammar)
  - [Check](#Check)
  - [Conversion](#Conversion)
  - [Results](#results)
- [Conclusion](#conclusion)

## Objectives

1. **Understand what an automaton is and what it can be used for.**
2. **Continuing the work in the same repository and the same project, 
the following need to be added: a. Provide a function in your grammar 
type/class that could classify the grammar based on Chomsky hierarchy.**
3. **According to your variant number (by universal convention it is register ID),**
**get the finite automaton definition and do the following tasks:**

a. Implement conversion of a finite automaton to a regular grammar.

b. Determine whether your FA is deterministic or non-deterministic.

c. Implement some functionality that would convert an NDFA to a DFA.

d. Represent the finite automaton graphically (Optional, and can be considered as a bonus point):

You can use external libraries, tools or APIs to generate the figures/diagrams.

Your program needs to gather and send the data about the automaton and the 
lib/tool/API return the visual representation.**
## Overview
Finite Automata(FA) is the simplest machine to recognize patterns.It is used to characterize a Regular Language, for example: /baa+!/.
Also it is used to analyze and recognize Natural language Expressions. The finite automata or
finite state machine is an abstract machine that has five elements or tuples. It has a set 
of states and rules for moving from one state to another but it depends upon the applied 
input symbol. Based on the states and the set of rules the input string can be either 
accepted or rejected. Basically, it is an abstract model of a digital computer which 
reads an input string and changes its internal state depending on the current input symbol. 
Every automaton defines a language i.e. set of strings it accepts. 
The following figure shows some essential features of general automation.

My laboratory work was done in Python language. Variant 20:

Q = {q0,q1,q2,q3}, <br>
∑ = {a,b,c}, <br>
F = {q3} <br>
δ(q0,a) = q0, <br>
δ(q0,a) = q1, <br>
δ(q2,a) = q2, <br>
δ(q1,b) = q2, <br>
δ(q2,c) = q3, <br>
δ(q3,c) = q3. <br>
## Implementation


### FiniteAutomaton class

```python
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

```
I used a class to set the standard for the requirements of what our Finite 
Automaton needs to generally look like. This includes the non-terminal and terminal states, the final state,
the starting state and the transitions that can take place. This part does not restrict


In this code we declare our lexer function, and split the function into lines and then into separate
chars, so that we can go character by character and analyze the code that is inserted.


### Conversion to grammar

```python
        for state in self.Q:
            for symbol in self.Sigma:
                if (state, symbol) in self.Delta:
                    next_states = self.Delta[(state, symbol)]
                    for next_state in next_states:
                        p.append((state, symbol, next_state))
        for final_state in self.F:
            p.append((final_state, '', 'e'))
        return Grammar(s, vn, vt, p)
```
I added a method “convert_to_grammar” in the class, it converts the finite automaton into a
grammar. We have a starting symbol S, non-terminal symbol Vn and terminal symbol VT and P
for production rules, which includes a nested loop that iterates over each state in Q and each input
symbol in Sigma. For each state-symbol pair, it checks if there is a transition defined in the Delta
function, if there is one, it retrieves the next state for the state-symbol pair and creates the
production rules. After that, it checks for final states, for each one it adds an epsilon-transition to
the grammar and transition to an empty string. The method maps the transitions of the finite
automaton to production rules of a grammar, and captures the behaviour of the automaton in a
language that grammars can describe 
### Conversion to DFA
```python
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
```
This method is responsible for converting non-deterministic finite automaton into a deterministic
finite automaton. Here we have a while loop that, for each state, it checks if it has already been
processed, if not, it initializes an entry in the transition dictionary for the given state. For each
input set it computes the set of next states for the given state and input symbol combination by
iterating over each state in the NFA transition function. Overall, it explores the states and
transitions of the NFA to construct and equivalent DFA.

### Checking the type


```python
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
```
Here we classify our grammar, as per the requirements, into the following categories:

Type 0 - Unrestricted Grammars:

This type includes all formal grammar. Type 0 grammar languages are recognized by turing machine.
These languages are also known as the Recursively Enumerable languages. 
The code checks for productions that break the norm, like longer left-hand sides or multiple nonterminals on the left.

Type 1 - Context-Sensitive Grammars:

This type of grammar generate context-sensitive languages.
The language generated by the grammar is recognized by the Linear Bound Automata 
The code ensures that all productions adhere to a context-sensitive vibe with len(lhs) <= len(rhs).

Type 2 - Context-Free Grammars:

This type of grammar generate context-free languages. 
The language generated by the grammar is recognized by a Pushdown automata.  In Type 2:
Each production is checked to have a single nonterminal on the left side.

Type 3 - Regular Grammars:

This type of grammar generate regular languages. These languages are exactly all languages that can be accepted by a
finite-state automaton. Type 3 is the most restricted form of grammar. 
The code checks for right and left linearity in productions.

### Results

```text
Q = ['q0', 'q0,q1', 'q2', 'q3']
Sigma = ['a', 'b', 'c']
Delta = {'q0': {'a': 'q0,q1', 'b': '', 'c': ''}, 'q0,q1': {'a': 'q0,q1', 'b': 'q2', 'c': ''}, 'q2': {'a': 'q2', 'b': '', 'c': 'q3'}, 'q3': {'a': '', 'b': '', 'c': 'q3'}}
q0 = q0
F = ['q3']


```

### Conclusion

To sum up, this lab work has given me a better understanding of formal languages and finite
automata. Deterministic or non-deterministic finite automata are basic building blocks for
language analysis and pattern recognition. Deterministic finite automata (DFAs) and non-deterministic
finite automata (NFAs) are two different categories that show off the flexibility and computing
capacity of these abstract machines. While NFAs allow for numerous pathways from one state to
another, DFAs follow a fixed sequence of states for every input string.I also studied and understood
better the Chomsky hierarchy. 