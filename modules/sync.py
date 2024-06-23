import os
from pathlib import Path
from tkinter import filedialog
import subprocess
import datetime


class SyncMine:
    _DH_ATUAL = datetime.datetime.now()
    _DH_FORMATADA = _DH_ATUAL.strftime("%d-%m-%Y %H:%M:%S")

    def __init__(self, login: str, passw: str):
        self._dir = None
        self._login = login
        self._passw = passw

    def get_up_dir(self):
        if os.path.exists("./log.txt"):
            with open("log.txt", "r") as file:
                self._dir = file.read()
        else:
            self._dir = filedialog.askdirectory()
            with open("log.txt", "x") as file:
                file.write(self._dir)

    def get_down_dir(self):
        self._down_dir = filedialog.askdirectory()

    def login(self):
        subprocess.run(["mega-logout"])
        subprocess.run(["mega-login", str(self._login), str(self._passw)])

    # def delete(self):
    #     subprocess.run(["mega-rm", "-rf", "/save_mine"])

    def upload(self):
        subprocess.run(["mega-put", str(self._dir), f"/{self._DH_FORMATADA}"])

    def download(self):
        # Get Mega Dirs
        saves = subprocess.run(["mega-ls"], capture_output=True, text=True)
        dir_names = saves.stdout.splitlines()

        # Get User option
        n = 0
        for i in dir_names:
            print(f"{n} : {i}")
            n += 1

        option = int(input("\nSave: "))
        save_selected = dir_names[option]
        print(f"Selecionado: {save_selected}")

        subprocess.run(["mega-get", str(save_selected), str(self._dir)])


sync_mine = SyncMine("fxflat16@gmail.com", "minesave10")
# sync_mine.login()
sync_mine.get_up_dir()
# sync_mine.upload()
# sync_mine.download()
