import telebot 
from flask import Flask, request
from threading import Thread

bot=telebot.TeleBot("6529482461:AAHb7C9m4LKtc2g5JdP0QHP8i2Iazy5ofQM")

bot.send_message(1413725506, "HOLA")


@bot.message_handler(commands=["start", "help"])
def cmd_start(message):
  if not message.chat.type == "private":
    return
  bot.send_message(
      message.chat.id,
      "Hola! 😁, Bienvenido a <b>Last Botonera</b> bot.\nAquí se encuentran los canales afiliados a la botonera y por ende, a <a href='https://t.me/LastHopePosting'>Last Hope</a>\n\n\n<u>Los comandos disponibles (por ahora) son</u>:\n\n/mostrar Si quiere SOLICITAR los CANALES de la Botonera e <b>Información</b> sobre el tiempo restante de la PRÓXIMA PUBLICACIÓN de dicha botonera en sus CANALES afiliados\n\n/ingresar Si quiere INGRESAR su CANAL EN la BOTONERA\n\n/start o /help Para mostrar ESTE mensaje de ayuda\n\n\n\n<u>Nota:</u>\nSi quiere notificar algo o tiene alguna duda consulte con mi creador y guapetón propietario de Last Hope ( ͡° ͜ʖ ͡°)\n\n👉<a href='https://t.me/mistakedelalaif'>Reima</a>👈",
      parse_mode="html",
      disable_web_page_preview=True)
  #/promocionar LA MÁS FACHERA utilidad de este bot, escucha bien pepillo 🦻\nCon este comando puedes hacer pxp (promocion de tu canal a través de otro owner como tú) sin tener que acosar por privado al pobre muchacho (o muchacha, ve a ver tú) (¬‿¬) Simplemente me envias tu publicación de promoción, yo le pido que confirme si quiere hacer el pxp contigo y si acepta, directamente publico las promos en los respectivos canales. Como requisitos indispensables es que tanto tú como él me tienen que dar admin y permisos para publicar, el otro requisito es que ambos ya hayan hablado conmigo y no me tengan bloqueado ¿Qué esperas para comenzar? ಠ_ಠ




def polling():
  while True:
    try:
      bot.infinity_polling()
    except:
      pass

hilo=Thread(name="hilo", target=polling)
hilo.start()
