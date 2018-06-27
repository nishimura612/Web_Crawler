# Web_Crawler
pythonでwebクローラーを作って見た

## バージョン情報  
- python 3.6.5  
- pip 10.0.1  
- scrapy 1.5.0

## Instalation

    $ pip3 install scrapy


## Test

    $ scrapy genspider sample blog.scrapinghub.com

- webクローラーの雛形が作成できるコマンド  
- 第一引数にSpaiderの名前
- 第二引数にクロール対象のドメインを指定

## Execute

    $ scrapy runspider sample.py -o sampleitems.jl  

## Execution result

    $ cat sampleitems.jl

## 参考文献
### [Scrapy入門①](https://sutaba-mac.site/scrapy-make-your-first-spider/#Scrapy)

### [Scrapy入門②](https://sutaba-mac.site/scrapy-s2-settings-and-items/)

