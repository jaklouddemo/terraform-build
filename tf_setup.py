from github import Github
import json
import os

access_key = input('Please enter your Github personal access key token: ')

def import_config(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data

def create_ws(wspath_list):
    for wspath in wspath_list:
        ws_name = '/'.join(wspath.split('/')[-1:])
        new_dir_cmd = 'cd ' + wspath + ' && terraform workspace new ' + ws_name
        print(new_dir_cmd)

def create_files(fpath_list):
    for fp in fpath_list:
        create_file_cmd = 'touch ' + fp
        print(create_file_cmd)

def auth_github(access_token):
    g = Github(access_token)
    return g

# Create github repositories from 'repos' dict
def create_repos(repo_inst, repos_dict):
    for name, desc in repos_dict.items():
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
def list_repos(repo_inst):
    for r in repo_inst.get_repos():
        print(r.name)

# Clone each of the newly created respositories to local machine
def clone_repos(repo_owner, repos_list):
    for repo_name in repos_list:
        git_clone_cmd = 'git clone ssh://git@github.com/' + repo_owner + '/' + repo_name + '.git'
        print(git_clone_cmd)
        #os.system(git_clone_cmd)

json_file = './tf_setup.json'
cfg = import_config(json_file)
base_path = cfg['github_local_parent_repo_dir']
repo_owner = cfg['github_repo_owner']

repos_dict = cfg['repos']
environments_dict = cfg['environments']
clouds_dict = cfg['clouds']
files_dict = cfg['files']

repos_list = list(repos_dict.keys())
environments_list = list(environments_dict.keys())
clouds_list = list(clouds_dict.keys())
files_list = list(files_dict.keys())

ws_list = []
wspath_list = []
fpath_list = []

for r in repos_list:
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
# repo_inst = auth_github(access_key).get_user()
# List repos
# list_repos(repo_inst)
print('## Terraform Enterprise')
print('')
print('### Example Multi-Cloud Workspace Deployment with Github')
print('')
print('#### Hierarchy Approach: [github_repository] / [terraform_workspace] / [cloud_provider] / [terraform_files]')
print('')
print('#### Based on HashiCorp recommended approach "Multiple Workspaces per Repo"')
print('')
print('<https://www.terraform.io/docs/cloud/workspaces/repo-structure.html>')
print('')
print('### Create Terraform Workspaces')
print('')
print('```console')
create_ws(wspath_list)
print('```')
print('')
print('### Touch Terraform Files')
print('')
print('```console')
create_files(fpath_list)
print('```')
print('')
print('### Create Remote Github Repos using python PyGithub module')
print('')
print('```console')
create_repos(repo_owner, repos_dict)
print('```')
print('')
print('### Clone to Local Github Repos')
print('')
print('```console')
clone_repos(repo_owner, repos_list)
print('```')
print('')
