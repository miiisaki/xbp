import doyolab

#シリアルポートを入力-------------------------
serial_port='/dev/tty.usbmodem14201'
#-------------------------------------------

#Arduinoとのシリアル通信設定-------------------
my_arduino = doyolab.set_serial(serial_port,9600)
#-------------------------------------------


#user_key、sub_idの設定---------------------
#自分のユーザーkeyを書く
user_key='8sFBNFegPAqSKZ3PDFUjLQPbvbKKtw'
#subIDはどのデバイスからのデータか、どのプロジェクトのデータかなどを認識するために使います
sub_id='pc'
#-------------------------------------------



#while Trueは無限ループ#----------------------
while True:
    # Arduinoからreadlineコマンドでデータを取得し、data_from_arduinoという変数に格納
    data_from_arduino=my_arduino.readline()
    #stripコマンドで、data_from_arduinoの中の余計な文字を削除
    #さらにintで文字で送られてきたデータをint型に変換
    data=int(data_from_arduino.strip())
    print(data)

    # データの設定--------------------------------
    datetime_data = ""
    int_data = data #Arduinoから受け取った値をここでint_dataにいれる
    float_data = ""
    txt_data = ""
    # -------------------------------------------

    # データの送信---------------------------------
    # user_key
    # sub_id
    # 日付データ（空白にしてもサーバーで自動で日付を入れてくれる）:datetim_data
    # 整数データ:int_data
    # 実数データ(小数を含むデータ):float_data
    # テキストデータ:txt_data
    ret = doyolab.sendData_To_doyolabIoTserver(user_key, sub_id, datetime_data, int_data, float_data, txt_data)
    print(ret)
    # -------------------------------------------
#-------------------------------------------

