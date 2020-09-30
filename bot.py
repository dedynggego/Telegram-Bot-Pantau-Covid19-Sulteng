import telebot
import data
import rumah_sakit

indo = data.indo1()
sulteng = data.prov()

api = '1310183418:AAEyGWIoq_G5HVCo5OyMhae3juw3pnAzOVQ'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome guys..')

@bot.message_handler(commands=['indo'])
def data_indo(message):
    positif = ''
    sembuh = ''
    dirawat = ''
    meninggal = ''
    tambahan_pos = ''
    tambahan_semb = ''
    tambahan_dirawat = ''
    tambahan_meni = ''

    for i in indo:
        positif = i['total']['positif']
        sembuh = i['total']['sembuh']
        dirawat = i['total']['dirawat']
        meninggal = i['total']['meninggal']
        tambahan_pos = i['penambahan']['positif']
        tambahan_semb = i['penambahan']['sembuh']
        tambahan_dirawat = i['penambahan']['dirawat']
        tambahan_meni = i['penambahan']['meninggal']
    
    data = "Data Covid19 di Indonesia sekarang:\n Positif: {} orang\n Sembuh: {} orang\n Dirawat: {} orang\n Meninggal: {} orang\n\n\n Penambahan:\n Positif: {}\n Sembuh: {}\n Dirawat: {}\n Meninggal: {}\n".format(positif,sembuh,dirawat,meninggal, tambahan_pos, tambahan_semb, tambahan_dirawat, tambahan_meni)
    bot.reply_to(message, data)

@bot.message_handler(commands=['sulteng'])
def data_sulteng(message):
    positif = ''
    sembuh = ''
    dirawat = ''
    meninggal = ''
    tambahan_pos = ''
    tambahan_semb = ''
    tambahan_dirawat = ''
    tambahan_meni = ''

    for i in sulteng:
        positif = i['kasus']
        sembuh = i['sembuh']
        dirawat = i['dirawat']
        meninggal = i['meninggal']
        tambahan_pos = i['penambahan']['positif']
        tambahan_semb = i['penambahan']['sembuh']
        tambahan_meni = i['penambahan']['meninggal']
    
    data = "Data Covid19 di Sulawesi Tengah sekarang:\n Positif: {} orang\n Sembuh: {} orang\n Dirawat: {} orang\n Meninggal: {} orang\n\n\n Penambahan:\n Positif: {}\n Sembuh: {}\n Meninggal: {}\n".format(positif,sembuh,dirawat,meninggal, tambahan_pos, tambahan_semb, tambahan_meni)
    bot.reply_to(message,data)

@bot.message_handler(commands=['rs'])
def rumahsakit(message):
    undata = rumah_sakit.undata()
    anutapura = rumah_sakit.anutapura()
    toli_toli = rumah_sakit.toli_toli()
    kolonodale = rumah_sakit.kolodale()
    banggai = rumah_sakit.banggai()
    data = "Daftar rumah sakit rujukan Covid-19 Sulteng: \n\n {}\n\n {}\n\n {}\n\n {}\n\n {}".format(undata, anutapura,toli_toli,kolonodale,banggai)
    bot.reply_to(message, data)


bot.polling()
