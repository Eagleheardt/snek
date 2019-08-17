import subprocess
import slackutils as utils

def restart_snek():
    subprocess.run('sudo systemctl restart snekTest.service', shell=True)

def checkStatus():
    result = utils.CLIENT.users_getPresence(user="UDKKZD7DG")
    print(result)
    return