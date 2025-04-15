from selenium import webdriver
import pandas as pd
import logging
from tqdm import tqdm
from utils import format_number, send_whatsapp_message, load_message_template
from screen_config import configure_screen

# Konfigurasi logging
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("Program dimulai.")
print("Program dimulai.")

# Baca data dari file Excel
def load_excel_data(file_name):
    try:
        df = pd.read_excel(file_name, engine='openpyxl', dtype=object, header=None)
        logging.info("Data berhasil dimuat dari file Excel.")
        print("Data berhasil dimuat dari file Excel.")
        return df.values.tolist()
    except Exception as e:
        logging.error(f"Gagal membaca file Excel: {e}")
        print(f"Gagal membaca file Excel: {e}")
        exit()

# Main program
data = load_excel_data('contacts.xlsx')

# Konfigurasi Selenium
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Atur posisi dan ukuran jendela browser
configure_screen(driver)

# Buka WhatsApp Web
driver.get("https://web.whatsapp.com")
input("Scan QR Code pada WhatsApp Web, lalu tekan Enter untuk melanjutkan...")

# Daftar pesan gagal
failed_messages = []

# Kirim pesan ke setiap nomor
message_template = load_message_template('message_template.txt')
total_messages = len(data[1:])
for i, row in enumerate(tqdm(data[1:], desc="Mengirim pesan", total=total_messages), start=1):
    nim, nama, telp, *rest = row
    number = format_number(telp)
    
    if not number:  # Skip jika nomor tidak valid
        logging.warning(f"Skipping invalid number for {nama} ({nim})")
        tqdm.write(f"Skipping invalid number for {nama} ({nim})")
        failed_messages.append([nim, nama, telp, "Nomor telepon tidak valid"])
        continue
    
    # Pesan yang akan dikirim
    message = message_template.replace("{nama}", str(nama)).replace("{nim}", str(nim))
    
    try:
        send_whatsapp_message(driver, number, message)
        logging.info(f"{nim} - {nama} selesai dikirim ({i}/{total_messages})")
        tqdm.write(f"{nim} - {nama} selesai dikirim ({i}/{total_messages})")
    except Exception as e:
        failed_messages.append([nim, nama, telp, str(e)])

# Simpan data pesan gagal ke file Excel
if failed_messages:
    failed_df = pd.DataFrame(failed_messages, columns=["NIM", "Nama", "Telepon", "Keterangan Error"])
    failed_df.to_excel('failed_messages.xlsx', index=False, engine='openpyxl')
    logging.info(f"Data pesan gagal disimpan ke 'failed_messages.xlsx'.")
    print(f"Data pesan gagal disimpan ke 'failed_messages.xlsx'.")
else:
    logging.info("Tidak ada pesan yang gagal.")
    print("Tidak ada pesan yang gagal.")

# Tutup driver setelah selesai
driver.quit()
logging.info("Program selesai.")
print("Program selesai.")
print("Semua tugas selesai! Log telah dicatat pada file 'log.txt'.")