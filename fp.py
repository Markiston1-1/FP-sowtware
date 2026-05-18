import flet as ft
import random

def main(page: ft.Page):

    # tirar dados
    def ChangeImage(e):

        imageList = [
            "images/Dice1.png",
            "images/Dice2.png",
            "images/Dice3.png",
            "images/Dice4.png",
            "images/Dice5.png",
            "images/Dice6.png"]

        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)

        diceImage.src = imageList[number1 - 1]
        diceImage2.src = imageList[number2 - 1]

        instructionsText.value = f"You rolled {number1} and {number2}"

        page.update()

    # page
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "auto"

    # texto
    instructionsText = ft.Text("Click the button to roll the dice",size=20)

    # dados
    diceImage = ft.Image(src="images/generic.png",width=100,height=100)

    diceImage2 = ft.Image(src="images/generic.png",width=100,height=100)

    # boton
    spinButton = ft.ElevatedButton(content=ft.Text("Spin Dice"),on_click=ChangeImage)

    # tablero
    board = ft.Image(src="images/tabla.png",width=600,height=600,fit=ft.BoxFit.CONTAIN)

    # tablero + fichas
    gameBoard = ft.Stack(
        width=600,
        height=600,
        controls=[board,

            # rojas
            ft.Container(content=ft.Image("images/ficharoja.png", width=35, height=35),left=70,top=70),

            ft.Container(content=ft.Image("images/ficharoja.png", width=35, height=35),left=120,top=70),

            ft.Container(content=ft.Image("images/ficharoja.png", width=35, height=35),left=70,top=120),

            ft.Container(content=ft.Image("images/ficharoja.png", width=35, height=35),left=120,top=120),

            # azules
            ft.Container(content=ft.Image("images/fichaazul.png", width=35, height=35),left=440,top=70),

            ft.Container(content=ft.Image("images/fichaazul.png", width=35, height=35),left=490,top=70),

            ft.Container(content=ft.Image("images/fichaazul.png", width=35, height=35),left=440,top=120),

            ft.Container(content=ft.Image("images/fichaazul.png", width=35, height=35),left=490,top=120),

            # verdes
            ft.Container(content=ft.Image("images/fichaverde.png", width=35, height=35),left=70,top=440),

            ft.Container(content=ft.Image("images/fichaverde.png", width=35, height=35),left=120,top=440),

            ft.Container(content=ft.Image("images/fichaverde.png", width=35, height=35),left=70,top=490),

            ft.Container(content=ft.Image("images/fichaverde.png", width=35, height=35),left=120,top=490),

            # amarillas
            ft.Container(content=ft.Image("images/fichaamarilla.png", width=35, height=35),left=440,top=440),

            ft.Container(content=ft.Image("images/fichaamarilla.png", width=35, height=35),left=490,top=440),

            ft.Container(content=ft.Image("images/fichaamarilla.png", width=35, height=35),left=440,top=490),

            ft.Container(content=ft.Image("images/fichaamarilla.png", width=35, height=35),left=490,top=490),])

    page.add(instructionsText,ft.Row([diceImage, diceImage2],alignment=ft.MainAxisAlignment.CENTER),spinButton,gameBoard)

ft.run(main=main, assets_dir="assets")