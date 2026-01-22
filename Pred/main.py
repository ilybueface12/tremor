import file_operations
from faker import Faker
import random
import os

fake = Faker("ru_RU")

alphabet_spisok = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'й͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


output_dir = "cards"
os.makedirs(output_dir, exist_ok=True)


for i in range(10):

    info = fake.name()
    infoj = fake.job()
    infoad = fake.address()
    lvl = random.randint(3, 18)

    abilities_list = ['Ледяной Прыжок', 'Тайный побег', 'Ледяной выстрел', \
    'Стремительный удар', 'Электрический выстрел', 'Кислотный взгляд', \
    'Огненный гуленый', 'Ледяной удар']
    selected = [random.choice(abilities_list) for _ in range(3)]
    abilities_result = (
        ' '.join(selected)
        .translate(str.maketrans(alphabet_spisok))
    )

    context = {
        "name": info,
        "job": infoj,
        "address": infoad,
        "Сила": lvl,
        "Ловкость": lvl,
        "Выносливость": lvl,
        "Интелект": lvl,
        "УДача": lvl,
        "special_ability": abilities_result
    }

    clean_name = info.replace(' ', '_').replace('.', '')
    path_to_file = os.path.join(output_dir, f"card_{i+1}_{clean_name}.txt")

    file_operations.render_template("charsheet.txt", path_to_file, context)

