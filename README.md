# 温度変換CLIツール

摂氏・華氏・ケルビン間の温度変換を行う Python 3 製のインタラクティブ CLI ツールです。

---

## 機能一覧

- **6種類の温度変換**
  - 摂氏 → 華氏 / 華氏 → 摂氏
  - 摂氏 → ケルビン / ケルビン → 摂氏
  - 華氏 → ケルビン / ケルビン → 華氏
- **変換履歴の表示** — セッション中に行った変換を一覧表示
- **履歴のファイル保存** — `results.txt` に変換履歴を書き出し
- **お気に入り登録** — よく使う温度に名前をつけて `favorites.json` に保存
- **お気に入り一覧表示** — 登録済みのお気に入り温度を表示
- **ANSIカラー出力** — ターミナルで見やすい色付き表示

---

## インストール方法

Python 3 のみ必要です。外部ライブラリは不要です。

```bash
git clone https://github.com/NaohiroTowatari/temp-converter.git
cd temp-converter
```

---

## 使い方

```bash
python3 main.py
```

起動後、メニューから番号を選択して操作します。

```
========================================
      温度変換ツール
========================================

変換の種類を選んでください:
  1. 摂氏 → 華氏
  2. 華氏 → 摂氏
  3. 摂氏 → ケルビン
  4. ケルビン → 摂氏
  5. 華氏 → ケルビン
  6. ケルビン → 華氏
  7. 変換履歴を表示
  8. 変換結果をファイルに保存
  9. お気に入りに登録
  10. お気に入りを表示
  0. 終了
```

### 操作例

1. `1` を入力して「摂氏 → 華氏」を選択
2. `100` を入力
3. `100.00°C = 212.00°F` と表示される

---

## ファイル構成

```
temp-converter/
├── main.py          # エントリーポイント。メインループと選択処理
├── converter.py     # 6種類の変換関数（純粋関数、副作用なし）
├── display.py       # ANSIカラー出力ユーティリティ
├── history.py       # 変換履歴の表示・results.txt への保存
├── favorites.py     # お気に入り温度の登録・表示（favorites.json に永続化）
├── tests/
│   ├── test_converter.py  # converter.py のユニットテスト
│   └── test_history.py    # history.py のユニットテスト
├── favorites.json   # お気に入りデータ（初回登録時に自動生成）
└── results.txt      # 変換履歴の保存先（保存操作時に自動生成）
```

---

## テストの実行方法

```bash
python3 -m unittest discover tests/
```

特定のテストファイルだけ実行する場合:

```bash
python3 -m unittest tests/test_converter.py
python3 -m unittest tests/test_history.py
```
