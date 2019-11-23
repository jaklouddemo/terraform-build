## Terraform Enterprise VCS Integration

### Example Multi-Cloud Workspace Deployment with VCS Repository
> _SaaS VCS providers currently supported: **github.com** and **gitlab.com**_

### Pre-Requisites

> Install Terraform and Git clients locally

#### Python Configuration and Script Usage

```console
bash-3.2$ pip install pyenv pipenv
bash-3.2$ pipenv install
bash-3.2$pipenv shell
(terraform-build) bash-3.2$ python ./tf_repo_setup.py
Please enter repo_type, valid options are ['gitlab', 'github']: <vcs_provider>
```

#### Configure Git global variables

```console
git config --global user.name "<repo_owner>"
git config --global user.email "<repo_owner_email>"
```

#### Customize Configuration Input File (./tf_repo_setup.json)

#### Hierarchy Approach
> ~/ [repository] / [terraform_workspace] / [cloud_provider] / [terraform_files]

#### Based on HashiCorp recommended approach "Multiple Workspaces per Repo"

> <https://www.terraform.io/docs/cloud/workspaces/repo-structure.html>

> Note: repos, environments, clouds and files must have a minimum of 1 key : value, more can also be added
```json
{
    "local_repo_base_dir": "~/code/terraform-repos",
    "repo_owner": "<repo_owner>",
    "git_global_email": "<repo_owner_emal>",
    "repos": {
        "terraform-compute": "Terraform Compute Modules",
        "terraform-network": "Terraform Network Modules",
        "terraform-security": "Terraform Security Modules"
    },
    "environments": {
        "dev": "Development Environment",
        "stage": "Stage Environment",
        "prod": "Prod Environment"
    },
    "clouds": {
        "aws": "AWS provider code",
        "azure": "Azure provider code",
        "vmware": "VMware provider code"
    },
    "files": {
        "main.tf": "Terraform main definition file",
        "outputs.tf": "Terraform output definition file",
        "variables.tf": "Terraform variable definition file",
        "README.md": "Readme markdown file describing code"
    }
}
```

### 1. Create Remote Repos Using Python Module

```console
repo_inst.create_repo(terraform-compute, description=Terraform Compute Modules)
repo_inst.create_repo(terraform-network, description=Terraform Network Modules)
repo_inst.create_repo(terraform-security, description=Terraform Security Modules)
```

### 2. Clone Remote Repos Locally

```console
cd ~/
git clone ssh://git@gitlab.com/jaklouddemo/terraform-compute.git
git clone ssh://git@gitlab.com/jaklouddemo/terraform-network.git
git clone ssh://git@gitlab.com/jaklouddemo/terraform-security.git
```

### 3. Create Local Repo Directory Structure & Empty Terraform Files

