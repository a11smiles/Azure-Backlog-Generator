from helpers.filesystem import FileSystem
from services.github import GitHub

#gh = GitHub()
#gh.authenticate(token="2fcaf1dd14b3cdde106b43e859ef4b2b20ee682b")
#gh.showRepos()
#gh.createUserRepo("blahblah")
#gh.createOrgRepo("DiscipledChurch", "blahblah")

f = FileSystem()
files = f.getFiles('./workitems/caf')
#files = f.getFiles('./tests/helpers/sample_path')
print(files)