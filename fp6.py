import flet as ft
import flet_audio as fta
import random
import asyncio
 
def main(page: ft.Page):
 
    page.title = "EL JUEGO DE CUBILETE"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "auto"
 
    turno_actual = 1
    botones_spin = {}
 
    def cambiar_turno():
        nonlocal turno_actual
        if turno_actual == 1:
            turno_actual = 2
        else:
            turno_actual = 1
        botones_spin[1].disabled = (turno_actual != 1)
        botones_spin[2].disabled = (turno_actual != 2)
 
    diceImages = ["images/Dice1.png","images/Dice2.png","images/Dice3.png","images/Dice4.png","images/Dice5.png","images/Dice6.png"]
    diceNames = {1: "8",2: "J",3: "Q",4: "K",5: "9",6: "As"}
    player_resets = []
 
    def calculatePoints(values):
        if values.count(1) == 5:
            return 5
        if values.count(4) == 5:
            return 3
        for number in range(2, 7):
            total = values.count(number) + values.count(1)
            if total == 5:  
                return 1
        return 0
 
    audio = fta.Audio(src="images/musica chill.mp3")
 
 
    songs = [{"src": "sound/song1.mp3", "title": "Bocanada"},
        {"src": "sound/song2.mp3", "title": "Subterranean Homesick Alien"},
        {"src": "sound/song3.mp3", "title": "Lurgee"},
        {"src": "sound/song4.mp3", "title": "TRUE LUST"},
        {"src": "sound/song5.mp3", "title": "Sweet boy"},]
    current_index = 0
 
    audio = fta.Audio(src=songs[current_index]["src"])
   
 
    async def playMusic(e):
        await audio.play()
 
    async def pauseMusic(e):
        await audio.pause()
 
    async def resumeMusic(e):
        await audio.resume()
 
    async def nextSong(e):
        nonlocal current_index
        await audio.pause()
        current_index = (current_index + 1) % len(songs)
        audio.src = songs[current_index]["src"]
        musicText.value = songs[current_index]["title"]
        page.update()
        await audio.play()
 
    async def prevSong(e):
        nonlocal current_index
        await audio.pause()
        current_index = (current_index - 1) % len(songs)
        audio.src = songs[current_index]["src"]
        musicText.value = songs[current_index]["title"]
        page.update()
        await audio.play()
 
    def volumeChange(e):
        audio.volume = volumeSlider.value / 100
 
 
    title = ft.Text("PROYECTO FINAL: JUEGO CUBILETE", size=35, weight=ft.FontWeight.BOLD)
    names = ft.Text("Hecho por Faisal, Daniel, Joaquin y Gabriel", size=18)
 
    musicText = ft.Text(songs[current_index]["title"], size=20, weight=ft.FontWeight.BOLD)
 
    playbutton = ft.ElevatedButton("Play", on_click=playMusic)
    pausebutton = ft.ElevatedButton("Pause", on_click=pauseMusic)
    resumebutton = ft.ElevatedButton("Resume", on_click=resumeMusic)
    prevbutton = ft.ElevatedButton("Anterior", on_click=prevSong)
    nextbutton = ft.ElevatedButton("Siguiente", on_click=nextSong)
    volumeSlider = ft.Slider(min=0, max=100, value=100, width=250, on_change=volumeChange)
   
 
    portada = ft.Column([title,names,musicText,ft.Row([prevbutton, playbutton, pausebutton, resumebutton, nextbutton,], alignment=ft.MainAxisAlignment.CENTER), ft.Text("Volumen"),volumeSlider],horizontal_alignment=ft.CrossAxisAlignment.CENTER, )
 
   
    def createPlayer(playerName, player_id):
        playerTitle = ft.Text(playerName, size=25, weight=ft.FontWeight.BOLD)
       
        initial_instruction = "activa y descativa los switches para decidir que dados se vuelven a tirar"
        resultText = ft.Text(initial_instruction, size=14, text_align=ft.TextAlign.CENTER)
       
        score = 0
        rollsLeft = 3
        needs_reset = False
       
        scoreText = ft.Text(f"Puntos: {score}/5")
        rollsText = ft.Text(f"Tiros restantes: {rollsLeft}")
 
        currentValues = [random.randint(1, 6) for _ in range(5)]
       
        diceControls = []
        switches = []
        diceImagesControls = []
 
        for i in range(5):
            diceImage = ft.Image(src=diceImages[currentValues[i] - 1], width=60, height=60)
            diceSwitch = ft.Switch(value=True, label="Girar")
 
            diceImagesControls.append(diceImage)
            switches.append(diceSwitch)
 
            diceBox = ft.Column([ft.Text(f"Dado {i + 1}", size=12, text_align=ft.TextAlign.CENTER), diceSwitch, diceImage],horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5)
            diceControls.append(diceBox)
 
        diceRow = ft.Row(diceControls, alignment=ft.MainAxisAlignment.CENTER, wrap=True)
 
        def spinDice(e):
            nonlocal score
            nonlocal rollsLeft
            nonlocal needs_reset
            if score >= 5:
                return
 
            resultText.value = f"{playerName} is spinning..."
            page.update()
 
            if needs_reset:
                for i in range(5):
                    switches[i].value = True
                needs_reset = False
           
            rollsLeft -= 1
 
           
            for i in range(5):
                if switches[i].value:
                    currentValues[i] = random.randint(1, 6)
                diceImagesControls[i].src = diceImages[currentValues[i] - 1]
           
            points = calculatePoints(currentValues)
           
            dados_texto = (f"{playerName} rolled: "
                f"{diceNames[currentValues[0]]}, "
                f"{diceNames[currentValues[1]]}, "
                f"{diceNames[currentValues[2]]}, "
                f"{diceNames[currentValues[3]]}, "
                f"{diceNames[currentValues[4]]}")
 
            if points > 0:
                 score += points
                 rollsLeft = 3
                 needs_reset = True
                 
                 if score >= 5:
                     resultText.value = f"{dados_texto}\n ¡{playerName} GANO ESTA RONDA!"
                 else:
                     resultText.value = f"{dados_texto}\n¡Consiguió {points} puntos, mantendra el turno!"
            else:
                 resultText.value = dados_texto
                 
           
                 if rollsLeft == 0:
                     resultText.value += "\nCambio de turno"
                     rollsLeft = 3
                     for i in range(5):
                         switches[i].value = True
                     cambiar_turno()
            scoreText.value = f"Puntos: {score}/5"
            rollsText.value = f"Tiros restantes: {rollsLeft}"
            page.update()
 
        spinButton = ft.ElevatedButton(f"Spin {playerName}", on_click=spinDice)
        botones_spin[player_id] = spinButton
 
        def reset_player_data():
            nonlocal score
            nonlocal rollsLeft
            nonlocal needs_reset
            nonlocal currentValues
            score = 0
            rollsLeft = 3
            needs_reset = False
            scoreText.value = f"Puntos: {score}/5"
            rollsText.value = f"Tiros restantes: {rollsLeft}"
            resultText.value = initial_instruction
            for i in range(5):
                switches[i].value = True
                currentValues[i] = random.randint(1, 6)
                diceImagesControls[i].src = diceImages[currentValues[i] - 1]
 
        player_resets.append(reset_player_data)
 
        playerBox = ft.Container(content=ft.Column([playerTitle, resultText, scoreText, rollsText, diceRow, spinButton],horizontal_alignment=ft.CrossAxisAlignment.CENTER),border=ft.border.all(2, "white"),border_radius=15,padding=20,margin=10,width=450)
        return playerBox
 
    player1 = createPlayer("Jugador 1", 1)
    player2 = createPlayer("Jugador 2", 2)
 
    game = ft.Column(
        [ft.Text("MODO PARA 2 JUGADORES", size=30, weight=ft.FontWeight.BOLD),ft.Row([player1, player2], alignment=ft.MainAxisAlignment.CENTER, wrap=True)],horizontal_alignment=ft.CrossAxisAlignment.CENTER,visible=False)
 
    def startGame(e):
        nonlocal turno_actual
        turno_actual = 1
        botones_spin[1].disabled = False
        botones_spin[2].disabled = True
       
        portada.visible = False
        startButton.visible = False
        game.visible = True
        restartButton.visible = True
        inicioButton.visible = True
        page.update()
 
    def restartGame(e):
        nonlocal turno_actual
        turno_actual = 1
        botones_spin[1].disabled = False
        botones_spin[2].disabled = True
       
        for reset_func in player_resets:
            reset_func()
        game.visible = False
        restartButton.visible = False
        portada.visible = True
        startButton.visible = True
        inicioButton.visible = False
    def iralinicio(e):
        game.visible = False
        restartButton.visible = False
        inicioButton.visible = False  
        portada.visible = True
        startButton.visible = True  
     
        page.update()
 
    startButton = ft.ElevatedButton("Empezar Juego", on_click=startGame, width=250)
    restartButton = ft.ElevatedButton("Reiniciar", on_click=restartGame, visible=False)
    inicioButton = ft.ElevatedButton("Home page", on_click=iralinicio, visible=False)
 
    page.add(portada,startButton,game,restartButton,inicioButton)
 
ft.run(main=main, assets_dir="assets")
