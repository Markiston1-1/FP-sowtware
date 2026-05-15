import flet as ft
import random

def main(page: ft.Page):
    #DADO
    def ChangeImage(e):
        imageList =["images/Dice1.png",
                    "images/Dice2.png",
                    "images/Dice3.png",
                    "images/Dice4.png",
                    "images/Dice5.png",
                    "images/Dice6.png"]
        number = random.randint(1,6)
        if number == 1:
            instructionsText.value = f"You spined the number {number}"
            diceImage.src = imageList[number - 1]
        elif number == 2:
            instructionsText.value = f"You spined the number {number}"
            diceImage.src = imageList[number - 1]
        elif number == 3:
            instructionsText.value = f"You spined the number {number}"
            diceImage.src = imageList[number - 1]
        elif number == 4:
            instructionsText.value = f"You spined the number {number}"
            diceImage.src = imageList[number - 1]
        elif number == 5:
            instructionsText.value = f"You spined the number {number}"
            diceImage.src = imageList[number - 1]
        elif number == 6:
            instructionsText.value = f"You spined the number {number}"
            diceImage.src = imageList[number - 1]

    

    #Page Setup
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    #Controls
    instructionsText = ft.Text(value="Click the buttom to roll the dice")
    diceImage = ft.Image(src="images/generic.png",width=100,height=100)
    spinButton = ft.Button(content="Spin Dice", height=30, width=100, style=ft.ButtonStyle(text_style=ft.TextStyle(size=10)),on_click=ChangeImage)
    
    page.add(instructionsText,diceImage, spinButton)

ft.run(main=main,assets_dir="assets")