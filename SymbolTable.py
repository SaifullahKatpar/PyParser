class SymbolTable(object):
    
    def __init__(self):
        self.symbols = {}
        self.pos = 0

    def insert(self,token):     
        self.symbols[(token[0],self.pos)] = token[1] 

    def lookup(self,symbol):
        if symbol in self.symbols.keys():
            return symbol
        return None

    def getTable(self):
        identifiers = {}
        for k,v in self.symbols.items():
            if v =='IDENTIFIER':
                identifiers[k] = v
        return identifiers

    def getLexicalBox(self):
        return self.symbols
