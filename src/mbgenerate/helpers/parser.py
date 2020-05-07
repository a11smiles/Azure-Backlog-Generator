import re
import json

class Parser():

    def links(self, desc):
        return re.sub(r'([\[]([^\]^\[]*)?[\]])([\(]([^\]^\[]*)?[\)])', r'<a href="\g<4>">\g<2></a>', desc)

    def json(self, content):
        try:
            data = json.loads(content)
            return data
        except json.JSONDecodeError as exc:
            return (False, exc.args)

    def validString(self, string):
        if str is not type(string):
            return False
        else:
            return bool(string and string.strip())