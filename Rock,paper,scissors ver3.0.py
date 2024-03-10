#じゃんけんプログラムGUIver
import tkinter as tk
from tkinter import messagebox
import random
import csv

# ユーザー・システムの勝利数、あいこ
userwin = 0
systemwin = 0
draw = 0
# システムが出す手
system = ['rock', 'scissors', 'paper']
# ユーザー及びシステムが出す手
userhand = ""
systemhand = ""
# 勝敗を表示する文字列変数
result = ""

# メインウィンドウを作成する
root = tk.Tk()
root.title("Rock,paper,scissors System")
# ウィンドウのサイズ
root.geometry("400x250+0+0")

# 最終結果をファイルにアップデートする関数
def update_stats(wins, losses, draws):
    try:
        with open('result.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # 既存の統計情報を読み込む
                prev_wins, prev_losses, prev_draws = int(row[0]), int(row[1]), int(row[2])
                wins += prev_wins
                losses += prev_losses
                draws += prev_draws
                break  # 最初の行のみ読み込む
    except FileNotFoundError:
        # ファイルが存在しない場合は新しく作成
        pass
    # 更新された統計情報を保存
    with open('result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        total_games = wins + losses + draws
        win_rate = wins / total_games * 100 if total_games > 0 else 0
        writer.writerow([wins, losses, draws, win_rate])

# 結果を表示する関数
def display_stats():
    try:
        with open('result.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # 勝率を四捨五入
                win_rate = round(float(row[3]), 2)
                sumgrade_label.config(text=f"\n=今までのじゃんけんの結果=\nユーザーの勝利数: {row[0]}回, \nユーザーの敗北数: {row[1]}回, \n引き分け数: {row[2]}回, \nユーザーの勝率: 約{win_rate}%",font=("Helvetica", 10))
                break
    except FileNotFoundError:
        sumgrade_label.config(text="統計情報がありません。")
    sumgrade_label.pack()

def button_clicked(button_id):
    global userhand, num, userwin, systemwin, draw

    if button_id == 1:
        userhand = 'rock'
    elif button_id == 2:
        userhand = 'scissors'
    elif button_id == 3:
        userhand = 'paper'

    # システムが出す手
    systemhand = random.choice(system)
    # ユーザーが出す手
    user_label.config(text=f"あなた: {userhand}")
    system_label.config(text=f"システム: {systemhand}")

    # あいこの場合
    if userhand == systemhand:
        result_label.config(text='あいこです')
        draw += 1
    # userが勝っている場合
    elif ((userhand == 'rock' and systemhand == 'scissors') or
          (userhand == 'scissors' and systemhand == 'paper') or
          (userhand == 'paper' and systemhand == 'rock')):
        result_label.config(text='ユーザーの勝ちです!')
        userwin += 1
    #システムが勝っている場合
    else:
        result_label.config(text='システムの勝ちです!')
        systemwin += 1

    num_label.config(text=f"~~{num}回目~~")
    num += 1

    if num > 5:
        # ファイルに記録を保存する
        update_stats(userwin, systemwin, draw)

        if userwin == systemwin:
            messagebox.showinfo("最終結果", "同点です。中々やりますね")
        elif userwin > systemwin:
            messagebox.showinfo("最終結果", "ユーザーの勝ちです。おめでとうございます。")
        else:
            messagebox.showinfo("最終結果", "システムの勝ちです。またの挑戦お待ちしております。")

        # 画面を非表示にする
        num_label.pack_forget()
        rock_button.pack_forget()
        scissors_button.pack_forget()
        paper_button.pack_forget()
        user_label.pack_forget()
        system_label.pack_forget()
        result_label.pack_forget()

        # 最初の画面を表示する
        title_label.pack()
        rule_label.pack()
        display_stats()
        start_button.pack(side="bottom")

#スタートボタンを押したときの処理
def start_game():
    global num, userwin, systemwin, draw
    num = 1
    userwin = 0
    systemwin = 0
    draw = 0

    # 回数を表示するラベルを作成
    global num_label
    num_label = tk.Label(root, text=f"~~{num}回目~~", font=("Helvetica", 10))

    # タイトル部分を非表示
    title_label.pack_forget()
    # ルール部分を非表示
    rule_label.pack_forget()
    # 成績部分を非表示
    sumgrade_label.pack_forget()
    # スタートボタンを非表示
    start_button.pack_forget()

    # ゲーム関連のウィジェットを表示
    num_label.pack()
    rock_button.pack(fill="x",padx=20,side="top")
    scissors_button.pack(fill="x",padx=20,side="top")
    paper_button.pack(fill="x",padx=20,side="top")
    user_label.pack()
    system_label.pack()
    result_label.pack()

"""起動したときの画面"""
# タイトルを表示する
title_label = tk.Label(root, text="じゃんけんゲーム", font=("Helvetica", 20))
title_label.pack()

# ルールを表示する
rule_label = tk.Label(root, text="~ルール~\n5回じゃんけんをします.\nスタートボタンを押して,ボタンを選んでください.",font=("Helvetica", 10))
rule_label.pack()

# 今までの成績を表示する
sumgrade_label = tk.Label(root, text="")
sumgrade_label.pack()
display_stats()

# スタートボタンを表示する
start_button = tk.Button(root, text="スタート", command=start_game)
start_button.pack(side="bottom")

"""スタートボタンが押された後の画面"""
# グー、チョキ、パーのボタンを表示する
rock_button = tk.Button(root, text="rock", command=lambda: button_clicked(1))
scissors_button = tk.Button(root, text="scissors", command=lambda: button_clicked(2))
paper_button = tk.Button(root, text="paper", command=lambda: button_clicked(3))

# ユーザーが押した手を表示する
user_label = tk.Label(root, text=f"あなた: {userhand}")
# システムが選んだ手を表示する
system_label = tk.Label(root, text=f"システム: {systemhand}")
# ユーザーとシステムが出した手から結果を表示する
result_label = tk.Label(root, text=result)

# Tkinterのイベントループを開始する
root.mainloop()