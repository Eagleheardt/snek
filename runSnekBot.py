import snekCommands as cmd
import snekUtils as utils
import decode as de
import slackutils
from slack import RTMClient
import connectionHandler as ch


#################
#   TODO LIST   #
#################

# Monthly formatted report: 
# Person who reported the most - number of reports 
#   (Snek's favorite person of the month)
# Most errant server - server number - number of issues
# Overall highest reporter - number of reports
# overall most errant server - number of reports
# Daily highest number of issues.
# Highest issues on a day in that month
# Daily average overall
# daily average on the month

##########################################################

###############################
###   Get the slack token   ###
###############################

de.MAIN_KEY = utils.WORKING_PATH + utils.KEY_PATH # prod location
SLACK_TOKEN = de.getToken() # Bot's Slack token

###############################
###   End the slack token   ###
###############################

# .----------------.  .----------------.  .----------------.  .-----------------.  
# | .--------------. || .--------------. || .--------------. || .--------------. | 
# | | ____    ____ | || |      __      | || |     _____    | || | ____  _____  | | 
# | ||_   \  /   _|| || |     /  \     | || |    |_   _|   | || ||_   \|_   _| | | 
# | |  |   \/   |  | || |    / /\ \    | || |      | |     | || |  |   \ | |   | | 
# | |  | |\  /| |  | || |   / ____ \   | || |      | |     | || |  | |\ \| |   | | 
# | | _| |_\/_| |_ | || | _/ /    \ \_ | || |     _| |_    | || | _| |_\   |_  | | 
# | ||_____||_____|| || ||____|  |____|| || |    |_____|   | || ||_____|\____| | | 
# | |              | || |              | || |              | || |              | | 
# | '--------------' || '--------------' || '--------------' || '--------------' | 
#  '----------------'  '----------------'  '----------------'  '----------------'  

if __name__ == '__main__':

    def main():
 
        @RTMClient.run_on(event='message')
        def handle(**kwargs):

            try:
                text = kwargs['data']['text']

            except KeyError:
                return
            except Exception as e:
                print(e)
                return

            if text:
                slackutils.CLIENT = kwargs['web_client']
                cmd.EVAL(kwargs['data'])

        rtm_client = RTMClient(token=SLACK_TOKEN)
        rtm_client.start()
        
    main()

# .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
# | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
# | | ____    ____ | || |  _________   | || |  _________   | || |  ____  ____  | || |     ____     | || |  ________    | |
# | ||_   \  /   _|| || | |_   ___  |  | || | |  _   _  |  | || | |_   ||   _| | || |   .'    `.   | || | |_   ___ `.  | |
# | |  |   \/   |  | || |   | |_  \_|  | || | |_/ | | \_|  | || |   | |__| |   | || |  /  .--.  \  | || |   | |   `. \ | |
# | |  | |\  /| |  | || |   |  _|  _   | || |     | |      | || |   |  __  |   | || |  | |    | |  | || |   | |    | | | |
# | | _| |_\/_| |_ | || |  _| |___/ |  | || |    _| |_     | || |  _| |  | |_  | || |  \  `--'  /  | || |  _| |___.' / | |
# | ||_____||_____|| || | |_________|  | || |   |_____|    | || | |____||____| | || |   `.____.'   | || | |________.'  | |
# | |              | || |              | || |              | || |              | || |              | || |              | |
# | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
#  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
