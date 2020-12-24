from gtts import gTTS
from playsound import playsound

i = input ('Enter you name: ')
x = 'hey' +i+ 'Welcome to my tool ,I hope you like it '
la='fr'
root = gTTS(text=x,lang=la,slow=False)
out=root.save('voice.mp3')
playsound('voice.mp3')
