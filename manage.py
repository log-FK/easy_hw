from modules.app import app
from modules.window import window
def main():
    try:
        window.show()
        app.exec()
    except Exception as eror:
        print(eror)
if __name__ == "__main__":
    main()