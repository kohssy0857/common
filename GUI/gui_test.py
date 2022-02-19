import PySimpleGUI as sg

#  セクション1 - オプションの設定と標準レイアウト
# sg.theme('Dark Blue 3')
sg.theme('Dark Brown')

layout = [
    [sg.Text('Python GUI')],
    [sg.Text('名前', size=(15, 1)), sg.InputText('○○〇×××')],
    [sg.Text('住所', size=(15, 1)), sg.InputText('△△△△村')],
    [sg.Text('電話番号', size=(15, 1)), sg.InputText('xxx-xxx-xxx')],
    [sg.Submit(button_text='実行ボタン'),sg.Quit(button_text='終了ボタン')]
]

# セクション 2 - ウィンドウの生成
window = sg.Window('住所を入力', layout)

# セクション 3 - イベントループ
while True:
    event, values = window.read()

    if event =='終了ボタン':
        ans=sg.PopupYesNo(' 本当に終了してよろしいですか？',title=' 確認します')
        ans.close()
        if ans=='Yes':
            print('button_exit')
            break
        # if ans=='No':
        #     window = sg.Window('住所を入力', layout)

    if event == None:
        print('WIN_exit')
        break


    # if event == sg.WIN_CLOSED:
    #     print('win_ break')
    #     break

    if event == '実行ボタン':
        show_message = "名前：" + values[0] + 'が入力されました。\n'
        show_message += "住所：" + values[1] + 'が入力されました。\n'
        show_message += "電話番号：" + values[2] + "が入力されました。"
        print(show_message)

        # ポップアップ
        sg.popup(show_message)

        # window["-OUTPUT-"].update(values[show_message])

# セクション 4 - ウィンドウの破棄と終了
window.close()