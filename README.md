# homeaccounting

DataBase table name - Expenses
(host="localhost", user="alex", password="alex67", database="home_acc_main_v1")
#CREATE DATABASE home_acc_main_v1;
#USE home_acc_main_v1;

        #CREATE TABLE Expenses (
        #    id INT AUTO_INCREMENT PRIMARY KEY,
        #    date DATE,
        #    description VARCHAR(255),
        #    amount DECIMAL(10, 2)
        #);

# date DATE,

# description VARCHAR(255),

# amount DECIMAL(10, 2),

# typeacc VARCHAR(255),

# currency varchar(3),

# extra VARCHAR(255),

# category VARCHAR(255)

Home Accounting test App

-----**\*** Назва колонок БД **\*\*\***\_\*\*

- ID
- Date
- Description
- Amount
- назва кошелька
- Валюта
- Екстра
- Категорія

# date DATE,

# description VARCHAR(255),

# amount DECIMAL(10, 2),

# typeacc VARCHAR(255),

# currency varchar(3),

# extra VARCHAR(255),

# category VARCHAR(255)

### Типи рахунків (КОШЕЛЬКІВ)

"Cash",
"AIB-4128", "AIB-7155", "AIB-VIKA", "Mono-5383", "PB-3871", "PB-6959", "AIB-Vlad"

### Валюти

"UAH" -- "EUR" -- "USD"

### Катнгорії

"Child", "IndebtCredit", "Education", "House",
"Car",
"Food",
"Cloth", "Medical", "FastFood", "Presents", "TelInet", "B--etween", "TrainBus"

Організація структури бази даних для програми ведення домашньої бухгалтерії може бути складною задачею, але ось кілька загальних порад:

1.  Таблиці:
    - Створіть окремі таблиці для різних типів фінансових операцій, таких як:
    - - - витрати = Дата операції, Сума, Опис, Категорія, Підкатегорія, Валюта, Помітка про регулярність
    - - - доходи = Дата операції, Сума, Опис, Категорія, Підкатегорія, Валюта, Помітка про регулярність
    - - - кредити, борги = Дата операції, Сума, Опис, Категорія, Підкатегорія, Валюта, Помітка про регулярність
2.  Категорії:

    - Створіть таблицю або список категорій

                 Категорії витрат:
                 1. Їжа і продукти харчування.
                 2. Житло (оренда або кредит за житло, комунальні послуги).
                 3. Транспорт (пальне, обслуговування авто, СТО).
                 4. Одяг та взуття.
                 5. Розваги і відпочинок.
                 6. Медичні послуги та страхування.
                 7. Освіта (курси, навчання, підручники).
                 8. Засоби особистої гігієни та домогосподарства.
                 9. Благодійність.
                 10. Кредитні виплати та борги.
                 11. громадський транспорт

                 Категорії доходів:
                 1. Основна заробітна плата.
                 2. Додатковий дохід (фріланс, парт-тайм робота, додаткова робота).
                 3. Виплата дивідендів або відсотків з інвестицій.
                 4. Пенсія або соціальні виплати.
                 5. Допомога від родини чи друзів.
                 6. Продаж речей або майна.

3.  Рахунки:

    - Можливо, вам знадобиться таблиця для обліку банківських рахунків, готівки та інших фінансових ресурсів.

      !!! - Створити окреме меню для введення Рахунків

      - Нал - Cash
      - AIB-001
      - AIB-002
      - AIB_Vika-001
      - AIB_Vika-002
      - Mono
      - PB-001
      - PB-002
      - PB-003

4.  Планування:

    - Додайте можливість створення бюджетів і планів витрат. Це допоможе користувачам встановити цілі і відстежувати їх виконання.

      !!! - Розробити сторінку для прогнозування бюджету на тиждень та місяць

5.  Звіти і аналіз:

    - Розробіть запити або звіти, що дозволять користувачам аналізувати свою фінансову діяльність за різними параметрами, наприклад, за місяцями, категоріями чи рахунками.

6.  Забезпечення безпеки:

    - Зверніть особливу увагу на безпеку даних. Зашифруйте чутливу інформацію і забезпечте доступ до неї лише авторизованим користувачам.

7.  Резервне копіювання:

    - Забезпечте можливість регулярного резервного копіювання даних, щоб уникнути їх втрати у випадку аварії.

8.  Розширюваність:
    - Плануйте структуру бази даних так, щоб вона була готова до розширення функціональності програми в майбутньому.

Виведення та зберігання сум по категоріях може бути виконано двома основними способами в SQL-базі даних:

1. Обчислення кожного разу: Ви можете обчислювати суми категорій кожного разу, коли користувач запитує про них, використовуючи SQL-запити з функціями агрегації, такими як `SUM()`. Цей підхід має певні переваги, такі як актуальність даних, але може бути менш ефективним при великій кількості операцій, оскільки потребує багаторазових обчислень.

