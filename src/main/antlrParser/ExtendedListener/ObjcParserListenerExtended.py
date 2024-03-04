from antlrParser.Objc.ObjectiveCParserListener import ObjectiveCParserListener
from antlrParser.BaseListener import BaseListener
from antlrParser.Objc.ObjectiveCParser import ObjectiveCParser
from model.IdentifierType import IdentifierType

class ObjcParserListenerExtended(ObjectiveCParserListener, BaseListener):

	def enterMethodDefinition(self, ctx):
		method_name = self.getMethodName(ctx)
		self.add_method(str(method_name), ctx.start.line, ctx.stop.line, IdentifierType.Method)

	def getMethodName(self, ctx: ObjectiveCParser.MethodDefinitionContext):
		selectorContext = ctx.methodSelector().selector()
		keywordDeclaratorContext = ctx.methodSelector().keywordDeclarator(0)
		if selectorContext != None:
			return selectorContext.identifier().IDENTIFIER()
		elif keywordDeclaratorContext != None:
			return keywordDeclaratorContext.selector().identifier().IDENTIFIER()
		else:
			return "UnknownMethodNameAtLine" + ctx.start.line