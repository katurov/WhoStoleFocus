#!/usr/bin/python                                                                                                       

'''
    Эта программа помогла мне разобраться, какое приложение перехватывает на себя фокус ввода и "съедает" часть набранного на клавиатуре текста. 

    Работа строится на том, что проверяется текущее приложение и если оно отличается от предыдущего - выводится в лог на экране. 
    Таким образом, что-то, что моргнет медленее третьей доли секунды - будет залогированно. Достаточно дождаться "мигания" и 
    просто посмотреть в лог.

    Как я вижу возможное развитие такой программы - в логирование текущего приложения для, например, автоматического учета "на что я трачу время".

    ВАЖНО: для запуска нужен системный PYTHON, а не тот, что ставится руками или из пакета (все дело в библиотеках - тому предоставляется доступ).
'''

try:
    from AppKit import NSWorkspace
except ImportError:
    print "Can't import AppKit -- maybe you're running python from brew?"
    print "Try running with Apple's /usr/bin/python instead."
    exit(1)

from datetime import datetime
from time import sleep

last_active_name = None
while True:
    active_app = NSWorkspace.sharedWorkspace().activeApplication()
    if active_app['NSApplicationName'] != last_active_name:
        last_active_name = active_app['NSApplicationName']
        print '%s: %s [%s]' % (
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            active_app['NSApplicationName'],
            active_app['NSApplicationPath']
        )
    sleep(0.3)