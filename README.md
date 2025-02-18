# 3301-rune-to-latin
A simple Python script that converts runes to latin characters as seen in Cicada 3301's Gematria Primus.

# Requirements
This script requires Python 3.6 or higher. No additional libraries need to be installed.

# How To Run
1. **Open a terminal**
- On *Windows*, press *Win + R*, then type *"cmd"* and hit *Enter*.
- On Mac/Linux, open the Terminal application.

2. **Navigate to the script's directory, e.g. where you saved it.**
- If the file *converter.py* is located on your desktop, type the following command:
```
cd %UserProfile%\Desktop
```

3. **Run the script.**
```
python converter.py
```

# Usage
1. Run the script (for a detailed guide on how to do this, check **How To Run** above).
2. You will be prompted to enter a string of runes. The script will transliterate the runes to their corresponding Latin characters based on Cicada 3301's Gematria Primus.
3. If you enter a character that isn't part of the rune mapping of the script, it will be returned as is.
4. To exit the program, type 1234.

# Examples
### Example 1: Normal rune input.
```
LP Input: ᚠᚢᚦᚩᚱᚳ
Text in Latin: FVTHORC
```

### Example 2: Invalid character detected in user input.
```
LP Input: ᚠᚢᚦ&ᚩᚱᚳ
Text in Latin: FVTH&ORC
```

# Explanation
- *mappings* includes a list of runic characters and their latin equivalents as seen from the [Gematria Primus](https://uncovering-cicada.fandom.com/wiki/Gematria_Primus?file=Testout.jpg)
- The function *decode_runes(rune_text)* translates a given user input by looking up each rune in the *mappings*. If the rune letter has a set equivalent in latin, it returns the mapped latin character, otherwise it returns any special character as is.

# Short FAQ For Newbies

### What Is Cicada 3301, Liber Primus, etc?
Cicada 3301 is a mysterious group that became known for posting complex puzzles online, starting in 2012. These puzzles challenged participants with cryptography & steganography. The group's ultimate purpose remains unclear, but as mentioned in the beginning of each puzzle, they are looking for "highly intelligent individuals".

You can read more about Cicada 3301 on [The Uncovering Cicada Fandom](https://uncovering-cicada.fandom.com/wiki/Uncovering_Cicada_Wiki), which also includes attempts at solving Liber Primus, Cicada's latest unresolved puzzle from 2014.

### What Are Runes?
Runes (often called Futhark if all runic rows follow a specific alphabetical order) are an ancient script system. Their earliest use dates back to around AD 200, particularly among northern European regions in the Germanic culture. In this particular case, Cicada 3301 used already existing characters from several rune alphabets to create their own, full runic futhark. The 2014 unresolved puzzle, called the Liber Primus, is primarily written in runes.

You can find the whole Liber Primus transcript to copy [here](https://github.com/rtkd/iddqd/blob/master/liber-primus__transcription--master/liber-primus__transcription--master.txt), and the already existing transliteration [here](https://pastebin.com/27fCrwPv).
