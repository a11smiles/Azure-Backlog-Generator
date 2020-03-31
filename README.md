
# Cloud Adoption Framework (CAF) Backlog
This repository contains scripts to automate the building of a backlog of stories required for one to adequately conduct and implement the Cloud Adoption Framework (CAF). The scripts can build the backlog in either Azure DevOps or GitHub.

## Overview
The [Microsoft Cloud Adoption Framework for Azure](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/) is the One Microsoft approach to cloud adoption in Azure, consolidating and shaping proven practices from Microsoft employees, partners, and customers.

Proper implementation of CAF requires solid architecture and migration experience along with rigorous amounts effort by Microsoft and the customer. Migration of on-premises workloads to the cloud is no small feat and includes many steps. Therefore, in order to assist cloud architects with migrating customers, those necessary steps have been compiled into a list of backlog items. This backlog will enable the cloud architect to manage an adoption and migration path in alignment to CAF.

## Execution
Prior to execution, please take a moment to fully read through the documentation below.

### Create a Backlog
To execute the script:
```
py ./src/create
```

### Running Tests
```
python -m unittest
```

## Shared Responsibility
Microsoft maintains a position of shared responsibility between itself and the customer. Under this shared responsibility, it is understood that appropriate cloud adoption requires active participation from the architect(s) involved and the customer unit(s). In this process, the customer should be prepared to make available network and identity administrators, application and data architects, and other security principals. By understanding requirements through active feedback, Microsoft and its technical architects can adequately assess customer needs and propose recommendations that are proven in practice and that successfully meet customer objectives.

## Technical Requirements
The scripts in this repository require Python as they rely on native Azure DevOps and GitHub SDKs. To execute these scripts, please [download Python](https://www.python.org/downloads/).

## Technical Guidelines
Below are the technical guidelines that should be followed when contributing to the project.

### Source
The application, including unit tests, are developed in Python in order to maintain compatibility between Azure DevOps and GitHub SDKs. The backlog items are developed in simple JSON format with very little metadata.

### Backlog Items
The backlog items are arranged in a collection of epics, features, stories and tasks with the necessary parent-child relationships. The following table outlines the correlations between the backlog items in Azure DevOps and GitHub.

| Azure DevOps | GitHub Issues |
|--------------|---------------|
| Epic         | Project       |
| Feature      | Milestone     |
| User Story   | Issue         |
| Task         | Checklist in the body of the Issue |

Tags will be created and applied in both platforms (in GitHub as _Labels_).

### Directory Structure
The directory structure follows a very simplistic heirarchy to fascilitate dependency creation and increase efficiency by minimizing overhead:
```
.
├── src                (source code)
├── tests              (unit tests)
└── workitems
    ├── 01_SampleEpic1
    │   ├── metadata.json
    │   └── 01_SampleFeature1
    │       ├── metadata.json
    │       └── 01_SampleStory1
    │           ├── metadata.json
    │           ├── 01_SampleTask1
    │           │   └── metadata.json
    │           └── 02_SampleTask2
    │               └── metadata.json
    └── 02_SampleEpic2
        ├── metadata.json
        ├── 01_SampleFeature1
        │   ├── metadata.json
        │   └── 01_SampleStory1
        │       ├── metadata.json
        │       └── 01_SampleTask1
        │           └── metadata.json
        └── 02_SampleFeature2
            ├── metadata.json
            └── 01_SampleStory1
                ├── metadata.json
                ├── 01_SampleTask1
                │   └── metadata.json
                └── 02_SampleTask2
                    └── metadata.json

```
The heirarchy above follows the structure of `Epic -> Feature -> User Story -> Task`. Each folder will contain a `metadata.json` file that follows the *Work Item Format* below and child items. Task folders will not contain any child work items and should only contain its metadata.

### Work Item Format
The format of the `metadata.json` file is the following:
```json
{
    "title": "Work Item Title",
    "description": "Some description of the work item",
    "tag": "Strategy | Plan | Ready | Innovation | Migration | First Workload | First Host | Workload Template",
}
```

**NOTE:** Tags **must** be one of those provided in the list above in order to correspond to the CAF mdoel.

## Contributing
Your experience and feedback are valuable and, therefore, your contributions are welcomed. Please create necessary issues and, optionally, pull requests for your feedback or contributions. Please adhere to the technical guidelines above when contributing to the source code.

Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
