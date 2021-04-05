import csv
import os
import json
import xlrd

class ReadData():

    directory = os.path.abspath("data")

    def __init__(self, file_name):
        self.file_path = self.directory + "/" + file_name

    def read_csv(self):
        data = list()
        with open(self.file_path, "r") as file:
            reader = csv.reader(file)
            # 忽略第一行title
            next(reader)
            for item in reader:
                data.append(item)
        return data

    def read_json(self):
        with open(self.file_path, "r") as file:
            json_data = json.loads(file.read())
        return json_data

    def read_excel(self):
        data = list()
        book = xlrd.open_workbook(self.file_path)
        sheet = book.sheet_by_index(0)
        # 第一行是标题, 从第二行读取
        for row in range(1, sheet.nrows):
            data.append(sheet.row_values(row))
        return data


if __name__ == "__main__":
    r = ReadData("category.xlsx")
    print(r.read_excel())