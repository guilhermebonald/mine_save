import requests
from tqdm import tqdm
import subprocess
import os


class MegaInstall:
    def __init__(self) -> None:
        pass

    def is_installed(self):
        # install check
        os.environ["PATH"] += (
            os.pathsep + os.environ["LOCALAPPDATA"] + "\\MEGAcmd"
        )  # set environ path by Mega Docs
        cmd_checker = subprocess.run(
            ["mega-ls"], shell=True, capture_output=True, text=True
        )
        return cmd_checker.stderr == ""

    def download_mega(self):
        url = "https://mega.nz/MEGAcmdSetup64.exe"

        response = requests.get(url, stream=True)
        file_size_bytes = response.headers.get("content-length", 0)

        progress_bar = tqdm(total=float(file_size_bytes), unit="iB", unit_scale=True)

        if response.status_code == 200:
            with open("MEGAcmdSetup.exe", "wb") as file:
                for data in response.iter_content(1024):
                    progress_bar.update(len(data))
                    file.write(data)
            progress_bar.close()
        else:
            print("Failed to Download File")

    def install_mega(self):
        subprocess.run(["MEGAcmdSetup", "/S"], shell=True)


mine = MegaInstall()
if mine.is_installed():
    # if installed here
    pass
else:
    mine.download_mega()
    mine.install_mega()
    os.environ["PATH"] += (
        os.pathsep + os.environ["LOCALAPPDATA"] + "\\MEGAcmd"
    )  # set environ path by Mega Docs
    ls = subprocess.run(["mega-ls"], shell=True, capture_output=True, text=True)
    print(ls.stdout)
