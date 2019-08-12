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
## HTML出力
以下にブラウザなどでアクセスします  
http://your.host.ipaddr/ipinfo/TargetIpAddr  
 ex)http://127.0.0.1/ipinfo/8.8.8.8
## json出力
以下にアクセスします  
http://your.host.ipaddr/ipinfo/json/TargetIpAddr  
 ex)http://127.0.0.1/ipinfo/json/8.8.8.8
## CLI
コマンドラインから直接叩くことも可能です  
```
$ python3 cli.py TragetIpAddr
```

# Install
## アプリケーションのダウンロード
```
git clone git@github.com:hualuhua/ipinfo.git
```

## abuseipdbのapikey(v2)の設定
1. API keyを未取得の場合は以下から取得  
開発時点では1000query/dayまで無料です。  
https://www.abuseipdb.com/

2. config.pyに記載されるabuseipdbkeyの値を上記で取得したものに書き換える  
なお、config.pyでflaskのportを指定できるようになっているが、後述のsystemdを使う場合はunitfileに該当の設定を書かないと有効にならない点注意
```
cd ipinfo
vim config.py
```

3. アプリケーションの実行
```
python3 flaskapp.py
```

4.unitfileの配置
デーモンとしてsystemdに登録したい場合に実施します。  
先に当アプリケーションを起動している場合は終了してください(ポート競合のため)。  
unitfileで相対パスが使えない関係上、各設定ファイルに絶対パスを書いている。  
ec2-userのディレクトリ直下で動く想定になっているので、別環境で動作させる場合は設定ファイルを書き換えること  
* flask.conf
* ipinfo.service

6. unit fileの配置
記載内容に問題がなければunitfileを登録する
```
sudo cp -p ipinfo.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start ipinfo.service
sudo systemctl enable ipinfo.service
```
