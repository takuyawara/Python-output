#じゃんけんプログラム

#①利用者にじゃんけんをするように呼び掛ける
#②利用者に入力欄が表示される
#③'グー','チョキ','パー'から選んでもらう
#④システムの方でも'グー','チョキ','パー'をランダムで選ぶ
#⑤③と④の結果から利用者が勝ちか，システムが勝ちか判断する
#⑥5回勝ったら勝ちとする→結果を表示する

#new
#sleep関数による処理の遅らせ
#過去の成績をcsvファイルに保存
#→過去の結果を反映できていなかったので訂正

import random
import time
import csv

#繰り返す回数の初期値
count=1
#ユーザー，システムの勝利数・あいこの初期値
userwin=0
systemwin=0
draw=0

#システムが出す手
system=['rock','scissors','paper']

#最終結果をファイルにアップデートする関数
def update_stats(wins,losses,draws):
    try:
        with open('result.csv','r') as file:
            reader=csv.reader(file)
            for row in reader:
                #既存の統計情報を読み込む
                prev_wins, prev_losses, prev_draws = int(row[0]), int(row[1]), int(row[2])
                wins += prev_wins
                losses += prev_losses
                draws += prev_draws
                break  # 最初の行のみ読み込む
    except FileNotFoundError:
        # ファイルが存在しない場合は新しく作成
        pass
    #更新された統計情報を保存
    with open('result.csv','w',newline='') as file:
        writer=csv.writer(file)
        total_games = wins + losses + draws
        win_rate = wins / total_games * 100 if total_games > 0 else 0
        writer.writerow([wins, losses, draws, win_rate])

#結果を表示する関数
def display_stats():
    try:
        with open('result.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # 勝率を四捨五入
                win_rate = round(float(row[3]), 2)
                print(f"ユーザーの勝利数: {row[0]}, ユーザーの敗北数: {row[1]}, 引き分け数: {row[2]}, ユーザーの勝率: 約{win_rate}%")
    except FileNotFoundError:
        print("統計情報がありません。")

#じゃんけんプログラム開始
print('じゃんけんプログラム')
display_stats()
time.sleep(1)
print('==========================================')
print('こんにちはユーザー! わたしとじゃんけんをしましょう！')
print('じゃんけんは全部で5回行います')
print('==========================================')

while count<=5:
    #システムが出す手
    systemhand=random.choice(system)
    #確認用
    #print(systemhand)

    print('■',count,'回目')
    print('最初はグー！じゃんけん！')

    #「rock」，「scissors」，「paper」以外であれば再度入力を求める
    while True:
        userhand=input('「rock」,「scissors」,「paper」の3つから1つを入力してください:')
        if userhand=='rock'or userhand=='scissors'or userhand=='paper':
            break

    print('ユーザー:',userhand)
    print('システム:',systemhand)

    #あいこの場合
    if userhand==systemhand:
        print('あいこです')
        draw=draw+1
    #userが勝っている場合
    elif ((userhand=='rock'and systemhand=='scissors')or
          (userhand=='scissors'and systemhand=='paper')or
          (userhand=='paper'and systemhand=='rock')):
        print('ユーザーの勝ちです!')
        userwin=userwin+1
    else:
        print('私の勝ちです!')
        systemwin=systemwin+1

    count=count+1
    #print('\n')

#5回分の結果を表示
time.sleep(1)
print('====================================')
print('ユーザー:',userwin,'勝')
print('システム:',systemwin,'勝')
print('あいこ:',draw,'回')

#ファイルに記録を保存する
update_stats(userwin,systemwin,draw)

if(userwin==systemwin):
    print('同点です。中々やりますね')
elif(userwin>systemwin):
    print('ユーザーの勝ちです。おめでとうございます!')
else:
    print('私の勝ちです。またの挑戦お待ちしてます。')
print('====================================')
time.sleep(1)
print('-------------------------------------------------------------------------------------------------')
print('結果が更新されました')
display_stats()
print('-------------------------------------------------------------------------------------------------')