2. Зберігання в окрему таблицю: Щоб підвищити продуктивність, ви можете створити окрему таблицю для сум по категоріях і оновлювати її при кожній фінансовій операції. Цей підхід називається "попередній агрегації" (pre-aggregation). Він дозволяє швидко отримувати суми без необхідності повторних обчислень, але потребує додаткового керування даними для їх актуалізації при кожній зміні.

Обираючи між цими підходами, вам слід враховувати розмір вашої бази даних, частоту додавання нових фінансових операцій і потреби у продуктивності. У більшості випадків оптимальний варіант полягає в зберіганні сум по категоріям в окремій таблиці для полегшення швидкого доступу до них, з оновленнями при додаванні нових операцій.

------------------............--------------

Напиши программу для ведения домашней бухгалтерии по следующему ТЗ:

1. Программа использует Базу данных muSQL.
2. Создать отдельные таблицы для следуюющих категорий:

child, indebt_credit, education, house, car, food, cloth, medical, fastfood_cafe, presents, train_bus, tel_inet, alms

Но с возможностью добавлять новые категории.

3. Таблица для категорий содержит следующие столбцы - id, date, description, amount, kind_money.
4. Создать таблицу с отдельными счетами и возможностью добавлять новые счета.
5. Все это в графическом интерфейсе используя tkinter.
6. Отдельная страница с отчетами. Отдельная страница с интерфейсом внесения данных. Отдельная страница планирования бюджета.
7. С возможностью редактирования данных.
8. С возможностью масштабирования программы.
9. Добавить кнопку выгрузки данных из категорий в csv файл.

---

-- Создание базы данных HomeAccounting_002, если она ещё не создана
CREATE DATABASE IF NOT EXISTS HomeAccounting_002;

-- Использование базы данных HomeAccounting
USE HomeAccounting_002;

-- Создание таблицы child
CREATE TABLE IF NOT EXISTS out_child (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
kind_money VARCHAR(255),
category VARCHAR(30)
);

-- Создание таблицы indebt_credit
CREATE TABLE IF NOT EXISTS out_indebt_credit (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
kind_money VARCHAR(255),
category VARCHAR(30)
);

-- Создание таблицы education
CREATE TABLE IF NOT EXISTS out_education (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
kind_money VARCHAR(255),
category VARCHAR(30)
);

-- Создание таблицы house
CREATE TABLE IF NOT EXISTS out_house (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
kind_money VARCHAR(255),
category VARCHAR(30)
);

-- Создание таблицы car
CREATE TABLE IF NOT EXISTS out_car (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
kind_money VARCHAR(255),
category VARCHAR(30)
);

-- Создание таблицы food
CREATE TABLE IF NOT EXISTS out_food (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
kind_money VARCHAR(255),
category VARCHAR(30)
);

-- Создание таблицы cloth
CREATE TABLE IF NOT EXISTS out_cloth (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
kind_money VARCHAR(255),
category VARCHAR(30)
);

-- Создание таблицы medical
CREATE TABLE IF NOT EXISTS out_medical (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
kind_money VARCHAR(255),
category VARCHAR(30)
);

-- Создание таблицы fastfood_cafe
CREATE TABLE IF NOT EXISTS out_fastfood_cafe (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
kind_money VARCHAR(255),
category VARCHAR(30)
);

-- Создание таблицы presents
CREATE TABLE IF NOT EXISTS out_presents (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
kind_money VARCHAR(255),
category VARCHAR(30)
);

-- Создание таблицы train_bus
CREATE TABLE IF NOT EXISTS out_train_bus (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
kind_money VARCHAR(255),
category VARCHAR(30)
);

-- Создание таблицы tel_inet
CREATE TABLE IF NOT EXISTS out_tel_inet (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
kind_money VARCHAR(255),
category VARCHAR(30)
);

-- Создание таблицы alms
CREATE TABLE IF NOT EXISTS out_alms (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
kind_money VARCHAR(255),
category VARCHAR(30)
);

---

#

CREATE DATABASE IF NOT EXISTS home_acc_main_v1;

USE home_acc_main_v1;

CREATE TABLE IF NOT EXISTS table_out (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
typeacc VARCHAR(255),
currency varchar(3),
extra VARCHAR(255),
category VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS table_in (
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE,
description VARCHAR(255),
amount DECIMAL(10, 2),
typeacc VARCHAR(255),
currency varchar(3),
extra VARCHAR(255),
category VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS typevalue (
id INT AUTO_INCREMENT PRIMARY KEY,
description VARCHAR(255),
typeval VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS typecurent (
id INT AUTO_INCREMENT PRIMARY KEY,
curent VARCHAR(3)
);
