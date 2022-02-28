questions_and_answers = {
    'question1': 'answer1', 
    'question2': 'answer2', 
    'question3': 'answer3',
    }

def ask_user(answers_dict):
    """
    Отвечает на три вопроса-ключа из словаря соответствующим значением. По команде quit прерывает работу. 
    """
    active = True
    while active:
        question = input('Задайте вопрос, либо напишите "стоп" для выхода ')
        for key, value in dict(answers_dict).items():
            if question == key:
                print(value)
        if question == 'стоп':
            active = False

if __name__ == "__main__":
    ask_user(questions_and_answers)