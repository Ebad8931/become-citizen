import Levenshtein

def evaluate_pronunciation(expected_text, recognized_text):

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


evaluate_pronunciation(
    'The quick brown fox jumps over the lazy dog.',
    'The quick brown fox jumps over the lazy dog.'
)

evaluate_pronunciation(
    'The quick brown fox jumps over the lazy dog.',
    'The quik brown fox jumped over the lazy dog.'
)

evaluate_pronunciation(
    'The quick brown fox jumps over the lazy dog.',
    'The slow green fox jumps over the tall cat.'
)

