import flet as ft
import flet_audio as fta
import random
import asyncio


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
    # NOMBRES DE LOS DADOS
    # =========================
    diceNames = {
        1: "8",
        2: "J",
        3: "Q",
        4: "K",
        5: "9",
        6: "As"
    }

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
        "PROYECTO FINAL: CUBILETE",
        size=35,
        weight=ft.FontWeight.BOLD
    )

    names = ft.Text(
        "Hecho por Faisal, Daniel, Joaquin y Gabriel",
        size=18
    )

    musicText = ft.Text(
        "Pon musica chill mientras juegas",
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
            "Activa o desactiva los switches para elegir qué dados se vuelven a girar",
            size=14,
            text_align=ft.TextAlign.CENTER
        )

        # =========================
        # VALORES INICIALES
        # =========================
        currentValues = [random.randint(1, 6) for _ in range(6)]

        diceControls = []
        switches = []
        diceImagesControls = []

        # =========================
        # CREAR 6 DADOS CON SWITCH
        # =========================
        for i in range(6):
            diceImage = ft.Image(
                src=diceImages[currentValues[i] - 1],
                width=60,
                height=60
            )

            diceSwitch = ft.Switch(
                value=True,
                label="Girar"
            )

            diceImagesControls.append(diceImage)
            switches.append(diceSwitch)

            diceBox = ft.Column(
                [
                    ft.Text(
                        f"Dado {i + 1}",
                        size=12,
                        text_align=ft.TextAlign.CENTER
                    ),
                    diceSwitch,
                    diceImage
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5
            )

            diceControls.append(diceBox)

        diceRow = ft.Row(
            diceControls,
            alignment=ft.MainAxisAlignment.CENTER,
            wrap=True
        )

        # =========================
        # SPIN
        # =========================
        async def spinDice(e):
            resultText.value = f"{playerName} is spinning..."
            page.update()

            await asyncio.sleep(1.5)

            for i in range(6):
                if switches[i].value:
                    currentValues[i] = random.randint(1, 6)

                diceImagesControls[i].src = diceImages[currentValues[i] - 1]

            resultText.value = (
                f"{playerName} rolled: "
                f"{diceNames[currentValues[0]]}, "
                f"{diceNames[currentValues[1]]}, "
                f"{diceNames[currentValues[2]]}, "
                f"{diceNames[currentValues[3]]}, "
                f"{diceNames[currentValues[4]]}, "
                f"{diceNames[currentValues[5]]}"
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