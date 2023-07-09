import pyttsx3 as p
import tkinter as t
import random as r

speaker=p.init()
files=open(r"Words.txt",'r')
word=files.readlines()
a=word[r.randint(0,len(word)-1)].rstrip()
score=0

rule='''General Instructions:
1. Press Start the game button to start playing
2. Once the game starts play button and entry box will be visible
3. Click on the play audio button to listen to the word and type the spelling of it in the
    entry box below
4. Correct answer gives +1 score and wrong answer terminates the game
5. Press close button to exit the game'''
def play():
    global a
    speaker.setProperty('rate',100)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)
    speaker.say(a)
    speaker.runAndWait()

def play_slow():
    global a
    speaker.setProperty('rate',50)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)
    speaker.say(a)
    speaker.runAndWait()   

def dplay():
    global audio,audio_slow
    audio["state"]="disabled"
    audio_slow["state"]="disabled"
    

def start():
    global spell,chk,audio,root,audio_slow
    root=t.Tk()
    root.title("Spelling game")
    root.geometry("1500x1000")
    root.configure(bg="LightSkyBlue1")
    h=t.Label(root,text="SPELLING GAME",font=("Arial", 90,"bold"),bg="LightSkyBlue1",fg="navy")
    h.pack(pady=20)
    s=t.Label(root,text="Score={}".format(score),font=("Arial", 50),bg="LightSkyBlue1",fg="navy")
    s.pack(pady=10)
    audframe=t.Frame(root)
    audframe.pack(pady=20)
    audio=t.Button(audframe,text="Play Audio Normal",bg="blue",font=("Arial", 30,"bold"),fg="white",command=play)
    audio.grid(row=0, column=0)
    audio_slow=t.Button(audframe,text="   Play Audio slow   ",bg="blue",font=("Arial", 30,"bold"),fg="white",command=play_slow)
    audio_slow.grid(row=0, column=2)
    entframe=t.Frame(root)
    entframe.pack(pady=20)
    spell = t.Entry(entframe,font=('Arial',30,'bold'))
    spell.grid(row=0, column=1)
    enter=t.Label(entframe,text="Enter the word",font=("Arial", 35,"bold"),bg="LightSkyBlue1",fg="navy")
    enter.grid(row=0, column=0)
    chk=t.Button(root,text="Check",font=("Arial",30,"bold"),bg="azure",fg="dark orange",command=lambda:[check(),dcheck(),dplay()])
    chk.pack(pady=10)
def dcheck():
    global chk,spell
    chk["state"]="disabled"
    spell["state"]="disabled"
    
def check():
    global w,a,spell,score,root
    w=spell.get()
    if str(w.rstrip()).lower()==str(a.rstrip()).lower():
        result=t.Label(root, text = 'Correct Answer !!!', font = ('Arial',35),fg="green",bg="LightSkyBlue1")
        a=word[r.randint(0,len(word)-1)].rstrip()
        score+=1
        result.pack(pady=5)
        t.Button(root,text="Next",font=("Arial", 25,"bold"),fg="white",bg="lime green",command=lambda:[root.destroy(),start()]).pack(pady=10)
    else:
        result=t.Label(root, text = 'Wrong answer. Correct answer is {}'.format(a), font = ('Arial',35),bg="LightSkyBlue1",fg="maroon")
        result.pack(pady=5)
        score=0
        t.Button(root,text="Play Again",font=("Arial", 25,"bold"),bg="maroon",fg="white",command=lambda:[root.destroy(),main()]).pack(pady=10)
def dstart():
    global start_game
    start_game["state"]="disabled"

def main():
    global root,start_game,a,score,w,intro
    intro=t.Tk()
    intro.title("Spelling game")
    intro.geometry("1500x1000")
    intro.configure(bg="LightSkyBlue1")
   
    head=t.Label(intro,text="Welcome to Spelling Game !",font=("Arial", 80,"bold"),fg='blue',bg="LightSkyBlue1")
    head.pack(pady=45)
    rules=t.Label(intro,justify=t.LEFT,text=rule,font=("Arial", 25,"bold"),fg="dark blue",bg="LightSkyBlue1")
    rules.pack(pady=25)
    start_game=t.Button(intro,text="Start the game",bg='light green',font=("Arial", 50,"bold"),fg="midnight blue",command=lambda:[start(),dstart(),intro.destroy()])
    start_game.pack(pady=25)
    intro.mainloop()

main()


