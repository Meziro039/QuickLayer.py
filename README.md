## 概要
QuickLayer.pyは、ファイル階層の相対パスを入力すると絶対パスを返答してくれるモジュールです。  
実行されるOSのファイル区切り文字に応じて出力されます。  
*Windows10以外の環境で検証していないので正常に出力されない可能性があります。  

## 使い方
### 基本
`quicklayer.get(__file__, "{Layer}")`

### {Layer}
`..` or `../..`  
上位層のフォルダまでの絶対パスを出力  
  
`hoge.txt`  
自身のフォルダのファイルまでの絶対パスを出力  
  
`hoge/fuga.txt`  
自身のフォルダの下位層ファイルまでの絶対パスを出力  
  
`../hoge.txt`  
上位層のファイルまでの絶対パスを出力  
  
*出力値はOSに対応したファイル区切り文字で出力されますが、入力のファイル区切り文字は`/`である必要があります。
  
## 利用例
```
[ファイル構成]
L hoge
.L fuga
.- fuga.txt
.L piyo
.- piyo.py
```

```
[Program]
// 自身の位置は`piyo.py`

file = quacklayer.get(__file__, "../fuga/fuga.txt")
print(file)
```

```
[Output]
(省略)/hoge/fuga/fuga.txt

```

*hoge/fuga/piyoには任意の値を入力してください。  

## エラー
`None`を返答します。

## 動作環境
Python 3.10  

## 更新履歴
v0.0.1.a a版 2022-06-06  
仮公開  
  
v0.0.1 初版 2022-06-07  
全体的に整えました。  
- READMEを作成
- 一部処理の記述方法を変更
- コメントアウトの見直し
- エラー処理の欠陥を修正
- 不要なコードを削除
- 不要なコメントアウトを削除
- test.pyを少しまともにした