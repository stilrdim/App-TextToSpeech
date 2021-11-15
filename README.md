# Text to speech
###### Simple text to speech CLI app using `pyttsx3`

### Save the text in a file? [Y]es/[N]o?
`Inputs:`
`Y` `N` `SETUP`

##
### You can create a settings.txt file manually or use SETUP as any of the inputs
>Example settings.txt
```
y
```
`y` Indicates you want to save the current file and you will be asked to provide a desired `file name`

# Text To Speech - Python

Use `speak` to convert some text to speech
```py
from text_to_speech import speak

user_input = input("> ")
speak(user_input)
```
  
Use `speak(content: String)` to turn text into speech and execute the speech

Use `save(content: String, filename: String` to turn text into speech and save it in an mp3 file

Use `check_for_stop(user_input: String)` to check if the user input was "stop" or "s", if so, closes the file 

Use `check_for_setup(user_input: String)` to check if the user input was "setup", if so, begins creating a settings.txt

`content: String`
Text to convert to speech

`filename: String`
File name WITHOUT extension. All files will be mp3
>Default: 'tts'

>Result: 'tts.mp3'
