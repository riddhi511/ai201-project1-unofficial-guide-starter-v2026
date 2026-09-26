QUESTIONS = [
    {
        "question": "Is the housing lottery random?",
        "expects": "credit hours"
    },
    {
        "question": "What do students say about dining hall wait times?",
        "expects": "wait"
    },
    {
        "question": "Which dorms are closest to campus?",
        "expects": "dorm"
    },
    {
        "question": "How do students get parking permits?",
        "expects": "permit"
    },
    {
        "question": "What happens if you miss course registration?",
        "expects": "registration"
    },
]

OUT_OF_SCOPE = [
    "What is the best restaurant in Paris?",
    "How do I file federal taxes?",
    "Who won the 2024 World Cup?",
    "What is the speed of light?",
    "How do I train a neural network?",
]


def answered():
    """Return questions that have both a question and an expects field."""
    return [q for q in QUESTIONS if q.get("question") and q.get("expects")]