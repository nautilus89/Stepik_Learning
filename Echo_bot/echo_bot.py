import telebot, datetime, requests
from telebot import types

bot_token = "1377725317:AAFJhHA9qrhQTIT5HZF0syrzDrPCN8LonSc"
bot = telebot.TeleBot(bot_token)
chat_id = '462513717'
now = datetime.datetime.now()     

######################################################################### WEATHER #####################################################################################

api_url = 'https://api.openweathermap.org/data/2.5/weather'

months = {    1:"Jan",
              2:"Feb",
              3:"Mar",
              4:"Apr",
              5:"May",
              6:"Jun",
              7:"Jul",
              8:"Aug",
              9:"Sep",
             10:"Oct",
             11:"Nov",
             12:"Dec"     }

thunderstorm =  u'\U0001F4A8'    # Code: 200's, 900, 901, 902, 905
drizzle =       u'\U0001F4A7'    # Code: 300's
rain =          u'\U00002614'    # Code: 500's
snowflake =     u'\U00002744'    # Code: 600's snowflake
snowman =       u'\U000026C4'    # Code: 600's snowman, 903, 906
atmosphere =    u'\U0001F301'    # Code: 700's foogy
clearSky =      u'\U00002600'    # Code: 800 clear sky
fewClouds =     u'\U000026C5'    # Code: 801 sun behind clouds
clouds =        u'\U00002601'    # Code: 802-803-804 clouds general
hot =           u'\U0001F525'    # Code: 904
defaultEmoji =  u'\U0001F300'    # default emojis
sunRiseEmoji =  u'\U0001F305'
sunSetEmoji =   u'\U0001F307'

def get_city(mes):
    city = "Moscow, RU"
    if (mes != "/w"):
        #city = mes[3:]
        city = mes
    return city

def get_weather(current_location):
    params = {
        'q': current_location,
        'appid': '7eb93f32a9e0bd6a154e87447fbfded6',
        'units': 'metric'
    }
    try:
        res = requests.get(api_url, params = params)
        data = res.json()
        #print(data)
        cur_day = str(datetime.date.today().day)
        cur_mon = months[datetime.date.today().month]
        sunrise_time = str(datetime.datetime.fromtimestamp(data['sys']['sunrise']))
        sunset_time = str(datetime.datetime.fromtimestamp(data['sys']['sunset']))
    
        str_1 = str(data['name'] + ", " + data['sys']['country'])
        str_2 = '\nToday: ' + cur_day + " " + cur_mon + " " + get_emoji(data['weather'][0].get('id')) + " " + data['weather'][0].get('main')
        str_3 = '\nCurrent temp: ' + str(int(data['main']['temp']))
        str_4 = '\nTemp MIN: ' + str(data['main']['temp_min'])
        str_5 = '\nTemp MAX: ' + str(data['main']['temp_max'])
        str_6 = '\n' + sunRiseEmoji + ' Sunrise at: ' + sunrise_time[11:16]
        str_7 = '\n' + sunSetEmoji + ' Sunset at: ' + sunset_time[11:16]
        return(str_1 + str_2 + str_3 + str_4 + str_5 + str_6 + str_7)
    except KeyError:
        return('Error. Try again')

def get_emoji(weather_id):
    if weather_id:
        if str(weather_id)[0] == '2' or weather_id == 900 or weather_id==901 or weather_id==902 or weather_id==905:
            return thunderstorm
        elif str(weather_id)[0] == '3':
            return drizzle
        elif str(weather_id)[0] == '5':
            return rain
        elif str(weather_id)[0] == '6' or weather_id==903 or weather_id== 906:
            return snowflake + ' ' + snowman
        elif str(weather_id)[0] == '7':
            return atmosphere
        elif weather_id == 800:
            return clearSky
        elif weather_id == 801:
            return fewClouds
        elif weather_id==802 or weather_id==803 or weather_id==803:
            return clouds
        elif weather_id == 904:
            return hot
        else:
            return defaultEmoji    # Default emoji

    else:
        return defaultEmoji   # Default emoji

#######################################################################################################################################################################
def draw_pane(id):
    global pane_number
    if (id == 1):
        pane_number = 1;
        markup = types.ReplyKeyboardMarkup()
        itembtn1 = types.KeyboardButton('start')
        markup.add(itembtn1)
        bot.send_message(chat_id, "Hello. Let's start!", reply_markup=markup)

    elif (id == 2):
        pane_number = 2;
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('weather')
        itembtn2 = types.KeyboardButton('torrent')
        markup.add(itembtn1, itembtn2)
        bot.send_message(chat_id, "Choose what you want:", reply_markup=markup)

    elif (id == 3):
        pane_number = 3;
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('ok')
        itembtn2 = types.KeyboardButton('change location')
        markup.add(itembtn1, itembtn2)
        bot.send_message(chat_id, "Choose what you want:", reply_markup=markup)

    elif (id == 4):
        pane_number = 4;
        bot.send_message(chat_id, "I can find movies for you. Parameters are: Full HD or 4K video quality and Russian dub translate. Enter movie's name (for example, Avengers):")

def find_movie(name):
    movie1 = name + ' 1080P DUB'
    movie2 = name + ' 2160P DUB'
    print(movie1 + '/' + movie2)

draw_pane(1)

#@bot.message_handler(commands=['start', 'help'])
@bot.message_handler(content_types=['text'])
def send_message(message):
    if (message.text == 'start'):
        bot.reply_to(message, "Commands:\n"
                                 "/weather /w shows the weather in yor city, default: Moscow, RU\n"
                                 "/time /date shows current time and date")
        draw_pane(2)
    elif (message.text == 'weather'):    
        bot.reply_to(message, get_weather(get_city('/w')))
        draw_pane(3)
    elif (message.text == 'ok'):
        draw_pane(2)
    elif (message.text == 'change location'):
        bot.send_message(chat_id, "type your location")
    elif (pane_number == 3 and message.text != ''):
        bot.reply_to(message, get_weather(get_city(message.text)))
    elif (message.text == 'torrent'):
        draw_pane(4)
    elif (pane_number == 4 and message.text != ''):
        find_movie(message.text)    

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)

#@bot.message_handler(commands=['time', 'date'])
#def send_time(message):
#    bot.reply_to(message, str(now))

#@bot.message_handler(commands=['weather', 'w'])
#def send_weather(message):    
#    bot.reply_to(message, get_weather(get_city(message.text)))
	
bot.polling()
