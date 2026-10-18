from PyQt6.QtWidgets import QFrame, QLabel
from PyQt6.QtCore import Qt
from .app import app

window = QFrame()
window.setWindowTitle("Weather app")

size = app.primaryScreen().size()
window.setGeometry(size.width() // 2 - 512, size.height() // 2 - 400, 1024, 800)

bg = QFrame(window)
bg.setStyleSheet("background-color: #808080")
bg.setGeometry(0, 0, 1024, 800)

colors = ["#fb1b28", "#00a43a", "#0088ee"]

# 9 цветных прямоугольников
boxes = []
for row in range(3):
    for col in range(3):
        box = QFrame(bg)
        box.setStyleSheet(f"background-color: {colors[row]}")
        box.setGeometry(16 + col * 336, 16 + row * 261, 320, 245)
        boxes.append(box)

# квадраты: ряды 0 и 2, колонки 0 и 2
for row in (0, 2):
    for col in (0, 2):
        box = boxes[row * 3 + col]

        sq1 = QFrame(box)
        sq1.setStyleSheet("background-color: white")
        sq1.setGeometry(70, 92, 60, 60)

        sq2 = QFrame(box)
        sq2.setStyleSheet("background-color: #d8ccc9")
        sq2.setGeometry(190, 92, 60, 60)

# лейблы: ряд 1, все колонки
for col in range(3):
    box = boxes[3 + col]

    label1 = QLabel("Лейбл 1", box)
    label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label1.setStyleSheet("color: black; background: transparent;")
    label1.setGeometry(0, 98, 320, 24)

    label2 = QLabel("Лейбл 2", box)
    label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label2.setStyleSheet("color: black; background: transparent;")
    label2.setGeometry(0, 122, 320, 24)