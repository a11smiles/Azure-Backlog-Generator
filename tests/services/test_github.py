import pytest
from mock import Mock, MagicMock, patch
from github import Github, Repository
from github.AuthenticatedUser import AuthenticatedUser
from github.Organization import Organization
from src.azbacklog.services import GitHub
from tests.helpers import Noniterable_str

@pytest.fixture
def mockGithub(monkeypatch):
    def mock_createRepo(*args, **kwargs):
        return Mock(spec=Repository)

    def mock_getUser(*args, **kwargs):
        return Mock(spec=AuthenticatedUser)

    def mock_getOrg(*args, **kwargs):
        return Mock(spec=Organization)

    mock = Mock(spec=Github)
    monkeypatch.setattr(Github, "get_user", mock_getUser)
    monkeypatch.setattr(Github, "get_organization", mock_getOrg)
    monkeypatch.setattr(AuthenticatedUser, "create_repo", mock_createRepo)
    monkeypatch.setattr(Organization, "create_repo", mock_createRepo)
    return mock

@patch('github.Github.__init__')
def test_authenticate(patched):
    patched.return_value = None
    
    gh = GitHub()
    gh.authenticate(username='test', password='test')
    patched.assert_called_with('test', 'test')

    gh.authenticate(hostname='test.com', token='test')
    patched.assert_called_with(base_url='https://test.com/api/v3', login_or_token='test')

    gh.authenticate(token='testToken')
    patched.assert_called_with('testToken')

    with pytest.raises(ValueError) as exc:
        gh.authenticate('something')
    assert "incorrect parameters were passed" in str(exc.value)

def test_getUser(mockGithub):
    gh = GitHub()
    gh.github = mockGithub
    gh.getUser()
    
    mockGithub.get_user.assert_called_with()

def test_getOrg(mockGithub):
    gh = GitHub()
    gh.github = mockGithub
    gh.getOrg('test')
    
    mockGithub.get_organization.assert_called_with('test')

def test_createUserRepo(mockGithub):
    gh = GitHub()
    gh.github = mockGithub
    user = gh.getUser()
    repo = gh.createUserRepo('testRepo')
    
    user.create_repo.assert_called_with(name='testRepo', has_issues=True, auto_init=True, private=True)

def test_createOrgRepo(mockGithub):
    gh = GitHub()
    gh.github = mockGithub
    org = gh.getOrg('testOrg')
    repo = gh.createOrgRepo('testOrg', 'testRepo')
    
    org.create_repo.assert_called_with(name='testRepo', has_issues=True, auto_init=True, private=True)

def test_createProject(mockGithub):
    gh = GitHub()
    gh.github = mockGithub
    repo = gh.getUser().create_repo()
    gh.createProject(repo, 'testOrg')
    
    repo.create_project.assert_called_with('testOrg')

def test_createMilestone(mockGithub):
    gh = GitHub()
    gh.github = mockGithub
    repo = gh.getUser().create_repo()
    gh.createMilestone(repo, 'testMilestone')
    
    repo.create_milestone.assert_called_with('testMilestone')

def test_createLabel(mockGithub):
    gh = GitHub()
    gh.github = mockGithub
    repo = gh.getUser().create_repo()
    gh.createLabel(repo, 'testLabel')
    
    repo.create_label.assert_called_with('testLabel')

def test_createLabels(mockGithub):
    def mock_createLabel(*args, **kwargs):
        return Noniterable_str(args[1])

    gh = GitHub()
    gh.github = mockGithub
    repo = gh.getUser().create_repo()
    gh.createLabel = MagicMock(side_effect=mock_createLabel)

    names = ['test1', 'test2']
    labels = gh.createLabels(repo, names)

    assert len(labels) == 2
    assert labels[0] == 'test1'
    assert labels[1] == "test2"

def test_createIssue(mockGithub):
    gh = GitHub()
    gh.github = mockGithub
    repo = gh.getUser().create_repo()
    gh.createIssue(repo, 'testMilestone', 'testTitle', 'testBody', [])
    
    repo.create_issue.assert_called_with('testTitle', body='testBody', milestone='testMilestone', labels=[])