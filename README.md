# pscom シリアル通信クラス (python)

簡単便利にシリアル送受信ができるように、シリアル通信クラスを作成。

## 必須条件

- コンピュータでシリアルポート（USBシリアル変換でもOK）が使えること
- pyserial がインストール済みであること

## 使い方
以下の例のように、Pscomオブジェクトを生成してポートを開き、send_textメソッドで文字列を送るだけです。
応答があれば戻り値として応答（受信文字列）が返されます。

応答がない（通信線が断線など）の場合は、約3秒待っても応答が無ければ ”ERROR” を返します。

```python
from pscom import *

object = Pscom()
object.open_port('COM3',115200)
answer = result = object.send_text(”Hello Serial World”)
print(answer)
```

## 実行
プログラムが main.py だとしたとき、実行は以下の通り。

**Windows**
```bash
python main.py
```

**Mac, Linux**
```bash
python3 main.py
```

## 受信スレッド
このプログラムは受信のためにスレッドを使っています。

スレッドは open_portメソッドを呼び出してポートが正常に開けた時点からプログラムの終了まで存在し続けます。
プログラムが終了するとスレッドも終了します。

## インストール
あなたのプロジェクト（フォルダ）の中に、pscomフォルダを**マルっとコピー**してください。

## その他
ファイルの構成は以下の通りです。

|ファイル    |内容|
|--|--|
|./pscom/\_\_init\_\_.py |モジュールの初期化|
|./pscom/pscom_module.py |pscomクラス本体|
|./test/basic_test.py  |pytestのテストメソッド|
|./main.py |サンプルプログラム|


正直、pythonのスレッドが遅い？のか、あんまり動作は速くないです。

