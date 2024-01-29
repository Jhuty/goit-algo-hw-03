from datetime import datetime

def get_days_from_today(date):
    date_object = datetime.strptime(date, '%Y-%m-%d')

    current_date = datetime.now()

    delta = current_date - date_object
    return delta.days
print(get_days_from_today('2024-01-01'))





import random
def get_numbers_ticket(min, max, quantity):
    numbers = random.sample(range(min, max + 1), quantity)
    if min < 0 or max > 1000 or not (min < quantity < max):
        return []
    else:
        return sorted(numbers)
print(get_numbers_ticket(1, 49, 6))






import re
def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number)
    if not cleaned_number.startswith(('+38', '38')):
        cleaned_number = '+38' + cleaned_number
    elif not cleaned_number.startswith('+'):
        cleaned_number = '+' + cleaned_number
    return cleaned_number
#print(normalize_phone())






from datetime import datetime, timedelta

users = [{"name": "John", "birthday": "2024.01.30"},
         {"name": "Alice", "birthday": "2024.02.04"},
         {"name": "Bob", "birthday": "2024.02.08"},]
def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday_date = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        if birthday_date < today:
            birthday_date = birthday_date.replace(year=today.year + 1)

        days_before_birthday = (birthday_date - today).days
        if days_before_birthday < 7:
            if birthday_date.weekday() >= 5:
                monday_after_birthday = birthday_date + timedelta(days=(7 - birthday_date.weekday()))
                congratulation_date = monday_after_birthday
            else:
                congratulation_date = birthday_date

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    return upcoming_birthdays
print(get_upcoming_birthdays(users))