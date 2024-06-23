import requests
from tqdm import tqdm
import subprocess
import os


class SaveMineUnix:
    def __init__(self) -> None:
        pass

    def check_installation(self):
        check = subprocess.run(["mega-ls"], shell=True, capture_output=True, text=True)
        print(check.stdout)


save = SaveMineUnix()
save.check_installation()
