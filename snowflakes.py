from random import randint, random, choice

import pygame as pg
import win32api
import win32con
import win32gui


def make_glass(background):
    hwnd = pg.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*background), 0, win32con.LWA_COLORKEY)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


def main():
    w, h = pg.display.Info().current_w // 2, pg.display.Info().current_h // 2
    screen = pg.display.set_mode((400, 300))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return


if __name__ == '__main__':
    pg.init()
    try:
        main()
    except KeyboardInterrupt:
        pass
    pg.quit()
