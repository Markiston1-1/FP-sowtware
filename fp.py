import flet as ft
import flet_audio as fta
import random
import time


def main(page: ft.Page):

    page.title = "Cubilete"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "auto"

    # =========================
    # IMAGENES
    # =========================
    diceImages = [
        "images/Dice1.png",
        "images/Dice2.png",
        "images/Dice3.png",
        "images/Dice4.png",
        "images/Dice5.png",
        "images/Dice6.png"
    ]

    # =========================
    # AUDIO
    # =========================
    audio = fta.Audio(src="audio/musica chill.mp3")
    page.services.append(audio)

    async def playMusic(e):
        await audio.play()

    async def pauseMusic(e):
        await audio.pause()

    async def resumeMusic(e):
        await audio.resume()

    def volumeChange(e):
        audio.volume = volumeSlider.value / 100

    # =========================
    # TITULOS
    # =========================
    title = ft.Text(
        "PROYECTO FINAL: CUBILETE ",
        size=35,
        weight=ft.FontWeight.BOLD
    )

    names = ft.Text(
        "Hecho por Faisal, Daniel, Joaquin y Gabriel",
        size=18
    )

    musicText = ft.Text(
        "Pon musica chill mientras juegas ",
        size=20
    )

    # =========================
    # BOTONES MUSICA
    # =========================
    playBtn = ft.ElevatedButton(
        "Play",
        on_click=playMusic
    )

    pauseBtn = ft.ElevatedButton(
        "Pause",
        on_click=pauseMusic
    )

    resumeBtn = ft.ElevatedButton(
        "Resume",
        on_click=resumeMusic
    )

    volumeSlider = ft.Slider(
        min=0,
        max=100,
        value=100,
        width=250,
        on_change=volumeChange
    )

    # =========================
    # PORTADA
    # =========================
    portada = ft.Column(
        [
            title,
            names,
            musicText,

            ft.Row(
                [
                    playBtn,
                    pauseBtn,
                    resumeBtn
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),

            ft.Text("Volume"),

            volumeSlider
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # =========================
    # FUNCION PARA CREAR JUGADOR
    # =========================
    def createPlayer(playerName):

        playerTitle = ft.Text(
            playerName,
            size=25,
            weight=ft.FontWeight.BOLD
        )

        resultText = ft.Text(
            "Click spin to roll dice",
            size=16
        )

        # =========================
        # CREAR 6 DADOS
        # =========================
        dice1 = ft.Image(src="images/generic.jpg", width=60, height=60)
        dice2 = ft.Image(src="images/generic.jpg", width=60, height=60)
        dice3 = ft.Image(src="images/generic.jpg", width=60, height=60)
        dice4 = ft.Image(src="images/generic.jpg", width=60, height=60)
        dice5 = ft.Image(src="images/generic.jpg", width=60, height=60)
        dice6 = ft.Image(src="images/generic.jpg", width=60, height=60)

        diceRow = ft.Row(
            [
                dice1,
                dice2,
                dice3,
                dice4,
                dice5,
                dice6
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            wrap=True
        )

        # =========================
        # SPIN
        # =========================
        def spinDice(e):

            resultText.value = f"{playerName} is spinning..."
            page.update()

            time.sleep(1.5)

            n1 = random.randint(1, 6)
            n2 = random.randint(1, 6)
            n3 = random.randint(1, 6)
            n4 = random.randint(1, 6)
            n5 = random.randint(1, 6)
            n6 = random.randint(1, 6)

            dice1.src = diceImages[n1 - 1]
            dice2.src = diceImages[n2 - 1]
            dice3.src = diceImages[n3 - 1]
            dice4.src = diceImages[n4 - 1]
            dice5.src = diceImages[n5 - 1]
            dice6.src = diceImages[n6 - 1]

            resultText.value = (
                f"{playerName} rolled: "
                f"{n1}, {n2}, {n3}, {n4}, {n5}, {n6}"
            )

            page.update()

        spinButton = ft.ElevatedButton(
            f"Spin {playerName}",
            on_click=spinDice
        )

        # =========================
        # PANEL JUGADOR
        # =========================
        playerBox = ft.Container(
            content=ft.Column(
                [
                    playerTitle,
                    resultText,
                    diceRow,
                    spinButton
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),

            border=ft.border.all(2, "white"),
            border_radius=15,
            padding=20,
            margin=10,
            width=450
        )

        return playerBox

    # =========================
    # DOS JUGADORES
    # =========================
    player1 = createPlayer("Jugador 1")
    player2 = createPlayer("Jugador 2")

    game = ft.Column(
        [
            ft.Text(
                "🎮 MODO 2 JUGADORES 🎮",
                size=30,
                weight=ft.FontWeight.BOLD
            ),

            ft.Row(
                [
                    player1,
                    player2
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                wrap=True
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        visible=False
    )

    # =========================
    # START
    # =========================
    def startGame(e):

        portada.visible = False
        startButton.visible = False

        game.visible = True
        restartButton.visible = True

        page.update()

    # =========================
    # RESTART
    # =========================
    def restartGame(e):

        game.visible = False
        restartButton.visible = False

        portada.visible = True
        startButton.visible = True

        page.update()

    startButton = ft.ElevatedButton(
        "Empezar Juego",
        on_click=startGame
    )

    restartButton = ft.ElevatedButton(
        "Reiniciar",
        on_click=restartGame,
        visible=False
    )

    # =========================
    # AGREGAR TODO
    # =========================
    page.add(
        portada,
        startButton,
        game,
        restartButton
    )


ft.run(main=main, assets_dir="assets")
