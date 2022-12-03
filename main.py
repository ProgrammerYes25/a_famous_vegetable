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

        # main_frame 구성
        main_frame = tk.Frame(root)
        main_frame.grid(row=0,column=0, sticky="nsew")
        main_page_name = tk.Label(main_frame, padx=20, pady=15, text="명의 나물", font="함초롬돋움")
        main_page_name.pack(anchor="nw")
        main_btn_frame = tk.Frame(main_frame)
        main_btn_frame.pack()
        main_list_btn = tk.Button(main_btn_frame, text="메뉴판", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.openFrame(list_frame)])
        main_list_btn.grid(row=0, column=1)
        main_home_btn = tk.Button(main_btn_frame, text="나물", fg="#88AE89", width=13, height=4, bg="#004003")
        main_home_btn.grid(row=0, column=2)
        main_diary_btn = tk.Button(main_btn_frame, text="식탁", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.openFrame(diary_frame)])
        main_diary_btn.grid(row=0, column=3)

        # list_frame 구성
        list_frame = tk.Frame(root)
        list_frame.grid(row=0,column=0, sticky="nsew")
        list_page_name = tk.Label(list_frame, padx=20, pady=15, text="명의 메뉴판", font="함초롬돋움")
        list_page_name.pack(anchor="nw")
        list_btn_frame = tk.Frame(list_frame)
        list_btn_frame.pack()
        list_list_btn = tk.Button(list_btn_frame, text="메뉴판", fg="#88AE89", width=13, height=4, bg="#004003")
        list_list_btn.grid(row=100, column=1)
        list_home_btn = tk.Button(list_btn_frame, text="나물", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.openFrame(main_frame)])
        list_home_btn.grid(row=100, column=2)
        list_diary_btn = tk.Button(list_btn_frame, text="식탁", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.openFrame(diary_frame)])
        list_diary_btn.grid(row=100, column=3)

        # diary_frame 구성
        diary_frame = tk.Frame(root)
        diary_frame.grid(row=0, column=0, sticky="nsew")
        diary_page_name = tk.Label(diary_frame,padx=20,pady=15,text="명의 식탁", font="함초롬돋움")
        diary_page_name.pack(anchor="nw")
        diary_btn_frame = tk.Frame(diary_frame)
        diary_btn_frame.pack()
        diary_list_btn = tk.Button(diary_btn_frame, text="메뉴판", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.openFrame(list_frame)])
        diary_list_btn.grid(row=100, column=1)
        diary_home_btn = tk.Button(diary_btn_frame,  text="나물", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.openFrame(main_frame)])
        diary_home_btn.grid(row=100, column=2)
        diary_diary_btn = tk.Button(diary_btn_frame, text="식탁", fg="#88AE89", width=13, height=4, bg="#004003")
        diary_diary_btn.grid(row=100, column=3)

        self.openFrame(main_frame)
        root.mainloop()

    def openFrame(self, frame):
        #프레임 전환
        frame.tkraise()
#실행
Main()
