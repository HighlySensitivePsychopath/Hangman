from guizero import *
from random import choice
from wordfreq import top_n_list

app=App("Hangman")
app.icon='9.PNG'

up_box=Box(app, width='fill', align='top')
left_box=Box(app,width='fill', align='left')
right_box=Box(app, width='fill', align='right')

title=Text(up_box, text="Hangman", font='Comic Sans MS', size=34)

middle_box=Box(left_box)
img=Picture(middle_box, image='0.PNG', align='left', width=200, height=450)


###########################################
def reset():
    global tries, j, password, progress, games, char_wrong
    char_wrong=[]
    tries = 11
    j = 0
    password = choice(list(filter(lambda x: len(x)<=9 and len(x) >= 4 and "'" not in x, top_n_list('en', 1000)))).upper()
    progress = list('_' * len(password))
    games+=1
    img.image='0.PNG'
    txt_progress.value=f'{tries} tries left.'
    txt_input.value=' '.join(progress)
    games_txt.value=f'Game number {games}.'
    txt_char_wrong.value=''
    txt_bx.value=''
    password_reveal.value=''

    #print(password)


def main():
    global tries, progress, password
    x=txt_bx.value.upper()
    global j #bez globala, j startuje od zera
    if tries > 0:
        any_guessed=False
        for i in range(len(password)):
            if x == password[i]:
                any_guessed=True
                progress[i]= x
        txt_input.value = ' '.join(progress)
        if password == ''.join(progress):
            txt_progress.value = 'You win!'
            txt_progress.text_color='green'
            tries=-1
        if not any_guessed:
            tries -= 1
            txt_progress.value = f'{tries} tries left.'
            if x not in char_wrong and x!='':
                char_wrong.append(x)
                txt_char_wrong.value=f"Wrong characters: {' '.join(char_wrong)}"

            j += 1
            if j<11:
                img.image = f"{j}.PNG"

    if tries == 0: #0 czy 1?
        txt_progress.value = 'You lose!'
        password_reveal.value=f'The word unguessed: \n {password}'
    txt_bx.value = ''

###########################################
tries = 10
j=0
password = choice(list(filter(lambda x: len(x)>=4 and "'" not in x,top_n_list('en', 1000)))).upper()
progress = list('_'*len(password))
games=1
char_wrong=[]

#print(password)
###########################################
txt_input=Text(right_box, text=' '.join(progress), font='Comic Sans MS', size=20)

txt_bx=TextBox(right_box, width=1)
label_txt_bx=Text(right_box, text="Input a letter and then press Enter", font='Comic Sans MS')
enter=PushButton(right_box, text='Enter', command=main) #, command=main
reset=PushButton(right_box, text='Reset', command=reset)



txt_progress=Text(right_box, text=f'{tries} tries left.', font='Comic Sans MS')


txt_char_wrong=Text(right_box, text='', font='Comic Sans MS', color='red')

games_txt=Text(right_box, text=f'Game number {games}.', font='Comic Sans MS', color='blue')

password_reveal=Text(right_box, text='', font='Comic Sans MS')

app.display()