import tkinter as tk
from tkinter import * 

from DBHelper import DBHelper
class Main:
    def __init__(self):
        # db 생성
        db = DBHelper()

        # 윈도우 생성
        root = tk.Tk()
        root.title("명의 나물")
        root.geometry("300x600")
        root.resizable(False, False)

#실행
Main()
