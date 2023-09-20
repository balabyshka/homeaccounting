import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Создайте подключение к базе данных MySQL
db = mysql.connector.connect(
    host="localhost",
    user="alex",
    password="alex67",
    database="HomeAccounting"
)

# Функция для добавления записей в базу данных


def add_expense():
    date = entry_date.get()
    description = entry_description.get()
    amount = entry_amount.get()

    cursor = db.cursor()
    query = "INSERT INTO Expenses (date, description, amount) VALUES (%s, %s, %s)"
    values = (date, description, amount)

    cursor.execute(query, values)
    db.commit()
    cursor.close()

    messagebox.showinfo("Успешно", "Запись добавлена")
    clear_entries()
    update_table()

# Функция для очистки полей ввода


def clear_entries():
    entry_date.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

# Функция для обновления отображения таблицы


def update_table():
    cursor = db.cursor()
    query = "SELECT * FROM Expenses ORDER BY date DESC LIMIT 10"
    cursor.execute(query)
    expenses = cursor.fetchall()
    cursor.close()

    for i in tree.get_children():
        tree.delete(i)

    for expense in expenses:
        tree.insert("", "end", values=expense)

# Функция для удаления выбранной записи


def delete_expense():
    selected_item = tree.selection()
    if selected_item:
        expense_id = tree.item(selected_item, "values")[0]
        cursor = db.cursor()
        query = "DELETE FROM Expenses WHERE id = %s"
        cursor.execute(query, (expense_id,))
        db.commit()
        cursor.close()
        update_table()

# Функция для редактирования выбранной записи


def edit_expense():
    selected_item = tree.selection()
    if selected_item:
        expense_id = tree.item(selected_item, "values")[0]
        new_amount = entry_amount.get()

        cursor = db.cursor()
        query = "UPDATE Expenses SET amount = %s WHERE id = %s"
        cursor.execute(query, (new_amount, expense_id))
        db.commit()
        cursor.close()
        update_table()


# Создайте графический интерфейс
root = tk.Tk()
root.title("Домашняя бухгалтерия")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_date = tk.Label(frame, text="Дата:")
label_date.grid(row=0, column=0)

entry_date = tk.Entry(frame)
entry_date.grid(row=0, column=1)

label_description = tk.Label(frame, text="Описание:")
label_description.grid(row=1, column=0)

entry_description = tk.Entry(frame)
entry_description.grid(row=1, column=1)

label_amount = tk.Label(frame, text="Сумма:")
label_amount.grid(row=2, column=0)

entry_amount = tk.Entry(frame)
entry_amount.grid(row=2, column=1)

button_add = tk.Button(frame, text="Добавить запись", command=add_expense)
button_add.grid(row=3, columnspan=2)

button_clear = tk.Button(frame, text="Очистить", command=clear_entries)
button_clear.grid(row=4, columnspan=2)

tree = ttk.Treeview(frame, columns=(
    "ID", "Дата", "Описание", "Сумма"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Дата", text="Дата")
tree.heading("Описание", text="Описание")
tree.heading("Сумма", text="Сумма")

tree.grid(row=5, columnspan=2)

button_delete = tk.Button(frame, text="Удалить запись", command=delete_expense)
button_delete.grid(row=6, column=0)

button_edit = tk.Button(
    frame, text="Редактировать запись", command=edit_expense)
button_edit.grid(row=6, column=1)

update_table()

root.mainloop()
