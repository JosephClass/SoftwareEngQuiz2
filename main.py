from curses import window
import CaseStudy
import os
from tkinter import *
window=Tk()
# add widgets here

window.title('Hello Python')
window.geometry("300x200+10+20")
window.mainloop()
# AccessData = CaseStudy.StudiKasus2(host="localhost" , port=3306 , user="root" , password=os.environ['PASS_MYSQL'])

# print(AccessData.create_db("Tryout2"))

# df = AccessData.import_csv("C:\\Users\\User-PC\\Desktop\\addresses.csv")

# AccessData.create_table("Tryout2","user",df)

# print(AccessData.load_data("Tryout2","user"))

