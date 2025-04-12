import os

def install_waydroid():
    os.system("sudo apt update")
    os.system("sudo apt install curl ca-certificates -y")
    os.system("curl https://repo.waydro.id | sudo bash")
    os.system("sudo apt install waydroid -y")

def init_waydroid(with_gapps=False):
    if with_gapps:
        os.system("sudo waydroid init -s GAPPS")
    else:
        os.system("sudo waydroid init")

    os.system("sudo systemctl start waydroid-container")
    os.system("waydroid show-full-ui")

def install_custom_rom(zip_path):
    if not os.path.exists(zip_path):
        print("❌ ZIP-файл не знайдено:", zip_path)
        return

    print("📦 Розпаковка архіву...")
    os.system("rm -rf ~/custom_rom")
    os.system(f"unzip '{zip_path}' -d ~/custom_rom")

    system_img = os.path.expanduser("~/custom_rom/system.img")
    if not os.path.exists(system_img):
        print("❌ У архіві не знайдено system.img!")
        return

    print("🔄 Заміна стандартного system.img у Waydroid...")
    os.system("sudo systemctl stop waydroid-container")
    os.system("sudo rm -f /var/lib/waydroid/system.img")
    os.system(f"sudo cp '{system_img}' /var/lib/waydroid/system.img")
    os.system("sudo chmod 644 /var/lib/waydroid/system.img")
    os.system("sudo systemctl start waydroid-container")

    print("✅ Кастомна Android-система встановлена успішно!")

while True:
    print("\n=== Меню встановлення Waydroid ===")
    print("1. Встановити Waydroid")
    print("2. Ініціалізувати Waydroid")
    print("3. Ініціалізувати Waydroid з GApps")
    print("4. Встановити кастомну Android-систему з ZIP")
    print("0. Вихід")

    try:
        cmd = int(input("---> "))
    except ValueError:
        print("❌ Невірне значення! Введи число.")
        continue

    if cmd == 1:
        install_waydroid()
    elif cmd == 2:
        init_waydroid()
    elif cmd == 3:
        init_waydroid(with_gapps=True)
    elif cmd == 4:
        zip_path = input("Вкажи повний шлях до ZIP-файлу (наприклад, /home/користувач/Bliss.zip): ")
        install_custom_rom(zip_path)
    elif cmd == 0:
        print("👋 До зустрічі!")
        break
    else:
        print("❌ Невірна опція! Спробуй ще раз.")
