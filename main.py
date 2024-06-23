import os
from dotenv import load_dotenv

load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASS")


if os.name == "nt":
    print("For Windows here")
elif os.name == "posix":
    print("For Linux here")


lg = """
Powered By:

███████╗██╗    ██╗ █████╗ ████████╗        ██████╗ 
██╔════╝██║    ██║██╔══██╗╚══██╔══╝        ██╔══██╗
███████╗██║ █╗ ██║███████║   ██║           ██████╔╝
╚════██║██║███╗██║██╔══██║   ██║           ██╔══██╗
███████║╚███╔███╔╝██║  ██║   ██║   ███████╗██████╔╝
╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝ 
"""

print(lg)
