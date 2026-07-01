from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
from tkinter.filedialog import askopenfilename, asksaveasfilename
import pygame
import string

root=Tk()
root.title('CHILLBOT')
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry('1000x600')
root.config(bg='black')

bg_img=Image.open('ai.png')
bg_img=bg_img.resize((w,h))
img=ImageTk.PhotoImage(bg_img)
bg=Canvas(root, width=w, height=h)
bg.place(x=0, y=0, relwidth=1, relheight=1)
bg.create_image(0, 0, anchor='nw', image=img)

a=bg.create_text(650, 50, text=" Welcome to ChillBot.", font=("OCR A Extended", 32, "bold"), fill="white")
c=bg.create_text(647, 100, text="\n(THE ULTIMATE TIMEPASS AGENT)", font=("OCR A Extended", 11, "bold"), fill="white")
text_box = Text(bg, bg='white', border=5, width=157, height=3)
bg.create_window(6, 550, anchor='nw', window=text_box)


def replies(event):
    x = text_box.get("1.0", "end-1c").strip().lower()
    
    if x in ['hello', 'hi', 'hey', 'sup']:
        messagebox.showinfo("ChillBot", "Hello! How may I help you today?")

    elif x in ['how are you?', 'how are you', "what's up", 'wassup', 'sup', 'wats good', 'wats up', "wat's up?"]:
        messagebox.showinfo("ChillBot", "I'm smashing today! How can I assist you?")

    elif x in ["good", "fine", "well", "ok", "okay", "w"]:
        messagebox.showinfo("ChillBot", "That's good to hear!")

    elif x in ["not good", "not fine", "not well", "not ok", "not okay", "l", "bad", "shit"]:
        messagebox.showinfo("ChillBot", "Hope you feel better soon!")
    elif x in ["bye", 'ok bye', 'okay bye']:
        messagebox.showinfo("ChillBot", "Bye! See you later!")
        exit()

    else:
        messagebox.showerror("ChillBot", "Please choose a questions from the given options, or click on them! I only have the ability to answer those for now.")

text_box.bind("<Return>", replies)
asker=bg.create_text(80, 537, text="how are you?", font=("OCR A Extended", 14, "bold"), fill="white")

expression = ""
def maths():
    m=Toplevel()
    m.title('Chill Math Window')
    m.geometry('315x370')
    

    def press(val):
        global expression
        expression += str(val)
        entry.delete(0, END)
        entry.insert(END, expression)

    def equal():
        global expression
        try:
            result = str(eval(expression))
            entry.delete(0, END)
            entry.insert(END, result)
            expression = result
        except:
            entry.delete(0, END)
            entry.insert(END, "Error")
            expression = ""

    def clear():
        global expression
        expression = ""
        entry.delete(0, END)

    def key_press(event):
        global expression
        if event.keysym == "Return":
            equal()
        elif event.keysym == "Escape":
            clear()
        else:
            expression = entry.get()

    entry = Entry(m, font=("Arial", 20), justify="right")
    entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")
    entry.focus()

    buttons=["7","8","9","/","4","5","6","*","1","2","3","-","0",".","=","+",]

    row, col = 1, 0
    for b in buttons:
        if b == "=":
            Button(m, text=b, width=5, height=2, font=("Arial", 14), command=equal).grid(row=row, column=col, padx=2, pady=2)
        else:
            Button(m, text=b, width=5, height=2, font=("Arial", 14), command=lambda x=b: press(x)).grid(row=row, column=col, padx=2, pady=2)
        col += 1
        if col == 4:
            col = 0
            row += 1

    Button(m, text="CLEAR", width=22, height=2, font=("Arial", 14), command=clear).grid(row=row, column=0, columnspan=4, padx=2, pady=2)

    entry.bind("<Key>", key_press)
    m.mainloop()

q1=Button(bg, text='MATH?', font=("OCR A Extended", 24, "bold"), command=maths, relief=RAISED, border=6)
q1.place(x=20, y=395)
def info():
    i=Toplevel()
    i.title('ChillBot - About')
    i.geometry('1000x600')
    i.config(bg='white')
    title=Label(i, text='The Creator of ChillBot', font=('Consolas', 20, 'bold'), bg='white', fg='black')
    title.pack(side=TOP)
    rest=Label(i, text='''\nArjunn Kalwaghe. Some say he was born with a keyboard in his hands.\n\n Others say he debugged his first program before he could walk.\n\n Neither has been confirmed, but neither has been denied.\n\nHis IQ is not measured in numbers. Numbers aren't big enough.\n\n He codes with the precision of a surgeon, the creativity of an artist,\n and the energy of someone who just had three energy drinks.\n\n When he sits down at his computer, the computer feels privileged. \n\nWhen he writes a function, the function works on the first try — out of respect.\n\n Physicists believe there are limits to human intelligence. \n\nNot for Arjunn. LChillBot is not just a project. It is a legacy. And its creator? A legend.\n\n\n\nAlso thanks alot for teaching me and helping me alot, Miss Ishika. You are the best''', font=("OCR A Extended", 14), bg='white')
    rest.pack()
    last=Label(i, text='🫡', font=('Consolas', 54, 'bold'), bg='white')
    last.pack(side=BOTTOM)
    
    i.mainloop()

life_advice = ["Have you tried turning it off and on again?",
    "Sleep on it. Everything looks better in the morning.",
    "Talk to someone you trust. A problem shared is a problem halved.",
    "Make a list. Break it into small steps. Tackle one at a time.",
    "Ask yourself: will this matter in 5 years?",
    "Stop overthinking. Take one small action right now.",
    "Drink water, take a walk, and come back to it.",
    "The answer is already inside you. Trust yourself.",
    "Maybe the real problem is a different problem in disguise.",
    "Have you eaten today? Seriously. Eat something first."]

