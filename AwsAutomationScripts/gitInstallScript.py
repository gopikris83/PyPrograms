import os
import re
import subprocess
import sys
import time
import urllib.request
from bs4 import BeautifulSoup
os.system('clear')
print("Clearing the terminal.....")
time.sleep(2)

def about():
    print("*****************************************************")
    print("This script will find the existing git version if any\nand also update/install latest git")
    print("*****************************************************")
    time.sleep(2)

def end():
    print('\nThank you for using this script. Have a great day!')
    return None

def run_cmd(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    rt = process.wait()
    output, error = process.communicate()
    #print(output) 
    return output  

# Checks the Git installation
def verifyInstall():
    pattern = ":"
    PATH = re.split(pattern, os.getenv('PATH'))
    if os.path.exists(PATH[3]+'/git'):
        bashCommand = run_cmd("git --version")
        return None
        #return (bashCommand.decode()).split()[2]
    else:
        return None

# User input
def user_decision():
    ans = input('Enter yes/no:')
    if ans.lower() == 'yes':
        return "yes"
    else:
        end()
        sys.exit()
        
# Get the git Version
def getAllGitVersion():
    link = 'https://mirrors.edge.kernel.org/pub/software/scm/git/'
    req = urllib.request.urlopen(link)
    html_page = req.read()
    req.close()
    soup = BeautifulSoup(html_page, "html.parser")
    tar_object = re.compile("git-\d\.\d+\.\d+\.tar\.gz")
    version_object = re.compile("\d\.\d+\.\d")
    href_list = []
    version_list = []
    for each in soup.find_all('a', href=True):
        tar_each = each.get("href")
        if tar_object.search(tar_each)!=None:
            href_list.append(link+tar_each)
            if version_object.search(tar_each)!=None:
                version_list.append(version_object.search(tar_each).group())
    #print('Version List :\n', '  '.join(map(str, version_list)))
    return href_list, version_list

def fresh_install(git_vers):
    href_list, ver_list = getAllGitVersion()
    usr_ver = select_version(git_vers, ver_list)
    installGit(href_list, usr_ver)
    return None

def select_version(git_vers, ver_list):
    while True:
        show_versions(git_vers,ver_list)
        usr_ver = input("\nSelect the version to install:")
        if usr_ver not in ver_list:
            continue
        else:
            return usr_ver

def show_versions(git_vers, ver_list):
    Flag = False
    if git_vers not in ver_list:
        for each in ver_list:
            print(each,)
    else:
        for each in ver_list:
            if each==git_vers:
                Flag=True
                continue
            if Flag:
                print(each,)
    return None

# Perform the git installtion and create symlink
def installGit(href_list, user_version):
    for each in href_list:
        if user_version in each:
            url = each
            break
    
    download_tar = "wget "+url
    run_cmd(download_tar)
    tar_extract = url.split(os.sep)[-1]
    cmd1 = "tar -zxf "+tar_extract
    run_cmd(cmd1)
    cmd2 = tar_extract.rstrip(".tar.gz")
    cmd3 = os.getcwd()+os.sep+cmd2
    os.chdir(cmd3)
    os.system("./configure")
    os.system("make")
    os.system("make install")
    os.system("ln -s /usr/local/bin/git /bin/git") 

def updateGit(git_ver):
    href_list, ver_list = getAllGitVersion()
    usr_ver = select_version(git_ver, ver_list)
    installGit(href_list, usr_ver)
    return None


def main():
    git_ver = verifyInstall()
    print(git_ver)
    if git_ver==None:
        print('Git is not installed.')
        print('Do you want to install git on this host?')
        user_resp = user_decision()
        fresh_install(git_ver)
        print('Now git is installed with version {}'.format(verifyInstall()))
        end()
    else:
        print('Git is already installed. Installed version is {}'.format(verifyInstall()))
        print('Do you want to update the git?')
        user_resp = user_decision()
        updateGit(git_ver)
        end()


if __name__ == '__main__':
    about()
    main()