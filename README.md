
# Overview

## Prior to running this script

Generate 'Personal access token' from <https://github.com/settings/tokens>
Enter description, select scopes below and save: 
  repo            => Full control of private repositories
  admin:repo_hook => Full control of repository hooks

<https://pygithub.readthedocs.io/en/latest/introduction.html>

Add the following entry under the [packages] section to the default 'Pipfile'

> [packages]
> PyGithub = "*"

Install package dependencies (PyGithub)
pipenv install

Run the script in the python virtual environment ('tfbuild' defined in Pipfile)
pipenv run ./tf_setup.py

Execute from the parent directory where you want to store each local repository as a child subdirectory

```console
tf_setup.json parameter descriptions, customize per environment
"github_local_parent_repo_dir": "Parent directory for Terraform Github repos"
"github_repo_owner": "Github account owner name",
"github_access_key": "Github personal access key token",
"repos": "Name and description of each Github repo"
"environments": "Name and description of each client environment"
"clouds": "Name and description of each client cloud"
"files": "Name and description of each standard .tf file for each environment/cloud"
```

## Terraform Enterprise

### Example Multi-Cloud Workspace Deployment with Github

#### Hierarchy Approach: [github_repository] / [terraform_workspace] / [cloud_provider] / [terraform_files]

#### Based on HashiCorp recommended approach "Multiple Workspaces per Repo"

<https://www.terraform.io/docs/cloud/workspaces/repo-structure.html>

### Create Terraform Workspaces

```console
cd /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-dev && terraform workspace new compute-dev
cd /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-stage && terraform workspace new compute-stage
cd /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-prod && terraform workspace new compute-prod
cd /Users/joe.akerson/code/terraform-repos/terraform-network/network-dev && terraform workspace new network-dev
cd /Users/joe.akerson/code/terraform-repos/terraform-network/network-stage && terraform workspace new network-stage
cd /Users/joe.akerson/code/terraform-repos/terraform-network/network-prod && terraform workspace new network-prod
cd /Users/joe.akerson/code/terraform-repos/terraform-security/security-dev && terraform workspace new security-dev
cd /Users/joe.akerson/code/terraform-repos/terraform-security/security-stage && terraform workspace new security-stage
cd /Users/joe.akerson/code/terraform-repos/terraform-security/security-prod && terraform workspace new security-prod
```

### Touch Terraform Files

```console
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-dev/aws/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-dev/aws/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-dev/aws/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-dev/azure/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-dev/azure/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-dev/azure/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-dev/vmware/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-dev/vmware/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-dev/vmware/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-stage/aws/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-stage/aws/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-stage/aws/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-stage/azure/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-stage/azure/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-stage/azure/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-stage/vmware/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-stage/vmware/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-stage/vmware/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-prod/aws/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-prod/aws/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-prod/aws/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-prod/azure/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-prod/azure/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-prod/azure/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-prod/vmware/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-prod/vmware/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-compute/compute-prod/vmware/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-dev/aws/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-dev/aws/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-dev/aws/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-dev/azure/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-dev/azure/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-dev/azure/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-dev/vmware/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-dev/vmware/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-dev/vmware/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-stage/aws/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-stage/aws/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-stage/aws/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-stage/azure/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-stage/azure/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-stage/azure/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-stage/vmware/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-stage/vmware/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-stage/vmware/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-prod/aws/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-prod/aws/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-prod/aws/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-prod/azure/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-prod/azure/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-prod/azure/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-prod/vmware/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-prod/vmware/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-network/network-prod/vmware/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-dev/aws/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-dev/aws/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-dev/aws/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-dev/azure/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-dev/azure/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-dev/azure/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-dev/vmware/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-dev/vmware/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-dev/vmware/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-stage/aws/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-stage/aws/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-stage/aws/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-stage/azure/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-stage/azure/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-stage/azure/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-stage/vmware/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-stage/vmware/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-stage/vmware/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-prod/aws/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-prod/aws/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-prod/aws/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-prod/azure/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-prod/azure/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-prod/azure/variables.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-prod/vmware/main.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-prod/vmware/outputs.tf
touch /Users/joe.akerson/code/terraform-repos/terraform-security/security-prod/vmware/variables.tf
```

### Create Remote Github Repos using python PyGithub module

```console
repo_inst.create_repo(terraform-compute, description=Terraform Compute Modules)
repo_inst.create_repo(terraform-network, description=Terraform Network Modules)
repo_inst.create_repo(terraform-security, description=Terraform Security Modules)
```

### Clone to Local Github Repos

```console
git clone ssh://git@github.com/jaklouddemo/terraform-compute.git
git clone ssh://git@github.com/jaklouddemo/terraform-network.git
git clone ssh://git@github.com/jaklouddemo/terraform-security.git
```
