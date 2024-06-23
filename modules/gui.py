import psutil
import flet as ft
from flet import ImageFit

process = []


def main(page: ft.Page):

    page.window_width = 500  # window's width is 200 px
    page.window_height = 500  # window's height is 200 px
    page.window_resizable = True

    page.add(
        ft.Column(
            [
                ft.Text("Powered By: Swat_B"),
                ft.Lottie(
                    src="https://lottie.host/89721ad9-0221-4b3b-8002-702ab7ad9c88/WvagNnuM4b.json",
                    repeat=True,
                    reverse=False,
                    animate=True,
                    fit=ImageFit.FIT_HEIGHT,
                ),
            ]
        ),
    )


ft.app(target=main)


# print(check_process("chrome.exe"))