```console
mkdir -p ~/code/terraform-repos/terraform-compute/compute-dev/aws && touch ~/code/terraform-repos/terraform-compute/compute-dev/aws/main.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-dev/aws && touch ~/code/terraform-repos/terraform-compute/compute-dev/aws/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-dev/aws && touch ~/code/terraform-repos/terraform-compute/compute-dev/aws/variables.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-dev/aws && touch ~/code/terraform-repos/terraform-compute/compute-dev/aws/README.md
mkdir -p ~/code/terraform-repos/terraform-compute/compute-dev/azure && touch ~/code/terraform-repos/terraform-compute/compute-dev/azure/main.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-dev/azure && touch ~/code/terraform-repos/terraform-compute/compute-dev/azure/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-dev/azure && touch ~/code/terraform-repos/terraform-compute/compute-dev/azure/variables.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-dev/azure && touch ~/code/terraform-repos/terraform-compute/compute-dev/azure/README.md
mkdir -p ~/code/terraform-repos/terraform-compute/compute-dev/vmware && touch ~/code/terraform-repos/terraform-compute/compute-dev/vmware/main.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-dev/vmware && touch ~/code/terraform-repos/terraform-compute/compute-dev/vmware/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-dev/vmware && touch ~/code/terraform-repos/terraform-compute/compute-dev/vmware/variables.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-dev/vmware && touch ~/code/terraform-repos/terraform-compute/compute-dev/vmware/README.md
mkdir -p ~/code/terraform-repos/terraform-compute/compute-stage/aws && touch ~/code/terraform-repos/terraform-compute/compute-stage/aws/main.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-stage/aws && touch ~/code/terraform-repos/terraform-compute/compute-stage/aws/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-stage/aws && touch ~/code/terraform-repos/terraform-compute/compute-stage/aws/variables.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-stage/aws && touch ~/code/terraform-repos/terraform-compute/compute-stage/aws/README.md
mkdir -p ~/code/terraform-repos/terraform-compute/compute-stage/azure && touch ~/code/terraform-repos/terraform-compute/compute-stage/azure/main.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-stage/azure && touch ~/code/terraform-repos/terraform-compute/compute-stage/azure/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-stage/azure && touch ~/code/terraform-repos/terraform-compute/compute-stage/azure/variables.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-stage/azure && touch ~/code/terraform-repos/terraform-compute/compute-stage/azure/README.md
mkdir -p ~/code/terraform-repos/terraform-compute/compute-stage/vmware && touch ~/code/terraform-repos/terraform-compute/compute-stage/vmware/main.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-stage/vmware && touch ~/code/terraform-repos/terraform-compute/compute-stage/vmware/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-stage/vmware && touch ~/code/terraform-repos/terraform-compute/compute-stage/vmware/variables.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-stage/vmware && touch ~/code/terraform-repos/terraform-compute/compute-stage/vmware/README.md
mkdir -p ~/code/terraform-repos/terraform-compute/compute-prod/aws && touch ~/code/terraform-repos/terraform-compute/compute-prod/aws/main.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-prod/aws && touch ~/code/terraform-repos/terraform-compute/compute-prod/aws/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-prod/aws && touch ~/code/terraform-repos/terraform-compute/compute-prod/aws/variables.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-prod/aws && touch ~/code/terraform-repos/terraform-compute/compute-prod/aws/README.md
mkdir -p ~/code/terraform-repos/terraform-compute/compute-prod/azure && touch ~/code/terraform-repos/terraform-compute/compute-prod/azure/main.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-prod/azure && touch ~/code/terraform-repos/terraform-compute/compute-prod/azure/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-prod/azure && touch ~/code/terraform-repos/terraform-compute/compute-prod/azure/variables.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-prod/azure && touch ~/code/terraform-repos/terraform-compute/compute-prod/azure/README.md
mkdir -p ~/code/terraform-repos/terraform-compute/compute-prod/vmware && touch ~/code/terraform-repos/terraform-compute/compute-prod/vmware/main.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-prod/vmware && touch ~/code/terraform-repos/terraform-compute/compute-prod/vmware/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-prod/vmware && touch ~/code/terraform-repos/terraform-compute/compute-prod/vmware/variables.tf
mkdir -p ~/code/terraform-repos/terraform-compute/compute-prod/vmware && touch ~/code/terraform-repos/terraform-compute/compute-prod/vmware/README.md
mkdir -p ~/code/terraform-repos/terraform-network/network-dev/aws && touch ~/code/terraform-repos/terraform-network/network-dev/aws/main.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-dev/aws && touch ~/code/terraform-repos/terraform-network/network-dev/aws/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-dev/aws && touch ~/code/terraform-repos/terraform-network/network-dev/aws/variables.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-dev/aws && touch ~/code/terraform-repos/terraform-network/network-dev/aws/README.md
mkdir -p ~/code/terraform-repos/terraform-network/network-dev/azure && touch ~/code/terraform-repos/terraform-network/network-dev/azure/main.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-dev/azure && touch ~/code/terraform-repos/terraform-network/network-dev/azure/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-dev/azure && touch ~/code/terraform-repos/terraform-network/network-dev/azure/variables.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-dev/azure && touch ~/code/terraform-repos/terraform-network/network-dev/azure/README.md
mkdir -p ~/code/terraform-repos/terraform-network/network-dev/vmware && touch ~/code/terraform-repos/terraform-network/network-dev/vmware/main.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-dev/vmware && touch ~/code/terraform-repos/terraform-network/network-dev/vmware/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-dev/vmware && touch ~/code/terraform-repos/terraform-network/network-dev/vmware/variables.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-dev/vmware && touch ~/code/terraform-repos/terraform-network/network-dev/vmware/README.md
mkdir -p ~/code/terraform-repos/terraform-network/network-stage/aws && touch ~/code/terraform-repos/terraform-network/network-stage/aws/main.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-stage/aws && touch ~/code/terraform-repos/terraform-network/network-stage/aws/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-stage/aws && touch ~/code/terraform-repos/terraform-network/network-stage/aws/variables.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-stage/aws && touch ~/code/terraform-repos/terraform-network/network-stage/aws/README.md
mkdir -p ~/code/terraform-repos/terraform-network/network-stage/azure && touch ~/code/terraform-repos/terraform-network/network-stage/azure/main.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-stage/azure && touch ~/code/terraform-repos/terraform-network/network-stage/azure/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-stage/azure && touch ~/code/terraform-repos/terraform-network/network-stage/azure/variables.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-stage/azure && touch ~/code/terraform-repos/terraform-network/network-stage/azure/README.md
mkdir -p ~/code/terraform-repos/terraform-network/network-stage/vmware && touch ~/code/terraform-repos/terraform-network/network-stage/vmware/main.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-stage/vmware && touch ~/code/terraform-repos/terraform-network/network-stage/vmware/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-stage/vmware && touch ~/code/terraform-repos/terraform-network/network-stage/vmware/variables.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-stage/vmware && touch ~/code/terraform-repos/terraform-network/network-stage/vmware/README.md
mkdir -p ~/code/terraform-repos/terraform-network/network-prod/aws && touch ~/code/terraform-repos/terraform-network/network-prod/aws/main.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-prod/aws && touch ~/code/terraform-repos/terraform-network/network-prod/aws/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-prod/aws && touch ~/code/terraform-repos/terraform-network/network-prod/aws/variables.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-prod/aws && touch ~/code/terraform-repos/terraform-network/network-prod/aws/README.md
mkdir -p ~/code/terraform-repos/terraform-network/network-prod/azure && touch ~/code/terraform-repos/terraform-network/network-prod/azure/main.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-prod/azure && touch ~/code/terraform-repos/terraform-network/network-prod/azure/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-prod/azure && touch ~/code/terraform-repos/terraform-network/network-prod/azure/variables.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-prod/azure && touch ~/code/terraform-repos/terraform-network/network-prod/azure/README.md
mkdir -p ~/code/terraform-repos/terraform-network/network-prod/vmware && touch ~/code/terraform-repos/terraform-network/network-prod/vmware/main.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-prod/vmware && touch ~/code/terraform-repos/terraform-network/network-prod/vmware/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-prod/vmware && touch ~/code/terraform-repos/terraform-network/network-prod/vmware/variables.tf
mkdir -p ~/code/terraform-repos/terraform-network/network-prod/vmware && touch ~/code/terraform-repos/terraform-network/network-prod/vmware/README.md
mkdir -p ~/code/terraform-repos/terraform-security/security-dev/aws && touch ~/code/terraform-repos/terraform-security/security-dev/aws/main.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-dev/aws && touch ~/code/terraform-repos/terraform-security/security-dev/aws/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-dev/aws && touch ~/code/terraform-repos/terraform-security/security-dev/aws/variables.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-dev/aws && touch ~/code/terraform-repos/terraform-security/security-dev/aws/README.md
mkdir -p ~/code/terraform-repos/terraform-security/security-dev/azure && touch ~/code/terraform-repos/terraform-security/security-dev/azure/main.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-dev/azure && touch ~/code/terraform-repos/terraform-security/security-dev/azure/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-dev/azure && touch ~/code/terraform-repos/terraform-security/security-dev/azure/variables.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-dev/azure && touch ~/code/terraform-repos/terraform-security/security-dev/azure/README.md
mkdir -p ~/code/terraform-repos/terraform-security/security-dev/vmware && touch ~/code/terraform-repos/terraform-security/security-dev/vmware/main.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-dev/vmware && touch ~/code/terraform-repos/terraform-security/security-dev/vmware/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-dev/vmware && touch ~/code/terraform-repos/terraform-security/security-dev/vmware/variables.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-dev/vmware && touch ~/code/terraform-repos/terraform-security/security-dev/vmware/README.md
mkdir -p ~/code/terraform-repos/terraform-security/security-stage/aws && touch ~/code/terraform-repos/terraform-security/security-stage/aws/main.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-stage/aws && touch ~/code/terraform-repos/terraform-security/security-stage/aws/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-stage/aws && touch ~/code/terraform-repos/terraform-security/security-stage/aws/variables.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-stage/aws && touch ~/code/terraform-repos/terraform-security/security-stage/aws/README.md
mkdir -p ~/code/terraform-repos/terraform-security/security-stage/azure && touch ~/code/terraform-repos/terraform-security/security-stage/azure/main.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-stage/azure && touch ~/code/terraform-repos/terraform-security/security-stage/azure/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-stage/azure && touch ~/code/terraform-repos/terraform-security/security-stage/azure/variables.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-stage/azure && touch ~/code/terraform-repos/terraform-security/security-stage/azure/README.md
mkdir -p ~/code/terraform-repos/terraform-security/security-stage/vmware && touch ~/code/terraform-repos/terraform-security/security-stage/vmware/main.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-stage/vmware && touch ~/code/terraform-repos/terraform-security/security-stage/vmware/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-stage/vmware && touch ~/code/terraform-repos/terraform-security/security-stage/vmware/variables.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-stage/vmware && touch ~/code/terraform-repos/terraform-security/security-stage/vmware/README.md
mkdir -p ~/code/terraform-repos/terraform-security/security-prod/aws && touch ~/code/terraform-repos/terraform-security/security-prod/aws/main.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-prod/aws && touch ~/code/terraform-repos/terraform-security/security-prod/aws/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-prod/aws && touch ~/code/terraform-repos/terraform-security/security-prod/aws/variables.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-prod/aws && touch ~/code/terraform-repos/terraform-security/security-prod/aws/README.md
mkdir -p ~/code/terraform-repos/terraform-security/security-prod/azure && touch ~/code/terraform-repos/terraform-security/security-prod/azure/main.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-prod/azure && touch ~/code/terraform-repos/terraform-security/security-prod/azure/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-prod/azure && touch ~/code/terraform-repos/terraform-security/security-prod/azure/variables.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-prod/azure && touch ~/code/terraform-repos/terraform-security/security-prod/azure/README.md
mkdir -p ~/code/terraform-repos/terraform-security/security-prod/vmware && touch ~/code/terraform-repos/terraform-security/security-prod/vmware/main.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-prod/vmware && touch ~/code/terraform-repos/terraform-security/security-prod/vmware/outputs.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-prod/vmware && touch ~/code/terraform-repos/terraform-security/security-prod/vmware/variables.tf
mkdir -p ~/code/terraform-repos/terraform-security/security-prod/vmware && touch ~/code/terraform-repos/terraform-security/security-prod/vmware/README.md
```

