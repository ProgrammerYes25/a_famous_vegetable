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
        root.geometry("300x500")
        root.resizable(False, False)

        # main_frame 구성
        main_frame = tk.Frame(root)
        main_frame.grid(row=0,column=0, sticky="nsew")
        # main_frame 구성 - 페이지 이름
        main_page_name = tk.Label(main_frame, padx=20, pady=15, text="명의 나물", font="함초롬돋움")
        main_page_name.pack(anchor="nw")
        # main_frame 구성 - 페이지 설명
        main_page_text = tk.Label(main_frame,  padx=30, pady=40,text="명의 나물은\n일상생활 속 마음의 양식을\n 충전할 수 있는\n 마음의 식당입니다. ", font="HY바다L")
        main_page_text.pack();
        # main_frame 구성 - 메뉴 이동 버튼
        list_btn = tk.Button(main_frame, padx=5, pady=10, text="명언과 명대사가 있는 메뉴판 보러가기", fg="#004003", width=35, height=2, bg="#A4E1B2", command=lambda:[self.open_frame(list_frame)])
        list_btn.pack();
        margin_label1 = tk.Label(main_frame,pady=10)
        margin_label1.pack()
        diary_btn = tk.Button(main_frame, padx=5, pady=10, text="나의 하루하루를 나누고 기록하는 식탁가기", fg="#004003", width=35, height=2, bg="#A4E1B2", command=lambda: [self.open_frame(diary_frame)])
        diary_btn.pack();
        margin_label2 = tk.Label(main_frame, pady=15)
        margin_label2.pack()
        # main_frame 구성 - 메뉴 버튼 구성
        main_btn_frame = tk.Frame(main_frame)
        main_btn_frame.pack()
        main_list_btn = tk.Button(main_btn_frame, text="메뉴판", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.open_frame(list_frame)])
        main_list_btn.grid(row=0, column=1)
        main_home_btn = tk.Button(main_btn_frame, text="나물", fg="#88AE89", width=13, height=4, bg="#004003")
        main_home_btn.grid(row=0, column=2)
        main_diary_btn = tk.Button(main_btn_frame, text="식탁", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.open_frame(diary_frame)])
        main_diary_btn.grid(row=0, column=3)

        # list_frame 구성
        list_frame = tk.Frame(root)
        list_frame.grid(row=0,column=0, sticky="nsew")
        # list_frame 구성 - 페이지 이름
        list_page_name = tk.Label(list_frame, padx=20, pady=15, text="명의 메뉴판", font="함초롬돋움")
        list_page_name.pack(anchor="nw")
        # list_frame 구성 - Listbo 구성
        list_listbox = tk.Listbox(list_frame, width=40, selectmode='extended', height=0)
        saying_tb  = db.get_saying_tb();
        for i in range(len(saying_tb)):
            list_listbox.insert(i, f'{saying_tb[i][0]}. {saying_tb[i][1]} - {saying_tb[i][2]}')
        list_listbox.pack()
        # list_frame 구성 - 메뉴 버튼 구성
        list_btn_frame = tk.Frame(list_frame)
        list_btn_frame.pack()
        list_list_btn = tk.Button(list_btn_frame, text="메뉴판", fg="#88AE89", width=13, height=4, bg="#004003")
        list_list_btn.grid(row=0, column=1)
        list_home_btn = tk.Button(list_btn_frame, text="나물", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.open_frame(main_frame)])
        list_home_btn.grid(row=0, column=2)
        list_diary_btn = tk.Button(list_btn_frame, text="식탁", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.open_frame(diary_frame)])
        list_diary_btn.grid(row=0, column=3)

        # diary_frame 구성
        diary_frame = tk.Frame(root)
        diary_frame.grid(row=0, column=0, sticky="nsew")
        diary_page_name = tk.Label(diary_frame,padx=20,pady=15,text="명의 식탁", font="함초롬돋움")
        diary_page_name.pack(anchor="nw")
        diary_btn_frame = tk.Frame(diary_frame)
        diary_btn_frame.pack()
        diary_list_btn = tk.Button(diary_btn_frame, text="메뉴판", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.open_frame(list_frame)])
        diary_list_btn.grid(row=0, column=1)
        diary_home_btn = tk.Button(diary_btn_frame, text="나물", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.open_frame(main_frame)])
        diary_home_btn.grid(row=0, column=2)
        diary_diary_btn = tk.Button(diary_btn_frame, text="식탁", fg="#88AE89", width=13, height=4, bg="#004003")
        diary_diary_btn.grid(row=0, column=3)

        self.open_frame(main_frame)
        root.mainloop()

    def open_frame(self, frame):
        #프레임 전환
        frame.tkraise()

#실행
Main()
