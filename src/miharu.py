# namiki
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


from re import X
import pyautogui 
import ctypes
import time
import pyautogui as pag


from itertools import count
import math
from webbrowser import get
import pyautogui as pag
from time import sleep
import time
import os
from re import X
import ctypes
import time
from PIL import Image 
import shutil
import img2pdf
from natsort import natsorted



# global 変数

answer_ja = ''





    
    
        #s = input("sと入力してください:")
x1 ,x2, y1, y2 = 0,0,0,0
interval = 2.3
pdf_img = []
pages = 0

def tab1_main(tab1):
    bg_col =  '#ffffe0'
    tab1['bg'] = bg_col
    


    def mouse():
        global x1,x2,x3,y1,y2,y3
        print("左上端をクリックしてください")
        messagebox.showinfo('確認', 'スクショ範囲の左上をクリック')
        xy1.delete(0, tk.END)
        xy2.delete(0, tk.END)
        try:
            while True:
                if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:
                    x, y = pag.position()
                    print(str(x) + ':' + str(y))
                    x1 = x
                    y1 = y
                    time.sleep(1)
                    break
                ### ここにクリック時の動作を記入する ###

        except KeyboardInterrupt:
            print('左上端終了')
        
        
        print("右下端をクリックしてください")
        messagebox.showinfo('確認', 'スクショ範囲の右下をクリック')
        try:
            while True:
                if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:
                    x, y = pag.position()
                    print(str(x) + ':' + str(y))
                    x2 = x
                    y2 = y
                    break
                ### ここにクリック時の動作を記入する ###

        except KeyboardInterrupt:
            print('右下端終了')

        print("クリックしたい場所を指定してください")
        messagebox.showinfo('確認', 'クリックしたい場所を指定してください')
        try:
            while True:
                if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:
                    x, y = pag.position()
                    print(str(x) + ':' + str(y))
                    x3 = x
                    y3 = y
                    break
                ### ここにクリック時の動作を記入する ###
        except KeyboardInterrupt:
            print('クリック場所指定終了')

    # テキストボックス -> マウスの座標表示      xy.insert(tkinter.END,"1234")で挿入　　　　.get()で取得　.delete(0, tkinter.END)でクリア
        xy1.insert(tk.END,'  ('+str(x1)+','+str(y1)+')')
        xy2.insert(tk.END,'  ('+str(x2)+','+str(y2)+')')
        
            
            

            
            
    def get_sukusyo():
        start = time.perf_counter()
        global pdf_img,interval,a1
        a1 = 0
        pdf_img.clear()
        global pages
    
        
        i = 1
        global path
        path = "sukusyo"
        
        try:
            shutil.rmtree(path)
        except:
            pass
        os.mkdir(path)
        
        abs_path = os. getcwd()
        print(abs_path)
        try:
            start_time = time.perf_counter()
            for i in range(int(pages.get())):

                img = pag.screenshot(region= (x1,y1,x2-x1,y2-y1))
                img.save(path + "/img"+str(i)+".png")
                print( "/img"+str(i)+".png"+"を保存しました")
                if i == 1:
                    pdf_img.append(path+"/img"+str(i)+".png")

                    i = i + 1
                    continue
                pdf_img.append(abs_path+'/'+path+"/img"+str(i)+".png")
 
                i = i + 1

                pyautogui.click(x3, y3)
                sleep(0.7)
        except KeyboardInterrupt:
            print('\n')
        messagebox.showinfo('確認', 'スライドの撮影が終了しました')
        print(*pdf_img)
        

        return pdf_img

        
        
    def png_to_pdf():
        global pdf_img
        outputpath= "file.pdf"
        try:
            os.remove(outputpath)
        except:
            pass
        layout = img2pdf.get_layout_fun((img2pdf.mm_to_pt(257), img2pdf.mm_to_pt(182)))
        pdf_img.pop(0)
        with open(outputpath, "wb") as f:
            f.write(img2pdf.convert([i for i in natsorted(pdf_img) if ".png" in i], layout_fun=layout))
                # フォルダの削除
        messagebox.showinfo('確認', 'PDF化できました')
        shutil.rmtree(path)

            
    # ラベル1の生成
    label1 = tk.Label(tab1, text='1.範囲および時間を指定してください', bg=bg_col,font=("", "13", "bold"))
    label1.pack(padx=5, pady=7)
    
    # ボタンの作成と配置
    label2 = tk.Label(tab1, text='左上：', bg=bg_col)
    label2.place(x=60, y=50, width = 40, height = 32)
    # テキストボックス -> マウスの座標表示      xy.insert(tkinter.END,"1234")で挿入　　　　.get()で取得　.delete(0, tkinter.END)でクリア
    xy1 = tk.Entry(tab1,relief="solid",width=20)
    xy1.place(x=100, y=50, width = 100, height = 32)
    
    label3 = tk.Label(tab1, text='右下：', bg=bg_col)
    label3.place(x=210, y=50, width = 40, height = 32)
    xy2 = tk.Entry(tab1,relief="solid",width=20)
    xy2.place(x=250, y=50, width = 100, height = 32)
    
    mouse_button = tk.Button(tab1, text="範囲決定",relief="solid", bg="white", fg = "#2f4f4f",bd=1, command = mouse )
    mouse_button.place(x = 360, y = 50, width = 70, height = 32)
    
    
    height = 26
    label4 = tk.Label(tab1, text='時間：', bg=bg_col)
    label4.place(x=60, y=100, width = 40, height = height)
    
    global pages


    pages = tk.Entry(tab1,relief="solid",width=20, justify="right")
    pages.place(x=170, y=100, width = 40, height = height)
    
    label_sec = tk.Label(tab1, text='枚', bg=bg_col)
    label_sec.place(x=210, y=100, width = 20, height =  height)
    



    # スクショのスタート
    label6 = tk.Label(tab1, text='2.スタートボタンを押してください', bg=bg_col,font=("", "13", "bold"))
    label6.place(x=43, y=140, width =380, height = 32)
    
    
    start_button = tk.Button(tab1, text="スタート",relief="solid", bg="white", fg = "#2f4f4f",bd=1, command = get_sukusyo)
    start_button.place(x = 160, y = 190, width = 120, height = 60)
    
    # スクショのスタート
    label7 = tk.Label(tab1, text='3.PDFに出力します', bg=bg_col,font=("", "13", "bold"))
    label7.place(x=50, y=260, width =200, height = 32)
    
    
    start_button = tk.Button(tab1, text="出力",relief="solid", bg="white", fg = "#2f4f4f",bd=1, command = png_to_pdf)
    start_button.place(x = 160, y = 320, width = 120, height = 60)
    
    
    
    
    
    return 0