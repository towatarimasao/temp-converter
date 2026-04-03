# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# 温度変換CLIツール
摂氏・華氏・ケルビン間の温度変換を行うPython CLIツール。

## 技術スタック
- Python 3
- 標準ライブラリのみ使用

## コマンド
- 実行: `python3 main.py`
- テスト: `python3 -m unittest discover tests/`

## コーディング規約
- 変数名はスネークケース（例: user_input）
- 関数には日本語でdocstringをつける
- ユーザー向け表示は全て日本語
- エラーハンドリングは必ず try/except で行う

## 禁止事項
- 外部ライブラリのインストール禁止
- グローバル変数の使用禁止
