from display import colored, Color

def save_history(history):
    """変換履歴をresults.txtに上書き保存する"""
    file_name = "results.txt"
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            if not history:
                f.write("変換履歴がありません。\n")
            else:
                for i, entry in enumerate(history, 1):
                    f.write(f"{i}. {entry}\n")
        print(colored(f"履歴を「{file_name}」に保存しました。", Color.GREEN))
    except OSError as e:
        print(colored(f"ファイルの保存に失敗しました: {e}", Color.RED))

def show_history(history):
    """変換履歴を表示する"""
    if not history:
        print("\n" + colored("履歴はまだありません。", Color.YELLOW))
        return
    print("\n" + colored("=" * 40, Color.BLUE))
    print(colored("      変換履歴", Color.BOLD, Color.BLUE))
    print(colored("=" * 40, Color.BLUE))
    for i, entry in enumerate(history, 1):
        print(f"  {colored(i, Color.CYAN)}. {entry}")
    print(colored("=" * 40, Color.BLUE))
