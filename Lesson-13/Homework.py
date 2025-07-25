from datetime import datetime
def calculate_age(birthdate):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        age_years = today.year - birthdate.year
    age_months = today.month - birthdate.month
    age_days = today.day - birthdate.day
    
    if age_days < 0:
        age_months -= 1
        age_days += (today - datetime(today.year, today.month, 1)).day
    
    if age_months < 0:
        age_years -= 1
        age_months += 12
    
    return f"Age: {age_years} years, {age_months} months, {age_days} days"




def days_until_next_birthday(birthdate):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    
    next_birthday = datetime(today.year, birthdate.month, birthdate.day)
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)
    
    days_remaining = (next_birthday - today).days
    
    return f"Days until next birthday: {days_remaining} days"



def meeting_end_time(current_datetime, duration_hours, duration_minutes):
    current_datetime = datetime.strptime(current_datetime, "%Y-%m-%d %H:%M")
    
    end_time = current_datetime + timedelta(hours=duration_hours, minutes=duration_minutes)
    
    return f"Meeting will end at: {end_time.strftime('%Y-%m-%d %H:%M')}"



from pytz import timezone
def convert_timezone(date_time_str, from_tz, to_tz):
    from_zone = timezone(from_tz)
    to_zone = timezone(to_tz)
    
    date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
    date_time = from_zone.localize(date_time)
    
    converted_time = date_time.astimezone(to_zone)
    
    return f"Converted time: {converted_time.strftime('%Y-%m-%d %H:%M')} in {to_tz}"



import time
def countdown_timer(target_datetime):
    target_datetime = datetime.strptime(target_datetime, "%Y-%m-%d %H:%M")
    
    while True:
        now = datetime.now()
        remaining_time = target_datetime - now
        
        if remaining_time.total_seconds() <= 0:
            print("Countdown finished!")
            break
        
        days, seconds = remaining_time.days, remaining_time.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        
        print(f"Time remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end='\r')
        time.sleep(1)



import re
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_regex, email):
        return "Valid email address."
    else:
        return "Invalid email address."



def format_phone_number(phone_number):
    phone_number = re.sub(r'\D', '', phone_number)  # Remove non-digit characters
    if len(phone_number) == 10:
        formatted_number = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
        return formatted_number
    else:
        return "Invalid phone number format. Please enter a 10-digit number."



def check_password_strength(password):
    if len(password) < 8:
        return "Password is too short. It must be at least 8 characters long."
    
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    
    if not re.search(r'\d', password):
        return "Password must contain at least one digit."
    
    return "Password is strong."



def find_word_occurrences(text, word):
    occurrences = []
    words = text.split()
    for index, w in enumerate(words):
        if w.lower() == word.lower():
            occurrences.append(index)
    return occurrences if occurrences else "Word not found in the text."



import re
def extract_dates(text):
    date_regex = r'\b\d{4}-\d{2}-\d{2}\b'  # Matches dates in YYYY-MM-DD format
    dates = re.findall(date_regex, text)
    
    return dates if dates else "No dates found in the text."
