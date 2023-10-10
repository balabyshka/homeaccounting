import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# from tkinter import *
# from tkinter import ttk

# Создайте подключение к базе данных MySQL
db = mysql.connector.connect(
    host="localhost",
    user="alex",
    password="alex67",
    database="home_acc_main_v1"
)


# date DATE,
# description VARCHAR(255),
# amount DECIMAL(10, 2),
# typeacc VARCHAR(255),
# currency varchar(3),
# extra VARCHAR(255),
# category VARCHAR(255)

# Функция для добавления записи в БД траты
def add_cost():
    date = entry_date.get()
    description = entry_description.get()
    amount = entry_amount.get()
    typeacc = entry_typeacc.get()
    currency = entry_currency.get()
    extra = entry_extra.get()
    category = entry_category.get()

    cursor = db.cursor()
    query = "INSERT INTO table_out (date, description, amount, typeacc, currency, extra, category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (date, description, amount, typeacc, currency, extra, category)

    cursor.execute(query, values)
    db.commit()
    cursor.close()

    messagebox.showinfo("Успешно", "Запись добавлена")
    # clear_entries()
    update_table()

# Функция для добавления записи в БД приход


def add_income():
    date = entry_date.get()
    description = entry_description.get()
    amount = entry_amount.get()
    typeacc = entry_typeacc.get()
    currency = entry_currency.get()
    extra = entry_extra.get()
    category = entry_category.get()

    cursor = db.cursor()
    query = "INSERT INTO table_in (date, description, amount, typeacc, currency, extra, category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (date, description, amount, typeacc, currency, extra, category)

    cursor.execute(query, values)
    db.commit()
    cursor.close()

    messagebox.showinfo("Успешно", "Запись добавлена")
    # clear_entries()
    update_table2()

# Функция для очистки полей ввода


def clear_entries():
    entry_date.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_typeacc.delete(0, tk.END)
    entry_currency.delete(0, tk.END)
    entry_extra.delete(0, tk.END)
    entry_category.delete(0, tk.END)


# Функция для обновления отображения таблицы


def update_table():
    cursor = db.cursor()
    query = "SELECT * FROM table_out ORDER BY id DESC LIMIT 10"
    cursor.execute(query)
    expenses = cursor.fetchall()
    cursor.close()

    for i in tree.get_children():
        tree.delete(i)

    for expense in expenses:
        tree.insert("", "end", values=expense)

# Функция для обновления отображения таблицы 002 income money


def update_table2():
    cursor = db.cursor()
    query = "SELECT * FROM table_in ORDER BY id DESC LIMIT 10"
    cursor.execute(query)
    expenses = cursor.fetchall()
    cursor.close()

    for i in tree2.get_children():
        tree2.delete(i)

    for expense in expenses:
        tree2.insert("", "end", values=expense)

# Функция для удаления выбранной записи


def delete_expense():
    selected_item = tree.selection()
    if selected_item:
        expense_id = tree.item(selected_item, "values")[0]
        cursor = db.cursor()
        query = "DELETE FROM table_out WHERE id = %s"
        cursor.execute(query, (expense_id,))
        db.commit()
        cursor.close()
        update_table()


def delete_expense2():
    selected_item = tree2.selection()
    if selected_item:
        expense_id = tree2.item(selected_item, "values")[0]
        cursor = db.cursor()
        query = "DELETE FROM table_in WHERE id = %s"
        cursor.execute(query, (expense_id,))
        db.commit()
        cursor.close()
        update_table2()

# Функция для редактирования выбранной записи COST money - ВИТРАТ


