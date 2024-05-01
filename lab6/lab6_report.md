# Report: Abstract Syntax Tree (AST) Generation

## Objective

1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST [2].
3. In addition to what has been done in the 3rd lab work do the following:
   1. In case you didn't have a type that denotes the possible types of tokens you need to:
      1. Have a type **_TokenType_** (like an enum) that can be used in the lexical analysis to categorize the tokens.
      2. Please use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.


## Results and Implementation

### Lexer

The lexer is implemented to tokenize an input equation using regular expressions, distinguishing token types such as numbers, mathematical operations, and parentheses. A `TokenType` enum class defines possible token categories, ensuring easy expansion and management of token types.

```python
class TokenType(Enum):
    OPEN_PARENTHESIS = auto()
    CLOSE_PARENTHESIS = auto()
    MATH_OPERATION = auto()
    NUMBERS = auto()
    START = auto(
}
```
The lexer checks for valid transitions between tokens to ensure syntactically correct sequences.
### Parser

The parser constructs an AST using nodes derived from the tokenized input. Each token type corresponds to a different node in the tree, with hierarchical relationships representing the syntactic structure of the mathematical expression.
```python
from anytree import Node, RenderTree

class Parser:
    def __init__(self, category_mapping, valid_tokens):
        self.category_mapping = category_mapping
        self.valid_tokens = valid_tokens
```

### Visualization
The AST can be visualized using RenderTree, which provides a clear, tree-like representation of the expression structure.
```python
if __name__ == "__main__":
    test_equation = "2*(3+4)"
    lexer = Lexer(test_equation)
    category_mapping, valid_tokens = lexer.lexer()
    parser = Parser(category_mapping, valid_tokens)
    parser.parse()
```


## Output

This is our AST with the nodes of the text we took out.

```
START
└── 2
    └── NUMBERS
        └── *
            └── MATH_OPERATION
                └── (
                    └── OPEN_PARENTHESIS
                        └── 3
                            └── NUMBERS
                                └── +
                                    └── MATH_OPERATION
                                        └── 4
                                            └── NUMBERS
                                                └── )
                                                    └── CLOSE_PARENTHESIS
```

In this tree:
- The root node is labeled `START`, indicating the start of parsing.
- The number `2` is a child of `START`, identified as a `NUMBERS` type, showing it's a numeric literal.
- The multiplication operator `*` follows, categorized under `MATH_OPERATION`, indicating a mathematical operation.
- The open parenthesis `(` initiates a new sub-expression, marked by `OPEN_PARENTHESIS`.
- Inside the parentheses, the number `3` is first, followed by the addition operator `+`, and then the number `4`, all appropriately categorized under their respective types (`NUMBERS` and `MATH_OPERATION`).
- The expression within the parentheses ends with a close parenthesis `)`, labeled as `CLOSE_PARENTHESIS`.


## Conclusion
By refining the lexer and parser, and implementing a detailed AST, we have achieved a robust foundation for interpreting and analyzing mathematical expressions. This infrastructure not only enhances our understanding of parsing mechanics but also serves as a basis for future language processing and compiler construction projects.