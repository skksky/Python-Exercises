# Python-Exercises

言語処理100本ノック with Python

## 課題

[言語処理100本ノック 2015](http://www.cl.ecei.tohoku.ac.jp/nlp100/)

## 環境

Docker 環境を使って検証しました。

```
$ docker pull python:3.6
$ docker run -it python:3.6 bash
```
Python のバージョンは`Python 3.6.4`です。

### はじめに
文字列の表示には`print`関数を使う。（Python3の場合）
```python
#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

str = "stressed"
print (str)         # stressed を表示
```
## 第1章: 準備運動

### 00. 文字列の逆順
#### 問題
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
#### 答え
```python
#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

str = "stressed"
print (str)         # stressed を表示
print (str[::-1])   # desserts を表示
```
#### 解説
スライスというテクニックを使うらしい。

`str[数字]`で、先頭から数字に入れた文字目を表示する。`0`だったら`s`が表示される。負の数を入力することもでき、逆順に数える。今回の例だと、`str[7]`と`str[-1]`は同義となる。
```python
str[0]        # 's'
str[7]        # 'd'
str[-1]       # 'd'
```
`:`を使って範囲指定をする。範囲の終わりの文字は結果に表示されないので注意。
```python
str[1:3]      # 'tr'
str[0:-3]     # 'stres'
str[:4]       # 'stre'
str[4:]       # 'ssed'
```
もうひとつ`:`をつけることで、ステップ数を表すことができる。
```python
str[0:6:2]    # 'srs', 0番目から6番目を2つ飛ばしで。
str[::3]      # 'see', 全体を3つ飛ばしで。
str[-3::2]    # 'sd'，負の数も指定可能。後ろから3番目から2つ飛ばしで。
str[::-3]     # 'dst'，ステップ数を負の数にすると逆順に全体を3つ飛ばしで。
```
なので、今回の課題は、「逆順に1ステップずつ遡る」と読み替えることができるので、`print (str[::-1])`と表すことができる。

### 01. 「パタトクカシーー」
#### 問題
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
#### 回答
```python
#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

str = "パタトクカシーー"
print (str)         # パタトクカシーー
print (str[::2])    # パトカー
```
#### 解説
これもステップを使えば簡単。今回の指定は「2つ飛ばしで表示する」と読み替えることができるので`print (str[::2])`でOK。

### 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
#### 問題
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
#### 回答
```python
#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

str0 = "パトカー"
str1 = "タクシー"
str2 = ""

for i, j in zip(str0, str1) :
    str2 = str2 + i + j

print (str2)      # パタトクカシーー
```
または
```python
#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

str = ""
tuple0 = tuple("パトカー")
tuple1 = tuple("タクシー")

for i,j in zip(tuple0, tuple1) :
    str = str + i + j

print (str)
```
#### 解説
まずは間違いから。ここでは、タプル（tuple）と for loop を利用しようとしました。タプルとは、イミュータブル（不変の）リストのことです。

参考：[【Python入門】リストとの違いは？タプルの使い方まとめ | 侍エンジニア塾ブログ | プログラミング入門者向け学習情報サイト](https://www.sejuku.net/blog/23964)

`tuple()`を使うことで、タプルを作る事ができます。
```python
# 文字列を変数に格納
str0 = "パトカー"
str1 = "タクシー"

# タプルを作成
tuple0 = tuple(str0)
print (tuple0)      # ('パ', 'ト', 'カ', 'ー')

tuple1 = tuple(str1)
print (tuple1)      # ('タ', 'ク', 'シ', 'ー')
```
これをfor文で取り出してあげればOKと思いましたが、このように書いてしまっておかしなこととなりました。
```python
#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

str0 = "パトカー"
str1 = "タクシー"
str2 = ""

tuple0 = tuple(str0)
print (tuple0)

tuple1 = tuple(str1)
print (tuple1)

for i in tuple0 :
    for j in tuple1 :
        str2 = str2 + i + j
print (str2)

# 結果
# ('パ', 'ト', 'カ', 'ー')
# ('タ', 'ク', 'シ', 'ー')
# パタパクパシパートタトクトシトーカタカクカシカーータークーシーー
```
冷静に考えればその通りなので、複数の値（i,j）を同時に処理できるようにしなければいけなさそうです。調べて見ると、`zip()`を使ってあげることでスマートに書けるようです。`zip()`は複数のシーケンスに並行して同時にアクセスするforループを作るのに便利な関数。

`zip()`を使うことで、回答例のように文字列を連結するパターンとタプルを活かしたパターンをつくることができました。
### 03. 円周率
#### 問題
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
#### 回答
```python
#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = str.replace('.', "")
str = str.replace(',', "")
str = str.split()

list = []
for i in str:
    list.append(len(i))

print (list)

# 結果
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

```
#### 解説
まず、`,`と`.`は邪魔なので`replace`を使って除去します。次に、`split`を使って単語ごとに分割します。`split`は引数なしだとスペースやタブで自動的に分割されます。引数にダブルクオートで囲った文字を入れると、区切り文字を指定することができます。

文字数を格納するリストを用意します。そこにfor文で格納していくわけですが、`len`を使って文字数をカウント、それを`append`を使ってリストに追加しています。

### 04. 元素記号
#### 問題
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
#### 回答
```python
#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = str.replace('.', "")
str = str.replace(',', "")
str = str.split()

single = [1, 5, 6, 7, 8, 9, 15, 16, 19]

dict = {}

for (num, word) in enumerate(str,1):
    if num in single:
        dict[num] = word[:1]
    else:
        dict[num] = word[:2]

print (dict)
# print (sorted(dict.items()))
# 結果
# {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mi', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca'}

```
#### 解説
辞書型を使います。辞書型（dict）とは、キー（名前）と値をセットにして扱うデータ形式のこと。キーを指定することで値を取り出すことができます。

for文では`enumerate`関数を使います。`enumerate`関数を使うとループする際にインデックスつきで要素を得ることができます。引数に数値を指定することで、カウントアップの数値の起点を指定する事ができます。今回は`1`からスタートです。

次にif文でリストにある要素と一致した場合を条件としたいので、`in`を使えばよさそうです。

参考：[リスト内に特定の要素があるかでif分岐 - Qiita](https://qiita.com/clarinet758/items/43fdc786685e7c13abf5)

辞書への値の追加は`辞書[キー] = 値`で追加、更新ができます。キーは数字で、値を元素にします。結果、1から順に元素が並んで出力されました。元素をキーにすると順番がバラバラになるので、その場合は`sorted`を使って並び替えてあげるとわかりやすそうです。順番はばらばらでも、課題としては正解です。

### 05. n-gram
#### 問題
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
#### 回答
```python
#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

def ngram(input,num):
    last_word = len(input) - num + 1
    output = []
    for i in range(0,last_word):
        output.append(input[i:i+num])
    return output

str = "I am an NLPer"
# 文字bi-gram
print(ngram(str,2))
# 単語bi-gram
print(ngram(str.split(),2))

# 結果
# ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
# [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
```
#### 解説
`n-gram`とは、「隣合うN個の塊」のことを指します。`単語n-gram`や`文字n-gram`があり、例えば「金持ち喧嘩せず」の文字 2-gram(bi-gram) は {金持, 持ち, ち喧, 喧嘩, 嘩せ, せず} となります。

参考：[自然言語処理はじめました - Ngramを数え上げまくる](https://www.slideshare.net/phyllo/ngram-10539181)

今回は、n-gramを返す関数を実装せよ、という課題ですので、`def`で関数を定義します。`()`内には引数として定義する変数を入れましょう。

`last_word`は、入力された文字列の長さからngramで取り出したい文字数を引いて1加えたものです。これがどういうことか説明するために、次のfor文を見てみます。

```python
for i in range(0,last_word):
    output.append(input[i:i+num])
```

`range`は連続した数字のオブジェクトを作るための関数です。

[【Python入門】range関数を使ってリストを作ろう！ | 侍エンジニア塾ブログ | プログラミング入門者向け学習情報サイト](https://www.sejuku.net/blog/23145)

このfor文の変数`i`の実行範囲は、ゼロから`last_word`、つまり今回の文字列の長さ13から`num`を引いて1加えた値、今回のbi-gramだと12がセットされます。tri-gramだったら11です。

次に、`output`リストに`input`をスライスした値を入力していくわけです。そうすると、bi-gramであれば順々に2文字ずつ取り出され、`i+num`が最後の文字に到達したときにforが終了します。

あとは、この関数`ngram`で得られた結果（return）を表示してあげるだけです。

この課題は全く分からなかったので以下サイトを参考に読み解きました。

参考：[言語処理100本ノック with Python（第1章） - Qiita](https://qiita.com/gamma1129/items/37bf660cf4e4b21d4267)

### 06. 集合
#### 問題
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
#### 回答
```python
#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

def ngram(input,num):
    last_word = len(input) - num + 1
    output = []
    for i in range(0,last_word):
        output.append(input[i:i+num])
    return output

str0 = "paraparaparadise"
str1 = "paragraph"

X = set(ngram(str0,2))
Y = set(ngram(str1,2))

print (X)
# ['pa', 'ar', 'ra', 'ap', 'pa', 'ar', 'ra', 'ap', 'pa', 'ar', 'ra', 'ad', 'di', 'is', 'se']
print (Y)
# ['pa', 'ar', 'ra', 'ag', 'gr', 'ra', 'ap', 'ph']

# 和集合
union = X | Y
print (union)

# 積集合
intersection = X & Y
print (intersection)

# 差集合
difference = X -Y
print (difference)

# 'se'というbi-gramがXおよびYに含まれるか
print ("se" in X)
print ("se" in Y)

# 結果
# {'se', 'ap', 'di', 'is', 'ra', 'ar', 'pa', 'ad'}
# {'ap', 'ag', 'ph', 'ra', 'gr', 'pa', 'ar'}
# {'se', 'ap', 'ag', 'di', 'ph', 'is', 'ra', 'ar', 'pa', 'gr', 'ad'}
# {'ap', 'ra', 'pa', 'ar'}
# {'se', 'ad', 'is', 'di'}
# True
# False
```
#### 解説
これは割りと書いてある通り、集合の作り方をそのままやればOK。

包含判定については、`in`を使うことで、`True` or `False`の判定ができる。

### 07. テンプレートによる文生成
#### 問題
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
#### 回答
```python
#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

x = 12
y = "気温"
z = 22.4

def tenki(x,y,z):
    return str(x) + u"時の" + y + u"は" + str(z)

print(tenki(x,y,z))

# 結果
# 12時の気温は22.4
```
#### 解説
文字列の連結は`+`でできるようです。`x`と`z`は`int`なので、`str`に変換するために、`str()`を使用しています。

### 08. 暗号文
#### 問題
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
#### 回答
```
#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

def cipher(input):
    output = ""
    for i in input:
        if i.islower():
            output += chr(219 - ord(i))
        else:
            output += i
    return output

input = "If you can dream it, you can do it."
coded = cipher(input)

print(cipher(input))
print(cipher(coded))
# 結果
# Iu blf xzm wivzn rg, blf xzm wl rg.
# If you can dream it, you can do it.
```
#### 解説
`ord`は組み込み関数で、「1 文字の Unicode 文字を表す文字列に対し、その文字の Unicode コードポイントを表す整数を返します。例えば、 ord('a') は整数 97 を返し、 ord('€') (ユーロ記号) は 8364 を返します。これは chr() の逆です。」というものです。

`chr`も組み込み関数で「Unicode コードポイントが整数 i である文字を表す文字列を返します。例えば chr(97) は文字列 'a' を、 chr(8364) は文字列 '€' を返します。 ord() の逆です。」というものです。

参考：[2. 組み込み関数 — Python 3.6.3 ドキュメント](https://docs.python.jp/3/library/functions.html)

ということがわかれば、あとは簡単。for文で文字を1つずつ読み込み、小文字だったら変換処理をして`output`に値を格納、そうでなければそのまま`output`に値を格納すればOkです。

### 09. Typoglycemia
#### 問題
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
#### 回答
```
#!/usr/local/bin python3.6
# -*- coding: utf-8 -*-

import random

input = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."


def typoglycemia(input):
    output = []
    for word in input.split(' '):
        if len(word) <= 4:
            output.append(word)
        else:
            middle_char = list(word[1:-1])
            random.shuffle(middle_char)
            output.append(word[0] + ''.join(middle_char) + word[-1])
    return ' '.join(output)

print(typoglycemia(input))
# 結果
# I cd'nuolt bleeive that I could aualctly urnantdsed what I was rianedg : the poneneahml peowr of the haumn mind .
```
#### 解説
`random`は`random.shuffle(list)`はできても、`random.shuffle(str)`はできません。また、`random.shuffle(list)`の結果を`str()`で変換しても`None`が返ってきてしまいます。

最終的には`join`でリストを文字列に変更すればいいという結論に落ち着きました。

## 第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

### 10. 行数のカウント
#### 問題
行数をカウントせよ．確認にはwcコマンドを用いよ．
#### 回答
`wc`コマンドでのカウント結果はこちら。
```
root@687baf7b1c81:/share/chapter2# ls
hightemp.txt
root@687baf7b1c81:/share/chapter2# wc -l hightemp.txt
24 hightemp.txt
```
Python のコードはこちら。
```

```
#### 解説
### 11. タブをスペースに置換
#### 問題
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
#### 回答
```
```
#### 解説
### 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
#### 問題
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
#### 回答
```
```
#### 解説
### 13. col1.txtとcol2.txtをマージ
#### 問題
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
#### 回答
```
```
#### 解説
### 14. 先頭からN行を出力
#### 問題
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
#### 回答
```
```
#### 解説
### 15. 末尾のN行を出力
#### 問題
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
#### 回答
```
```
#### 解説
### 16. ファイルをN分割する
#### 問題
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
#### 回答
```
```
#### 解説
### 17. １列目の文字列の異なり
#### 問題
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
#### 回答
```
```
#### 解説
### 18. 各行を3コラム目の数値の降順にソート
#### 問題
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
#### 回答
```
```
#### 解説
### 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
#### 問題
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
#### 回答
```
```
#### 解説
