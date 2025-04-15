from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse
import time

def format_number(telp):
    if not telp or len(str(telp)) < 9:
        return None
    return "+62" + str(telp)[1:] if str(telp).startswith("0") else str(telp)

def encode_message(message):
    # Encode pesan agar sesuai dengan format URL
    return urllib.parse.quote(message)

def send_whatsapp_message(driver, number, message):
    try:
        # Encode pesan sebelum dimasukkan ke dalam URL
        encoded_message = encode_message(message)

        # Buka URL WhatsApp Web dengan pesan
        url = f"https://web.whatsapp.com/send?phone={number}&text={encoded_message}"
        driver.get(url)
        time.sleep(5)  # Tunggu halaman memuat

        # Tunggu elemen input pesan tersedia
        message_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @data-tab="10"]'))
        )
        time.sleep(3)  # Tunggu metadata tampil
        # Kirim pesan dengan tombol Enter
        message_box.send_keys(Keys.ENTER)
        time.sleep(3)  # Tunggu pesan terkirim
    except Exception as e:
        raise Exception(f"Error sending message: {e}")

def load_message_template(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_name}' tidak ditemukan.")
