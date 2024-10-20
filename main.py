import tkinter as tk

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



# Запускаем главный цикл приложения
root.mainloop()