def edit_expense():
    selected_item = tree.selection()
    if selected_item:
        expense_id = tree.item(selected_item, "values")[0]
        new_amount = entry_amount.get()
        new_typeacc = entry_typeacc.get()
        new_date = entry_date.get()
        new_description = entry_description.get()
        new_currency = entry_currency.get()
        new_extra = entry_extra.get()
        new_category = entry_category.get()

        cursor = db.cursor()
        query = "UPDATE table_out SET amount = %s, typeacc = %s, date = %s, description = %s, currency = %s, extra = %s, category = %s WHERE id = %s"
        cursor.execute(query, (new_amount, new_typeacc, new_date,
                       new_description, new_currency, new_extra, new_category, expense_id))
        db.commit()
        cursor.close()
        update_table()


# Функция для редактирования выбранной записи INCOME money - ВХІДНИХ


def edit_income():
    selected_item = tree2.selection()
    if selected_item:
        expense_id = tree2.item(selected_item, "values")[0]
        new_amount = entry_amount.get()
        new_typeacc = entry_typeacc.get()
        new_date = entry_date.get()
        new_description = entry_description.get()
        new_currency = entry_currency.get()
        new_extra = entry_extra.get()
        new_category = entry_category.get()

        cursor = db.cursor()
        query = "UPDATE table_in SET amount = %s, typeacc = %s, date = %s, description = %s, currency = %s, extra = %s, category = %s WHERE id = %s"
        cursor.execute(query, (new_amount, new_typeacc, new_date,
                       new_description, new_currency, new_extra, new_category, expense_id))
        db.commit()
        cursor.close()
        update_table2()


# Создайте графический интерфейс
root = tk.Tk()
root.title("Home Money")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# ДАТА
label_date = tk.Label(frame, text="Дата:")
label_date.grid(row=0, column=0)

entry_date = tk.Entry(frame)
entry_date.grid(row=0, column=1)

# Описание
label_description = tk.Label(frame, text="Опис:")
label_description.grid(row=1, column=0)

entry_description = tk.Entry(frame)
entry_description.grid(row=1, column=1)

# Сумма
label_amount = tk.Label(frame, text="Сума:")
label_amount.grid(row=2, column=0)

entry_amount = tk.Entry(frame)
entry_amount.grid(row=2, column=1)

# РАХУНОК
label_typeacc = tk.Label(frame, text="Рахунок:")
label_typeacc.grid(row=3, column=0)

entry_typeacc = ttk.Combobox(frame,
                             values=[
                                 "Cash",
                                 "AIB-4128",
                                 "AIB-7155",
                                 "AIB-VIKA",
                                 "Mono-5383",
                                 "PB-3871",
                                 "PB-6959",
                                 "AIB-Vlad"])
print(dict(entry_typeacc))
entry_typeacc.grid(row=3, column=1)
entry_typeacc.current(1)

# entry_typeacc = tk.Entry(frame)
# entry_typeacc.grid(row=3, column=1)

# ВАЛЮТА
label_currency = tk.Label(frame, text="Валюта:")
label_currency.grid(row=4, column=0)

entry_currency = ttk.Combobox(frame,
                              values=[
                                  "UAH",
                                  "EUR",
                                  "USD"])
print(dict(entry_currency))
entry_currency.grid(row=4, column=1)
entry_currency.current(1)

# entry_currency = tk.Entry(frame)
# entry_currency.grid(row=4, column=1)

# Екстра
label_extra = tk.Label(frame, text="Екстра:")
label_extra.grid(row=5, column=0)

entry_extra = tk.Entry(frame)
entry_extra.grid(row=5, column=1)

# Категорія
label_category = tk.Label(frame, text="Категорія:")
label_category.grid(row=6, column=0)

entry_category = ttk.Combobox(frame,
                              values=[
                                  "Child",
                                  "IndebtCredit",
                                  "Education",
                                  "House",
                                  "Car",
                                  "Food",
                                  "Cloth",
                                  "Medical",
                                  "FastFood",
                                  "Presents",
                                  "TelInet",
                                  "B--etween",
                                  "TrainBus"])
print(dict(entry_category))
entry_category.grid(row=6, column=1)
entry_category.current(1)

# entry_category = tk.Entry(frame)
# entry_category.grid(row=6, column=1)


