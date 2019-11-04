#必要モジュールのインポート
import math
import tkinter as tk
import csv

#ボタン押下時に実行　csvを生成
def run():

    #変数宣言
    name = nameB.get()
    ofs = float(ofsB.get())
    ofst = float(ofstB.get())
    delta = int(deltaB.get())
    size = float(sizeB.get())
    sizet = float(sizetB.get())
    length = int(lengthB.get())

    #csv書き込み　vmdeditorのフォーマットに合わせる
    with open('result.csv','w',newline="") as f:
        writer = csv.writer(f,quoting = csv.QUOTE_NONE)
        writer.writerow(['Vocaloid Motion Data 0002'])
        writer.writerow(['Model'])
        writer.writerow(['Motion','bone','x','y','z','rx','ry','rz','x_p1x','x_p1y','x_p2x','x_p2y','y_p1x','y_p1y','y_p2x','y_p2y','z_p1x','z_p1y','z_p2x','z_p2y','r_p1x','r_p1y','r_p2x','r_p2y'])
        writer.writerow(['Expression','name','fact'])
    #表情の中身を書き込む
        loopcount = 0
        for i in range (0,length + 1,delta):
            writer.writerow([i,name,ofs + ((ofst - ofs) / math.floor(length / delta)) * loopcount + (1 - loopcount % 2 * 2) * (size + ((sizet - size) / math.floor(length / delta)) * loopcount)])
            loopcount += 1
        #のこり
        else:
            writer.writerow(['Camera','d','a','x','y','z','rx','ry','rz','x_p1x','x_p1y','x_p2x','x_p2y','y_p1x','y_p1y','y_p2x','y_p2y','z_p1x','z_p1y','z_p2x','z_p2y','r_p1x','r_p1y','r_p2x','r_p2y','d_p1x','d_p1y','d_p2x','d_p2y','a_p1x','a_p1y','a_p2x','a_p2y'])
            writer.writerow(['Light','r','g','b','x','y','z'])


#ウィンドウ定義
win = tk.Tk()
win.geometry("500x500")
win.title('モーフゆらゆらツール')
#ラベル
nameL = tk.Label(win,text = 'モーフ名')
nameL.pack()

#テキストボックス
nameB = tk.Entry(win)
nameB.pack()
nameB.insert(tk.END,'笑い')

#ラベル offset
ofsL = tk.Label(win,text = '基準値')
ofsL.pack()

#テキストボックス
ofsB = tk.Entry(win)
ofsB.pack()
ofsB.insert(tk.END,0.5)

#ラベル offsettarget
ofstL = tk.Label(win,text = '基準値の目標値(揺れながらだんだん増えていく時とか')
ofstL.pack()

#テキストボックス
ofstB = tk.Entry(win)
ofstB.pack()
ofstB.insert(tk.END,0.8)

#ラベル
deltaL = tk.Label(win,text = '周期(キーフレーム間隔)')
deltaL.pack()

#テキストボックス
deltaB = tk.Entry(win)
deltaB.pack()
deltaB.insert(tk.END,3)

#ラベル
sizeL = tk.Label(win,text = '振幅')
sizeL.pack()

#テキストボックス
sizeB = tk.Entry(win)
sizeB.pack()
sizeB.insert(tk.END,0.1)

#ラベル　sizetarget
sizetL = tk.Label(win,text = '振幅の目標値(だんだん収束させたい時に)')
sizetL.pack()

#テキストボックス
sizetB = tk.Entry(win)
sizetB.pack()
sizetB.insert(tk.END,0.0)

#ラベル
lengthL = tk.Label(win,text = '長さ(フレーム数)')
lengthL.pack()

#テキストボックス
lengthB = tk.Entry(win)
lengthB.pack()
lengthB.insert(tk.END,30)

#ボタン
runbtn = tk.Button(win,text = 'run',command = run)
runbtn.pack()

#最下部に置くこと　ここまででループする
win.mainloop()
