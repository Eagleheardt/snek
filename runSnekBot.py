import snekCommands as cmd
import decode as de
from slack import RTMClient
import snekUtils as utils

###############################
###   Get the slack token   ###
###############################

de.MAIN_KEY = utils.PATH + "snekBotTest/data/snekTest" # prod location
SLACK_TOKEN = de.getToken() # Bot's Slack token

###############################
###   End the slack token   ###
###############################

############################################################################
############################################################################

if __name__ == '__main__':

    def main():
 
        @RTMClient.run_on(event='message')
        def handle(**kwargs):

            try:
                text = kwargs['data']['text']

            except KeyError:
                return

            if text:
                utils.CLIENT = kwargs['web_client']
                cmd.EVAL(kwargs)

        rtm_client = RTMClient(token=SLACK_TOKEN)
        rtm_client.start()
        
    main()

