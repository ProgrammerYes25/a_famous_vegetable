import tkinter as tk
from inOutputClass import inOutputClass


class Main:
    def __init__(self):
        # db 생성
        self.get_index = (0,[])
        in_out = inOutputClass()
        self.get_diary_in_db = None
        # 윈도우 생성
        self.root = tk.Tk()
        self.root.title("명의 나물")
        self.root.geometry("300x500")
        self.root.resizable(False, False)


        # main_frame 구성
        main_frame = tk.Frame(self.root)
        main_frame.grid(row=0,column=0, sticky="nsew")
        # main_frame 구성 - 페이지 이름
        main_page_name = tk.Label(main_frame, padx=20, pady=15, text="명의 나물", font="함초롬돋움")
        main_page_name.pack(anchor="nw")
        # main_frame 구성 - 페이지 설명
        main_page_text = tk.Label(main_frame,  padx=30, pady=40,text="명의 나물은\n일상생활 속 마음의 양식을\n 충전할 수 있는\n 마음의 식당입니다. ", font="HY바다L")
        main_page_text.pack()
        # main_frame 구성 - 메뉴 이동 버튼
        list_btn = tk.Button(main_frame, padx=5, pady=10, text="명언과 명대사가 있는 메뉴판 보러가기", fg="#004003", width=35, height=2, bg="#A4E1B2", command=lambda:[self.open_frame(list_frame)])
        list_btn.pack()
        margin_label1 = tk.Label(main_frame,pady=10)
        margin_label1.pack()
        diary_btn = tk.Button(main_frame, padx=5, pady=10, text="나의 하루하루를 나누고 기록하는 식탁가기", fg="#004003", width=35, height=2, bg="#A4E1B2", command=lambda: [self.open_frame(diary_frame)])
        diary_btn.pack()
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
        list_frame = tk.Frame(self.root)
        list_frame.grid(row=0,column=0, sticky="nsew")
        # list_frame 구성 - 페이지 이름
        list_page_name = tk.Label(list_frame, padx=20, pady=15, text="명의 메뉴판", font="함초롬돋움")
        list_page_name.pack(anchor="nw")
        # list_frame 구성 - Listbox 구성
        list_listbox = tk.Listbox(list_frame, width=40, exportselection=True, selectmode='extended', height=20)
        saying_tb = in_out.get_db()
        for i in range(len(saying_tb)):
            list_listbox.insert(i, f'{saying_tb[i][0]}. {saying_tb[i][1]} - {saying_tb[i][2]}')
        # list_frame 구성 - list_frame 메뉴 구성
        list_menu_frame = tk.Frame(list_frame)
        list_menu_diary_btn = tk.Button(list_menu_frame, width=13, height=2, text="명언 추가하기", fg="#004003", bg="#A4E1B2", command=lambda:[self.open_frame(add_frame)])
        list_menu_diary_btn.grid(row=0, column=1)
        list_menu_diary_btn = tk.Button(list_menu_frame, width=13, height=2, text="명대사&가사 추가하기", fg="#004003", bg="#A4E1B2", command=lambda:[self.open_frame(add_frame2)])
        list_menu_diary_btn.grid(row=0, column=2)
        list_menu_diary_btn = tk.Button(list_menu_frame, width=13, height=2, text="고른 명언으로\n일기 쓰기", fg="#004003", bg="#A4E1B2", command=lambda:[self.open_frame_diary(diary_add_frame, list_listbox)])
        list_menu_diary_btn.grid(row=0, column=3)
        list_menu_frame.pack()
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
        diary_frame = tk.Frame(self.root)
        diary_frame.grid(row=0, column=0, sticky="nsew")
        diary_page_name = tk.Label(diary_frame,padx=20,pady=15,text="명의 식탁", font="함초롬돋움")
        diary_page_name.pack(anchor="nw")
        # list_frame 구성 - Listbox 구성
        diary_list_listbox = tk.Listbox(diary_frame, width=40, exportselection=True, selectmode='extended', height=20)
        diary_tb = in_out.get_diary_db()
        if diary_tb==None:
             diary_list_listbox.insert(0,"일기가 없습니다.")
        for i in range(len(diary_tb)):
            diary_list_listbox.insert(i, f'{diary_tb[i][1]}')
        diary_menu_frame = tk.Frame(diary_frame)
        diary_menu_btn = tk.Button(diary_menu_frame, width=13, height=2, text="일기보기", fg="#004003", bg="#A4E1B2",
                                        command=lambda: [self.open_frame_diary_view(in_out, diary_list_listbox, list_frame, main_frame)])
        diary_menu_btn.grid(row=0, column=1)
        diary_menu_frame.pack()
        diary_list_listbox.pack()

        diary_btn_frame = tk.Frame(diary_frame)
        diary_btn_frame.pack()
        diary_list_btn = tk.Button(diary_btn_frame, text="메뉴판", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.open_frame(list_frame)])
        diary_list_btn.grid(row=0, column=1)
        diary_home_btn = tk.Button(diary_btn_frame, text="나물", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.open_frame(main_frame)])
        diary_home_btn.grid(row=0, column=2)
        diary_diary_btn = tk.Button(diary_btn_frame, text="식탁", fg="#88AE89", width=13, height=4, bg="#004003")
        diary_diary_btn.grid(row=0, column=3)

        # add_frame 구성
        add_frame = tk.Frame(self.root)
        add_frame.grid(row=0, column=0, sticky="nsew")
        # list_frame 구성 - 페이지 이름
        add_page_name = tk.Label(add_frame, padx=20, pady=15, text="좋아하는 명언 추가하기", font="함초롬돋움")
        add_page_name.pack(anchor="nw")
        entry1_frame = tk.Frame(add_frame, padx=5)
        entry1_frame.pack()
        name_saying = tk.Label(entry1_frame, text="누가한 말인가요?")
        name_saying.grid(row=0, column=1)
        get_saying_name = tk.Entry(entry1_frame, width=40)
        get_saying_name.grid(row=1, column=1)
        entry2_frame = tk.Frame(add_frame, padx=5)
        entry2_frame.pack()
        saying = tk.Label(entry2_frame, text="내용을 알려주세요" )
        saying.grid(row=2, column=1)
        get_saying = tk.Entry(entry2_frame, width=40)
        get_saying.grid(row=3, column=1)
        input_btn = tk.Button(entry2_frame, text="등록", width=40, command=lambda:[self.input_saying(in_out,list_listbox, list_frame, get_saying.get(), get_saying_name.get())])
        input_btn.grid(row=4, column=1)

        # add_frame 구성
        add_frame = tk.Frame(self.root)
        add_frame.grid(row=0, column=0, sticky="nsew")
        # list_frame 구성 - 페이지 이름
        add_page_name = tk.Label(add_frame, padx=20, pady=15, text="좋아하는 명언 추가하기", font="함초롬돋움")
        add_page_name.pack(anchor="nw")
        entry1_frame = tk.Frame(add_frame, padx=5)
        entry1_frame.pack()
        name_saying = tk.Label(entry1_frame, text="누가한 말인가요?")
        name_saying.grid(row=0, column=1)
        get_saying_name = tk.Entry(entry1_frame, width=40)
        get_saying_name.grid(row=1, column=1)
        entry2_frame = tk.Frame(add_frame, padx=5)
        entry2_frame.pack()
        saying = tk.Label(entry2_frame, text="내용을 알려주세요")
        saying.grid(row=2, column=1)
        get_saying = tk.Entry(entry2_frame, width=40)
        get_saying.grid(row=3, column=1)
        input_btn = tk.Button(entry2_frame, text="등록", width=40,command=lambda: self.input_saying1(in_out, list_listbox, list_frame, get_saying, get_saying_name))
        input_btn.grid(row=4, column=1)

        # add_frame2 구성
        add_frame2 = tk.Frame(self.root)
        add_frame2.grid(row=0, column=0, sticky="nsew")
        # add_frame2 구성 - 페이지 이름
        add_page_name2 = tk.Label(add_frame2, padx=20, pady=15, text="좋아하는 명언 추가하기", font="함초롬돋움")
        add_page_name2.pack(anchor="nw")
        entry3_frame = tk.Frame(add_frame2, padx=5)
        entry3_frame.pack()
        name_saying2 = tk.Label(entry3_frame, text="어디서 들은 말인가요?")
        name_saying2.grid(row=0, column=1)
        get_saying_name2 = tk.Entry(entry3_frame, width=40)
        get_saying_name2.grid(row=1, column=1)
        entry4_frame = tk.Frame(add_frame2, padx=5)
        entry4_frame.pack()
        saying2 = tk.Label(entry4_frame, text="내용을 알려주세요")
        saying2.grid(row=2, column=1)
        get_saying2 = tk.Entry(entry4_frame, width=40)
        get_saying2.grid(row=3, column=1)
        input_btn2 = tk.Button(entry4_frame, text="등록", width=40, command=lambda: [self.input_saying2(in_out, list_listbox, list_frame, get_saying2, get_saying_name2)])
        input_btn2.grid(row=4, column=1)


        # diary_add_frame 구성
        diary_add_frame = tk.Frame(self.root)
        diary_add_frame.grid(row=0, column=0, sticky="nsew")
        # diary_add_frame 구성 - 페이지 이름
        diary_page_name = tk.Label(diary_add_frame, padx=20, pady=15, text="일기 추가하기", font="함초롬돋움")
        diary_page_name.pack(anchor="nw")
        date_frame = tk.Frame(diary_add_frame, padx=5)
        date_frame.pack()
        add_date = tk.Label(date_frame, text="날짜를 입력하세요")
        add_date.grid(row=0, column=1)
        get_date = tk.Entry(date_frame, width=40)
        get_date.grid(row=1, column=1)
        get_diary_frame = tk.Frame(diary_add_frame, padx=5)
        get_diary_frame.pack()
        add_diary = tk.Label(get_diary_frame, text="당신의 이야기를 들려주세요")
        add_diary.grid(row=2, column=1)
        get_diary = tk.Entry(get_diary_frame, width=40)
        get_diary.grid(row=3, column=1)
        input_diary_btn = tk.Button(get_diary_frame, text="등록", width=40,
                               command=lambda: self.input_diary(in_out, diary_list_listbox, list_frame, get_date, get_diary))
        input_diary_btn.grid(row=4, column=1)


        # diary_view 구성


        self.open_frame(main_frame)
        self.root.mainloop()

    def open_frame(self, frame):
        #프레임 전환
        frame.tkraise()
    def open_frame_diary(self, frame, list_listbox):
        #프레임 전환
        self.get_index = list_listbox.curselection()
        frame.tkraise()
    def open_frame_diary_view(self, in_out, list_listbox, list_frame, main_frame):
        #프레임 전환
        cho = list(list_listbox.curselection())
        c = cho[0]
        get_diary_in_db = in_out.get_diary_view(c+1)
        # diary_view 구성
        diary_view_frame = tk.Frame(self.root)
        diary_view_frame.grid(row=0, column=0, sticky="nsew")
        # diary_view 구성 - 페이지 이름
        in_text = str(get_diary_in_db[0][1]) + "-일기"
        diary_view_page_name = tk.Label(diary_view_frame, text=in_text, padx=20, pady=15, font="함초롬돋움")
        diary_view_page_name.pack(anchor="nw")
        c = get_diary_in_db[0][2]
        say_text = in_out.get_saying_view(c+1)
        in_text = "명언 : "+say_text[0][1]
        diary_view_frame2 = tk.Frame(diary_view_frame, padx=5)
        diary_view_frame2.pack()
        diary_view_saying = tk.Label(diary_view_frame2, text=in_text)
        diary_view_saying.grid(row=0, column=1)
        in_text = "일기 : "+get_diary_in_db[0][3]
        diary_text_view = tk.Label(diary_view_frame2, text=in_text)
        diary_text_view.grid(row=1, column=1)

        diary_btn_frame_view = tk.Frame(diary_view_frame)
        diary_btn_frame_view.pack()
        diary_list_btn_view = tk.Button(diary_btn_frame_view, text="메뉴판", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.open_frame(list_frame)])
        diary_list_btn_view.grid(row=0, column=1)
        diary_home_btn_view = tk.Button(diary_btn_frame_view, text="나물", fg="#004003", width=13, height=4, bg="#88AE89", command=lambda:[self.open_frame(main_frame)])
        diary_home_btn_view.grid(row=0, column=2)
        diary_diary_btn_view = tk.Button(diary_btn_frame_view, text="식탁", fg="#88AE89", width=13, height=4, bg="#004003")
        diary_diary_btn_view.grid(row=0, column=3)
        diary_view_frame.tkraise()

    def input_saying1(self, in_out, list_listbox, frame, get_saying, get_saying_name):
        in_out.add_saying(get_saying_name.get(),get_saying.get(), "명언")
        saying_tb = in_out.get_db()
        list_listbox.insert(len(saying_tb)-1, f'{saying_tb[len(saying_tb)-1][0]}. {saying_tb[len(saying_tb)-1][1]} - {saying_tb[len(saying_tb)-1][2]}')
        list_listbox.pack()
        self.open_frame(frame)

    def input_saying2(self, in_out, list_listbox, frame, get_saying, get_saying_name):
        in_out.add_saying(get_saying_name.get(),get_saying.get(),  "명대사&가사")
        saying_tb = in_out.get_db()
        list_listbox.insert(len(saying_tb)+1, f'{saying_tb[len(saying_tb)-1][0]}. {saying_tb[len(saying_tb)-1][1]} - {saying_tb[len(saying_tb)-1][2]}')
        list_listbox.pack()
        self.open_frame(frame)#실행

    def input_diary(self, in_out, list_listbox, frame, get_date, get_diary):
        index = list(self.get_index)
        index = index[0]
        in_out.add_diary(get_date.get(),index, get_diary.get())
        diary_tb = in_out.get_diary_db()
        list_listbox.insert(len(diary_tb), f'{len(diary_tb), diary_tb[len(diary_tb)-1][1]}')
        list_listbox.pack()
        self.open_frame(frame)#실행


Main()
