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
        print("❌ ZIP file not found:", zip_path)
        return

    print("📦 Extracting archive...")
    os.system("rm -rf ~/custom_rom")
    os.system(f"unzip '{zip_path}' -d ~/custom_rom")

    system_img = os.path.expanduser("~/custom_rom/system.img")
    if not os.path.exists(system_img):
        print("❌ system.img not found in the archive!")
        return

    print("🔄 Replacing default system.img in Waydroid...")
    os.system("sudo systemctl stop waydroid-container")
    os.system("sudo rm -f /var/lib/waydroid/system.img")
    os.system(f"sudo cp '{system_img}' /var/lib/waydroid/system.img")
    os.system("sudo chmod 644 /var/lib/waydroid/system.img")
    os.system("sudo systemctl start waydroid-container")

    print("✅ Custom Android system installed!")

while True:
    print("\n=== Waydroid Installer Menu ===")
    print("1. Install Waydroid")
    print("2. Initialize Waydroid")
    print("3. Initialize Waydroid with GApps")
    print("4. Install custom Android system from ZIP")
    print("0. Exit")

    try:
        cmd = int(input("---> "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        continue

    if cmd == 1:
        install_waydroid()
    elif cmd == 2:
        init_waydroid()
    elif cmd == 3:
        init_waydroid(with_gapps=True)
    elif cmd == 4:
        zip_path = input("Enter full path to the ZIP file (e.g. /home/user/Bliss.zip): ")
        install_custom_rom(zip_path)
    elif cmd == 0:
        print("👋 Exiting.")
        break
    else:
        print("❌ Unknown option!")
