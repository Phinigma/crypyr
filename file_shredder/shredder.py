import os
import random
from PyQt5.QtWidgets import QMessageBox

class FileShredder:
    def __init__(self):
        pass

    def shred_file(self, file_path, passes=3):
        """Securely delete a file by overwriting it multiple times"""
        try:
            # Show SSD warning before proceeding
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setWindowTitle("SSD Warning")
            warning.setText("Warning: Secure file deletion is not fully reliable on SSDs due to data remapping. Proceed only if you're aware of the limitations.")
            warning.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            response = warning.exec_()

            if response == QMessageBox.Cancel:
                return False  # Exit the function if the user cancels

            # Proceed with shredding
            with open(file_path, 'ba+', buffering=0) as f:
                length = f.tell()
                for _ in range(passes):
                    f.seek(0)
                    f.write(bytearray(random.getrandbits(8) for _ in range(length)))
            os.remove(file_path)
            return True
        except Exception as e:
            print(f"Error shredding file: {e}")
            return False
