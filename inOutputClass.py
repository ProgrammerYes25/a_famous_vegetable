from DBHelper import DBHelper


class inOutputClass:
    def __init__(self):
        self.db = DBHelper()
    def get_db(self):
        return self.db.get_saying_tb();
    def get_diary_db(self):
        return self.db.get_diary_tb();
    def get_diary_view(self, date_diary):
        return self.db.get_diary_view(date_diary)
    def get_saying_view(self, index_num):
        return self.db.get_saying_view(index_num)
    def add_saying(self,name_saying, saying,  category):
        self.db.insert_saying_tb(name_saying, saying,  category)
    def add_diary(self, get_date, index, get_diary):
        self.db.insert_diary_tb(get_date,  index,  get_diary)