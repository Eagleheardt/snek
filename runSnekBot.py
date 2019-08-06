import Command as command
import decode as de
from slack import RTMClient, WebClient
import snekUtils as utils

##############################
###   Client 2.0 Updated   ###
##############################

USER_ID = '' # Snek's user ID

###############################
###   Get the slack token   ###
###############################

de.MAIN_KEY = "snekbot/data/snek_token" # prod location
SLACK_TOKEN = de.getToken() # Bot's Slack token

###############################
###   End the slack token   ###
###############################

############################################################################
############################################################################

def shouldHandle(user=USER_ID, text=''):
    return (user != USER_ID
        and len(text) is not 0)

if __name__ == '__main__':

    def main():
 
        @RTMClient.run_on(event='message')
        def handle(**kwargs):
            data = kwargs['data']
            text = data['text']
            if data['user'] != USER_ID:
                utils.CLIENT = data['web_client']
                print(data)
                command.EVAL(kwargs)

        rtm_client = RTMClient(token=SLACK_TOKEN)
        rtm_client.start()
        
    main()

