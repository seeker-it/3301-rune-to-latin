mappings = {
    'ᚠ': 'F', 'ᚢ': 'V', 'ᚦ': 'TH', 'ᚩ': 'O', 'ᚱ': 'R', 'ᚳ': 'C',
    'ᚷ': 'G', 'ᚹ': 'W', 'ᚻ': 'H', 'ᚾ': 'N', 'ᛁ': 'I', 'ᛄ': 'J',
    'ᛇ': 'EO', 'ᛈ': 'P', 'ᛉ': 'X', 'ᛋ': 'S', 'ᛏ': 'T', 'ᛒ': 'B',
    'ᛖ': 'E', 'ᛗ': 'M', 'ᛚ': 'L', 'ᛝ': 'NG', 'ᛟ': 'OE', 'ᛞ': 'D',
    'ᚪ': 'A', 'ᚫ': 'AE', 'ᚣ': 'Y', 'ᛡ': 'IA', 'ᛠ': 'EA'
}

def decode_runes(rune_text):
    decoded_text = "".join(mappings.get(char, char) for char in rune_text)
    return decoded_text

if __name__ == "__main__":
    while True:
        user_input = input("Enter LP runes: (or type '1234' to quit): ")
        if user_input.lower() == '1234':
            break
        translation = decode_runes(user_input)
        print("Text in latin:", translation)
        print(f"---------------------------------------------------------------------------------------------------------------------")