motivation = ["You got this. No, really. YOU. GOT. THIS. 💪",
    "Every expert was once a beginner. Keep going!",
    "The fact that you're trying already puts you ahead.",
    "Small progress is still progress. Don't stop now.",
    "You've survived 100% of your bad days so far. Legend.",
    "Difficult roads often lead to beautiful destinations.",
    "Be the energy you wish to see in the world. ✨",
    "Your future self is cheering you on right now."]

excuses = ["My dog ate my motivation.",
    "Mercury is in retrograde.",
    "I was going to, but then I got distracted by a very interesting documentary.",
    "My horoscope said today wasn't the day.",
    "I sneezed and lost my train of thought.",
    "The universe clearly doesn't want me to do it today.",
    "I was emotionally unavailable.",
    "My hands were busy doing... things."]

yes_no = ["YES. Absolutely. Do it.",
    "NO. Trust your gut — don't.",
    "Maybe. Flip a coin and go with your gut reaction.",
    "The stars say YES, but your wallet says NO.",
    "Only if you'd be happy telling your mum about it.",
    "Ask me again after coffee.",
    "YES — but wait a week first.",
    "NO — but in the nicest possible way.", 'YES', 'NO']

facts = ["Honey never spoils. Archaeologists have found 3000-year-old honey in Egyptian tombs that was still perfectly edible.",
    "A day on Venus is longer than a year on Venus.",
    "Octopuses have three hearts, nine brains, and blue blood.",
    "The Eiffel Tower grows about 15cm taller in summer due to heat expanding the metal.",
    "Cleopatra lived closer in time to the Moon landing than to the construction of the Great Pyramid.",
    "A group of flamingos is called a flamboyance.",
    "The shortest war in history lasted 38–45 minutes. It was between Britain and Zanzibar in 1896.",
    "Bananas are berries, but strawberries are not.",
    "There are more possible iterations of a game of chess than there are atoms in the observable universe.",
    "A bolt of lightning is five times hotter than the surface of the sun.",
    "The human body contains enough carbon to make about 900 pencils.",
    "Sharks are older than trees. They've existed for over 400 million years.",
    "A sneeze travels at about 160 km/h.",
    "The word 'nerd' was first used in a Dr. Seuss book in 1950.",
    "Butterflies taste with their feet.",
    "There are more stars in the universe than grains of sand on all of Earth's beaches.",
    "A group of crows is called a murder.",
    "The average person walks about 100,000 miles in their lifetime — enough to circle the Earth four times.",
    "Wombat poop is cube-shaped.",
    "The Great Wall of China is not visible from space with the naked eye. That's a myth.",
    "Cows have best friends and get stressed when separated from them.",
    "The first computer bug was an actual bug — a moth found in a Harvard computer in 1947.",
    "It rains diamonds on Neptune and Uranus.",
    "A human brain generates enough electricity to power a small light bulb.",
    "The tongue is the strongest muscle in the body relative to its size.",
    "Penguins propose to their mates with a pebble.",
    "There is a species of jellyfish that is biologically immortal.",
    "Your nose can detect over 1 trillion different scents.",
    "The dot over the letters 'i' and 'j' is called a tittle.",
    "A day on Mercury lasts longer than a year on Mercury.",
    "The average cloud weighs about 500,000 kg.",
    "Sloths can hold their breath longer than dolphins — up to 40 minutes.",
    "Oxford University is older than the Aztec Empire.",
    "There are more trees on Earth than stars in the Milky Way.",
    "Blind people dream. If they were born blind, they dream in sound, smell, and touch.",
    "The fingerprints of a koala are indistinguishable from those of a human.",
    "A jiffy is an actual unit of time — 1/100th of a second.",
    "Ants never sleep and don't have lungs.",
    "The human eye can detect a single photon of light in complete darkness.",
    "Rats laugh when tickled, but at a frequency humans can't hear.",
    "The Pacific Ocean is larger than all of Earth's landmass combined.",
    "You can hear a blue whale's heartbeat from 3km away.",
    "Goats have rectangular pupils so they can see nearly 360 degrees.",
    "The Sahara Desert was green and full of rivers about 10,000 years ago.",
    "A single strand of spaghetti is called a spaghetto.",
    "Hot water freezes faster than cold water. This is called the Mpemba effect.",
    "The average person spends 6 months of their life waiting at red lights.",
    "Humans share 50% of their DNA with bananas.",
    "There are more possible shuffles of a deck of cards than atoms on Earth.",
    "A group of pugs is called a grumble.",]

