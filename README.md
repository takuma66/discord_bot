# discord_bot
VALORANTのカスタムマッチ用ディスコードbot
## コマンド一覧
* /map マップをランダムに選択
* /coin 裏か表を出力
* /team VCに入っている人をランダムに５人選択(未実装)

## ファイルの説明
### discordbot.py
* 実際に動くソースコード

### bot_token.txt
* botのトークン情報というものを書いたファイル
* discordbot.pyの中にも同じ値が書いている
* **絶対に他の人に知られてはいけない**

### Procfile
* heroku(サーバー)で動かすコードを指定するためのファイル
* 基本的に変更する必要はない
### runtime.txt
* pythonのバージョンを指定しているファイル

### requirements.txt
* 使用している外部ライブラリをここに書く必要がある
