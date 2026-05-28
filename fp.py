import flet as ft
import random

CELL = 40
BOARD = 15

RED = "#ff3b30"
BLUE = "#007aff"
GREEN = "#34c759"
YELLOW = "#ffd60a"

WHITE = "#ffffff"
GRAY = "#d1d1d1"
BLACK = "#000000"


def main(page: ft.Page):

    page.title = "Parchís"
    page.window_width = 900
    page.window_height = 950
    page.bgcolor = "#f2f2f2"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    board = ft.Stack(
        width=CELL * BOARD,
        height=CELL * BOARD,
    )

    # =========================
    # FUNCION COLOR CASILLA
    # =========================

    def get_color(r, c):

        color = WHITE

        # CASAS GRANDES
        if r < 6 and c < 6:
            color = RED

        elif r < 6 and c > 8:
            color = BLUE

        elif r > 8 and c < 6:
            color = GREEN

        elif r > 8 and c > 8:
            color = YELLOW

        # CUADROS QUE MARCASTE
        # ahora son grises
        if (r, c) in [(5, 5), (5, 9), (9, 5), (9, 9)]:
            color = GRAY

        # ZONAS BLANCAS CERCA DEL CENTRO
        if 6 <= r <= 8 and 0 <= c <= 5:
            color = WHITE

        if 6 <= r <= 8 and 9 <= c <= 14:
            color = WHITE

        if 0 <= r <= 5 and 6 <= c <= 8:
            color = WHITE

        if 9 <= r <= 14 and 6 <= c <= 8:
            color = WHITE

        # CAMINOS GRISES
        if r == 6 or r == 8 or c == 6 or c == 8:
            color = GRAY

        # CAMINO CENTRAL
        if c == 7 and r < 7:
            color = RED

        if c == 7 and r > 7:
            color = GREEN

        if r == 7 and c < 7:
            color = YELLOW

        if r == 7 and c > 7:
            color = BLUE

        # LUGARES SEGUROS
        safe_spots = [
            (2, 6),
            (6, 12),
            (12, 8),
            (8, 2),
            (6, 2),
            (2, 8),
            (8, 12),
            (12, 6),
        ]

        if (r, c) in safe_spots:
            color = "#9e9e9e"

        # CENTRO
        if 6 <= r <= 8 and 6 <= c <= 8:
            color = WHITE

        return color

    # =========================
    # DIBUJAR TABLERO
    # =========================

    for r in range(BOARD):
        for c in range(BOARD):

            square = ft.Container(
                width=CELL,
                height=CELL,
                bgcolor=get_color(r, c),
                border=ft.border.all(1, BLACK),
                left=c * CELL,
                top=r * CELL,
            )

            board.controls.append(square)

    # =========================
    # CENTRO
    # =========================

    center = ft.Container(
        width=CELL * 3,
        height=CELL * 3,
        left=6 * CELL,
        top=6 * CELL,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(bgcolor=RED, expand=True),
                        ft.Container(bgcolor=BLUE, expand=True),
                    ],
                    spacing=0,
                    expand=True,
                ),
                ft.Row(
                    [
                        ft.Container(bgcolor=GREEN, expand=True),
                        ft.Container(bgcolor=YELLOW, expand=True),
                    ],
                    spacing=0,
                    expand=True,
                ),
            ],
            spacing=0,
            expand=True,
        ),
    )

    board.controls.append(center)

    # =========================
    # FICHAS
    # =========================

    pieces = [

        # ROJAS
        (1, 1, RED),
        (1, 3, RED),
        (3, 1, RED),
        (3, 3, RED),

        # AZULES
        (1, 11, BLUE),
        (1, 13, BLUE),
        (3, 11, BLUE),
        (3, 13, BLUE),

        # VERDES
        (11, 1, GREEN),
        (11, 3, GREEN),
        (13, 1, GREEN),
        (13, 3, GREEN),

        # AMARILLAS
        (11, 11, YELLOW),
        (11, 13, YELLOW),
        (13, 11, YELLOW),
        (13, 13, YELLOW),
    ]

    def move_piece(e):

        piece = e.control

        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])

        new_left = piece.left + (dx * CELL)
        new_top = piece.top + (dy * CELL)

        if 0 <= new_left <= CELL * 14:
            piece.left = new_left

        if 0 <= new_top <= CELL * 14:
            piece.top = new_top

        page.update()

    for row, col, color in pieces:

        piece = ft.Container(
            width=28,
            height=28,
            bgcolor=color,
            border_radius=50,
            border=ft.border.all(2, BLACK),
            left=col * CELL + 6,
            top=row * CELL + 6,
            on_click=move_piece,
            shadow=ft.BoxShadow(
                blur_radius=8,
                color="#00000044",
                offset=ft.Offset(2, 2),
            ),
        )

        board.controls.append(piece)

    # =========================
    # DADO
    # =========================

    dice_text = ft.Text(
        "🎲 1",
        size=30,
        weight=ft.FontWeight.BOLD,
    )

    def roll_dice(e):

        value = random.randint(1, 6)

        dice_text.value = f"🎲 {value}"

        page.update()

    # =========================
    # INTERFAZ
    # =========================

    page.add(
        ft.Column(
            [
                ft.Text(
                    "PARCHÍS",
                    size=40,
                    weight=ft.FontWeight.BOLD,
                ),

                board,

                ft.Row(
                    [
                        dice_text,

                        ft.ElevatedButton(
                            "Tirar dado",
                            on_click=roll_dice,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.app(target=main)