future = ["The stars are aligning in your favour. Something unexpected will bring you joy today.",
    "A stranger's smile today will stay with you longer than you think.",
    "You are on the verge of a breakthrough. Trust the process.",
    "The universe has been saving something good for you. It arrives soon.",
    "Today is not the day to hold back. Say what you feel.",
    "A decision you've been avoiding will make itself clear before sundown.",
    "Someone is thinking about you right now. Warmly.",
    "The road ahead is clearer than it appears. Take one step.",
    "Your patience is about to be rewarded in a way you didn't expect.",
    "An old connection will resurface and remind you of who you truly are.",
    "The moon watches over dreamers. You are one of them.",
    "Fortune favours you today — but only if you leave the house.",
    "Something you lost will find its way back to you.",
    "A moment of silence today will give you the answer you've been seeking.",
    "The energy you put out today will return to you threefold.",
    "You are closer to your goal than yesterday. Keep moving.",
    "A small act of kindness today will ripple further than you know.",
    "The stars say: stop waiting for permission. Begin.",
    "Today holds a quiet magic. Pay attention to the small things.",
    "An opportunity disguised as an inconvenience is heading your way.",
    "You will laugh today — genuinely, unexpectedly, and loudly.",
    "The universe is not against you. It's setting the stage.",
    "Something you've been dreaming about is trying to find you too.",
    "Your instincts today are sharper than usual. Trust them.",
    "A conversation today will change how you see something important.",
    "The moon whispers: rest is not weakness. Recharge.",
    "You are being guided, even when it doesn't feel like it.",
    "Watch for a sign today. You'll know it when you see it.",
    "The chapter you're in is hard, but it is not the last one.",
    "Your energy is magnetic today. Use it wisely.",
    "Something beautiful is growing quietly in your life right now.",
    "The stars have noted your effort. A reward is being prepared.",
    "Today is a good day to forgive — yourself most of all.",
    "An unexpected message will lift your spirits.",
    "Luna sees great things ahead. But first — drink some water.",
    "You will find exactly what you need, right when you need it.",
    "A dream you nearly gave up on is still worth chasing.",
    "The moon is on your side tonight. Make a wish.",
    "Courage is calling your name today. Answer it.",
    "Something ordinary will feel extraordinary before the day is over.",]

jokes = [("Why don't scientists trust atoms?", "Because they make up everything."),
    ("Why did the scarecrow win an award?", "Because he was outstanding in his field."),
    ("I told my wife she was drawing her eyebrows too high.", "She looked surprised."),
    ("Why don't eggs tell jokes?", "They'd crack each other up."),
    ("What do you call fake spaghetti?", "An impasta."),
    ("Why did the bicycle fall over?", "Because it was two-tired."),
    ("I'm reading a book about anti-gravity.", "It's impossible to put down."),
    ("What do you call cheese that isn't yours?", "Nacho cheese."),
    ("Why can't you give Elsa a balloon?", "Because she'll let it go."),
    ("What do you call a fish without eyes?", "A fsh."),
    ("Why did the math book look so sad?", "Because it had too many problems."),
    ("I asked the librarian if they had books about paranoia.", "She whispered: 'They're right behind you.'"),
    ("What do you call a sleeping dinosaur?", "A dino-snore."),
    ("Why don't skeletons fight each other?", "They don't have the guts."),
    ("I used to hate facial hair.", "But then it grew on me."),
    ("What's a vampire's favourite fruit?", "A blood orange."),
    ("Why did the golfer bring an extra pair of pants?", "In case he got a hole in one."),
    ("What do you call a factory that makes okay products?", "A satisfactory."),
    ("I told my doctor I broke my arm in two places.", "He told me to stop going to those places."),
    ("Why did the invisible man turn down the job?", "He couldn't see himself doing it."),
    ("What do you call a bear with no teeth?", "A gummy bear."),
    ("Why did the tomato turn red?", "Because it saw the salad dressing."),
    ("I only know 25 letters of the alphabet.", "I don't know why."),
    ("What's brown and sticky?", "A stick."),
    ("Why can't a nose be 12 inches long?", "Because then it'd be a foot."),
    ("What do you call an alligator in a vest?", "An investigator."),
    ("I told a joke about construction.", "I'm still working on it."),
    ("Why did the stadium get hot after the game?", "All the fans left."),
    ("What's a skeleton's least favourite room?", "The living room."),
    ("I have a joke about time travel, but you didn't like it.", ""),
    ("Why do cows wear bells?", "Because their horns don't work."),
    ("What did the ocean say to the beach?", "Nothing, it just waved."),
    ("I'm on a seafood diet.", "I see food and I eat it."),
    ("Why did the coffee file a police report?", "It got mugged."),
    ("What do you call a lazy kangaroo?", "A pouch potato."),
    ("Why did the student eat his homework?", "The teacher told him it was a piece of cake."),
    ("What did one wall say to the other?", "I'll meet you at the corner."),
    ("Why are elevator jokes so good?", "They work on many levels."),
    ("What do lawyers wear to court?", "Lawsuits."),
    ("Why don't scientists trust stairs?", "Because they're always up to something."),
    ("I asked my dog what two minus two is.", "He said nothing."),
    ("What do you call a pony with a cough?", "A little hoarse."),
    ("Why did the picture go to jail?", "Because it was framed."),
    ("What do you call a snowman with a six-pack?", "An abdominal snowman."),
    ("I used to play piano by ear.", "Now I use my hands."),
    ("What's orange and sounds like a parrot?", "A carrot."),
    ("Why did the cookie go to the doctor?", "Because it was feeling crummy."),
    ("I told my cat a joke.", "He wasn't a-mused."),
    ("What do you call a sad cup of coffee?", "Depresso."),
    ("Why did the hipster burn his tongue?", "He drank his coffee before it was cool."),]

