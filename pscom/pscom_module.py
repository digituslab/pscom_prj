"""
シリアル通信クラス
pscom_module.py

pyserialを使って簡単にテキストデータの送受信ができるようにラップ。
2021-5-16, WATABE, Yoshihisa

使うときは xxx.py の先頭で以下のインポートが必要
import pscom
または、、、
from pscom import *

バグレポート：digituslab@gmail.com
"""
from serial import *
import threading
import time

class Pscom:

    port_object:Serial
    thread_object:threading.Thread
    received_flag:bool
    received_buffer_fixed:str
    received_buffer:str

    def __init__(self) -> None:
        """このクラスのコンストラクタ
           各種内部変数の初期化とオブジェクトの生成を行う
        """
        self.port_object = None
        self.thread_object = None
        self.received_flag = False
        self.received_buffer_fixed = ""
        self.received_buffer = ""
        pass

    def receiver_thread(self):
        """受信スレッド
        """
        while True:
            single_byte = self.port_object.read(1)
            single_char = single_byte.decode(encoding='ascii')

            if single_char == '\r':
                # Complete
                self.received_buffer_fixed = self.received_buffer
                self.received_buffer = ""
                self.received_flag = True
                # print(self.received_buffer_fixed)
            else:
                # In progress
                self.received_buffer = self.received_buffer + single_char

    def open_port(self,port_name:str,baud_rate:int):
        """シリアルポートを開く

        Args:
            port_name (str): ポート名（WindowsならCOM1など）
            baud_rate (int): ボーレート（例：9600）

        Returns:
            bool: 成功＝True, 失敗=False
        """
        try:
            self.port_object = Serial(port_name,baud_rate)
            self.thread_object = threading.Thread(target=self.receiver_thread)
            self.thread_object.setDaemon(True)
            self.thread_object.start()
        except Exception as exc:
            return False

        return True

    def send_text(self,text:str):
        """テキストを送信

        Args:
            text (str): 送信する文字列（CRは自動で付くので不要）

        Returns:
            str: 応答文字列（エラーが起きた時は"ERROR"を返す）
        """
        wait_limit:int
        wait_limit = 30
        try:
            self.received_buffer_fixed = ""
            self.received_flag = False
            self.port_object.write(bytearray((text + '\r'),encoding='ascii'))
            while self.received_flag == False and wait_limit > 0:
                wait_limit = wait_limit - 1
                time.sleep(0.1)
                pass

            return self.received_buffer_fixed
        except Exception as exc:
            print(exc)
            return "ERROR"
