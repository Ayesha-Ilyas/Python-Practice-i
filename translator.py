from googletrans import Translator
sentence=str(input("say....."))
translator=Translator()
translated_sentence=translator.translate(sentence,src='en',dest='ur')
print(translated_sentence.text)

