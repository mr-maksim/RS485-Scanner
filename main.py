import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports

# Функция для обновления списка доступных COM-портов
def update_ports():
    # Получаем список всех доступных COM-портов
    ports = serial.tools.list_ports.comports()
    com_combobox['values'] = [port.device for port in ports]

# Создаем главное окно
root = tk.Tk()

# Задаем ширину и высоту окна
width = 800
height = 600

# Устанавливаем размеры окна
root.geometry(f"{width}x{height}")

# Центрируем окно на экране
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width - width) / 2)
y_coordinate = int((screen_height - height) / 2)

# Перемещаем окно в центр экрана
root.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

root.title('RS485 Scanner')

# Фрейм для поиска устройств
search_frame = tk.LabelFrame(root, text='Поиск устройств')
search_frame.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')

## Фрейм для выбора COM порта
com_port_frame = tk.LabelFrame(search_frame, text='Выбор COM порта')
com_port_frame.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')

com_label = tk.Label(com_port_frame, text='COM Порт:')
com_label.grid(row=0, column=0, padx=5, pady=5)

com_combobox = ttk.Combobox(com_port_frame, values=[])
com_combobox.grid(row=0, column=1, padx=5, pady=5)

refresh_button = tk.Button(com_port_frame, text='Обновить', command=update_ports)
refresh_button.grid(row=0, column=2, padx=5, pady=5)

# Обновляем порты при запуске приложения
update_ports()

# Запускаем главный цикл приложения
root.mainloop()