#!/usr/bin/env python

import argparse
import mbgenerate.helpers as helpers
import mbgenerate.services as services

parser = argparse.ArgumentParser(description="Generate a backlog of workitems for migration.")
parser.add_argument('-t', '--token', required=True, help="GitHub or Azure DevOps token")
parser.add_argument('-r', '--repo', choices=['azure', 'github'], help="Targetted repository type")
parser.add_argument('-p', '--project', help="Project name to create")
parser.add_argument('-o', '--org', help="Optional. If the target is a GitHub organization, specify the organization's name.")
parser.add_argument('-m', '--migrate', choices=['caf', 'tfs'], help="Type of migration backlog to create")
args = parser.parse_args()

#gh = GitHub()
#gh.authenticate(token="2fcaf1dd14b3cdde106b43e859ef4b2b20ee682b")
#gh.showRepos()
#gh.createUserRepo("blahblah")
#gh.createOrgRepo("DiscipledChurch", "blahblah")

#print(args.token)

#fs = helpers.FileSystem()
#files = fs.getFiles('./workitems/caf')
#files = f.getFiles('./tests/helpers/sample_path')
#val = helpers.Validation()
#val.ValidateMetadata(files)


