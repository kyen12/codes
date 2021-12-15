import sys
import tkinter as tk
from tkinter.constants import END, S
import tkinter.messagebox as tkm
import random, json

root = tk.Tk()

# ウインドウのタイトルを定義する
root.title(u'Buttonを使ってみる')

# ここでウインドウサイズを定義する
root.geometry('600x400')

# ボタンが押されたら呼び出される関数
def addNumber(text):
    ListBox_first.insert(tk.END, text)
    ListBox_first(['disabled'])

def addList(text):
    ListBox_you.insert(tk.END, text)
    Entry_you.delete(0, tk.END)

def deleteSelectedList():
    selectedIndex = tk.ACTIVE
    ListBox_you.delete(selectedIndex)

def reset():
    ListBox_note.delete(0, tk.END)
    ListBox_you.delete(0, tk.END)
    Entry_keta.delete(0,tk.END)
    Entry_void.delete(0,tk.END)
    Entry_you.delete(0,tk.END)
    ListBox_note.insert(tk.END,'Hit&Blow　  始めます')
    ListBox_note.insert(tk.END,'当てる値の桁数を決めてください。(左の欄から)')

def main(text):
    ListBox_note.delete(0, tk.END)
    ListBox_note.insert(tk.END, text)
    ListBox_you.delete(0, tk.END)
    Entry_keta.delete(0,tk.END)
    Entry_void.delete(0,tk.END)
    Entry_you.delete(0,tk.END)
    ListBox_note.insert(tk.END,'Hit&Blow　  始めます')
    ListBox_note.insert(tk.END,'当てる値の桁数を決めてください。(左の欄から)')

    

def addmain(text):
    digit = text
    with open("record.json") as f:
            jsn = json.load(f)
    counter = jsn["{}".format(digit)]["count"]
    count = counter
    old_record = jsn["{}".format(digit)]["record"]
    Entry_void.delete(0,tk.END)
    b_list=random.sample(range(1,9),int(digit)) 
    print(b_list)
    Entry_void.insert(tk.END,b_list)
    ListBox_note.delete(0,tk.END)
    ListBox_note.insert(tk.END,"-------------------------------")
    ListBox_note.insert(tk.END,"桁数 : {}".format(digit))
    ListBox_note.insert(tk.END,"制限回数 : {}".format(count))
    ListBox_note.insert(tk.END,"現在の最速記録 : {}　　です".format(old_record))
    ListBox_note.insert(tk.END,"ゲームスタート！！")
    ListBox_note.insert(tk.END,"( 途中で中止したい場合は'break'と入力してください )")
    ListBox_note.insert(tk.END,"-------------------------------")
    ListBox_note.insert(tk.END,'入力して下さい(残り'+str(counter)+'回)...')

def main2():
    digit = Entry_keta.get()
    with open("record.json") as f:
        jsn = json.load(f)
    counter = jsn["{}".format(digit)]["count"]
    count = counter
    old_record = jsn["{}".format(digit)]["record"]
    h_count=0
    b_list=Entry_void.get()
    b_list =b_list.replace(' ','')
    b_list=list(map(int,b_list))    
    ass = Entry_you.get()
    Entry_you.delete(0,tk.END)
    if ass=='break':
                main('終了します')
    elif ass=='hint':    
        if h_count==0:
            h=random.randint(1,4)
            ListBox_note.insert(tk.END,'ヒント:'+str(h)+'桁目の数字は'+str(b_list[int(h)-1])+'です')
            h_count+=1
        else:
            ListBox_note.insert(tk.END,'ヒントは一回すでに使用しているので利用できません')

    elif not ass.isdigit():
        ListBox_note.insert(tk.END,'数字以外が入力されています')
    elif len(ass)!=int(digit):
        ListBox_note.insert(tk.END,'入力されたのが'+str(digit)+'桁ではありません')


            
    else:
        ass_list=list(map(int,ass))
        ListBox_you.insert(tk.END,ass_list)

        H=0
        B=0
        for i,j in zip(ass_list,b_list):
            if i==j:
                H+=1
                     #B+=1
            elif i in b_list:
                B+=1
            else:
                pass
        counter-=1
        if H==int(digit):
            ListBox_note.insert(tk.END,'クリアです')
            new_record=count-counter                        
            if new_record < (int(old_record)):
                jsn["{}".format(digit)]["record"] = new_record
                with open("record.json", "w") as f:
                    json.dump(jsn, f, indent=4)
                ListBox_note.insert(tk.END,'***祝***')
                ListBox_note.insert(tk.END,'NEW RECORD:'+str(new_record))                
                ListBox_note.insert(tk.END,'新記録として保存されました！！')

            else:
                ListBox_note.insert(tk.END,'記録更新ならず...次こそは更新しよう！')

        if counter==0:
                ListBox_note.insert(tk.END,'ゲームオーバー')
                ListBox_note.insert(tk.END,'正解 : {}\n\n'.format(b_list))

        ListBox_note.insert(tk.END,'Hit:'+str(H)+'   Blow:'+str(B))
        ListBox_note.insert(tk.END,'------------------------------------------')



    

# 自分がわのせつてい
Static_setumei = tk.Label(
    text=u'*/*/*/*/*/数字当てゲーム/*/*/*/*/*\n'\
      '--<ルール説明>----------------------------------------------------\n'\
      '|  0 ~ 9からなる任意の桁数の値を当てよう！                         |\n'\
      '|  入力した数のうち、値も順番も完全に一致してるものの個数を「Hit」、|\n'\
      '|  値はあっているが順番が間違えているものの個数を「Blow」とする。   |\n'\
      '|  桁数ボタンで最初に桁を入力　リセットボタンでリセットできます。   |\n'\
      '|  左の入力ボタンから、上に入れた数字を入力できます。               |\n'
      '|  制限回数以内に値を当てることができればゲームクリア！！           |\n'\
      '|  最速記録の場合はレコードに記録されます。                        |\n'\
      '-----------------------------------------------------------------')
Static_setumei.place(x=10, y=250)

Static1 = tk.Label(text=u'▼　あなた　▼')
Static1.place(x=35,y=10)

Entry_void = tk.Entry(width=10)
Entry_void.place(x=-20, y=-20)

Entry_you = tk.Entry(master=root, width = 20)
Entry_you.insert(tk.END, u'')
Entry_you.place(x=15, y=30)

Button_you = tk.Button(text=u'入力ボタン', width=16, command=lambda:main2())       
Button_you.place(x=15, y= 50)

ListBox_you = tk.Listbox(width =20)
ListBox_you.place(x=15, y=70)

#　その他
Static_reset = tk.Label(text=u'▼　リセット用　▼')
Static_reset.place(x=150, y=10)

Button_reset = tk.Button(text=u'リセット',width=15, command=lambda:reset())
Button_reset.place(x=150, y=35)

Static_reset = tk.Label(text=u'▼　桁数入力用　▼')
Static_reset.place(x=150, y=60)

Entry_keta = tk.Entry(width=15)
Entry_keta.place(x=150, y=85)

Button_keta = tk.Button(text=u'桁数',width =15, command=lambda:addmain(Entry_keta.get()))
Button_keta.place(x=150, y=110)

ListBox_note = tk.Listbox(width = 50, height=15)
ListBox_note.place(x=270,y=10)

ListBox_note.insert(tk.END,'Hit&Blow　  始めます')
ListBox_note.insert(tk.END,'当てる値の桁数を決めてください。(左の欄から)')


root.mainloop()