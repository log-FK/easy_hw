from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtCore import Qt
from .app import app

window = QWidget()

WIDTH_WINDOW = 1024
HEIGHT_WINDOW = 800

size = app.primaryScreen().size()

window.setGeometry(
    (size.width() // 2) - (WIDTH_WINDOW // 2),
    (size.height() // 2) - (HEIGHT_WINDOW // 2),
    WIDTH_WINDOW,
    HEIGHT_WINDOW
)

main_layout = QHBoxLayout(window)

bg = QFrame()
bg.setStyleSheet("background-color: #808080")
main_layout.addWidget(bg)

layout = QVBoxLayout(bg)
layout.setSpacing(16)

grid = QGridLayout()
grid.setSpacing(16)
layout.addLayout(grid)

RED = "#fb1b28"
GREEN = "#00a43a"
BLUE = "#0088ee"


def square(color):
    sq = QFrame()
    sq.setStyleSheet(
        f"background-color: {color}; "
        "min-width: 60px; max-width: 60px; "
        "min-height: 60px; max-height: 60px;"
    )
    return sq


def squares_card(color, row, col):
    # карточка с двумя квадратами
    card = QFrame()
    card.setStyleSheet(f"background-color: {color}")
    card_layout = QHBoxLayout(card)

    card_layout.addWidget(square("white"))
    card_layout.addWidget(square("#d8ccc9"))

    grid.addWidget(card, row, col)


def empty_card(color, row, col):
    # пустая карточка
    card = QFrame()
    card.setStyleSheet(f"background-color: {color}")
    grid.addWidget(card, row, col)


def labels_card(color, row, col):
    # карточка с двумя лейблами по центру
    card = QFrame()
    card.setStyleSheet(f"background-color: {color}")
    card_layout = QVBoxLayout(card)

    label1 = QLabel("Лейбл 1")
    label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label1.setStyleSheet("color: black; background: transparent;")
    card_layout.addWidget(label1)

    label2 = QLabel("Лейбл 2")
    label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label2.setStyleSheet("color: black; background: transparent;")
    card_layout.addWidget(label2)

    grid.addWidget(card, row, col)


# верхний ряд (красный)
squares_card(RED, 0, 0)
empty_card(RED, 0, 1)
squares_card(RED, 0, 2)

# средний ряд (зелёный)
labels_card(GREEN, 1, 0)
labels_card(GREEN, 1, 1)
labels_card(GREEN, 1, 2)

# нижний ряд (синий)
squares_card(BLUE, 2, 0)
empty_card(BLUE, 2, 1)
squares_card(BLUE, 2, 2)