questions = [
        ("Always be 10 minutes late", "Always be 20 minutes early"),
        ("Live without music", "Live without movies"),
        ("Be able to fly", "Be able to turn invisible"),
        ("Know when you'll die", "Know how you'll die"),
        ("Have unlimited money but no friends", "Have amazing friends but always be broke"),
        ("Only eat sweet food forever", "Only eat salty food forever"),
        ("Be famous but hated", "Be unknown but loved"),
        ("Live in the past", "Live in the future"),
        ("Never use social media again", "Never watch TV/Netflix again"),
        ("Be able to talk to animals", "Be able to speak every human language"),
        ("Always feel cold", "Always feel hot"),
        ("Have no sleep but full energy", "Sleep 12 hours but feel amazing"),
        ("Lose all your memories", "Never make any new ones"),
        ("Be the funniest person in the room", "Be the smartest person in the room"),
        ("Fight one horse-sized duck", "Fight 100 duck-sized horses"),
        ("Always say what you think", "Never speak again"),
        ("Explore the deep ocean", "Explore outer space"),
        ("Have a rewind button for life", "Have a pause button for life"),
        ("Know all the world's secrets", "Have everyone trust you completely"),
        ("Be stuck on a deserted island alone", "Be stuck with someone you hate"),
        ("Give up your phone for a year", "Give up eating out for a year"),
        ("Be a master of every instrument", "Be a master of every sport"),
        ("Always be slightly too hot", "Always have a slightly itchy nose"),
        ("Read minds but not control them", "Control actions but not read minds"),
        ("Live without the internet", "Live without air conditioning and heating"),
    ]

reactions = [
        "Bold choice. ✦", "A classic pick.", "Living on the edge ",
        "Respect.", "Interesting... very interesting.", "The universe approves.",
        "That tracks.", "Solid. Very solid.", "Stars aligned on that one ", "Ooh, daring! ✦", "The road less taken.", "Unexpected. Love it ",
        "Bold move.", "The stars didn't see that coming ",
        "Controversial. I respect it.", "A true wildcard.", "Noted.",]

moods = [
    ("Zen",              "ChillBot is completely relaxed. Everything is smooth."),
    ("Laid Back",        "ChillBot is vibing. No stress, no rush."),
    ("Floating",         "ChillBot is drifting peacefully. Time feels slow."),
    ("Energized",        "ChillBot woke up on the right side. Full of good vibes."),
    ("Contemplative",    "ChillBot is thinking deep thoughts. Go easy on the questions."),
    ("Sleepy",           "ChillBot is half-asleep but still here. Keep it brief."),
    ("Neutral",          "ChillBot is just... here. Vibing neutrally."),
    ("Focused",          "ChillBot is in the zone. Ready to help with anything."),
    ("Mellow",           "ChillBot is smooth like butter. Everything flows."),
    ("Dreamy",           "ChillBot is in its own world. Poetic mood incoming."),
    ("Grounded",         "ChillBot is solid and present. Totally here for you."),
    ("Playful",          "ChillBot is feeling fun. Let's joke around."),
    ("Reflective",       "ChillBot is looking inward. Thoughtful answers coming."),
    ("Breezy",           "ChillBot is light and easy. Nothing heavy today."),
    ("Cozy",             "ChillBot is wrapped in comfort. Safe space activated."),
]

roasts = [
    "You're not stupid, you just have bad luck thinking.",
    "I'd agree with you but then we'd both be wrong.",
    "You have your entire life to be an idiot. Take the day off.",
    "I'd call you a tool but tools are actually useful.",
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "I'd explain it to you but I left my crayons at home.",
    "You're proof that even the universe makes typos.",
    "Your wifi password is probably 'password123', isn't it.",
    "I've seen better plans come out of a fortune cookie.",
    "You're not the dumbest person alive, but you better hope they don't die.",
    "Somewhere out there, a tree is working very hard to produce oxygen for you. Apologize to it.",
    "You have the energy of a dying phone at 2%.",
    "I'd roast you harder but my parents told me not to burn trash.",
    "You're like a software update. Whenever I see you I think 'not now'.",
    "If brains were petrol you wouldn't have enough to power a fly's motorbike.",
    "You're the human equivalent of a participation trophy.",
    "Error 404: Personality not found.",
    "You're not lazy. You're just on energy-saving mode. Permanently.",
    "I'd say you peaked in high school but I'm not sure you peaked.",
    "You have miles of potential... all of it underground.",
    "Calling you average would be a compliment.",
    "You're like Monday. Nobody asked for you but here you are.",
    "I'd roast you, but my mom said I'm not allowed to burn garbage.",
    "You're like a broken pencil. Completely pointless.",
    "Even your reflection thinks about leaving.",
    "You're not a bad person. You're just a lot.",
    "If you were a spice, you'd be flour.",
    "You have the charisma of a damp napkin.",
    "Luna has processed your entire personality and returned: null.",
    "You make me believe in alien life. There's no way you're fully human.",
    "You can never be as good as Arjun."
]

