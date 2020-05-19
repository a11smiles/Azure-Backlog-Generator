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

    def _createProject(self, repo, name, body):
        return repo.create_project(name, body=body)

    def _createMilestone(self, repo, title, desc):
        return repo.create_milestone(title, description=desc)

    def _createLabel(self, repo, name):
        return repo.create_label(name)

    def _createLabels(self, repo, names):
        labels = []
        for name in names:
            labels.extend(self._createLabel(repo, name))

        return labels

    def _createIssue(self, repo, milestone, title, body, labels):
        return repo.create_issue(title, body=body, milestone=milestone, labels=labels)

    def _buildDescription(self, desc, tasks):
        pass

    def deploy(self, config, workitems):
        if config.org != None:
            repo = self._createOrgRepo(config.org, config.project)
        else:
            repo = self._createUserRepo(config.project)

        projCnt = 1
        featCnt = 1
        for epic in workitems:
            if projCnt < len(workitems):
                print('├── Creating project: ' + epic.title + " ({:02d}".format(projCnt) + "_" + epic.title + ")...")
            else:
                print('└── Creating project: ' + epic.title + " ({:02d}".format(projCnt) + "_" + epic.title + ")...")
            project = self._createProject(repo, "{:02d}".format(projCnt) + "_" + epic.title, epic.description)

            if projCnt < len(workitems):
                epicStr = "│   "
            else: 
                epicStr = "    "

            projFeatCnt = 1
            for feature in epic.features:
                if projFeatCnt == len(epic.features):
                    print(epicStr + '└── Creating milestone: ' + feature.title + " ({:02d}".format(featCnt) + "_" + feature.title + ")...")
                else:
                    print(epicStr + '├── Creating milestone: ' + feature.title + " ({:02d}".format(featCnt) + "_" + feature.title + ")...")
                milestone = self._createMilestone(repo, "{:02d}".format(featCnt) + "_" + feature.title, feature.description)
                
                if projFeatCnt < len(epic.features):
                    featStr = epicStr + "│   "
                else:
                    featStr = epicStr + "    "

                storyCnt = 1
                for story in feature.userStories:

                    if storyCnt == len(feature.userStories):
                        print(featStr + '└── Creating issue: ' + story.title + "...")
                    else:
                        print(featStr + '├── Creating issue: ' + story.title + "...")

                    issue = self._createIssue(repo, milestone, story.title, story.description, [])
            
                    storyCnt += 1
                projFeatCnt += 1
                featCnt += 1
            projCnt += 1
