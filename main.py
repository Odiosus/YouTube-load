# подключаем библиотеки
from tkinter import *
from tkinter import ttk
import pytube
from tkinter import messagebox
from tkinter import font

# рисуем главное окно
root = Tk()
# размер и позиция окна
root.geometry("500x250+400+200")
root.resizable(False, False)
# заголовок окна
root.title("MY: YT-load")
# прозрачность окна
root.attributes("-alpha", 0.5)
# цвет фона
root.config(bg='#1f1f21')
font_all = font.Font(family="Arial", size=15, weight="normal", slant="roman")

label_style = ttk.Style()
label_style.configure("My.TLabel",  # имя стиля
                      font="Arial 13",  # шрифт
                      foreground="#fc5100",  # цвет текста
                      background="#1f1f1f")  # фоновый цвет


# механика кнопки Скачать
def download():
    # пробуем скачать видео по ссылке
    try:
        # формируем адрес
        ytlink = link1.get()
        # переводим его в нужный формат
        youtubelink = pytube.YouTube(ytlink)
        # получаем ссылку на видео с самым высоким качеством
        video = youtubelink.streams.get_highest_resolution()
        # скачиваем видео
        video.download()
        # выводим результат
        result = "Загрузка завершена"
        messagebox.showinfo("Готово", result)
    # если скачать не получилось
    except:
        # выводим сообщение об ошибке
        result = "Ссылка не работает"
        messagebox.showerror("Ошибка", result)


# при нажатии на кнопку очистки очищаем строку с адресом видео
def reset():
    link1.set("")


# при нажатии на кнопку выхода — закрываем окно с интерфейсом
def exit():
    root.destroy()


# заголовок формы
lb = ttk.Label(root, text="Загружаю видео с YouTube ", font=font_all, padding=8,
               background="#1f1f21", foreground="#fc5100")
lb.pack(pady=15)
# пояснительный текст для поля с адресом
lb1 = ttk.Label(root, text="Ссылка на видео:", font=font_all, background="#1f1f21", foreground="#fc5100")
lb1.place(x=10, y=80)

# поле ввода адреса видео
link1 = StringVar()
En1 = Entry(root, textvariable=link1, font=font_all, background="#1f1f1f", foreground="#fc5100")
En1.place(x=230, y=80)

# кнопка скачивания
btn_download = ttk.Button(root, text="Скачать", command=download, style="My.TLabel")
# расположение кнопки
btn_download.pack(anchor="n", pady=70)

# кнопки очистки и выхода
btn_reset = ttk.Button(root, text="Очистить", command=reset, style="My.TLabel")
btn_reset.place(x=160, y=190)
btn_exit = ttk.Button(root, text=" Выход ", command=exit, style="My.TLabel")
btn_exit.place(x=250, y=190)

# запускаем окно
root.mainloop()
