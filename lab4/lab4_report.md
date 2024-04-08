# Report for the Third Laboratory Work

<br><br>
<br><br>

## Contents

- [Objectives](#objectives)
- [Implementation](#implementation)
  - [Lexer-functionality](#Lexer-functionality)
  - [Parser](#parser)
  - [Splitting](#Splitting)
  - [Checking the type](#checking-the-type)
  - [Results](#results)
- [Conclusion](#conclusion)

## Objectives

1. **Understand what lexical analysis [1] is.**
2. **Get familiar with the inner workings of a lexer/scanner/tokenizer.**
3. **Implement a sample lexer and show how it works.**
## Implementation

### Lexer functionality

The duty of a lexer is to turn a sequence of single characters into a sequence of so called tokens. 
A token is a chunk of characters associated with a certain token-type. 
Most programming languages define individual lexer rules for things like names (identifiers), 
string literals, numbers, whitespace and comments.


### Parser

```python
def parse(file):
    contents = open(file, "r").read()
    tokens = lexer(contents)
    return tokens

```
In this code we have a class which will open our file to read, which in my case is named test.myLang
, and then gets and returns the tokens from our lexer function

### Splitting

```python
def lexer(contents):
    lines = contents.split('\n')
    items = []
    for line in lines:
        chars = list(line)
        tokens = []

        temp_str = ""
```

In this code we declare our lexer function, and split the function into lines and then into separate
chars, so that we can go character by character and analyze the code that is inserted.


### Splitting into tokens

```python
        quote_count = 0
        for char in chars:
            if char == '"' or char == "'":
                quote_count += 1
            if quote_count % 2 == 0:
                in_quotes = False
            else:
                in_quotes = True
            if char == " " and in_quotes is False:
                tokens.append(temp_str)
                temp_str = ""
            else:
                temp_str += char
            print (temp_str)
        tokens.append(temp_str)
```
We do want in our code for strings which are contained within brackets to be considered a single
expression, so this part of the code does that, while also looking for spaces, and adds words
to our list of tokens

### Checking the type

```python
        for token in tokens:
            if token[0] == '"' or token[0] == "'":
                if token[-1] == '"' or token[-1] == "'":
                    items.append(("string", token))
                else:
                    print("Error, Wrong format of String")
                    break
            elif re.match(r"[.a-zA-Z]+", token):
                items.append(("symbol", token))
            elif re.match(r"[.0-9]+", token):
                items.append(("number", token))
            elif token in "+-*/":
                items.append(("expression", token))

    return items

```
Then, for each token noted down through our previous process, we determine what type it is.
I've discerned 4 types, which are symbols, number, expression and string. It is also able to
show when a string isn't entered in correctly based on the parenthesis.//

### Results

```text
print "Hello, World!"
print "Who cares"
a = 1 + 1

turns into:

[('symbol', 'print'), ('symbol', 'print'),
('string', '"Who cares"'), ('symbol', 'a'), ('number', '1'), ('expression', '+'), ('number', '1')]


```

### Conclusion

In this lab we built a really basic example of a Lexer, which is able to 
split our inserted code and details into tokens, which can then be classified.
This is the base step in creating our own programming language.