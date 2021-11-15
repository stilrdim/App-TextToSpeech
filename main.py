from text_to_speech import save, speak, SETTINGS_FILE, check_for_setup, check_for_stop, create_settings

print("""
 _______________________________________________________
|                Welcome to TextToSpeech                |
|                                                       |
| Type "STOP" or "S" to exit at any time.               |
| These inputs are NOT case sensitive.                  |
|                                                       |
| You can create a settings.txt file with each setting  |
| on a new line to avoid retyping them every time or    |
| use "SETUP" as any of the inputs.                     |
|                                                       |
|                                                       |
| Examples:     y                                       |
|              Yes                                      |
|                                                       |
|                                                       |
|                                  Copyright Stil 2021  |
|_______________________________________________________|
                 https://github.com/stilrdim/TextToSpeech\n\n
""")

try:
    with open(SETTINGS_FILE, 'r+') as f:
        file_content = f.read()

    # settings = file_content.split('\n')
    settings = file_content

    save_or_not = settings[0]

# Settings file not found
except FileNotFoundError:
    save_or_not = input("Save the text in a file? [Y]es/[N]o\n").lower()
    check_for_stop(save_or_not)
    check_for_setup(save_or_not)
    if save_or_not == '':
        save_or_not = 'n'
        print(save_or_not)

    # Hardcoded settings
    suffix = 1
except IndexError:
    create_settings(SETTINGS_FILE)
    save_or_not = 'n'  # Just to stop the IDE warning

print('Current settings: %s' % save_or_not)

while True:
    contents = []
    while True:
        user_input = input('> ')
        if user_input == '':
            break
        check_for_stop(user_input)
        check_for_setup(user_input)
        contents.append(user_input)

    user_input = " ".join(contents)

    # Run
    if save_or_not[0] == 'n':
        speak(content=user_input)

    # Run and Save
    if save_or_not[0] == 'y':
        tts_filename = input('File name:\t\t\tExample: new_file\n')
        save(content=user_input, filename=tts_filename)

