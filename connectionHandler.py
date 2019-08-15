import subprocess

def restart_snek():
    subprocess.run('sudo systemctl restart snekTest.service', shell=True)