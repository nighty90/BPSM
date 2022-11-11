#!usr/local/bin/python

def ask_question(the_question, store_dict):
    val = input(the_question + "\n")
    store_dict[the_question] = val


if __name__ == "__main__":
    qa = {}
    question_set = [
        "What's your name?",
        "How old are you?",
        "What is your favourite colour?",
        "Do you like Python?",
        "The world is flat: True or False?"
    ]
    for question in question_set:
        ask_question(question, qa)

    for question, answer in qa.items():
        print(f"For question: {question}")
        print(f"Your answer is: {answer}")