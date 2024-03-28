from guizero import *
from random import choice
from wordfreq import top_n_list


wejscie=open('dict.txt', 'r')
words=[i.strip() for i in wejscie]
wejscie.close()

app=App("Wisielec")
app.icon='10.jpg'

up_box=Box(app, width='fill', align='top')
left_box=Box(app,width='fill', align='left')
right_box=Box(app, width='fill', align='right')

title=Text(up_box, text="Hangman", font='Comic Sans MS', size=34)


img=Picture(left_box, image='0.jpg', align='left', width=150, height=300)
###########################################
def reset():
    global tries, j, password, progress
    tries = 11
    j = 0
    password = choice(list(filter(lambda x: len(x) >= 4 and "'" not in x, top_n_list('en', 1000)))).upper()
    progress = list('_' * len(password))
    img.image='0.jpg'
    txt_progress.value=f'{tries} tries left.'
    txt_input.value=' '.join(progress)


def main():
    global tries, progress, password
    x=txt_bx.value.upper()
    global j #bez globala, j startuje od zera
    if tries > 0:
        # jak wczytać x??? napisać osobną funkcję!
        #x =
        any_guessed=False
        for i in range(len(password)):
            if x == password[i]:
                any_guessed=True
                progress[i]= x
        txt_input.value = ' '.join(progress)
        if progress == password:
            txt_progress.value = 'You win!'
        if not any_guessed:
            tries -= 1
            txt_progress.value = f'{tries} tries left.'
            j += 1
            img.image = f"{j}.jpg"

    if tries == 1: #0 czy 1?
        txt_progress.value = 'You lose!'

###########################################
tries = 11
j=0
password = choice(list(filter(lambda x: len(x)>=4 and "'" not in x,top_n_list('en', 1000)))).upper()
progress = list('_'*len(password))
#print(password)
###########################################
txt_input=Text(right_box, text=' '.join(progress), font='Comic Sans MS', size=20)

txt_bx=TextBox(right_box, width=1)
label_txt_bx=Text(right_box, text="Input a letter and then press Enter", font='Comic Sans MS')
enter=PushButton(right_box, text='Enter', command=main) #, command=main
reset=PushButton(right_box, text='Reset', command=reset)


txt_progress=Text(right_box, text=f'{tries} tries left.', font='Comic Sans MS')


app.display()