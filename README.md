# Web_Crawler
pythonでwebクローラーを作って見た

## バージョン情報  
- python 3.6.5  
- pip 10.0.1  
- scrapy 1.5.0

## Scrapyのインストール方法

    $ pip3 install scrapy


## クローラーの雛形生成コマンド

    $ scrapy genspider sample blog.scrapinghub.com

- webクローラーの雛形が作成できるコマンド  
- 第一引数にSpaiderの名前(クラス名の末尾に自動的にSpaiderが追記されることに注意)
- 第二引数にクロール対象のドメインを指定

## 実行方法

    $ scrapy runspider sample.py -o sampleitems.jl  

## 実行結果

    $ cat sampleitems.jl


## プロジェクト単位でwebクローラーを作成

    $ scrapy startproject testproject

    (以下のようなメッセージが表示される)
    New Scrapy project 'testproject', using template directory '/usr/local/lib/python3.6/site-packages/scrapy/templates/project', created in:
    /Users/kazu/Github/Web_Crawler/testproject

    You can start your first spider with:
        cd testproject
        scrapy genspider example example.com

    (上記のメッセージにしたがってコマンドを実行)
    $ cd testproject
    $ scrapy genspider First https://jp.techcrunch.com/

- webクローラーをプロジェクト単位で雛形を生成するコマンド

## プロジェクトのファイル構成確認方法
projectのファイル構成を見るのは$ ls -Rとかでも良いが、treeコマンドをbrewでインストールしておくと便利．

    $ tree . 

## Scrapyの設定ファイルの記述
- Scrapyの設定ファイルは,settings.pyというファイルで記述されている．  
- 忘れないうちに，クロール間隔の調節を行う．なぜなら，クロール元のwebサイトにアクセスしすぎて迷惑をかけないため．  

settings.pyの中の

    # DOWNLOAD_DELAY = 3

とコメントアウトされている内容をコメントを外して有効にする

    DOWNLOAD_DELAY = 3

数字は秒数(ミリ秒ではない)を表しているため，この場合はクロール間隔が3秒になる．  

クロール間隔をミリ秒(ms)で指定したい場合は，以下のようにする．

    DOWNLOAD_DELAY = 1.25



## 参考文献
### [Scrapy入門①](https://sutaba-mac.site/scrapy-make-your-first-spider/#Scrapy)

### [Scrapy入門②](https://sutaba-mac.site/scrapy-s2-settings-and-items/) <- 現在の進捗はココ
　

