
def score_input(test_name, test_score=0,
            invalid_message='Invalid test score, try again!'):
    """Validates and prints/returns parameters"""
    MIN_SCORE = 0
    MAX_SCORE = 100
    try:
        if test_score >= MIN_SCORE and test_score <= MAX_SCORE:
            print(test_name + ": 0")
            return {test_name:test_score}
        else:
            print(invalid_message)
            return invalid_message
    except TypeError:
        print(invalid_message)
        return invalid_message


