from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi WebDriver di luar fungsi
service = Service(r'direktori web driver')
driver = webdriver.Chrome(service=service)

def cek_peserta(id_peserta, is_first_iteration):
    try:
        # Akses halaman pengumuman hanya sekali untuk iterasi pertama
        if is_first_iteration:
            driver.get('https://www.jotform.com/form/243191829415460')

            # Tunggu dan klik tombol "Start"
            start_button = WebDriverWait(driver, 7).until(
                EC.element_to_be_clickable((By.ID, 'jfCard-welcome-start'))
            )
            start_button.click()

            # Tunggu dan klik tombol "Next"
            next_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Next")]'))
            )
            next_button.click()

            # Beralih ke iframe sebelum mengakses elemen di dalamnya
            WebDriverWait(driver, 5).until(
                EC.frame_to_be_available_and_switch_to_it((By.ID, 'customFieldFrame_74'))
            )

        else:
            # Pindah ke iframe setiap iterasi setelah yang pertama
            driver.switch_to.frame('customFieldFrame_74')

        # Tunggu hingga field ID peserta tersedia dan terlihat
        input_field = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'access-code'))
        )

        # Bersihkan field sebelum mengisi
        driver.execute_script("arguments[0].value = '';", input_field)
        # Masukkan ID peserta
        driver.execute_script("arguments[0].value = arguments[1];", input_field, id_peserta)

        # Klik tombol "Auto Complete Fields"
        auto_complete_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'autofill'))
        )
        auto_complete_button.click()

        # Tunggu hasil autofill
        time.sleep(2.3)

        message_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'message'))
            )

        message_text = message_field.text
        if "Unknown access code" in message_text:
            error_message = f'Peserta {id_peserta} tidak lolos'
            print(error_message)
            file_gagal.write(error_message + "\n")
            driver.switch_to.default_content()
            return False

        driver.switch_to.default_content()
        # Ambil Asal Universitas dari halaman berikutnya
        asal_universitas = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "input_80"))
        ).get_attribute("value")

         # Klik tombol "Next" untuk pindah ke halaman nama
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="nextButton_1"]'))
        )
        next_button.click()

        # Ambil Nama Lengkap dari halaman
        nama_lengkap = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "input_82"))
        ).get_attribute("value")
        
        # print(f"Nama peserta ditemukan: {nama_lengkap}")

       

        # print("Tombol Next berhasil diklik, berpindah ke halaman berikutnya.")

        
        # Simpan hasil
        result_text = f'Peserta {id_peserta} lolos!,Nama: {nama_lengkap},Asal Universitas: {asal_universitas}'
        print(result_text)
        file_output.write(result_text + "\n")

        # Kembali ke halaman input ID peserta dengan klik "Previous" dua kali
        driver.switch_to.default_content()
        
        # Klik tombol "Previous" pertama
        
        previous_button_1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cid_82"]/div/div[3]/button[1]'))
        )
        previous_button_1.click()
        
        time.sleep(2)  # Beri jeda sebelum klik kedua

        # Klik tombol "Previous" kedua untuk kembali ke halaman ID
        previous_button_2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cid_80"]/div/div[3]/button[1]'))
        )
        previous_button_2.click()
        
        
        # print("Tombol Previous kedua berhasil diklik, kembali ke halaman input ID peserta.")

        driver.switch_to.default_content()

        return True

    except Exception as e:
        error_message = f'{id_peserta}'
        print(error_message)
        file_error.write(error_message + "\n")
        driver.switch_to.default_content()
        return False

# Jumlah peserta yang lolos
jumlah_lolos = 0

# JIKA INGIN MENGGUNAKAN RENTANG =================================
# Jumlah peserta yang lolos
# jumlah_lolos = 0
# mulaidari = 1
# jumlah_peserta = 1000  # Ganti dengan jumlah peserta yang ingin diperiksa
# # Contoh penggunaan
# is_first_iteration = True  # Tandai iterasi pertama
# for i in range(mulaidari, jumlah_peserta + 1):
#     id_peserta = f'TLD25-{i:05d}'
#     if cek_peserta(id_peserta, is_first_iteration):
#         jumlah_lolos += 1
#     is_first_iteration = False  # Set ke False setelah iterasi pertama

    # Menyimpan jumlah total peserta yang lolos
# summary_text = f'Peserta yang lolos untuk rentang peserta no id {mulaidari} sampai {jumlah_peserta} adalah {jumlah_lolos}'
# ========================================================================

# JIKA INGIN MENGGUNAKAN FILE======================================================================
# Baca file ID peserta dari 'pesertalolos.txt'
with open("id_peserta.txt", "r") as file_input, open("data1lolos.txt", "w") as file_output, open("data2gagal.txt", "w") as file_gagal, open("data3error.txt", "w") as file_error:
    is_first_iteration = True  # Tandai iterasi pertama
    for line in file_input:
        id_peserta = line.strip()  # Hapus spasi dan baris baru dari ID peserta
        if cek_peserta(id_peserta, is_first_iteration):
            jumlah_lolos += 1
        is_first_iteration = False  # Set ke False setelah iterasi pertama

    # Menyimpan jumlah total peserta yang lolos
    summary_text = f'Total peserta yang lolos adalah: {jumlah_lolos}'
    print(summary_text)
    file_output.write(summary_text)

# Tutup driver setelah semua peserta diperiksa
driver.quit()
