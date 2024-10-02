# Text to Morse code convertor dict

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '.......', '.': '.-.-.-'
}


# function to convert txt to morse
def to_morse(text):
    """ This fun will convert the given text to morse cord"""
    texts = text.upper()
    morse_word = ""
    for _ in range(len(texts)):
        morse_code = morse_code_dict[texts[_]]
        # print(f"{morse_code}", end=' ')
        morse_word += f"{morse_code} "
    return morse_word


# print(f"{morse_code_dict['A']} {morse_code_dict['b'.upper()]}")

# Get the input from the user to convert the text to morse code

text = input("Enter the text which you need to convert to morse : \n")
# print(text)

output = to_morse(text)

print(f"The text that you entered : \n{text}")
print("\n")
print(f"The relevant Morse code is : \n{output}")
