キャリブレーションを行うためのサンプルプログラムです。

機密情報は含まれておりません。

# 使い方
依存関係のインストール
```
poetry install
```

configのコピーと設定
```
cp config.sample.json config.json
```

チェッカーボードを撮影
40枚程度
```
poetry run python shoot.py
```

キャリブレーション
```
poetry run python calibration.py
```

補正
```
poetry run python correction.py
```
