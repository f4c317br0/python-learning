class MarvinMorseCoder:
    MORSE_CODE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    @staticmethod
    def encode(text):
        words = text.upper().split()
        new_txt = []
        for word in words:
            letters = [
                MarvinMorseCoder.MORSE_CODE[ch]
                for ch in word
                if ch in MarvinMorseCoder.MORSE_CODE
            ]
            new_txt.append(' '.join(letters))
        return '   '.join(new_txt)

    @staticmethod
    def decode(morse):
        reverse = {v: k for k, v in MarvinMorseCoder.MORSE_CODE.items()}
        words = morse.strip().split('   ')
        new_txt = []
        for word in words:
            letters = word.split(' ')
            decoded = ''.join(reverse.get(el, '?') for el in letters if el)
            new_txt.append(decoded)
        return ' '.join(new_txt)


print(MarvinMorseCoder.encode("HELLO"))
print(MarvinMorseCoder.decode(".... . .-.. .-.. ---"))
print(MarvinMorseCoder.encode("   hello   world   "))
print(MarvinMorseCoder.decode("..-. --- ---   -... .- .-."))
