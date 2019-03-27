from microsoftbotframework import MsBot
#from tasks import *
#from task_rule import *
#from tasks_search import *
from tasksmodel import * 

bot = MsBot()
bot.add_process(echo_response)

if __name__ == '__main__':
    bot.run()