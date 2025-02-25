import Levenshtein

def evaluate_pronounciation_levenshtein(expected_text, recognized_text):

     # Calculate Levenshtein distance between expected and recognized speech
    distance = Levenshtein.distance(expected_text, recognized_text)

    print(distance)
    
    # Define a threshold for "close match" (you can adjust this based on testing)
    threshold = 5  # Adjust this based on your test results
    
    if distance == 0:
        print("Excellent pronunciation!")
    elif distance <= threshold:
        print("You're close! Keep practicing.")
    else:
        print("Try again, you're a bit off.")


def evaluate_pronounciation(expected_text,user_text):
    """Compares the user's spoken text with the expected text and provides feedback."""
    if not user_text:
        print("No speech detected. Try again!")
    
    expected_words = set(expected_text.lower().split())
    user_words = set(user_text.lower().split())

    correct_words = expected_words & user_words

    if len(correct_words) / len(expected_words) > 0.8:
        print("Great job! Your pronunciation is close to perfect.")
    elif len(correct_words) / len(expected_words) > 0.5:
        print("Good effort! Some words could be clearer.")
    else:
        print("Try again! Focus on clearer pronunciation.")


evaluate_pronounciation_levenshtein(
    'The quick brown fox jumps over the lazy dog.',
    'The quick brown fox jumps over the lazy dog.'
)

evaluate_pronounciation_levenshtein(
    'The quick brown fox jumps over the lazy dog.',
    'The quik brown fox jumped over the lazy dog.'
)

evaluate_pronounciation_levenshtein(
    'The quick brown fox jumps over the lazy dog.',
    'The slow green fox jumps over the tall cat.'
)

evaluate_pronounciation(
    'The quick brown fox jumps over the lazy dog.',
    'The quick brown fox jumps over the lazy dog.'
)

evaluate_pronounciation(
    'The quick brown fox jumps over the lazy dog.',
    'The quik brown fox jumped over the lazy dog.'
)

evaluate_pronounciation(
    'The quick brown fox jumps over the lazy dog.',
    'The slow green fox jumps over the tall cat.'
)
