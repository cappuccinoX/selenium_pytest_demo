import csv
import os
import json

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


if __name__ == "__main__":
    r = ReadData("login.csv")
    print(r.read_csv())