import flet as ft
import pyperclip

def main(page: ft.Page):
    page.title = "Encryption(and also decryption) machine"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)
    page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)

    Morse = {
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.',
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..',
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.',
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-',
        'Y': '-.--', 
        'Z': '--..', 
        '0': '-----', 
        '1': '.----', 
        '2': '..---',
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...',
        '8': '---..', 
        '9': '----.', 
        ' ': '/'
    }

    PolarCenit = {
        'P': 'C', 
        'O': 'E', 
        'L': 'N', 
        'A': 'I', 
        'R': 'T', 
        'C': 'P', 
        'E': 'O',
        'N': 'L', 
        'I': 'A', 
        'T': 'R'
    }

    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    input = ft.TextField(label="Write a message")
    output = ft.TextField(label="Result", read_only=True)

    EncryptionMethods = ft.Dropdown(label="Choose a method of encryption", value="Morse Code", options=[
        ft.dropdown.Option("Morse Code"),
        ft.dropdown.Option("A1Z26"),
        ft.dropdown.Option("Polar Cenit")
    ])

    def LettersToMorse(text):
        result = ""
        for char in text.upper():
            if char in Morse:
                result += Morse[char] + " "
            else:
                result += "? "
        return result.strip()

    def MorseToLetters(code):
        words = code.split(" ")
        result = ""
        for word in words:
            found = False
            for key in Morse:
                if Morse[key] == word:
                    result += key
                    found = True
                    break
            if not found:
                result += "?"
        return result

    def LettersToA1z26(text):
        result = ""
        for char in text.upper():
            if char in Alphabet:
                number = 1
                for letter in Alphabet:
                    if char == letter:
                        break
                    number += 1
                result += str(number) + " "
            else:
                result += "? "
        return result.strip()

    def a1z26ToLetters(code):
        numbers = code.split(" ")
        result = ""
        for num in numbers:
            found = False
            for i in range(26):
                if str(i + 1) == num:
                    result += Alphabet[i]
                    found = True
                    break
            if not found:
                result += "?"
        return result

    def LettersToPolar(text):
        result = ""
        for char in text.upper():
            if char in PolarCenit:
                result += PolarCenit[char]
            else:
                result += char
        return result

    def PolarToLetters(text):
        PolarCenitBackwards = {}
        for key in PolarCenit:
            PolarCenitBackwards[PolarCenit[key]] = key

        result = ""
        for char in text.upper():
            if char in PolarCenitBackwards:
                result += PolarCenitBackwards[char]
            else:
                result += char
        return result

    def EncryptAndDecrypt(encrypt):
        text = input.value.strip()
        if text == "":
            output.value = "Please enter a message!"
            page.update()
            return

        if EncryptionMethods.value == "Morse Code":
            if encrypt:
                output.value = LettersToMorse(text)
            else:
                output.value = MorseToLetters(text)

        elif EncryptionMethods.value == "A1Z26":
            if encrypt:
                output.value = LettersToA1z26(text)
            else:
                output.value = a1z26ToLetters(text)

        elif EncryptionMethods.value == "Polar Cenit":
            if encrypt:
                output.value = LettersToPolar(text)
            else:
                output.value = PolarToLetters(text)
        page.update()

    def copy_result(e):
        pyperclip.copy(output.value)
        output.value += "(result successfully copied)"
        page.update()

    page.add(ft.Column([
        input,
        EncryptionMethods,
        ft.Row([
            ft.ElevatedButton("Encrypt", on_click=lambda e: EncryptAndDecrypt(True)),
            ft.ElevatedButton("Decrypt", on_click=lambda e: EncryptAndDecrypt(False)),
            ft.ElevatedButton("Copy", on_click=copy_result)
        ]),
        output
    ]))

ft.app(target=main)