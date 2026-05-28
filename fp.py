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
        number3 = random.randint(1,6)
        number4 = random.randint(1,6)
        number5 = random.randint(1,6)

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

        if number3 == 1:
            diceImage3.src = imageList[number3 - 1]
        elif number3 == 2:
            diceImage3.src = imageList[number3 - 1]
        elif number3 == 3:
            diceImage3.src = imageList[number3 - 1]
        elif number3 == 4:
            diceImage3.src = imageList[number3 - 1]
        elif number3 == 5:
            diceImage3.src = imageList[number3 - 1]
        elif number3 == 6:
            diceImage3.src = imageList[number3 - 1]

        if number4 == 1:
            diceImage4.src = imageList[number4 - 1]
        elif number4 == 2:
            diceImage4.src = imageList[number4 - 1]
        elif number4 == 3:
            diceImage4.src = imageList[number4 - 1]
        elif number4 == 4:
            diceImage4.src = imageList[number4 - 1]
        elif number4 == 5:
            diceImage4.src = imageList[number4 - 1]
        elif number4 == 6:
            diceImage4.src = imageList[number4 - 1]

        if number5 == 1:
            diceImage5.src = imageList[number5 - 1]
        elif number5 == 2:
            diceImage5.src = imageList[number5 - 1]
        elif number5 == 3:
            diceImage5.src = imageList[number5 - 1]
        elif number5 == 4:
            diceImage5.src = imageList[number5 - 1]
        elif number5 == 5:
            diceImage5.src = imageList[number5 - 1]
        elif number5 == 6:
            diceImage5.src = imageList[number5 - 1]

        instructionsText.value = f"You spined the numbers {number1}, {number2}, {number3}, {number4} and {number5}"

        page.update()

    #Page Setup
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Controls del dado
    instructionsText = ft.Text(value="Click the buttom to roll the dice")

    diceImage = ft.Image(src="images/generic.jpg",width=200,height=200)

    diceImage2 = ft.Image(src="images/generic.jpg",width=200,height=200)

    diceImage3 = ft.Image(src="images/generic.jpg",width=200,height=200)

    diceImage4 = ft.Image(src="images/generic.jpg",width=200,height=200)

    diceImage5 = ft.Image(src="images/generic.jpg",width=200,height=200)

    spinButton = ft.Button(content=ft.Text("Spin Dice"),height=50,width=130,style=ft.ButtonStyle(text_style=ft.TextStyle(size=15)),on_click=ChangeImage)

    page.add(instructionsText,ft.Row(controls=[diceImage,diceImage2,diceImage3,diceImage4,diceImage5],alignment=ft.MainAxisAlignment.CENTER),spinButton,)

ft.run(main=main, assets_dir="assets")