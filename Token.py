
class Token(object):
    def __init__(self, type, val, pos):
        self.type = type
        self.val = val
        self.pos = pos

    def __str__(self):
        return '<%s,%s, %s>' % (self.type, self.val, self.pos)

    def getToken(self):
        return (self.val,self.type)
