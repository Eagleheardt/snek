import subprocess
import slackutils as utils

def restart_snek():
    subprocess.run('sudo systemctl restart snekTest.service', shell=True)

def checkStatus():
    result = utils.CLIENT.presence_query(ids="UDKKZD7DG")
    print(result)
    return