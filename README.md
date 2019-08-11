# What is this ?
所定のURLにIPアドレスを投げるとRDAPi(またはNIR)とabuseipdb.comの一部の情報を引っ張ってくるアプリです。

# requirement
* python3 (3.7.4で開発)
  modules
  * flask
  * ipwhois : https://ipwhois.readthedocs.io/en/latest/README.html
  * json
  * requests
 
# Usage
## アプリケーションのダウンロード
git clone git@github.com:hualuhua/ipinfo.git

## abuseipdbのapikey(v2)の設定
1. API keyを未取得の場合は以下から取得  
   https://www.abuseipdb.com/

2. config.pyに記載されるabuseipdbkeyの値を上記で取得したものに書き換える
```
cd ipinfo
vim config.py
```

3. アプリケーションの実行
```
python3 ipinfo.py
```

4. リクエスト
以下のようなURLにアクセスする  
http://YourHostIP:5000/get_whois/RequestIP  
ex) http://127.0.0.1:5000/get_whois/8.8.8.8

5.(デーモン化したい場合)unitfileの配置
unitfileで相対パスが使えない関係上、各設定ファイルに絶対パスを書いている。  
ec2-userのディレクトリ直下で動く想定になっているので、別環境で動作させる場合は設定ファイルを書き換えること  
* flask.conf
* ipinfo.service

1. unit fileの配置
記載内容に問題がなければunitfileを登録する
```
sudo cp -p ipinfo.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start ipinfo.service
sudo systemctl enable ipinfo.service
```
