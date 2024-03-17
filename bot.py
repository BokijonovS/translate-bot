from data.loader import bot, db
import handlers



db.create_table_users()




if __name__ == '__main__':
    bot.infinity_polling()
