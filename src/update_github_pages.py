import subprocess

def gitAdd():

    try:
        commandAdd = "git add ."
        subprocess.run(commandAdd)
        print("The files have been staged succesfully.")

    except subprocess.SubprocessError:
        print("The git add command could not be executed successfully, please review it and try again.")


def gitCommit():

    try: 
        commandCommit = 'git commit -m "feat(docs): update webpage on github pages (test)"'
        subprocess.run(commandCommit)
        print("The commit has been created succesfully.")

    except subprocess.SubprocessError:
        print("The git commit command could not be executed successfully, please review it and try again.")

def gitPull():

    try:
        commandPull = "git pull origin main"
        subprocess.run(commandPull)
        print("The files have been pulled from the remote repository succesfully.")

    except subprocess.SubprocessError:
        print("The git add pull could not be executed successfully, please review it and try again.")


def gitPush():

    try:
        commandPush = "git push -u origin main"
        subprocess.run(commandPush)
        print("The files have been pushed to remote repository succesfully.")

    except subprocess.SubprocessError:
        print("The git push command could not be executed successfully, please review it and try again.")


def updateGitHubPages():

    gitAdd()

    gitCommit()

    gitPull()

    gitPush()

if __name__ == "__main__":

    #Execute it in the terminal with "python .\src\update_github_pages.py".
    updateGitHubPages()