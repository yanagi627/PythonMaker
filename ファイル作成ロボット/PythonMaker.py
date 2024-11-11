from enum import StrEnum
import tkinter as tk
import os
import shutil
from rich import print
Template_path = os.path.dirname(__file__)


class File_path(StrEnum):
    """ファイルパス一覧"""

    Templete_Python = f"{Template_path}\\ファイル.テンプレート.py"
    Templete_ReadMe = f"{Template_path}\\Readme.md"
    Main = "\\__main__.py"


class PythonMaker(tk.Frame):
    """記入されたファイル名から、1.フォルダ、2.ファイル、3.readme、を作成する。"""

    def __init__(self, master):
        super().__init__(master)

 # 画面レイアウト---------------------------------------------------------------------------------------
        label = tk.Label(text="ファイル名を記入してください。")
        self.label2 = tk.Label(text="")
        """実行結果のラベル"""
        self.entry = tk.Entry()
        button = tk.Button(text="実行", command=lambda: self.get_text())

        label.pack()
        self.entry.pack()
        button.pack()
# -----------------------------------------------------------------------------------------------------        

    def get_text(self):
        """
        入力に記入された名前を取得し、処理各種を羅列。
        メゾット名があってない気がするので要確認
        """

        name = self.entry.get()
        dirpath = rf"C:\Users\w-yanagi\Desktop\Python\code\{name}"
        
        try:
            self.make_folder(name, dirpath)
            self.make_file(name,dirpath)
            self.make_readme(name,dirpath)
            self.print_label("ファイルの作成完了！")

        except Exception as e:
            print(e)
            self.print_label(e.args[-1])

    def make_folder(self, name, path):
        """新規フォルダの作成"""
        os.mkdir(path)

    def make_file(self, name, path):
        """新規Pythonファイルの作成"""
        shutil.copy(File_path.Templete_Python, path + File_path.Main)

        with open(path + File_path.Main, encoding="utf-8", mode="r") as f:
            Python_text = f.read()

        with open(path + File_path.Main, encoding="utf-8", mode="w") as f:
            f.write(Python_text.replace("File_Name", name))
            

    def make_readme(self, name, path):
        """新規ReadMeファイルの作成"""
        shutil.copy(File_path.Templete_ReadMe, path + f"\\Readme.md")

        with open(path + f"\\Readme.md", encoding="utf-8") as f:
            Readme_text = f.readlines()
            Readme_text.insert(0, f"# {name}\n")


        with open(path + f"\\Readme.md", encoding="utf-8", mode="w") as f:
            f.writelines(Readme_text)

        self.print_label("ファイルの作成完了！")

    def print_label(self, text):
        """ラベル２に失敗成功を出力"""
        self.label2["text"] = text
        self.label2.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("ファイル作成ロボット")
    root.geometry("300x100")
    Python_maker = PythonMaker(root)
    Python_maker.pack()

    root.mainloop()
