# *ObjectiveCParser*

*ObjectiveCParser* performs a static analysis on Objective-C code to calculate the metric *lines of code per method*. The result is written to a *.csv file. *ObjectiveCParser* is a python script, which uses a generated [antlr4](https://wwwpyt.antlr.org) parser for the given Objective-C language grammar from [antlr-grammars-v4](https://github.com/antlr/grammars-v4).

> Please star this repository, if you found the project helpful :)

## Installation Requirements
Make sure python3 (including pip3) is installed.

Install [antlr4](https://wwwpyt.antlr.org), which enables parsing source code.
```sh
pip3 install antlr4-python3-runtime
pip3 install antlr4-tools
```

## How to analyse your Objective-C code?
```sh
git clone https://github.com/alschmut/ObjectiveCParser.git
python3 src/main/ProjectParser.py /path/to/MyObjectiveCProject
```

This generates a `*.csv` file with the below structure:

|path                               |method_loc
|---                                |---
|/path/to/MyFile.m/someMethod       |1
|/path/to/MyFile.m/anotherMethod    |5

## How to add a new programming language with antlr4

### Generate Python classes for a new grammar
- Find the <new_language> grammar on [antlr-grammars-v4](https://github.com/antlr/grammars-v4)
- Create a new folder `<new_language>` inside `src/main/antlrParser/`
- Copy paste all `.g4` files like Parser, Lexer or UnicodeClasses into the <new_language> folder
- Execute `antlr4 -Dlanguage=Python3 *.g4` inside your <new_language> folder. This generates some Python3 classes and other files

### Override generated listener methods
- Create a new file `<new_language>ListenerExtended.py` inside `src/main/antlrParser/ExtendedListener/`
- Create a new class which just looks similar to the other existing classes like `ObjcParserListenerExtended` and extend the BaseListener class
- Override the language specific `enter...()` functions. To find out which functions to override, have a look at the hierarchical grammar definition inside `<your_language>Parser.g4`. Then store the obtained values inside the predefined BaseListener class.

### Walk through the new grammar
Create another function inside the `src/main/antlrParser/LanguageParser.py` like below. Replace the placeholder with your generated/created classes.
```python
def parse_<your_language>_file(self, input_stream: InputStream):
    lexer = <your_generated_lexer>(input_stream)
    stream = CommonTokenStream(lexer)
    parser = <your_generated_parser>(stream)
    tree = parser.<your_top_level_grammar_node>()
    listener = <your_expanded_listener>()
    return self.walk(listener, tree)
```
### Add your supported language extension
Inside `src/main/antlrParser/Lanague.py` an enum with all supported programming languages is stored. Add your language name with its file-extension

### Add new option to use your parse_<your_language>_file function
The `LanguageParser.parse_file()` function calls the appropriate parsing function for each language. Add yours with another if-statement checking the file extension


