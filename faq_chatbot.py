import nltk
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

faq_data = {

    "What is CodeAlpha?":
    "CodeAlpha is a software development company offering internships.",

    "How many tasks should I complete?":
    "You need to complete at least 2 or 3 tasks.",

    "Will I receive a certificate?":
    "Yes, after successful completion of internship requirements.",

    "How can I submit my project?":
    "Submit your project using the official submission form.",

    "Do I need to upload code to GitHub?":
    "Yes, upload your source code to GitHub repository.",

    "What is artificial intelligence?":
    "Artificial Intelligence is the simulation of human intelligence by machines."
}

questions = list(faq_data.keys())

def preprocess(text):
    text = text.lower()
    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )
    return text

vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(
    [preprocess(question) for question in questions]
)

def get_response(user_input):

    user_vector = vectorizer.transform(
        [preprocess(user_input)]
    )

    similarity_scores = cosine_similarity(
        user_vector,
        faq_vectors
    )

    best_match_index = similarity_scores.argmax()

    best_score = similarity_scores[0][best_match_index]

    if best_score > 0.2:
        return faq_data[questions[best_match_index]]

    return "Sorry, I couldn't find an answer."

print("\n===== FAQ CHATBOT =====")

while True:

    user_question = input("\nYou: ")

    if user_question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = get_response(user_question)

    print("Bot:", response)