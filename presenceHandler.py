import subprocess
import slackutils as utils

def restart_snek():
    subprocess.run('sudo systemctl restart snek.service', shell=True)

def checkStatus():
    result = utils.CLIENT.users_getPresence(user="UDKKZD7DG")
    print(result)
    if result['presence'] is not 'active':
        #restart_snek()
        print("OPIT")
        return
    return