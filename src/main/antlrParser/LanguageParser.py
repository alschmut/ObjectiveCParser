from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream
from antlrParser.Language import Language
from antlrParser.Language import Language
from typing import List

from antlrParser.Objc.ObjectiveCLexer import ObjectiveCLexer
from antlrParser.Objc.ObjectiveCParser import ObjectiveCParser
from antlrParser.ExtendedListener.ObjcParserListenerExtended import ObjcParserListenerExtended

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

    def parse_file(self, file_extension: List[str], file_content: str):
        input_stream = InputStream(file_content)
        if file_extension == Language.ObjcHeader.value or file_extension == Language.ObjcImplementation.value:
            return LanguageParser.parse_objc_file(self, input_stream)
        else:
            return []