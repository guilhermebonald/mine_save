import os
from dotenv import load_dotenv
from modules import main_sync
from time import sleep

load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASS")

lg = """

███████╗ █████╗ ██╗   ██╗███████╗    ███╗   ███╗██╗███╗   ██╗███████╗
██╔════╝██╔══██╗██║   ██║██╔════╝    ████╗ ████║██║████╗  ██║██╔════╝
███████╗███████║██║   ██║█████╗      ██╔████╔██║██║██╔██╗ ██║█████╗  
╚════██║██╔══██║╚██╗ ██╔╝██╔══╝      ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  
███████║██║  ██║ ╚████╔╝ ███████╗    ██║ ╚═╝ ██║██║██║ ╚████║███████╗
╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
                                                                                                      
"""

print("\nPowered By: SwatBonald")
sleep(2)
print(lg)

main_sync = main_sync.SyncMine(login=login, passw=password)


if os.name == "nt":
    print("For Windows here")
elif os.name == "posix":
    while True:
        print("1 - Salvar | 2 - Carregar | 3 - Sair")
        option = int(input("-> "))
        if option == 1:
            main_sync.login()
            main_sync.get_dir()
            main_sync.upload()
        elif option == 2:
            main_sync.login()
            main_sync.get_dir()
            main_sync.download()
        elif option == 3:
            break
        else:
            print("Digite uma opção válida")
