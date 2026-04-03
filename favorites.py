import json
import os
from display import colored, Color

# お気に入りを保存するファイル名
FAVORITES_FILE = "favorites.json"

# 有効な単位の一覧
VALID_UNITS = ["°C", "°F", "K"]

def _load_favorites():
    """favorites.json からお気に入りを読み込む。ファイルがなければ空リストを返す"""
    if not os.path.exists(FAVORITES_FILE):
        return []
    try:
        with open(FAVORITES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(colored(f"お気に入りの読み込みに失敗しました: {e}", Color.RED))
        return []

def _save_favorites(favorites):
    """お気に入りを favorites.json に保存する"""
    try:
        with open(FAVORITES_FILE, "w", encoding="utf-8") as f:
            json.dump(favorites, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(colored(f"お気に入りの保存に失敗しました: {e}", Color.RED))

def add_favorite():
    """お気に入り温度を登録する"""
    print(colored("\n--- お気に入り登録 ---", Color.BOLD, Color.CYAN))

    # ラベル入力
    label = input("名前（例: 体温、沸点）: ").strip()
    if not label:
        print(colored("エラー: 名前を入力してください。", Color.RED))
        return

    # 温度値入力
    try:
        value = float(input("温度の値: "))
    except ValueError:
        print(colored("エラー: 数値を入力してください。", Color.RED))
        return

    # 単位選択
    print(f"単位を選んでください: {colored('1', Color.CYAN)}.°C  {colored('2', Color.CYAN)}.°F  {colored('3', Color.CYAN)}.K")
    unit_choice = input("選択 (1〜3): ").strip()
    unit_map = {"1": "°C", "2": "°F", "3": "K"}
    if unit_choice not in unit_map:
        print(colored("エラー: 1〜3 を入力してください。", Color.RED))
        return
    unit = unit_map[unit_choice]

    # 保存
    favorites = _load_favorites()
    favorites.append({"label": label, "value": value, "unit": unit})
    _save_favorites(favorites)
    print(colored(f"「{label}: {value}{unit}」をお気に入りに登録しました。", Color.GREEN))

def show_favorites():
    """登録済みのお気に入り温度を一覧表示する"""
    favorites = _load_favorites()

    print("\n" + colored("=" * 40, Color.CYAN))
    print(colored("      お気に入り温度", Color.BOLD, Color.CYAN))
    print(colored("=" * 40, Color.CYAN))

    if not favorites:
        print(colored("  お気に入りはまだ登録されていません。", Color.YELLOW))
    else:
        for i, entry in enumerate(favorites, 1):
            label = entry.get("label", "")
            value = entry.get("value", 0)
            unit  = entry.get("unit", "")
            print(f"  {colored(i, Color.CYAN)}. {label}: {colored(f'{value}{unit}', Color.GREEN, Color.BOLD)}")

    print(colored("=" * 40, Color.CYAN))
