# NORADのTLE起動データを取得してDBに格納するサンプル

## 何ができるのか

* NORAD TLEを公開しているcelestrakの[ホームページ](https://www.celestrak.com/NORAD/elements/)からTLEを取得
* 取得したデータに付加情報をつけてDB(SQLite3)に保存

## 動作環境

オリジナルの作者(shinyorke)の動作環境より.

* gitクライアント(何でもOK)
    * ソースコードを取得するために使う
    * 面倒くさい方は直接ダウンロードしてもらってもOK
* Python 3系の最新Ver
    * 3.6以上を推奨
    * 試してはいませんが,3.3.x以上なら動くと思う
    * 2.7.x系は未検証ですが多分動くと思います(がオススメしません&対応する気は無いです)
* Scrapyのインストールが必要(後述)
    * 1.4.0で検証(作成時点の最新バージョン)
* MacOS Sierra(10.12.6)
    * 上記のPythonバージョンおよびScrapyバージョンであればOS関係なく動くハズ

## セットアップ

### 1. リポジトリをclone or ダウンロードする

#### クローンの場合

```bash
$ git clone https://github.com/inTheRye/scrapy-sample-baseball.git
$ git checkout scrape-space-object
```

#### ダウンロードの場合

```bash
$ wget https://github.com/inTheRye/scrapy-sample-baseball/archive/scrape-space-object.zip
$ unzip master.zip
```

### 2. Pythonをインストール

* [ダウンロードサイト(公式)](https://www.python.org/downloads/)
* お使いのOS・プラットフォームに合わせてお使いください
* (繰り返しになりますが)Python 3.6以上が推奨です！

### 3. Scrapyをインストール

```bash
$ pip install scrapy
```

## 使い方

### 1. ディレクトリに移動

Scrapyのエンドポイントにcdします.

```bash
$ cd scrapy-sample-baseball/space_object
```

なお,ダウンロードで手に入れた人は最初のディレクトリ名が変わるので注意

```bash
$ cd scrapy-sample-baseball-scrape-space-object/space_object
```

### 2. TLEを取得

scrapyのコマンドで取得します.

初回実施の時はDBファイル(space_object.db)が生成され,同時にSchemeも作成されます.

```bash
$ scrapy crawl tle
```

## データについて

### 構造

[space_object/space_object/item.py](https://github.com/inTheRye/scrapy-sample-baseball/blob/scrape-space-object/space_object/space_object/items.py)に乗っているカラムと解説が全てです.

カラムの名称はsgp4モジュールの属性の略称を用いています.

詳細は各Itemのコメントを参照ください.

### Table Scheme

[space_object/space_object/pipelines.py](https://github.com/inTheRye/scrapy-sample-baseball/blob/scrape-space-object/space_object/space_object/pipelines.py)にCreate Table文があります.

カラムの意味と解説はItemと全く同じです(id値とcreate_date/update_dateがあるぐらいの違い)

なお,indexは全く貼っていないので必要な方は随時書き換えてもらえると.
