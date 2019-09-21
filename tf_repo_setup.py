from gitlab import Gitlab
from github import Github
import json
import os

valid_input = ['gitlab', 'github']
creds_file = '../creds.json'
repo_setup_file = './tf_repo_setup.json'

def import_config(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data

def create_ws(wspath_list):
    for wspath in wspath_list:
        ws_name = '/'.join(wspath.split('/')[-1:])
        new_dir_cmd = 'cd ' + wspath + ' && terraform workspace new ' + ws_name
        print(new_dir_cmd)

def update_repo(rpath_list):
    for rpath in rpath_list:
        update_repo_cmd = 'cd ' + rpath + ' && git add . && git commit -m \"Initial Commit\" && git push -u origin master'
        print(update_repo_cmd)

def create_files(fpath_list):
    for fp in fpath_list:
        dpath = os.path.dirname(fp)
        create_file_cmd = 'mkdir -p ' + dpath + ' && touch ' + fp
        print(create_file_cmd)

def auth_github(access_token):
    gh = Github(access_token)
    return gh

def auth_gitlab(access_token):
    gl = Gitlab('https://gitlab.com', private_token=access_token)
    return gl

# Create github repositories from 'repos' dict
def create_repos(repo_type, repo_inst, repos_dict):
    for name, desc in repos_dict.items():
        if repo_type == 'github':
            print('repo_inst.create_repo(' + name + ', description=' + desc + ')')
        elif repo_type == 'gitlab':
            print('repo_inst.create_repo(' + name + ', description=' + desc + ')')
    #     new_repo = repo_inst.create_repo(
    #         name,
    #         allow_rebase_merge=True,
    #         auto_init=True,
    #         description=desc,
    #         has_issues=False,
    #         has_projects=False,
    #         has_wiki=False,
    #         private=True,
    #         )
    #     return(new_repo)

# List all github repositiories for username
def list_repos(repo_type, repo_inst):
    if repo_type == 'github':
        for r in repo_inst.get_repos():
            print(r.name)

# Clone each of the newly created respositories to local machine
def clone_repos(repo_type, repo_owner, repos_list):
    for repo_name in repos_list:
        git_clone_cmd = 'git clone ssh://git@' + repo_type + '.com/' + repo_owner + '/' + repo_name + '.git'
        print(git_clone_cmd)
        #os.system(git_clone_cmd)

while True:
    try:
        repo_type = input('Please enter repo_type, valid options are ' + str(valid_input) + ': ')
        if repo_type in valid_input:
            break
    except ValueError:
        print('Invalid input, exiting...')
        exit()


creds = import_config(creds_file)

cfg = import_config(repo_setup_file)

base_path = cfg['local_repo_base_dir']
repo_owner = cfg['repo_owner']
access_key = creds[repo_type]

repos_dict = cfg['repos']
environments_dict = cfg['environments']
clouds_dict = cfg['clouds']
files_dict = cfg['files']

repos_list = list(repos_dict.keys())
environments_list = list(environments_dict.keys())
clouds_list = list(clouds_dict.keys())
files_list = list(files_dict.keys())

rpath_list = []
ws_list = []
wspath_list = []
fpath_list = []

for r in repos_list:
    rpath = base_path + '/' + r
    rpath_list.append(rpath)
    for e in environments_list:
        rstr = r.split('-')[1]
        ws = rstr + '-' + e
        fpstr = base_path + '/' + r + '/' + ws
        wspath_list.append(fpstr)
        for c in clouds_list:
            for f in files_list:
                fp = fpstr + '/' + c + '/' + f
                fpath_list.append(fp)

# Authenticate
if repo_type == 'github':
    repo_inst = auth_github(access_key)
elif repo_type == 'gitlab':
    repo_inst = auth_gitlab(access_key)

# List repos
#list_repos(repo_inst)
#print(list_repos)

print('## Terraform Enterprise VCS Integration')
print('')
print('### Example Multi-Cloud Workspace Deployment with VCS Repository')
print('> _SaaS VCS providers currently supported: **github.com** and **gitlab.com**_')
print('')

print('### Pre-Requisites')
print('')
print('> Install Terraform and Git clients locally')
print('')

print('#### Python Configuration and Script Usage')
print('')
print('```console')
print('bash-3.2$ pip install pyenv pipenv')
print('bash-3.2$ pipenv install')
print('bash-3.2$pipenv shell')
print('(terraform-build) bash-3.2$ python ./tf_repo_setup.py')
print("Please enter repo_type, valid options are ['gitlab', 'github']: <vcs_provider>")
print('```')
print('')

print('#### Configure Git global variables')
print('')
print('```console')
print('git config --global user.name \"<repo_owner>\"')
print('git config --global user.email \"<repo_owner_email>\"')
print('```')
print('')

print('#### Customize Configuration Input File (./tf_repo_setup.json)')
print('')
print('#### Hierarchy Approach')
print('> ~/ [repository] / [terraform_workspace] / [cloud_provider] / [terraform_files]')
print('')
print('#### Based on HashiCorp recommended approach "Multiple Workspaces per Repo"')
print('')
print('> <https://www.terraform.io/docs/cloud/workspaces/repo-structure.html>')
print('')
print('> Note: repos, environments, clouds and files must have a minimum of 1 key : value, more can also be added')
print('```json')
print(json.dumps(cfg, indent=4))
print('```')
print('')

print('### 1. Create Remote Repos Using Python Module')
print('')
print('```console')
create_repos(repo_type, repo_owner, repos_dict)
print('```')
print('')

print('### 2. Clone Remote Repos Locally')
print('')
print('```console')
print('cd ~/')
clone_repos(repo_type, repo_owner, repos_list)
print('```')
print('')

print('### 3. Create Local Repo Directory Structure & Empty Terraform Files')
print('')
print('```console')
create_files(fpath_list)
print('```')
print('')

print('### 4. Create Terraform Workspaces')
print('')
print('```console')
create_ws(wspath_list)
print('```')
print('')

print('### 5. Add New Files to Git Repo, Commit and Push to Master')
print('')
print('```console')
update_repo(rpath_list)
print('```')
print('')
