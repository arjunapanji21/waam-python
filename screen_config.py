import screeninfo

def configure_screen(driver):
    screens = screeninfo.get_monitors()
    if len(screens) > 1:
        print("Pilih layar untuk menjalankan browser:")
        for idx, screen in enumerate(screens):
            print(f"{idx + 1}. {screen}")
        choice = int(input("Masukkan nomor layar: ")) - 1
        screen = screens[choice]
    else:
        screen = screens[0]

    driver.set_window_rect(x=screen.x, y=screen.y, width=screen.width // 2, height=screen.height)