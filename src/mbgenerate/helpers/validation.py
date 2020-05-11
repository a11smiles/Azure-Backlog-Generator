from .parser import Parser

class Validation():

    def _validateTitle(self, meta) -> bool:
        if "title" not in meta:
            return False
        if not Parser().validString(meta["title"]):
            return False 
        return True

    def _validateDescription(self, meta) -> bool:
        if "description" not in meta:
            return False
        if not Parser().validString(meta["description"]):
            return False 
        return True

    def _validateTags(self, meta) -> (bool, []):
        if "tags" not in meta:
            return (False,)

        return True
        
    def _validateRoles(self, meta) -> (bool, []):
        if "roles" not in meta:
            return (False,)

        return True

    def validateMetadata(self, json) -> bool:
        if json == None:
            return False
        
        if not self._validateTitle(json):
            return False
        
        if not self._validateDescription(json):
            return False
        
        tags = self._validateTags(json)
        if (isinstance(tags, bool) and not tags) or (not isinstance(tags, bool) and isinstance(tags[0], bool) and not tags[0]):
            return False
        
        roles = self._validateRoles(json)
        if (isinstance(roles, bool) and not roles) or (not isinstance(roles, bool) and isinstance(roles[0], bool) and not roles[0]):
            return False

        return True

