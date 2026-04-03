import os
import tempfile
import unittest
from unittest.mock import patch

# save_history が書き込むファイル名を差し替えるためにパッチを使用
from history import save_history


class TestSaveHistory(unittest.TestCase):
    """save_history() のテスト"""

    def _read_saved_file(self, file_path):
        """保存されたファイルの内容を読み取る"""
        with open(file_path, encoding="utf-8") as f:
            return f.read()

    def test_履歴ありの場合に番号付きで書き込まれる(self):
        """変換履歴がある場合、番号付きで各エントリが保存される"""
        history = ["0.00°C = 32.00°F", "100.00°C = 212.00°F"]
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, "results.txt")
            with patch("history.open", unittest.mock.mock_open()) as mock_file:
                # 実ファイルに書き込むためパッチせず、tmpファイルを使う
                pass

        # 実際のファイルI/Oを使ったテスト
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".txt", delete=False, encoding="utf-8"
        ) as tmp:
            tmp_path = tmp.name

        try:
            # save_history が使うファイル名をtmpに差し替える
            with patch("history.open", side_effect=lambda name, mode, **kw: open(tmp_path, mode, **kw)):
                save_history(history)
            content = self._read_saved_file(tmp_path)
            self.assertIn("1. 0.00°C = 32.00°F", content)
            self.assertIn("2. 100.00°C = 212.00°F", content)
        finally:
            os.unlink(tmp_path)

    def test_履歴なしの場合にメッセージが書き込まれる(self):
        """変換履歴が空の場合、「変換履歴がありません。」が保存される"""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".txt", delete=False, encoding="utf-8"
        ) as tmp:
            tmp_path = tmp.name

        try:
            with patch("history.open", side_effect=lambda name, mode, **kw: open(tmp_path, mode, **kw)):
                save_history([])
            content = self._read_saved_file(tmp_path)
            self.assertIn("変換履歴がありません。", content)
        finally:
            os.unlink(tmp_path)

    def test_上書き保存されること(self):
        """2回保存した場合、2回目の内容のみが残る（追記ではなく上書き）"""
        first_history = ["0.00°C = 32.00°F"]
        second_history = ["100.00°C = 212.00°F", "-40.00°C = -40.00°F"]

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".txt", delete=False, encoding="utf-8"
        ) as tmp:
            tmp_path = tmp.name

        try:
            with patch("history.open", side_effect=lambda name, mode, **kw: open(tmp_path, mode, **kw)):
                save_history(first_history)
                save_history(second_history)
            content = self._read_saved_file(tmp_path)
            # 1回目の内容が残っていないことを確認
            self.assertNotIn("0.00°C = 32.00°F", content)
            # 2回目の内容のみ残っていることを確認
            self.assertIn("1. 100.00°C = 212.00°F", content)
            self.assertIn("2. -40.00°C = -40.00°F", content)
        finally:
            os.unlink(tmp_path)


if __name__ == "__main__":
    unittest.main()
