#!/usr/bin/env python3

from converter import (
    celsius_to_fahrenheit, fahrenheit_to_celsius,
    celsius_to_kelvin, kelvin_to_celsius,
    fahrenheit_to_kelvin, kelvin_to_fahrenheit,
)
from display import colored, Color
from history import show_history, save_history
from favorites import add_favorite, show_favorites

def main():
    """メインループ: 変換の種類を選択して温度変換を実行する"""
    print(colored("=" * 40, Color.CYAN))
    print(colored("      温度変換ツール", Color.BOLD, Color.CYAN))
    print(colored("=" * 40, Color.CYAN))

    history = []

    while True:
        print(colored("\n変換の種類を選んでください:", Color.BOLD))
        print(f"  {colored('1', Color.CYAN)}. 摂氏 → 華氏")
        print(f"  {colored('2', Color.CYAN)}. 華氏 → 摂氏")
        print(f"  {colored('3', Color.CYAN)}. 摂氏 → ケルビン")
        print(f"  {colored('4', Color.CYAN)}. ケルビン → 摂氏")
        print(f"  {colored('5', Color.CYAN)}. 華氏 → ケルビン")
        print(f"  {colored('6', Color.CYAN)}. ケルビン → 華氏")
        print(f"  {colored('7', Color.CYAN)}. 変換履歴を表示")
        print(f"  {colored('8', Color.CYAN)}. 変換結果をファイルに保存")
        print(f"  {colored('9', Color.CYAN)}. お気に入りに登録")
        print(f"  {colored('10', Color.CYAN)}. お気に入りを表示")
        print(f"  {colored('0', Color.RED)}. 終了")
        print()

        choice = input("選択 (0〜10): ").strip()

        if choice == "0":
            print(colored("終了します。", Color.YELLOW))
            break
        elif choice == "7":
            show_history(history)
            continue
        elif choice == "8":
            save_history(history)
            continue
        elif choice == "9":
            add_favorite()
            continue
        elif choice == "10":
            show_favorites()
            continue

        # 変換の種類: (入力単位名, 入力記号, 出力単位名, 出力記号, 変換関数)
        conversions = {
            "1": ("摂氏", "°C", "華氏", "°F", celsius_to_fahrenheit),
            "2": ("華氏", "°F", "摂氏", "°C", fahrenheit_to_celsius),
            "3": ("摂氏", "°C", "ケルビン", "K", celsius_to_kelvin),
            "4": ("ケルビン", "K", "摂氏", "°C", kelvin_to_celsius),
            "5": ("華氏", "°F", "ケルビン", "K", fahrenheit_to_kelvin),
            "6": ("ケルビン", "K", "華氏", "°F", kelvin_to_fahrenheit),
        }

        if choice in conversions:
            from_name, from_unit, to_name, to_unit, fn = conversions[choice]
            try:
                value = float(input(f"{from_name}の温度を入力してください ({from_unit}): "))
                result = fn(value)
                entry = f"{value:.2f}{from_unit} = {result:.2f}{to_unit}"
                result_str = (
                    f"{colored(f'{value:.2f}{from_unit}', Color.YELLOW)} = "
                    f"{colored(f'{result:.2f}{to_unit}', Color.GREEN, Color.BOLD)}"
                )
                print(f"\n{colored('結果:', Color.BOLD)} {result_str}")
                history.append(entry)
            except ValueError:
                print(colored("エラー: 数値を入力してください。", Color.RED))
        else:
            print(colored("エラー: 0〜10 の数字を入力してください。", Color.RED))

if __name__ == "__main__":
    main()
