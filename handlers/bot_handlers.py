
from my_bot.main_bot import bot
from telebot import types
from doctors.super_class import  dentist,therapist,cardiologist
from database.database import add_appointment

current_doctor = None
current_time = None
current_first_name = None
current_last_name = None
current_phone = None

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Dentist", "Therapist", "Cardiologist")
    bot.send_message(
        message.chat.id,
        "Welcome to the Clinic Bot! Please choose a doctor:",
        reply_markup=markup,
    )

@bot.message_handler(func=lambda message: message.text in ["Dentist", "Therapist", "Cardiologist"])
def choose_doctor(message):
    global current_doctor
    if message.text == "Dentist":
        current_doctor = dentist
    elif message.text == "Therapist":
        current_doctor = therapist
    elif message.text == "Cardiologist":
        current_doctor = cardiologist

    if current_doctor.schedule:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for time in current_doctor.schedule:
            markup.add(time)
        bot.send_message(
            message.chat.id,
            f"{current_doctor.name} is available at the following times:",
            reply_markup=markup,
        )
        bot.register_next_step_handler(message, choose_time)
    else:
        bot.send_message(message.chat.id, f"Sorry, {current_doctor.name} has no available times.")

def choose_time(message):
    global current_time
    time = message.text
    if current_doctor.book_time(time):
        current_time = time
        bot.send_message(message.chat.id, "Please enter your first name:")
        bot.register_next_step_handler(message, get_first_name)
    else:
        bot.send_message(
            message.chat.id,
            "Invalid time or already booked. Please try again.",
        )

def get_first_name(message):
    global current_first_name
    current_first_name = message.text
    bot.send_message(message.chat.id, "Please enter your last name:")
    bot.register_next_step_handler(message, get_last_name)

def get_last_name(message):
    global current_last_name
    current_last_name = message.text
    bot.send_message(message.chat.id, "Please enter your phone number:")
    bot.register_next_step_handler(message, confirm_booking)

def confirm_booking(message):
    global current_phone, current_doctor, current_time, current_first_name, current_last_name
    current_phone = message.text

    add_appointment(
        doctor_name=current_doctor.name,
        time=current_time,
        first_name=current_first_name,
        last_name=current_last_name,
        phone=current_phone)

    bot.send_message(
        message.chat.id,
        f"Appointment confirmed:\n"
        f"Doctor: {current_doctor.name}\n"
        f"Time: {current_time}\n"
        f"Patient: {current_first_name} {current_last_name}\n"
        f"Phone: {current_phone}",
    )
    current_doctor = None
    current_time = None
    current_first_name = None
    current_last_name = None
    current_phone = None