# КНОПКИ
button_add = tk.Button(frame, text="Add Cost", command=add_cost)
button_add.grid(row=0, column=2)
button_add = tk.Button(frame, text="Add Income", command=add_income)
button_add.grid(row=1, column=2)
# button_add = tk.Button(frame, text="Добавить запись3", command=add_expense)
# button_add.grid(row=2, column=2)
# button_add = tk.Button(frame, text="Добавить запись4", command=add_expense)
# button_add.grid(row=3, column=2)

button_clear = tk.Button(frame, text="Очистить", command=clear_entries)
button_clear.grid(row=3, column=2)

tree = ttk.Treeview(frame, columns=(
    "1", "2", "5", "3", "6", "4", "7", "8"), show="headings")

tree.column('1', width=20)
tree.column('2', width=80)
tree.column('3', width=80)
tree.column('4', width=80)
tree.column('5', width=100)
tree.column('6', width=100)
tree.column('7', width=100)
tree.column('8', width=100)

tree.heading("1", text="ID")
tree.heading("2", text="Дата")
tree.heading("5", text="Опис")
tree.heading("3", text="Сумма")
tree.heading("6", text="Рахунок")
tree.heading("4", text="Валюта")
tree.heading("7", text="Екстра")
tree.heading("8", text="Категорія")

tree.grid(row=9, columnspan=5)

# 222
tree2 = ttk.Treeview(frame, columns=(
    "1", "2", "5", "3", "6", "4", "7", "8"), show="headings")

tree2.column('1', width=20)
tree2.column('2', width=80)
tree2.column('3', width=80)
tree2.column('4', width=80)
tree2.column('6', width=100)
tree2.column('5', width=100)
tree2.column('7', width=100)
tree2.column('8', width=100)

tree2.heading("1", text="ID")
tree2.heading("2", text="Дата")
tree2.heading("5", text="Опис")
tree2.heading("3", text="Сумма")
tree2.heading("6", text="Рахунок")
tree2.heading("4", text="Валюта")
tree2.heading("7", text="Екстра")
tree2.heading("8", text="Категорія")

tree2.grid(row=10, columnspan=5)


button_delete = tk.Button(frame, text="Удалить Cost", command=delete_expense)
button_delete.grid(row=8, column=6)

button_delete = tk.Button(
    frame, text="Удалить income", command=delete_expense2)
button_delete.grid(row=10, column=6)

button_edit = tk.Button(
    frame, text="Edit cost", command=edit_expense)
button_edit.grid(row=8, column=5)

button_edit = tk.Button(
    frame, text="Edit income", command=edit_income)
button_edit.grid(row=10, column=5)


# заполняем поля ввода значениями выделенной позиции в общем списке

# def get_selected_row(event):
#     # будем обращаться к глобальной переменной
#     global selected_tuple
#     # получаем позицию выделенной записи в списке
#     # this is the id of the selected tuple
#     index = selected_item.curselection()[0]
#     # получаем значение выделенной записи
#     selected_tuple = selected_item.get(index)
#     # удаляем то, что было раньше в поле ввода
#     e1.delete(0, END)
#     # и добавляем туда текущее значение названия покупки
#     e1.insert(END, selected_tuple[1])
#     # делаем то же самое с другими полями
#     e2.delete(0, END)
#     e2.insert(END, selected_tuple[2])
#     e3.delete(0, END)
#     e3.insert(END, selected_tuple[3])
#     e4.delete(0, END)
#     e4.insert(END, selected_tuple[4])


#     # привязываем выбор любого элемента списка к запуску функции выбора
# list1.bind('<<ListboxSelect>>', get_selected_row)


# Працюючий КОМБОБОКС
# comboExample = ttk.Combobox(frame,
#                             values=[
#                                 "UAH",
#                                 "EUR",
#                                 "USD"])
# print(dict(comboExample))
# comboExample.grid(row=9, column=5)
# comboExample.current(1)


update_table()
update_table2()

root.mainloop()
