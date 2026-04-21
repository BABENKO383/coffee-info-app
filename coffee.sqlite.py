import sqlite3

conn = sqlite3.connect('coffee.sqlite')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE coffee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roast_level TEXT,
    ground_type TEXT,
    taste_description TEXT,
    price REAL,
    package_volume TEXT
)
''')

coffee_data = [
    ('Эфиопия Иргачефф', 'Средняя', 'В зернах', 'Цитрусовые, жасмин', 850, '250 г'),
    ('Колумбия Супремо', 'Темная', 'Молотый', 'Шоколад, орехи', 720, '500 г'),
    ('Бразилия Сантос', 'Светлая', 'В зернах', 'Карамель, фрукты', 650, '500 г'),
    ('Коста-Рика Таррасу', 'Средняя', 'Молотый', 'Яблоко, мед', 890, '250 г'),
    ('Гватемала Антигуа', 'Темная', 'В зернах', 'Какао, специи', 780, '500 г'),
    ('Индия Монсунд', 'Средняя', 'Молотый', 'Пряности, орехи', 690, '250 г'),
    ('Кения АА', 'Светлая', 'В зернах', 'Ягоды, цитрус', 950, '250 г'),
]

cursor.executemany('''
INSERT INTO coffee (name, roast_level, ground_type, taste_description, price, package_volume)
VALUES (?, ?, ?, ?, ?, ?)
''', coffee_data)

conn.commit()
conn.close()

print("✅ База данных coffee.sqlite успешно создана!")
print("📊 Добавлено записей:", len(coffee_data))