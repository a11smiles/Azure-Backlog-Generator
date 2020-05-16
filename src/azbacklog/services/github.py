from github import Github

class GitHub():
    
    def __init__(self, username=None, password=None, hostname=None, token=None):
        if username != None and password != None:
            self.github = Github(username, password)
        elif hostname != None and token != None:
            self.github = Github(base_url=f'https://{hostname}/api/v3', login_or_token=f'{token}')
        elif token != None:
            self.github = Github(token)
        else:
            raise ValueError("incorrect parameters were passed")

    def _getUser(self):
        return self.github.get_user()

    def _getOrg(self, orgName):
        return self.github.get_organization(orgName)

    def _createUserRepo(self, name):
        return self._getUser().create_repo(name=f'{name}', has_issues=True, auto_init=True, private=True)

    def _createOrgRepo(self, orgName, name):
        return self._getOrg(orgName).create_repo(name=f'{name}', has_issues=True, auto_init=True, private=True)

    def _createProject(self, repo, name):
        return repo.create_project(name)

    def _createMilestone(self, repo, title):
        return repo.create_milestone(title)

    def _createLabel(self, repo, name):
        return repo.create_label(name)

    def _createLabels(self, repo, names):
        labels = []
        for name in names:
            labels.extend(self._createLabel(repo, name))

        return labels

    def _createIssue(self, repo, milestone, title, body, labels):
        return repo.create_issue(title, body=body, milestone=milestone, labels=labels)

    def deploy(self, config, workitems):
        if config.org != None:
            repo = self._createOrgRepo(config.org, config.project)
        else:
            repo = self._createUserRepo(config.project)

        for epic in workitems:
            project = self._createProject(repo, epic.title)

            for feature in epic.features:
                milestone = self._createMilestone(repo, feature.title)

                for story in feature.userStories:
                    issue = self._createIssue(repo, milestone, story.title, story.description, [])
            
