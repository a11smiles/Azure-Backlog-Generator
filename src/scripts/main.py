#!/usr/bin/env python

import argparse
import azbacklog.helpers as helpers
import azbacklog.services as services

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='azbacklog', description="Generate a backlog of work items.", allow_abbrev=False)
    parser.add_argument('-t', '--token', required=True, help="GitHub or Azure DevOps token")
    parser.add_argument('-r', '--repo', choices=['azure', 'github'], help="targetted repository type")
    parser.add_argument('-p', '--project', help="project name to create")
    parser.add_argument('-o', '--org', help="Optional. If the target is a GitHub organization, specify the organization's name.")
    parser.add_argument('-b', '--backlog', choices=['caf', 'tfs'], help="type of backlog to create")
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

    bl = helpers.Backlog()
    bl.build('./workitems/caf')


