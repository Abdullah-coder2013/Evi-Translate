from deep_translator import GoogleTranslator
language = input("Which Language to translate? (Enter in Code e.g. English=en, German=de): ")
word = input("Which Word/Sentence do you want to translate?: ")
translated = GoogleTranslator(source='auto', target=language).translate(word)
print(translated)