# Text to speech
###### Simple text to speech CLI app using `pyttsx3`

### Save the text in a file? [Y]es/[N]o?
`Inputs:`
`Y` `N` `SETUP` `STOP`

### [M]ale or [F]emale voice?
`Inputs:`
`M` `F` `SETUP` `STOP`

##
### You can create a settings.txt file manually or use SETUP as any of the inputs
>Example settings.txt
```
y
f
```
`y` Indicates you want to save the current file and you will be asked to provide a desired `file name`
`f` For `female` voice

# Text To Speech - Python

Use `speak` to convert some text to speech
```py
from text_to_speech import speak

user_input = input("> ")
speak(user_input, 'female')
```
  
Use `speak(content, gender)` to turn text into speech and execute the speech

Use `save(content, filename, gender` to turn text into speech and save it in an mp3 file

Use `check_for_stop(user_input)` to check if the user input was "stop" or "s", if so, closes the file 

Use `check_for_setup(user_input)` to check if the user input was "setup", if so, begins creating a settings.txt

`content: str`
Text to convert to speech

`filename: str`
File name WITHOUT extension. All files will be mp3
>Default: `tts`

>Result: `tts.mp3`

`gender: str`
The gender of the voice
>Default: `male`
