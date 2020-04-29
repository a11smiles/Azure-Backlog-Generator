import re

class Parser():

    def links(self, desc):
        return re.sub(r'([\[]([^\]^\[]*)?[\]])([\(]([^\]^\[]*)?[\)])', r'<a href="\g<4>">\g<2></a>', desc)
