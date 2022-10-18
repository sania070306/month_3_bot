from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, extra, FsmMentor

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
FsmMentor.register_handlers_fsm_list_of_mentors(dp)

extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
