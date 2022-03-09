"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {
    'Как дела?': 'Хорошо!', 
    'Что делаешь?': 'Программирую!', 
    'Чем занят?': 'С тобой беседую!', 
    'Как настроение?': 'Отлично!'
    }

def ask_user(answers_dict):
  
  input_qwes = input('Введите вопрос: ')
   
  while True:
        
    if input_qwes == 'Как дела?':
      return answers_dict['Как дела?']
            
    
    elif input_qwes == 'Что делаешь?':
      return answers_dict['Что делаешь?']
            
    elif input_qwes == 'Чем занят?':
      return answers_dict['Чем занят?']
            
            
    elif input_qwes == 'Как настроение?':
      return answers_dict['Как настроение?']
            

    else:
      print('Пара ответ- вопрос не найдена!')
      break
            

        

print(ask_user(questions_and_answers))
    
if __name__ == "__ask_user__":
    ask_user(questions_and_answers)
