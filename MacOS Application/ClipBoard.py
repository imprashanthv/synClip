import pyperclip
class ClipBoard:
    def __init__(self):
        self.current_content = ""

    def run(self):
        while True:
            try:
                self.current_content = pyperclip.waitForNewPaste()
                print(self.current_content)
            except KeyboardInterrupt:
                print("Application stopped")