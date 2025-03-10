import flet as ft
def main(page: ft.Page):
    x = 1
    songon = False
    def chooseAudio():
        nonlocal x, songon
        if x == 0:
            x = 5
        elif x == 6:
            x = 1
        if x == 1:
            audio1.play()
            cursong.value = "Everlong - Foo Fighters" #Best song
            img.src = "https://i1.sndcdn.com/artworks-pewMD4eo1wHAArvs-SEQCIQ-t500x500.jpg"
            songon = True
            playpause.text = "| |"
        elif x == 2:
            audio2.play()
            cursong.value = "Iris - Goo Goo Dolls"
            img.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxjmtBZpGBC7absKUwzAyx3JOZPHE27EpfoA&s"
            songon = True
            playpause.text = "| |"
        elif x == 3:
            audio3.play()
            cursong.value = "Drain You - Nirvana"
            img.src = "https://upload.wikimedia.org/wikipedia/en/b/b7/NirvanaNevermindalbumcover.jpg"
            songon = True
            playpause.text = "| |"
        elif x == 4:
            audio4.play()
            cursong.value = "Creep - Radiohead"
            img.src = "https://upload.wikimedia.org/wikipedia/en/0/0f/Radiohead.pablohoney.albumart.jpg"
            songon = True
            playpause.text = "| |"
        elif x == 5:
            audio5.play()
            cursong.value = "You're all I want - Cigarettes After Sex"
            img.src = "https://f4.bcbits.com/img/a3109576526_65"
            songon = True
            playpause.text = "| |"
        page.update()

    def nextSong(e):
        nonlocal x, songon
        if songon:
            if x == 1:
                audio1.pause()
            elif x == 2:
                audio2.pause()
            elif x == 3:
                audio3.pause()
            elif x == 4:
                audio4.pause()
            elif x == 5:
                audio5.pause()

        x += 1
        chooseAudio()

    def previousSong(e):
        nonlocal x, songon
        if songon:
            if x == 1:
                audio1.pause()
            elif x == 2:
                audio2.pause()
            elif x == 3:
                audio3.pause()
            elif x == 4:
                audio4.pause()
            elif x == 5:
                audio5.pause()
        x -= 1
        chooseAudio()
        
    def togglePlayPause(e):
        nonlocal songon
        if songon:
            if x == 1:
                audio1.pause()
            elif x == 2:
                audio2.pause()
            elif x == 3:
                audio3.pause()
            elif x == 4:
                audio4.pause()
            elif x == 5:
                audio5.pause()
            songon = False
            playpause.text = "I>"
        else:
            chooseAudio()
        page.update()
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment  = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK
    img = ft.Image(src="", width=350, height=350)
    cursong = ft.Text("", size=40, color=ft.Colors.WHITE)
    playpause = ft.ElevatedButton(text="Play", color = ft.Colors.WHITE, on_click=togglePlayPause)
    nextButton = ft.ElevatedButton(text=">>", color = ft.Colors.WHITE, on_click=nextSong)
    previousButton = ft.ElevatedButton(text="<<", color = ft.Colors.WHITE, on_click=previousSong)

    audio1 = ft.Audio(src="your/folder/path/here/Foo Fighters - Everlong (Official HD Video).mp3")
    audio2 = ft.Audio(src="your/folder/path/here/Goo Goo Dolls – Iris [Official Music Video] [4K Remaster].mp3")
    audio3 = ft.Audio(src="your/folder/path/here/Nirvana - Drain You (Audio).mp3")
    audio4 = ft.Audio(src="your/folder/path/here/Radiohead - Creep.mp3")
    audio5 = ft.Audio(src="your/folder/path/here/You're All I Want - Cigarettes After Sex.mp3")
    page.overlay.append(audio1)
    page.overlay.append(audio2)
    page.overlay.append(audio3)
    page.overlay.append(audio4)
    page.overlay.append(audio5)
    buttons = ft.Row (controls= [previousButton, playpause, nextButton], alignment=ft.MainAxisAlignment.CENTER, width=300) #I figured this out by reading the links you sent, so dont go accusing me of chatgpt, i only used it for figuring out how to use a variable that applies to every function so it doesnt have to be inside
    page.add(img, cursong, buttons)
    page.update()
    chooseAudio()
ft.app(target=main)
#Reptilia is so good