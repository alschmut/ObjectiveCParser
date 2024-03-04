from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream
from antlrParser.Language import Language
from antlrParser.Language import Language

from antlrParser.Objc.ObjectiveCLexer import ObjectiveCLexer
from antlrParser.Objc.ObjectiveCParser import ObjectiveCParser
from antlrParser.ExtendedListener.ObjcParserListenerExtended import ObjcParserListenerExtended

# from antlrParser.Swift5.Swift5Lexer import Swift5Lexer
# from antlrParser.Swift5.Swift5Parser import Swift5Parser
# from antlrParser.ExtendedListener.Swift5ParserListenerExtended import Swift5ParserListenerExtended

class LanguageParser():

    def get_supported_extensions(self):
        return [extension.value for extension in Language]

    def walk(self, listener, tree):
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        return listener.get_methods()
    
    def parse_objc_file(self, input_stream: InputStream):
        lexer = ObjectiveCLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ObjectiveCParser(stream)
        tree = parser.translationUnit()
        listener = ObjcParserListenerExtended()
        return self.walk(listener, tree)
    
    def parse_swift_file(self, input_stream: InputStream):
        lexer = Swift5Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = Swift5Parser(stream)
        tree = parser.translationUnit()
        listener = Swift5ParserListenerExtended()
        return self.walk(listener, tree)

    def parse_file(self, file_extension: [str], file_content: str):
        input_stream = InputStream(file_content)
        if file_extension == Language.ObjcHeader.value or file_extension == Language.ObjcImplementation.value:
            return LanguageParser.parse_objc_file(self, input_stream)
        else:
            return []
        # elif file_extension == Language.Swift.value:
        #     return LanguageParser.parse_swift_file(self, input_stream)