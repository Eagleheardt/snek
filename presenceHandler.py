import subprocess
import snekUtils as utils
import schedule

def restart_snek():
    subprocess.run('sudo systemctl restart snek.service', shell=True)

def checkStatus(aClient):
    result = aClient.users_getPresence(user=utils.SNEK_ID)
    if str(result['presence']) != 'active':
        utils.snekLogger("Snek offline unexpectedly.")
        restart_snek()
        return
    return