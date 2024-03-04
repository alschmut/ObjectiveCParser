from antlrParser.Swift5.Swift5ParserListener import Swift5ParserListener
from antlrParser.BaseListener import BaseListener
from antlrParser.Swift5.Swift5Parser import Swift5Parser
from model.IdentifierType import IdentifierType

class Swift5ParserListenerExtended(Swift5ParserListener, BaseListener):

	def enterFunction_declaration(self, ctx: Swift5Parser.Function_declarationContext):
		function_name = ctx.function_name().identifier().Identifier()
		print(function_name)