### 4. Create Terraform Workspaces

```console
cd ~/code/terraform-repos/terraform-compute/compute-dev && terraform workspace new compute-dev
cd ~/code/terraform-repos/terraform-compute/compute-stage && terraform workspace new compute-stage
cd ~/code/terraform-repos/terraform-compute/compute-prod && terraform workspace new compute-prod
cd ~/code/terraform-repos/terraform-network/network-dev && terraform workspace new network-dev
cd ~/code/terraform-repos/terraform-network/network-stage && terraform workspace new network-stage
cd ~/code/terraform-repos/terraform-network/network-prod && terraform workspace new network-prod
cd ~/code/terraform-repos/terraform-security/security-dev && terraform workspace new security-dev
cd ~/code/terraform-repos/terraform-security/security-stage && terraform workspace new security-stage
cd ~/code/terraform-repos/terraform-security/security-prod && terraform workspace new security-prod
```

### 5. Add New Files to Git Repo, Commit and Push to Master

```console
cd ~/code/terraform-repos/terraform-compute && git add . && git commit -m "Initial Commit" && git push -u origin master
cd ~/code/terraform-repos/terraform-network && git add . && git commit -m "Initial Commit" && git push -u origin master
cd ~/code/terraform-repos/terraform-security && git add . && git commit -m "Initial Commit" && git push -u origin master
```
