import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = '6093866073:AAHekHSXx2kGpMQ3N89sCiauoNDdwQuR3J4'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

tasks = []

def start(update, context):
    update.message.reply_text('Привет! Я TODO бот. Чем я могу помочь?')

def show_tasks(update, context):
    if tasks:
        task_list = '\n'.join(tasks)
        update.message.reply_text(f'Список задач:\n{task_list}')
    else:
        update.message.reply_text('Список задач пуст.')

def add_task(update, context):
    task = update.message.text.replace('/add ', '')
    tasks.append(task)
    update.message.reply_text(f'Задача "{task}" добавлена.')

def delete_task(update, context):
    index = int(update.message.text.replace('/delete ', ''))
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        update.message.reply_text(f'Задача "{deleted_task}" удалена.')
    else:
        update.message.reply_text('Недопустимый индекс задачи.')


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("tasks", show_tasks))
    dp.add_handler(CommandHandler("add", add_task))
    dp.add_handler(CommandHandler("delete", delete_task))

    # Запуск бота
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
