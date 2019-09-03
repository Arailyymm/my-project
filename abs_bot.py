# -*- coding: utf-8 -*-
import requests
import datetime
import pandas as pd
import telebot
class abs_bot():
    
    def __init__(self,token):
        self.api_url = "https://api.telegram.org/bot"+token+"/"
        self.token=token
        
    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        #print (result_json)
        return result_json
    

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp
    
    def forward_message(self, chat_id, from_id, mess_id):
        params = {'chat_id': chat_id, 'from_chat_id': from_id, 'message_id': mess_id }
        method = 'forward_message'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
            return last_update
       

       

token="807664295:AAH32rsgIaVbJrgQ2GCOQuKUoXhsVmQmT9c"
bot = abs_bot(token)  
data = pd.read_excel("greetings.xlsx")
now = datetime.datetime.now()
admission_id='418148602'
bot2=telebot.TeleBot(token)


#print((data[data['Greetings'] == 'привет']).count()[0])

def main():  
    new_offset = None
    hour = now.hour
    
    while True:
        bot.get_updates(new_offset)
        last_update = bot.get_last_update()
        if(type(last_update) == type({}) and ('message' in last_update or 'callback_query' in last_update)):
            last_update_id = last_update['update_id']
            
            if('callback_query' in last_update):
                callback_query = last_update['callback_query']
                from_id=last_update['callback_query']['from']['id']
                
                #print(callback_query)
              
                callback_data=callback_query['data']
               
                    
                
                if(callback_data == 'поступление'):
                    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                    button = telebot.types.InlineKeyboardButton(text='Как поступить на грант', 
                                                                    callback_data='как поступить на грант')
                    button2 = telebot.types.InlineKeyboardButton(text='Cписок обязательных документов', 
                                                                    callback_data='cписок обязательных документов')
                    markup.add(button)
                    markup.add(button2)
                        
                    bot2.send_message(chat_id=from_id, 
                                        text='Вопросы о поступлении',reply_markup=markup)
                elif(callback_data == 'студентам'):
                    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                    button3 = telebot.types.InlineKeyboardButton(text='Учебный процесс' ,
                                                                  callback_data='Учебный процесс'  )
                    
                    
                    button4 = telebot.types.InlineKeyboardButton(text='Дом студентов', 
                                                                    callback_data='Дом студентов' )
                    
                    
                    ##
                    button5 = telebot.types.InlineKeyboardButton(text='Студенческая клиника', 
                                                                    callback_data='Студенческая клиника')
                    button6 = telebot.types.InlineKeyboardButton(text='Военная кафедра', 
                                                                    callback_data='Военная кафедра')
                    button7 = telebot.types.InlineKeyboardButton(text='Практика и стажировки', 
                                                                    callback_data='Практика и стажировкит')
                   
                    
                    
                    ##
                    markup.add(button3)
                    markup.add(button4)
                    ##
                    markup.add(button5)
                    markup.add(button6)
                    markup.add(button7)
                    
                    
                    ##
                        
                    bot2.send_message(chat_id=from_id, 
                                        text='Часто задаваемые вопросы',reply_markup=markup)
                elif (callback_data=='Учебный процесс'):
                    markup=telebot.types.InlineKeyboardMarkup(row_width=2)
                    button21= telebot.types.InlineKeyboardButton(text='Летник',callback_data='Летник')
                    button20= telebot.types.InlineKeyboardButton(text='Пересдача',callback_data='Пересдача')
                    button22= telebot.types.InlineKeyboardButton(text='Стипендия',callback_data='Стипендия')
                    markup.add(button21)
                    markup.add(button20)
                    markup.add(button22)
                        
                    bot2.send_message(chat_id=from_id, 
                                        text='вопросы: Раздел Учебный процесс',reply_markup=markup)
                
                elif (callback_data=='Дом студентов'):
                    markup=telebot.types.InlineKeyboardMarkup(row_width=2)
                    button25= telebot.types.InlineKeyboardButton(text='GPA',callback_data='GPA')
                    button26= telebot.types.InlineKeyboardButton(text='Восстановление документов',callback_data='Дом студентов')
                    button27= telebot.types.InlineKeyboardButton(text='Платники',callback_data='Платники')
                    markup.add(button25)
                    markup.add(button26)
                    markup.add(button27)
                    bot2.send_message(chat_id=from_id, 
                                        text='вопросы: Раздел Дом студентов',reply_markup=markup)
                    
                    
                elif (callback_data=='Студенческая клиника'):
                    markup=telebot.types.InlineKeyboardMarkup(row_width=2)
                    button30= telebot.types.InlineKeyboardButton(text='Адрес',callback_data='Адрес')
                    button31= telebot.types.InlineKeyboardButton(text='Прикрепление к поликлиннике',callback_data='Прикрепление')
                    markup.add(button30)
                    markup.add(button31)
                    bot2.send_message(chat_id=from_id, 
                                        text='вопросы: Раздел Студенческая клиника',reply_markup=markup)
                    
                    ##tut
                   
                elif (callback_data=='Летник'):
                    markup=telebot.types.InlineKeyboardMarkup(row_width=2)
                    button35= telebot.types.InlineKeyboardButton(text='Код Услуги',callback_data='Код услуги(летник)')
                    button36= telebot.types.InlineKeyboardButton(text='Стоимость',callback_data='Стоимость(летник)')
                    button37= telebot.types.InlineKeyboardButton(text='Период летника',callback_data='Период летник')

                    button37= telebot.types.InlineKeyboardButton(text='Случаи летника',callback_data='Reretake')
                    button38= telebot.types.InlineKeyboardButton(text='Бал',callback_data='Бал')

                    markup.add(button35)
                    markup.add(button36)
                    markup.add(button37)
                    markup.add(button38)
                    bot2.send_message(chat_id=from_id, 
                                        text='вопросы: Раздел Летник',reply_markup=markup)
            
                elif (callback_data=='Пересдача'):
                    markup=telebot.types.InlineKeyboardMarkup(row_width=2)
                    button40= telebot.types.InlineKeyboardButton(text='Код Услуги',callback_data='Код услуги(пересдачи)')
                    button41= telebot.types.InlineKeyboardButton(text='Стоимость',callback_data='Стоимость(пересдачи)')
                    button42= telebot.types.InlineKeyboardButton(text='Время пересдачи',callback_data='Время')
                    
                    markup.add(button40)
                    markup.add(button41)    
                    markup.add(button42)
                    bot2.send_message(chat_id=from_id,      
                                        text='вопросы: Раздел Пересдача',reply_markup=markup)
                
                elif (callback_data=='Стипендия'):
                    markup=telebot.types.InlineKeyboardMarkup(row_width=2)
                    button45= telebot.types.InlineKeyboardButton(text='Бал',callback_data='Бал стипендии')
                    button46= telebot.types.InlineKeyboardButton(text='Президентская стипендия',callback_data='Президентская')
                    button47= telebot.types.InlineKeyboardButton(text='Карта',callback_data='Карта')
                    
                    markup.add(button45)
                    markup.add(button46)    
                    markup.add(button47)
                    bot2.send_message(chat_id=from_id,      
                                        text='вопросы: Раздел Стипендия',reply_markup=markup)
                
                elif (callback_data=='GPA'):
                    markup=telebot.types.InlineKeyboardMarkup(row_width=2)
                    button50= telebot.types.InlineKeyboardButton(text='Оценка',callback_data='Оценка')
                    button51= telebot.types.InlineKeyboardButton(text='Транскрипт',callback_data='Транскрипт')
                    button52= telebot.types.InlineKeyboardButton(text='Как посчитать GPA',callback_data='Считать')
                    
                    markup.add(button50)
                    markup.add(button51)    
                    markup.add(button52)
                    bot2.send_message(chat_id=from_id,      
                                        text='вопросы: Раздел Стипендия',reply_markup=markup)
                    
                elif (callback_data=='Восстановление документов'):
                    markup=telebot.types.InlineKeyboardMarkup(row_width=2)
                    button55= telebot.types.InlineKeyboardButton(text='Студенческий билет',callback_data='Студенческий билет')
                    button56= telebot.types.InlineKeyboardButton(text='Банковская карта',callback_data='Банковская карта')
                    button57= telebot.types.InlineKeyboardButton(text='Онай',callback_data='Онай')
                    
                    markup.add(button55)
                    markup.add(button56)    
                    markup.add(button57)
                    bot2.send_message(chat_id=from_id,      
                                        text='вопросы: Раздел Восстановление документов',reply_markup=markup)    
                
                elif (callback_data=='Платники'):
                    markup=telebot.types.InlineKeyboardMarkup(row_width=2)
                    button60= telebot.types.InlineKeyboardButton(text='Оплата учебы',callback_data='Оплата учебы')
                    button61= telebot.types.InlineKeyboardButton(text='Грант',callback_data='Грант')
                    button62= telebot.types.InlineKeyboardButton(text='Переводы',callback_data='Переводы')
                    
                    markup.add(button60)
                    markup.add(button61)    
                    markup.add(button62)
                    bot2.send_message(chat_id=from_id,      
                                        text='вопросы: Раздел Восстановление документов',reply_markup=markup)
                
                
                elif (callback_data=='Военная кафедра'):
                    markup=telebot.types.InlineKeyboardMarkup(row_width=2)
                    button70= telebot.types.InlineKeyboardButton(text='Военная кафедра',callback_data='Военка')
                    
                     
                    markup.add(button70)
                    bot2.send_message(chat_id=from_id,      
                                        text='вопросы: Раздел Военная кафедра',reply_markup=markup) 
                elif (callback_data=='Практика и стажировка'):
                    markup=telebot.types.InlineKeyboardMarkup(row_width=2)
                    button80= telebot.types.InlineKeyboardButton(text='Практика и стажировка',callback_data='Практика')
                    
                    markup.add(button80)
                
                    bot2.send_message(chat_id=from_id,      
                                        text='вопросы: Раздел  Практика и стажировка',reply_markup=markup)
                else:
                   questions=pd.read_excel("questions.xlsx")
                   
                   questions_1=questions[questions['Questions'] == callback_data]
                   if(questions_1.count()[0] >= 1):
                        answer=questions_1.iloc[0]['Answers']
                        bot.send_message(from_id, answer)
                   else:
                       try:
                            words=callback_data.split()
                            for word in words:
                                questions_2=questions[questions['Questions'] == word]
                                if(questions_2.count()[0] >= 1):
                                    answer=questions_2.iloc[0]['Answers']
                                    bot.send_message(from_id, answer)
                                    break
                       except:
                            pass

                
                
                
            else:
                last_chat_id = last_update['message']['chat']['id']
                last_mess_id = last_update['message']['message_id']
                if('text' in last_update['message']):
                    last_chat_text = last_update['message']['text']
                    last_chat_name = last_update['message']['chat']['first_name']
                    mess=last_chat_text.lower()
                    questions=pd.read_excel("questions.xlsx")
                    questions_1=questions[questions['Questions'] == mess]
                    gr=data[data['Greetings'] == mess].count()[0] >= 1
                    answered=False
                    
                
                 
                    if (gr  and 6 <= hour < 12):
                            bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
                       
    
                    elif (gr and 12 <= hour < 17):
                        bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
    
                    elif (gr and 17 <= hour <= 23):
                        bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
                    
                    elif (gr and hour < 6):
                        bot.send_message(last_chat_id, 'Доброй ночи, {}'.format(last_chat_name))
                    
                    elif(questions_1.count()[0] >= 1):
                        answer=questions_1.iloc[0]['Answers']
                        bot.send_message(last_chat_id, answer)
                    
                    
                    elif(mess=='data'):
                        bot.send_message(last_chat_id, 'Доброй ночи, {}'.format(last_chat_name))
                        
                   
                    elif(mess == '/help' or mess=='/start'):
    
                        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
                        button = telebot.types.InlineKeyboardButton(text='Поступающим', 
                                                                    callback_data='поступление')
                        
                        
                        
                        button1 = telebot.types.InlineKeyboardButton(text='Студентам', 
                                                                    callback_data='студентам')
                        markup.add(button)
                        markup.add(button1)
                        
                        bot2.send_message(chat_id=last_chat_id, 
                                        text='Отправьте боту вопрос и он ответит на него',reply_markup=markup)
                    
                    else:
                       try:
                            words=mess.split()
                            for word in words:
                                print(word)
                                questions_2=questions[questions['Questions'] == word]
                                if(questions_2.count()[0] >= 1):
                                    answer=questions_2.iloc[0]['Answers']
                                    bot.send_message(last_chat_id, answer)
                                    answered=True
                                    break
                       except Exception as error:
                            #print(error)
                            pass
                        
                    if answered==False:
                        
                        bot2.forward_message(admission_id, last_chat_id,last_mess_id)
                        
                else:
                    
                    bot2.forward_message(admission_id, last_chat_id,last_mess_id)
                    
       
            new_offset = last_update_id + 1
            


if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()

