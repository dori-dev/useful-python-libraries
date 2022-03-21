"""googletrans library
"""
import googletrans
from googletrans import Translator
# pip install googletrans


print(googletrans.LANGUAGES)


gt = Translator()

response = gt.translate('سلام', 'en', 'fa')
print(response)
print(response.text)
print(response.src)
print(response.extra_data)

print(gt.translate('چطوری', 'ar'))

sentences = [
    'hello',
    'wow',
    'how are you',
    'it\'s good',
]

result = gt.translate(sentences, dest='fa', src='en')
print(result)

for sentence in result:
    print(sentence)
