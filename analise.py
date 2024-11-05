import nltk

from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

start = SentimentIntensityAnalyzer()

texto = "I love this video, congrats"

sentimento = start.polarity_scores(texto)

print(sentimento)




