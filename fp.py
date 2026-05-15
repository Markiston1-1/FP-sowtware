import flet as ft
import random

def main(page: ft.Page):

    #DADO
    def ChangeImage(e):

        imageList = ["images/Dice1.png",
                     "images/Dice2.png",
                     "images/Dice3.png",
                     "images/Dice4.png",
                     "images/Dice5.png",
                     "images/Dice6.png"]

        number1 = random.randint(1,6)
        number2 = random.randint(1,6)

        if number1 == 1:
            diceImage.src = imageList[number1 - 1]
        elif number1 == 2:
            diceImage.src = imageList[number1 - 1]
        elif number1 == 3:
            diceImage.src = imageList[number1 - 1]
        elif number1 == 4:
            diceImage.src = imageList[number1 - 1]
        elif number1 == 5:
            diceImage.src = imageList[number1 - 1]
        elif number1 == 6:
            diceImage.src = imageList[number1 - 1]

        if number2 == 1:
            diceImage2.src = imageList[number2 - 1]
        elif number2 == 2:
            diceImage2.src = imageList[number2 - 1]
        elif number2 == 3:
            diceImage2.src = imageList[number2 - 1]
        elif number2 == 4:
            diceImage2.src = imageList[number2 - 1]
        elif number2 == 5:
            diceImage2.src = imageList[number2 - 1]
        elif number2 == 6:
            diceImage2.src = imageList[number2 - 1]

        instructionsText.value = f"You spined the numbers {number1} and {number2}"

        page.update()

    #Page Setup
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    #Controls del Dice
    instructionsText = ft.Text(value="Click the buttom to roll the dice")

    diceImage = ft.Image(src="images/generic.png",width=100,height=100)

    diceImage2 = ft.Image(src="images/generic.png",width=100,height=100)

    spinButton = ft.Button(content="Spin Dice",height=30,width=100,style=ft.ButtonStyle(text_style=ft.TextStyle(size=10)),on_click=ChangeImage)

    page.add(instructionsText,ft.Row(controls=[diceImage, diceImage2],alignment=ft.MainAxisAlignment.CENTER),spinButton,)

ft.run(main=main, assets_dir="assets")