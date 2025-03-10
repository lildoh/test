import flet as ft
import random

questions = [
    {
        "question": "What is Do’s favorite band?",
        "answers": ["Nirvana", "Limp Bizkit", "Radiohead", "Foo Fighters"],
        "correct": 2,
    },
    {
        "question": "Who is known as the king of pop?",
        "answers": ["Elvis Presley", "Micheal Jackson", "Freddie Mercury", "Drake"],
        "correct": 1,
    },
    {
        "question": "What is Rafael’s favorite song?",
        "answers": ["Un Coco", "Silla", "Una Bala", "Paraiso"],
        "correct": 3,
    },
    {
        "question": "What album by Radiohead made a shift in the genre of Radiohead?",
        "answers": ["Pablo Honey", "Kid A", "The Bends", "OK COMPUTER"],
        "correct": 1,
    },
    {
        "question": "What emotion does Radiohead most explore in their songs?",
        "answers": ["Grief", "Joy", "Sadness", "Yearn"],
        "correct": 2,
    },
    {
        "question": "Who did Thom Yorke take inspiration from for Fake Plastic Trees?",
        "answers": ["Jeff Buckley", "Kurt Cobain", "Euronymous", "Curt Kobein"],
        "correct": 0,
    },
    {
        "question": "Which band's debut album is titled “Is This It”?",
        "answers": ["Franz Ferdinand", "Interpol", "Arctic Monkeys", "The Strokes"],
        "correct": 3,
    },
    {
        "question": "What song is well known for being in the movie “Fight Club”?",
        "answers": ["Drain You", "Everlong", "All I Think About Now", "Where is my mind?"],
        "correct": 3,
    },
    {
        "question": "What song by Deftones Includes the lyrics “it’s too bad.. You’re married to me.”",
        "answers": ["Digital Bath", "Rosemary", "Mascara", "Rx Queen"],
        "correct": 2,
    },
    {
        "question": "When was the Treaty of Versailles signed?",
        "answers": ["June 28, 1919", "December 8th, 1917", "March 7th, 1904", "June 11, 1919"],
        "correct": 0,
    },
    {
        "question": "What’s Rafael’s rank in Rocket League’s 1v1?",
        "answers": ["Plat III", "Gold II", "Champ I", "SSL"],
        "correct": 1,
    },
    {
        "question": "What is a boolean?",
        "answers": ["A fundamental concept in computing that represents a value that can only be either true or false ", "A hardware device that allows you to enter data into a computer or interact with a computer", "A default function in VSCode which allows us to make a flet screen with an elevated button", "A command"],
        "correct": 0,
    },
    {
        "question": "Does Teacher Braulio play Rocket League ranked?",
        "answers": ["No, he is a casual", "He doesn't even play Rocket League", "HECK YEAH HE A TRYHARD", "Ceiling shot"],
        "correct": 0,
    },
    {
        "question": "What is Teacher Braulio’s go-to character in Super Smash Bros?",
        "answers": ["Steve", "Incineroar", "Jigglypuff", "Kirby"],
        "correct": 2,
    },
    {
        "question": "Which band wrote “Creep”?",
        "answers": ["Limp Bizkit", "Coldplay", "Nirvana", "Radiohead"],
        "correct": 3,
    },
    {
        "question": "Which band wrote the song “Everlong”",
        "answers": ["CAS", "The Strokes", "Arctic Monkeys", "Foo Fighters"],
        "correct": 3,
    },
    {
        "question": "What is Goo Goo Dolls most famous song",
        "answers": ["Iris", "Black Balloon", "Slide", "Valentine"],
        "correct": 0,
    },
    {
        "question": "Which album features the song “Do I Wanna Know”",
        "answers": ["Favorite Worst Nightmare", "Humbug", "The Car", "AM"],
        "correct": 3,
    },
    {
        "question": "How many bones are in the human body?",
        "answers": ["270", "207", "206", "216"],
        "correct": 2,
    },
    {
        "question": "Which song by Nirvana features the song “About a Girl”?",
        "answers": ["In Utero", "MTV Plugged In", "Bleach", "In Rainbows"],
        "correct": 2,
    },
]

current = 0
score = 0

def randomizerQ():
    random.shuffle(questions)

def startQ(page):
    global current, score
    randomizerQ()  
    current = 0
    score = 0
    page.controls.clear()
    page.add(ft.Column([
        ft.Text("Welcome to the Impossible Quiz", size=30),
        ft.Text("By: Rafael, Do, Ana, and Jin", size=15),
        ft.ElevatedButton("START", on_click=beginQpage)
    ]))

def beginQpage(e):
    showQ(e.page)

def showQ(page):
    global current
    if len(questions) > current:
        question = questions[current]["question"]
        options = questions[current]["answers"]
        page.controls.clear()

        questionLabel = ft.Text(f"{question}", size=20)

        optionButtons = [
            ft.ElevatedButton(option, on_click=lambda e, option=option: nextQuestion(page, option))
            for option in options
        ]
        #answers box ^
        nextButton = ft.ElevatedButton("SKIP", on_click=lambda e: nextQuestion(page, None))

        page.add(ft.Column([questionLabel, *optionButtons, nextButton]))
        page.add(ft.Text(f"Current score: {score}/{len(questions)}", size=20))

    else:
        showR(page)

def nextQuestion(page, selectedOption):
    global current, score
    if selectedOption:
        correctAnswer = questions[current]["answers"][questions[current]["correct"]]
        if selectedOption == correctAnswer:
            score += 1

    current += 1
    showQ(page)

def exitQuiz():
    pass
    #i actually no se como hacerlo

def showR(page):
    page.controls.clear()
    resultLabel = ft.Text(f"SCORE: {score}/{len(questions)}", size=20)
    restartButton = ft.ElevatedButton("RESTART", on_click=startQ)
    exitButton = ft.ElevatedButton("EXIT", on_click=exitQuiz)
    buttonRow = ft.Row([restartButton, exitButton])

    page.add(ft.Column([resultLabel, buttonRow]))

def main(page):
    page.title = "The IMPOSSIBLE Quiz"
    startQ(page)

ft.app(target=main)