# подключаем библиотеки
from tkinter import *
import pytube
from tkinter import messagebox

# рисуем главное окно
root = Tk()
# размер и позиция окна
root.geometry("500x350+400+200")
root.resizable(False, False)
# заголовок окна
root.title("MY: YT-load")
# цвет фона
root.config(bg='#D3D3D3')


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
        Result = "Загрузка завершена"
        messagebox.showinfo("Готово", Result)
    # если скачать не получилось
    except:
        # выводим сообщение об ошибке
        Result = "Ссылка не работает"
        messagebox.showerror("Ошибка", Result)


# при нажатии на кнопку очистки очищаем строку с адресом видео
def reset():
    link1.set("")


# при нажатии на кнопку выхода — закрываем окно с интерфейсом
def Exit():
    root.destroy()


# заголовок формы
lb = Label(root, text="Загружу видео с YouTube ", font=('Arial,15,bold'), bg='#D3D3D3')
lb.pack(pady=15)
# пояснительный текст для поля с адресом
lb1 = Label(root, text="Ссылка на видео :", font=('Arial,15,bold'), bg='#D3D3D3')
lb1.place(x=10, y=80)

# поле ввода адреса видео
link1 = StringVar()
En1 = Entry(root, textvariable=link1, font=('Arial,15,bold'))
En1.place(x=230, y=80)

# кнопка скачивания
btn1 = Button(root, text="Скачать", font=('Arial,10,bold'), bd=4, command=download)
btn1.place(x=330, y=130)

# кнопки очистки и выхода
btn2 = Button(root, text="Очистить", font=('Arial,10,bold'), bd=4, command=reset)
btn2.place(x=160, y=190)
btn3 = Button(root, text=" Выход ", font=('Arial,10,bold'), bd=4, command=Exit)
btn3.place(x=250, y=190)

# запускаем окно
root.mainloop()
