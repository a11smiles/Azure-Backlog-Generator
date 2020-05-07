from .parser import Parser

class Validation():

    def validateMetadata(self, file) -> bool:
        isValid = True
        content = None
        #with open(file, encoding='utf-8') as f:
        #    content = f.read()
        #    f.close()

        #json = Parser().json(content)
        
        return isValid

    def validateTitle(self, meta) -> bool:
        if "title" not in meta:
            return False
        if not Parser().validString(meta["title"]):
            return False 
        return True

    def validateDescription(self, meta) -> bool:
        if "description" not in meta:
            return False
        if not Parser().validString(meta["description"]):
            return False 
        return True

    def validateTags(self, meta) -> (bool, []):
        if "tags" not in meta:
            return (False,)

        return True
        
    def validateRoles(self, meta) -> (bool, []):
        if "roles" not in meta:
            return (False,)

        return True
