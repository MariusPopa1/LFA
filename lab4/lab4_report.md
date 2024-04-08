# Report for the Fourth Laboratory Work

<br><br>
<br><br>

## Contents

- [Objectives](#objectives)
- [Overview](#Overview)
- [Implementation](#implementation)
  - [Lexer functionality](#Lexer-functionality)
  - [Split](#split)
  - [Labelling](#Labelling)
  - [Forming the string](#forming-the-string)
  - [Results](#results)
- [Conclusion](#conclusion)

## Objectives

1. **Write and cover what regular expressions are, what they are used for;**

2. **Below you will find 3 complex regular expressions per each variant. 
Take a variant depending on your number in the list of students and do the following:**

**a. Write a code that will generate valid combinations of symbols conform given regular 
expressions (examples will be shown).**

**b. In case you have an example, where symbol may be written undefined number of times, 
take a limit of 5 times (to evade generation of extremely long combinations);**

**c. Bonus point: write a function that will show sequence of processing regular expression 
(like, what you do first, second and so on)**

## Implementation
### What are regular expressions?

A regular expression (regex) is a sequence of characters that define a search pattern. Here’s how to write regular 
expressions:

Start by understanding the special characters used in regex, such as “.”, “*”, “+”, “?”, and more.
Choose a programming language or tool that supports regex, such as Python, Perl, or grep.
Write your pattern using the special characters and literal characters.
Use the appropriate function or method to search for the pattern in a string.
Examples: 
To match a sequence of literal characters, simply write those characters in the pattern.
To match a single character from a set of possibilities, use square brackets, e.g. [0123456789] matches any digit.
To match zero or more occurrences of the preceding expression, use the star (*) symbol.
To match one or more occurrences of the preceding expression, use the plus (+) symbol.
It is important to note that regex can be complex and difficult to read, so it is recommended to use tools like regex 
testers to debug and optimize your patterns.
A regular expression (sometimes called a rational expression) is a sequence of characters that define a search pattern, 
mainly for use in pattern matching with strings, or string matching, i.e. “find and replace” like operations. 
Regular expressions are a generalized way to match patterns with sequences of characters. 
It is used in every programming language like C++, Java and Python. 

What is a regular expression and what makes it so important? 
Regex is used in Google Analytics in URL matching in supporting search and replaces in most popular editors like 
Sublime, Notepad++, Brackets, Google Docs, and Microsoft Word.





### Split

```python
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

```

In the provided code , a meticulous approach is undertaken to parse a given expression into its constituent 
elements. The algorithm is specifically designed to differentiate among various characters and symbols such as 
parentheses, letters, numbers, and specific operators (+, *, and ?) with a clear hierarchical order of precedence.
This careful separation ensures that compound elements, like those involving parentheses or raised to a power, are 
correctly identified and isolated without misinterpretation. By appending these elements into a list, the snippet 
efficiently organizes the input expression into a structured and easily manipulable format. Such an organization is 
crucial for further processing or analysis of the expression, enabling a wide range of applications from simple
parsing tasks to more complex computational linguistics or mathematical expression evaluation procedures. 
The final step of printing the list of separated elements serves as a direct feedback mechanism, illustrating the 
effectiveness of the parsing process and providing a clear, immediate insight into the structure of the original 
expression. This meticulous approach underscores the importance of detail-oriented parsing in computational tasks, 
highlighting the blend of precision and adaptability needed to handle diverse and complex input scenarios effectively.


### Labelling

```python
     if elements[count].count('*') != 0:
                codes_list[count] = 3  # 0 up to 5
            if elements[count].count('?') != 0:
                codes_list[count] = 4  # Maybe show
            if elements[count].count('+') != 0:
                codes_list[count] = 5  # 1 up to 5
            if elements[count].count('^') != 0:
                codes_list[count] = 6
```

After we have split the given string into smaller bits each with their own needed information, we now have to go through
the process of actually doing what is intended by the notation. However, for visibility purposes, I have chosen to first
label each individual case based on specific properties, as is, but not limited to what it is in the code above. These
labels help us understand the different characteristics of each expression, and be able to understand the program 
better, and also for someone else to understand what is going on in the code. In this part of the program, we are 
dealing with the process of assigning numeric codes to these segments based on the presence of particular characters 
within them. This method of labeling allows for a structured approach to handling the diverse functionalities or 
attributes each segment represents, according to the predefined legend of symbols and their corresponding numeric
codes. Specifically:

The presence of an asterisk (*) in a segment assigns it a code of 3. This code could represent a range or a condition, 
such as "0 up to 5," implying that this segment is to be interpreted as allowing a value within a specified range.
A question mark (?) within a segment assigns it a code of 4, which might denote uncertainty or a conditional scenario, 
possibly interpreted as "Maybe show." This suggests that the segment's inclusion or processing might be contingent upon
some condition. The plus symbol (+) assigns a code of 5 to the segment, potentially indicating a numeric range of 
"1 up to 5." This could imply that the segment allows for a minimum of one instance up to a maximum of five, or some 
similar constraint. Lastly, the caret symbol (^) gives a segment a code of 6, which could represent a unique or special
condition or feature not covered by the other symbols. By assigning these numeric codes based on the presence of 
specific symbols, the program creates a clear, easy-to-understand framework for interpreting the segments. 
This coding system not only aids in the program's internal processing logic, making the implementation of the 
intended behaviors more straightforward but also enhances the readability and maintainability of the code. 
It allows developers or users, both present and future, to quickly grasp the significance of each segment based 
on its assigned code. Furthermore, this approach facilitates the addition of new functionalities or the modification
of existing ones by simply adjusting the symbol-to-code mapping or the logic associated with each code, thereby making
the program more adaptable and scalable.


### Forming the string

```python
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
```
Now that we have our complex expression split into smaller, processable bits, and each one of them has a label where 
we are able to tell what their intended purpose is in this expression, all that remains is actually achieving and 
outputting the desired result. For this, we just use the regex rules and some intuition based on the examples
given in the variant, to tell the program what exactly needs to be added to our result, which will be a simple display 
string, where we go through dozens of checks to add onto it based on the bits we split before. Here it was important to
set certain rules for the "OR" case, as it differs a bit from the other cases because of the use of vertical bars, so I 
added one more at the end to be able to easily delimit the end of the string

### Results

```text
Given Expression:  (a|b)(c|d)E*G?
Separated elements of the expression:  ['a|b|', 'c|d|', 'E*', 'G?']
Coded list for each of the elements:  [20, 20, 3, 4]
The final randomly generated output:  acEE

Given Expression:  P(Q|R|S)T(UV|W|X)*Z+
Separated elements of the expression:  ['P', 'Q|R|S|', 'T', 'UV|W|X|*', 'Z+']
Coded list for each of the elements:  [1, 20, 1, 21, 5]
The final randomly generated output:  PRTWZZZ

Given Expression:  1(0|1)*2(3|4)^536
Separated elements of the expression:  ['1', '0|1|*', '2', '3|4|^5', '3', '6']
Coded list for each of the elements:  [1, 21, 1, 24, 1, 1]
The final randomly generated output:  124444436
```

The transformation process elegantly unfolds as it translates complex, regex-like expressions into actionable codes and 
eventually into specific outputs, demonstrating a sophisticated mechanism of interpretation and generation. Initially, 
each expression undergoes a meticulous segmentation, breaking down into discernible parts that isolate unique patterns 
and symbols. This essential step ensures that each component, with its distinct characteristics—be it a choice between 
characters, repetition, or conditional appearance—is individually addressed. Following this, a coding system assigns 
numerical values to these segments, a method that translates symbolic intricacies into a universally understandable 
numeric format. Such coding not only simplifies the interpretation process but also lays down a concrete foundation for
the subsequent generation phase. In this final step, the codes guide the construction of an output string that adheres 
to the original expression's rules, producing varied results like acEE, PRTWZZZ, or 124444436. This output generation, 
inherently flexible, can easily yield a multitude of possible strings, each conforming to the predefined constraints, 
showcasing the process's ability to encapsulate the complexity of regex-like expressions in a structured and 
comprehensible manner.
### Conclusion

The task of interpreting regular expression-like patterns and generating possible outputs showcases an innovative 
approach to understanding and utilizing the power of pattern matching and symbolic representation. 
Through the methodical breakdown of complex expressions into individually coded segments, we not only simplify the 
inherent complexity of regex constructs but also bridge the gap between abstract pattern definitions and their practical
applications. This process, characterized by its segmentation, coding, and generation phases, not only demystifies the
operations behind regex patterns but also highlights the adaptability and precision such methods bring to computational 
problem-solving. The ability to produce varied, rule-compliant outputs from a given expression underlines the 
robustness and flexibility of this approach. It exemplifies how structured interpretation and creative generation 
can work hand in hand to tackle tasks that require both strict adherence to rules and the capacity for varied outcomes.
This endeavor not only enriches our understanding of regex expressions and their potential uses but also opens avenues 
for further exploration in automating and optimizing pattern-based computations and data parsing in various domains.