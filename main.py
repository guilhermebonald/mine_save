import os
from dotenv import load_dotenv
from modules import main_sync
from time import sleep

load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASS")

lg = """
Powered By: SwatBonald


███████╗ █████╗ ██╗   ██╗███████╗    ███╗   ███╗██╗███╗   ██╗███████╗
██╔════╝██╔══██╗██║   ██║██╔════╝    ████╗ ████║██║████╗  ██║██╔════╝
███████╗███████║██║   ██║█████╗      ██╔████╔██║██║██╔██╗ ██║█████╗  
╚════██║██╔══██║╚██╗ ██╔╝██╔══╝      ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  
███████║██║  ██║ ╚████╔╝ ███████╗    ██║ ╚═╝ ██║██║██║ ╚████║███████╗
╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
                                                                     
                                        
"""

print(lg)

main_sync = main_sync.SyncMine(login=login, passw=password)


# if os.name == "nt":
#     print("For Windows here")
# elif os.name == "posix":
#     print("For Linux here")
