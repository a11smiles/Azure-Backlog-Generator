from github import Github

class GitHub():
    
    def authenticate(self, username=None, password=None, hostname=None, token=None):
        if username!=None and password!=None:
            self.github = Github(username, password)
        elif hostname!=None and token!=None:
            self.github = Github(base_url=f'https://{hostname}/api/v3', login_or_token=f'{token}')
        elif token!=None:
            self.github = Github(token)
        else:
            raise ValueError("incorrect parameters were passed")

    def configure(self):
        raise NotImplementedError()

    def getUser(self):
        return self.github.get_user()

    def getOrg(self, orgName):
        return self.github.get_organization(orgName)

    def createUserRepo(self, name):
        return self.getUser().create_repo(name=f'{name}', has_issues=True, auto_init=True, private=True)

    def createOrgRepo(self, orgName, name):
        return self.getOrg(orgName).create_repo(name=f'{name}', has_issues=True, auto_init=True, private=True)