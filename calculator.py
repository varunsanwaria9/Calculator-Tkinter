from tkinter import Tk,Label,Button,Entry

root = Tk()
root.geometry("300x270")

class calculator():
    def __init__(self):
        self.solve = ""
        self.temp = ""
    
    def body(self):
        print(f"Solve:{self.solve}")
        Button(root,text="Clear",bg="Grey",width=5,command=vs.clear_btn).grid(row=1,column=2)
        Label(root,text=self.temp,height=5).grid(row=1,column=8)
        Label(root,text="",width=2).grid(row=2,column=1)
        Button(root,text="1",bg="Grey",width=5,command=vs.dis_1).grid(row=2,column=2)
        Label(root,text="",width=3).grid(row=2,column=3)
        Button(root,text="2",bg="Grey",width=5,command=vs.dis_2).grid(row=2,column=4)
        Label(root,text="",width=3).grid(row=2,column=5)
        Button(root,text="3",bg="Grey",width=5,command=vs.dis_3).grid(row=2,column=6)
        Label(root,text="",width=3).grid(row=2,column=7)
        Button(root,text="/",bg="Grey",width=5,command=vs.div_btn).grid(row=2,column=8)
        Label(root,text="",height=1).grid(row=3,column=1)
        Label(root,text="",width=2).grid(row=4,column=1)
        Button(root,text="4",bg="Grey",width=5,command=vs.dis_4).grid(row=4,column=2)
        Label(root,text="",width=3).grid(row=4,column=3)
        Button(root,text="5",bg="Grey",width=5,command=vs.dis_5).grid(row=4,column=4)
        Label(root,text="",width=3).grid(row=4,column=5)
        Button(root,text="6",bg="Grey",width=5,command=vs.dis_6).grid(row=4,column=6)
        Label(root,text="",width=3).grid(row=4,column=7)
        Button(root,text="*",bg="Grey",width=5,command=vs.mul_btn).grid(row=4,column=8)
        Label(root,text="",height=1).grid(row=5,column=1)
        Label(root,text="",width=2).grid(row=6,column=1)
        Button(root,text="7",bg="Grey",width=5,command=vs.dis_7).grid(row=6,column=2)
        Label(root,text="",width=3).grid(row=6,column=3)
        Button(root,text="8",bg="Grey",width=5,command=vs.dis_8).grid(row=6,column=4)
        Label(root,text="",width=3).grid(row=6,column=5)
        Button(root,text="9",bg="Grey",width=5,command=vs.dis_9).grid(row=6,column=6)
        Label(root,text="",width=3).grid(row=6,column=7)
        Button(root,text="-",bg="Grey",width=5,command=vs.sub_btn).grid(row=6,column=8)
        Label(root,text="",height=1).grid(row=7,column=1)
        Label(root,text="",width=2).grid(row=8,column=1)
        Button(root,text=".",bg="Grey",width=5,command=vs.dis_dot).grid(row=8,column=2)
        Label(root,text="",width=3).grid(row=8,column=3)
        Button(root,text="0",bg="Grey",width=5,command=vs.dis_0).grid(row=8,column=4)
        Label(root,text="",width=3).grid(row=8,column=5)
        Button(root,text="=",bg="Grey",width=5,command=vs.solution).grid(row=8,column=6)
        Label(root,text="",width=3).grid(row=8,column=7)
        Button(root,text="+",bg="Grey",width=5,command=vs.add_btn).grid(row=8,column=8)
        root.mainloop()

    def dis_1(self):
        self.temp += "1"
        self.solve += self.temp
        vs.body()

    def dis_2(self):
        self.temp += "2"
        self.solve += self.temp
        vs.body()

    def dis_3(self):
        self.temp += "3"
        self.solve += self.temp
        vs.body()

    def dis_4(self):
        self.temp += "4"
        self.solve += self.temp
        vs.body()

    def dis_5(self):
        self.temp += "5"
        self.solve += self.temp
        vs.body()

    def dis_6(self):
        self.temp += "6"
        self.solve += self.temp
        vs.body()

    def dis_7(self):
        self.temp += "7"
        self.solve += self.temp
        vs.body()

    def dis_8(self):
        self.temp += "8"
        self.solve += self.temp
        vs.body()

    def dis_9(self):
        self.temp += "9"
        self.solve += self.temp
        vs.body()

    def dis_0(self):
        self.temp += "0"
        self.solve += self.temp
        vs.body()

    def dis_dot(self):
        self.temp += "."
        self.solve += self.temp
        vs.body()

    def clear_btn(self):
        self.temp = ""
        self.solve = ""
        vs.body()

    def add_btn(self):
        self.temp = ""
        self.solve += "+"
        vs.body()

    def sub_btn(self):
        self.temp = ""
        self.solve += "-"
        vs.body()

    def mul_btn(self):
        self.temp = ""
        self.solve += "*"
        vs.body()

    def div_btn(self):
        self.temp = ""
        self.solve += "/"
        vs.body()

    def solution(self):
        self.temp = eval(self.solve)
        self.solve = str(self.temp)
        vs.body()

vs = calculator()
vs.body() 