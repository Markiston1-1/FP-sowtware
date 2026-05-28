Lolito67
manguconhuevo_
Invisible

Helado de chocolate (Frio) [GMBL],  — 8:04 PM
faisal q tu vas a hacer
osea cual es tu parte
Lolito67 [V5RC],  — 8:12 PM
yo voy hacer lo del moviemiento y todo eso
no se porquer dialer gabriel se queja
el hizo algo pila de simple
el solo pocisiono todo
Markiston — 8:13 PM
compai yo hize el dado y me faltasn mas fichas
Lolito67 [V5RC],  — 8:13 PM
todo eso e pila de facil
acabod e ver el codigo
Markiston — 8:13 PM
yo tuve quer cambiar el codigo del dado
para que sean dos
y que se spineen diferente
Lolito67 [V5RC],  — 8:14 PM
tt pero sigue siendo facil puede que te haya tomado tiempo
Markiston — 8:14 PM
se estaban spineando lso dos la misma cosa
Lolito67 [V5RC],  — 8:14 PM
aun asi no quita el hehco que todos aun tiene que ayudar
daniel
a tu las reglas con joaquin
toy tratando ede arreglar el lio de github ya que todos no tenemso el mismo locationq ue gabriel
 [V5RC], 
Helado de chocolate (Frio) [GMBL],  — 8:16 PM
q reglas
yo no me se las reglas del juego porq yo nunca lo juge
como 3
veces
Lolito67 [V5RC],  — 8:17 PM
tt busca un video es facil el juego
almeno de explica
loco nama diciendo tu parte y la de joaquin son las mas dificil
Adrian — 8:35 PM
Boy
 [MEME], 
Lolito67 [V5RC],  — 8:41 PM
aun asi no quita el hehco que todos aun tiene que ayudar
Lolito67
 inició una llamada. — 8:41 PM
Clouty [Poet],  — 8:55 PM
Imagen
Clouty [Poet],  — 8:56 PM
Imagen
Clouty [Poet],  — 8:58 PM
Imagen
Adrian — 8:59 PM
Imagen
Helado de chocolate (Frio) [GMBL],  — 9:02 PM
tuff anime pfp
Imagen
Adrian — 9:05 PM
Imagen
Jason — 9:23 PM
@G00dD4Y!
Imagen
y ahora van a saca otra
Imagen
Imagen
Adrian — 9:28 PM
eso ta tuff
Helado de chocolate (Frio) [GMBL],  — 9:35 PM
nesesito eso
Imagen
Adrian — 9:41 PM
Imagen
Lolito67 [V5RC],  — 9:52 PM
import flet as ft
import random

CELL = 40
BOARD = 15

message.txt
6 KB
﻿
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

    def get_color(r, c):

        color = WHITE

        if r < 6 and c < 6:
            color = RED

        elif r < 6 and c > 8:
            color = BLUE

        elif r > 8 and c < 6:
            color = GREEN

        elif r > 8 and c > 8:
            color = YELLOW

        if (r, c) in [(5, 5), (5, 9), (9, 5), (9, 9)]:
            color = GRAY

        if 6 <= r <= 8 and 0 <= c <= 5:
            color = WHITE

        if 6 <= r <= 8 and 9 <= c <= 14:
            color = WHITE

        if 0 <= r <= 5 and 6 <= c <= 8:
            color = WHITE

        if 9 <= r <= 14 and 6 <= c <= 8:
            color = WHITE

        if r == 6 or r == 8 or c == 6 or c == 8:
            color = GRAY

        if c == 7 and r < 7:
            color = RED

        if c == 7 and r > 7:
            color = GREEN

        if r == 7 and c < 7:
            color = YELLOW

        if r == 7 and c > 7:
            color = BLUE

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

        if 6 <= r <= 8 and 6 <= c <= 8:
            color = WHITE

        return color

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

    pieces = [

        (1, 1, RED),
        (1, 3, RED),
        (3, 1, RED),
        (3, 3, RED),

        (1, 11, BLUE),
        (1, 13, BLUE),
        (3, 11, BLUE),
        (3, 13, BLUE),

        (11, 1, GREEN),
        (11, 3, GREEN),
        (13, 1, GREEN),
        (13, 3, GREEN),

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

    dice_text = ft.Text(
        "🎲 1",
        size=30,
        weight=ft.FontWeight.BOLD,
    )

    def roll_dice(e):

        value = random.randint(1, 6)

        dice_text.value = f"🎲 {value}"

        page.update()

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