quiz = [
        ("What is the largest planet in our solar system?", ["Mars", "Jupiter", "Saturn", "Neptune"], "Jupiter"),
        ("How many bones are in the human body?", ["196", "206", "216", "186"], "206"),
        ("What is the chemical symbol for gold?", ["Go", "Gd", "Au", "Ag"], "Au"),
        ("Which country invented pizza?", ["France", "Greece", "USA", "Italy"], "Italy"),
        ("What is the fastest land animal?", ["Lion", "Horse", "Cheetah", "Leopard"], "Cheetah"),
        ("How many continents are there?", ["5", "6", "7", "8"], "7"),
        ("What gas do plants absorb?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "Carbon Dioxide"),
        ("Who painted the Mona Lisa?", ["Picasso", "Da Vinci", "Monet", "Van Gogh"], "Da Vinci"),
        ("What is the capital of Japan?", ["Beijing", "Seoul", "Bangkok", "Tokyo"], "Tokyo"),
        ("How many sides does a hexagon have?", ["5", "6", "7", "8"], "6"),
        ("What is the smallest country in the world?", ["Monaco", "San Marino", "Vatican City", "Liechtenstein"], "Vatican City"),
        ("Which planet is closest to the sun?", ["Venus", "Earth", "Mars", "Mercury"], "Mercury"),
        ("What is H2O commonly known as?", ["Salt", "Water", "Oxygen", "Hydrogen"], "Water"),
        ("How many players are on a basketball team?", ["4", "5", "6", "7"], "5"),
        ("What is the longest river in the world?", ["Amazon", "Yangtze", "Mississippi", "Nile"], "Nile"),
        ("Which element has the symbol O?", ["Gold", "Osmium", "Oxygen", "Oganesson"], "Oxygen"),
        ("What year did World War 2 end?", ["1943", "1944", "1945", "1946"], "1945"),
        ("How many strings does a guitar have?", ["4", "5", "6", "7"], "6"),
        ("What is the hardest natural substance?", ["Gold", "Iron", "Diamond", "Quartz"], "Diamond"),
        ("Which ocean is the largest?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific"),
    ]

def lifeadvice():
    l = Toplevel()
    l.title('Chill Advisor')
    l.geometry('600x175')
    l.config(bg='midnight blue')
    i=Label(l, text='What is your problem???', font=('Consolas', 18), bg='midnight blue', fg='yellow')
    i.pack(pady=10)
    def show():
        messagebox.showinfo('ADVICE', random.choice(life_advice))
    e = Entry(l, width=50, border=2)
    e.pack(pady=10)       
    b = Button(l, text='Generate Advice', command=show, font=("OCR A Extended", 12), relief=RAISED, border=5, bg='midnight blue', fg='yellow')
    b.pack(pady=5)
    l.mainloop()

def motiv():
    l = Toplevel()
    l.title('Chill Motivation')
    l.geometry('600x175')
    l.config(bg='#0d0014')
    i=Label(l, text='CLICK HERE TO GET MOTIVATED!!!', font=('Consolas', 18), bg='#0d0014', fg='yellow')
    i.pack(pady=10)
    def show():
        messagebox.showinfo('MOTIVATION!!!', random.choice(motivation))
    b = Button(l, text='GET MOTIVATED!!!', command=show, font=("OCR A Extended", 12), relief=RAISED, border=5, bg='#0d0014', fg='yellow')
    b.pack(pady=30)
    l.mainloop()

def ex():
    l = Toplevel()
    l.title('Chill Excuse Generator')
    l.geometry('600x175')
    l.config(bg='#070d1f')
    i=Label(l, text='Need an Excuse?', font=('Consolas', 18), bg='#070d1f', fg="#30a4cb")
    i.pack(pady=10)
    def show():
        messagebox.showinfo('Excuse', random.choice(excuses))
    b = Button(l, text='Generate Excuse', command=show, font=("OCR A Extended", 12), relief=RAISED, border=5, bg='#070d1f', fg="#30a4cb")
    b.pack(pady=30)
    l.mainloop()

def yesno():
    l = Toplevel()
    l.title('Chill Answerer')
    l.geometry('600x175')
    l.config(bg='#0a1f0a')
    i=Label(l, text='What is your question???', font=('Consolas', 18), bg='#0a1f0a', fg='yellow')
    i.pack(pady=10)
    def show():
        messagebox.showinfo('Yes or No?', random.choice(yes_no))
    e = Entry(l, width=50, border=2)
    e.pack(pady=10)       
    b = Button(l, text='YES or NO?', command=show, font=("OCR A Extended", 12), relief=RAISED, border=5, bg='#0a1f0a', fg='yellow')
    b.pack(pady=5)
    l.mainloop()

def joker():
    l = Toplevel()
    l.title('Chill Joker')
    l.geometry('600x175')
    l.config(bg='#540404')
    i=Label(l, text='CHILLBOT JOKER!!!\nHERE TO MAKE YOU SMILE 😉', font=('Consolas', 18), bg="#540404", fg='yellow')
    i.pack(pady=10)
    def show():
        setup, punchline = random.choice(jokes)
        messagebox.showinfo("Chill 😂", f"{setup}\n\n{punchline}")
    b = Button(l, text='Generate Joke!', command=show, font=("OCR A Extended", 12), relief=RAISED, border=5, bg='#540404', fg='yellow')
    b.pack(pady=5)
    l.mainloop()

def game():
    pygame.init()

    
    WIDTH, HEIGHT = 600, 600
    CELL = 20
    COLS = WIDTH // CELL
    ROWS = HEIGHT // CELL
    FPS = 10

    BLACK  = (0,   0,   0)
    GREEN  = (50,  200, 50)
    DGREEN = (30,  140, 30)
    RED    = (220, 50,  50)
    WHITE  = (255, 255, 255)
    GRAY   = (30,  30,  30)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    font_big  = pygame.font.SysFont("Arial", 48, bold=True)
    font_small = pygame.font.SysFont("Arial", 24)

    def new_game():
        snake = [(COLS // 2, ROWS // 2)]
        direction = (1, 0)
        food = spawn_food(snake)
        score = 0
        return snake, direction, food, score

    def spawn_food(snake):
        while True:
            pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
            if pos not in snake:
                return pos

    def draw_cell(x, y, color, inner_color=None):
        rect = pygame.Rect(x * CELL + 1, y * CELL + 1, CELL - 2, CELL - 2)
        pygame.draw.rect(screen, color, rect, border_radius=4)
        if inner_color:
            inner = pygame.Rect(x * CELL + 5, y * CELL + 5, CELL - 10, CELL - 10)
            pygame.draw.rect(screen, inner_color, inner, border_radius=2)

    def draw_food(x, y):
        cx = x * CELL + CELL // 2
        cy = y * CELL + CELL // 2
        pygame.draw.circle(screen, RED, (cx, cy), CELL // 2 - 2)
        
        pygame.draw.circle(screen, (255, 130, 130), (cx - 3, cy - 3), 3)

    def draw_grid():
        for gx in range(0, WIDTH, CELL):
            pygame.draw.line(screen, GRAY, (gx, 0), (gx, HEIGHT))
        for gy in range(0, HEIGHT, CELL):
            pygame.draw.line(screen, GRAY, (0, gy), (WIDTH, gy))

    def show_overlay(title, score):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        screen.blit(overlay, (0, 0))

        t1 = font_big.render(title, True, WHITE)
        t2 = font_small.render(f"Score: {score}", True, WHITE)
        t3 = font_small.render("Press SPACE to play", True, (180, 180, 180))

        screen.blit(t1, t1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
        screen.blit(t2, t2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
        screen.blit(t3, t3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

    snake, direction, food, score = new_game()
    state = "start"   

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if state == "playing":
                    if event.key == pygame.K_UP    and direction != (0,  1): direction = (0, -1)
                    if event.key == pygame.K_DOWN  and direction != (0, -1): direction = (0,  1)
                    if event.key == pygame.K_LEFT  and direction != (1,  0): direction = (-1, 0)
                    if event.key == pygame.K_RIGHT and direction != (-1, 0): direction = (1,  0)

                if event.key == pygame.K_SPACE:
                    if state in ("start", "dead"):
                        snake, direction, food, score = new_game()
                        state = "playing"

        
        if state == "playing":
            head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            
            if not (0 <= head[0] < COLS and 0 <= head[1] < ROWS):
                state = "dead"
            
            elif head in snake:
                state = "dead"
            else:
                snake.insert(0, head)
                if head == food:
                    score += 1
                    food = spawn_food(snake)
                else:
                    snake.pop()

       
        screen.fill(BLACK)
        draw_grid()

       
        for i, (x, y) in enumerate(snake):
            color = GREEN if i == 0 else DGREEN
            inner = (80, 220, 80) if i == 0 else None
            draw_cell(x, y, color, inner)

       
        draw_food(*food)


        score_surf = font_small.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surf, (8, 8))

        if state in ("start", "dead"):
            title = "SNAKE" if state == "start" else "GAME OVER"
            show_overlay(title, score)

        pygame.display.flip()

    pygame.quit()

def fortune():
    l = Toplevel()
    l.title('Chillest Fortune Teller')
    l.geometry('500x150')
    l.config(bg="#EDAD2D")
    i=Label(l, text='FORTUNE TELLER\nWANNA KNOW ABOUT YOUR FUTURE?', font=('Consolas', 18), bg="#EDAD2D", fg='#540404')
    i.pack(pady=10)
    def show():
        messagebox.showinfo("Chill Fortune Teller", random.choice(future))
    b = Button(l, text='Divine Future', command=show, font=("OCR A Extended", 12), relief=RAISED, border=5, bg='#EDAD2D', fg='#540404')
    b.pack(pady=5)
    l.mainloop()

def fact():
    l = Toplevel()
    l.title('Chill Facts')
    l.geometry('500x150')
    l.attributes('-topmost', True)
    l.lift()   
    l.config(bg="#26DFAE")
    i=Label(l, text='FACT MASTER!\nWANNA KNOW A RANDOM FACT?', font=('Consolas', 18), bg="#26DFAE", fg="#000000")
    i.pack(pady=10)
    def show():
        messagebox.showinfo("Chill Facts", random.choice(facts))
    b = Button(l, text='Random Fact', command=show, font=("OCR A Extended", 12), relief=RAISED, border=5, bg='#26DFAE', fg='#000000')
    b.pack(pady=5)
    

def texter():
    a = Toplevel()
    a.title('CHILL TEXT EDITOR')
    a.rowconfigure(0, minsize=5, weight=3)
    a.columnconfigure(1, minsize=5, weight=3)
    
    def yes():
        op = askopenfilename(filetypes=[('All files', '*.*'), ('Text files', '*.txt'), ('Python files', '*.py')])
        if not op:
            return
        txt_edit.delete(1.0, END)
        with open(op, 'r') as y:
            l = y.read()
            txt_edit.insert(END, l)
        a.title(f"TEXT EDITOR - {op}")

    def no():
        op = asksaveasfilename(defaultextension='.txt', filetypes=[('All files', '*.*'), ('Text files', '*.txt'), ('Python files', '*.py')])
        if not op:
            return
        with open(op, 'w') as x:
            m = txt_edit.get(1.0, END)
            x.write(m)
        a.title(f'TEXT EDITOR - {op}')

    txt_edit = Text(a)
    f = Frame(a, relief=RAISED, bd=6)
    b1 = Button(f, text='Open', command=yes)
    b2 = Button(f, text='Save As', command=no)

    b1.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
    b2.grid(row=1, column=0, sticky='ew', padx=5)
    f.grid(row=0, column=0, sticky='ns')
    txt_edit.grid(row=0, column=1, sticky='nsew')

    a.mainloop()

def choice():
    l = Toplevel()
    l.title('ChillBot — Would You Rather')
    l.geometry('500x200')
    l.config(bg="#0a0a1a")

    t = Label(l, text='✦ WOULD YOU RATHER ✦', font=('Consolas', 16, 'bold'), bg="#0a0a1a", fg="#c8a4f8")
    t.pack(pady=15)

    def load():
        q = random.choice(questions)

        popup = Toplevel(l)
        popup.title('Would You Rather')
        popup.geometry('420x220')
        popup.config(bg="#0a0a1a")
        Label(popup, text='Would you rather...', font=('Consolas', 11, 'italic'), bg="#0a0a1a", fg="#9988cc").pack(pady=(15, 5))
        Label(popup, text=f'A)  {q[0]}\n\n— OR —\n\nB)  {q[1]}', font=('Consolas', 10), bg="#0a0a1a", fg="#e0e0ff", justify='center').pack(pady=5)

        bf = Frame(popup, bg="#0a0a1a")
        bf.pack(pady=12)

        def pick(choice):
            popup.destroy()
            showpopup = Toplevel(l)
            showpopup.title('ChillBot')
            showpopup.geometry('340x120')
            showpopup.config(bg="#0a0a1a")
            showpopup.grab_set()
            Label(showpopup, text=f'You chose {choice}!\n\n{random.choice(reactions)}', font=('Consolas', 11), bg="#0a0a1a", fg="#c8a4f8", justify='center').pack(pady=20)
            Button(showpopup, text='OK', command=showpopup.destroy, font=('Consolas', 10), bg="#1a0a2e", fg="#c8a4f8", relief=RAISED, border=3).pack()

        Button(bf, text='  A  ', command=lambda: pick('A'), font=('Consolas', 11, 'bold'), bg="#1a0a2e", fg="#c8a4f8", relief=RAISED, border=4).pack(side=LEFT, padx=20)
        Button(bf, text='  B  ', command=lambda: pick('B'), font=('Consolas', 11, 'bold'), bg="#1a0a2e", fg="#c8a4f8", relief=RAISED, border=4).pack(side=LEFT, padx=20)

    b = Button(l, text='Give me one!', command=load, font=('Consolas', 12), relief=RAISED, border=5, bg="#1a0a2e", fg="#c8a4f8")
    b.pack(pady=10)

    l.mainloop()

def passgen():
    l = Toplevel()
    l.title('ChillBot Password Generator 🔒')
    l.geometry('500x300')
    l.config(bg="#3e1076")

    def generate():
        chars = string.ascii_letters + string.digits + string.punctuation
        pw = ''.join(random.choice(chars) for _ in range(12))
        e.delete(0, END)
        e.insert(0, pw)

    a = Label(l, text='Get Your Password Generated Here!', font=('Consolas', 18), bg="#3e1076", fg="#FFFFFF")
    a.pack(pady=25)
    b = Button(l, text='Generate Password', command=generate, font=("OCR A Extended", 12), relief=RAISED, border=5, bg='#3e1076', fg="#FFFFFF")
    b.pack(pady=20)
    e = Entry(l, width=20, border=2)
    e.pack(pady=30)

    l.mainloop()

def mood():
    l = Toplevel()
    l.title("What's ChillBot's Mood? ")
    l.geometry('375x165')
    l.config(bg="#A61665")
    i=Label(l, text="WHAT'S THE MOOD TODAY?", font=('Consolas', 18), bg="#A61665", fg="#D2D2D2")
    i.pack(pady=10)
    def show():
        messagebox.showinfo("ChillBot's Moods'", random.choice(moods))
    b = Button(l, text="What's the Mood?", command=show, font=("OCR A Extended", 12), relief=RAISED, border=5, bg='#A61665', fg='#D2D2D2')
    b.pack(pady=5)

    l.mainloop()

def roast():
    l = Toplevel()
    l.title('ChillBot Roasts You 🔥')
    l.geometry('350x170')
    l.attributes('-topmost', True)
    l.lift()   
    l.config(bg="#000000")
    i=Label(l, text='CHILLBOT ROASTS YOU!\nWANNA GET HUMBLED?', font=('Consolas', 18), bg="#000000", fg="#D30A0A")
    i.pack(pady=10)
    def show():
        messagebox.showinfo("Get Roasted", random.choice(roasts))
    b = Button(l, text='Roast Me', command=show, font=("OCR A Extended", 12), relief=RAISED, border=5, bg="#000000", fg='#D30A0A')
    b.pack(pady=5)
    c=Label(l, text='🥲', font=20, bg="#000000", fg="#FFFFFF")
    c.pack(pady=10)

def coinflip():
    l = Toplevel()
    l.title('Chill Coin Flip 🌙')
    l.geometry('400x160')
    l.config(bg="#0a0a1a")
    l.lift()
    l.attributes('-topmost', True)

    Label(l, text='COIN FLIP', font=('Consolas', 16, 'bold'), bg="#0a0a1a", fg="#c8a4f8").pack(pady=(18, 8))

    def flip():
        result = random.choice(["HEADS", "TAILS"])
        messagebox.showinfo("Chill Toss", f"It's... {result}!")
        l.lift()

    Button(l, text='Flip It', command=flip, font=('Consolas', 12), relief=RAISED, border=5, bg="#1a0a2e", fg="#c8a4f8").pack(pady=5)

def trivia():
    random.shuffle(quiz)
    q_list = quiz[:10] 
    score = [0]
    index = [0]

    l = Toplevel()
    l.title('Chill Quiz')
    l.geometry('600x240')
    l.config(bg="#000000")
    l.lift()
    l.attributes('-topmost', True)

    Label(l, text='CHILLBOT QUIZZER', font=('Consolas', 16, 'bold'), bg="#000000", fg="#02a958").pack(pady=(15, 5))

    progress_var = StringVar()
    Label(l, textvariable=progress_var, font=('Consolas', 9), bg="#000000", fg="#02a958").pack()

    q_var = StringVar()
    Label(l, textvariable=q_var, font=('Consolas', 11), bg="#000000", fg="#02a958",
          wraplength=440, justify='center').pack(pady=12)

    btn_frame = Frame(l, bg="#000000")
    btn_frame.pack()

    feedback_var = StringVar()
    Label(l, textvariable=feedback_var, font=('Consolas', 10), bg="#000000", fg="#0fa351").pack(pady=8)

    def load_question():
        i = index[0]
        if i >= len(q_list):
            show_result()
            return

        q, opts, _ = q_list[i]
        progress_var.set(f"Question {i + 1} of {len(q_list)}  |  Score: {score[0]}")
        q_var.set(q)
        feedback_var.set("")

        for widget in btn_frame.winfo_children():
            widget.destroy()

        shuffled = opts[:]
        random.shuffle(shuffled)

        for opt in shuffled:
            Button(btn_frame, text=opt, font=('Consolas', 10),
                   relief=RAISED, border=3, bg="#000000", fg="#b9f7e0",
                   activebackground="#000000", activeforeground="#ffffff",
                   width=18, command=lambda o=opt: check(o)).pack(side=LEFT, padx=5)

    def check(chosen):
        _, _, answer = q_list[index[0]]
        if chosen == answer:
            score[0] += 1
            feedback_var.set("✅ Correct! ✅")
        else:
            feedback_var.set(f"❌ Wrong! ❌\n It was {answer}.")
        index[0] += 1
        l.after(900, load_question)

    def show_result():
        for widget in btn_frame.winfo_children():
            widget.destroy()
        q_var.set("")
        feedback_var.set("")
        progress_var.set("")

        total = len(q_list)
        s = score[0]
        if s == total:
            msg = "PERFECT SCORE! ChillBot is impressed. 🌟"
        elif s >= total * 0.7:
            msg = "Solid work. The stars approve. ✨"
        elif s >= total * 0.4:
            msg = "Not bad. Could be worse. 🌙"
        else:
            msg = "...ChillBot is concerned. Study up. 🪐"

        Label(btn_frame, text=f"You scored {s} / {total}", font=('Consolas', 14, 'bold'),
              bg="#0a0a1a", fg="#0fa351").pack(pady=(10, 4))
        Label(btn_frame, text=msg, font=('Consolas', 11),
              bg="#0a0a1a", fg="#0fa351").pack(pady=4)
        Button(btn_frame, text='Play Again', font=('Consolas', 10), relief=RAISED, border=4,
               bg="#1a0a2e", fg="#0fa351", command=restart).pack(pady=10)

    def restart():
        random.shuffle(quiz)
        q_list[:] = quiz[:10]
        score[0] = 0
        index[0] = 0
        load_question()

    load_question()

q3=Button(bg, text='ADVICE?', font=("OCR A Extended", 24, "bold"), command=lifeadvice, relief=RAISED, border=6)
q3.place(x=170, y=395)
q2=Button(bg, text='About', font=("OCR A Extended", 12, "bold"), command=info, relief=RAISED, border=6)
q2.place(x=20, y=10)
q4=Button(bg, text='MOTIVATION', font=("OCR A Extended", 24, "bold"), command=motiv, relief=RAISED, border=6)
q4.place(x=800, y=395)
q5=Button(bg, text='EXCUSES', font=("OCR A Extended", 24, "bold"), command=ex, relief=RAISED, border=6)
q5.place(x=1075, y=395)
q6=Button(bg, text='YES / NO', font=("OCR A Extended", 24, "bold"), command=yesno, relief=RAISED, border=6)
q6.place(x=20, y=300)
q7=Button(bg, text='JOKES', font=("OCR A Extended", 24, "bold"), command=joker, relief=RAISED, border=6)
q7.place(x=365, y=395)
q8=Button(bg, text='FORTUNE?', font=("OCR A Extended", 24, "bold"), command=fortune, relief=RAISED, border=6)
q8.place(x=250, y=300)
q9=Button(bg, text='FACTS', font=("OCR A Extended", 24, "bold"), command=fact, relief=RAISED, border=6)
q9.place(x=20, y=205)
q0=Button(bg, text='TEXT EDITOR', font=("OCR A Extended", 24, "bold"), command=texter, relief=RAISED, border=6)
q0.place(x=190, y=205)
q11=Button(bg, text='WOULD YOU RATHER', font=("OCR A Extended", 24, "bold"), command=choice, relief=RAISED, border=6)
q11.place(x=895, y=110)
q12=Button(bg, text='SNAKE', font=("OCR A Extended", 24, "bold"), command=game, relief=RAISED, border=6)
q12.place(x=890, y=300)
q13=Button(bg, text='GENERATE PASSWORD', font=("OCR A Extended", 24, "bold"), command=passgen, relief=RAISED, border=6)
q13.place(x=875, y=205)
q14=Button(bg, text='🤖', font=("OCR A Extended", 24, "bold"), command=mood, relief=RAISED, border=6)
q14.place(x=810, y=300)
q15=Button(bg, text='GET ROASTED', font=("OCR A Extended", 24, "bold"), command=roast, relief=RAISED, border=6)
q15.place(x=20, y=110)
q16=Button(bg, text='FLIP COIN', font=("OCR A Extended", 24, "bold"), command=coinflip, relief=RAISED, border=6)
q16.place(x=1035, y=300)
q17=Button(bg, text='QUIZ?', font=("OCR A Extended", 24, "bold"), command=trivia, relief=RAISED, border=6)
q17.place(x=300, y=110)

root.mainloop()