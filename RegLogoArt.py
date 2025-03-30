import os
import subprocess
import importlib.util

import pytz
import platform
import os
from datetime import datetime
import requests
os.system('cls' if os.name == 'nt' else 'clear')

try:
    import pytz
except ImportError:
    os.system('pip install pytz')
    
import pytz
# Hàm kiểm tra kết nối mạng
def check_network():
    try:
        requests.get('https://www.google.com', timeout=5)
        return True
    except requests.ConnectionError:
        return False   
if not check_network():
            # In thông báo khi không có kết nối mạng
    print("Đã Có Lỗi Xảy Ra. Vui Lòng Inbox Telegram : @Quanhau2010 hoặc @HerlysWarService. Cảm Ơn Vì Đã Sử Dụng")
    quit()  # Dừng chương trình nếu không có kết nối mạng
# Hàm lấy IP công cộng
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        return ip_data.get("ip", "Không xác định")
    except requests.exceptions.RequestException as e:
        return "Không thể lấy IP"

# Hàm kiểm tra loại thiết bị
def check_device():
    system = platform.system()
    if system == "Linux":
        # Có thể là Android hoặc một hệ thống Linux khác
        return "Điện thoại"
    elif system == "Darwin":
        # macOS (Máy tính Apple)
        return "Máy tính Mac"
    elif system == "Windows":
        return "Máy tính Windows"
    else:
        return "Không xác định"

# Lấy thông tin hiện tại (ngày, múi giờ)
timezone = pytz.timezone("Asia/Ho_Chi_Minh")
current_time = datetime.now(timezone).strftime("%d/%m/%Y")

# Lấy thông tin thiết bị và IP
device_type = check_device()
ipv6 = get_public_ip()

# Lấy thông tin từ các URL (thông tin banner)
thongtin = requests.get('https://keyherlyswar.x10.mx/Toolupdate/jiraylo/thongtin.json').text
thongbao = requests.get("https://keyherlyswar.x10.mx/Toolupdate/jiraylo/thongbao.json").text
version = requests.get("https://keyherlyswar.x10.mx/Toolupdate/jiraylo/version.json").text
Copyright = requests.get("https://keyherlyswar.x10.mx/Toolupdate/jiraylo/copyright.json").text

# Lấy key từ file KeyToolHerlys.txt và che 4 số cuối
def get_key():
    try:
        with open('/sdcard/HERLYSWAR/KeyToolHerlys.txt', 'r') as file:
            key = file.read().strip()
            # Che 4 số cuối của key
            if len(key) > 4:
                return key[:-4] + "****"
            return key
    except FileNotFoundError:
        return "Không tìm thấy key"
    except Exception as e:
        return f"Lỗi: {str(e)}"

key = get_key()

# Tạo banner
banner = f"""    ██╗  ██╗███████╗██████╗ ██╗  ██╗   ██╗███████╗
    ██║  ██║██╔════╝██╔══██╗██║  ╚██╗ ██╔╝██╔════╝
    ███████║█████╗  ██████╔╝██║   ╚████╔╝ ███████╗
    ██╔══██║██╔══╝  ██╔══██╗██║    ╚██╔╝  ╚════██║
    ██║  ██║███████╗██║  ██║███████╗██║   ███████║
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝

           ████████╗ ██████╗  ██████╗ ██╗
           ╚══██╔══╝██╔═══██╗██╔═══██╗██║
              ██║   ██║   ██║██║   ██║██║
              ██║   ██║   ██║██║   ██║██║
              ██║   ╚██████╔╝╚██████╔╝███████╗
              ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
  Copyright : {Copyright} | Version : {version}
═════════════════════════════════════════════════════
{thongtin}
════════════════ THÔNG BÁO ══════════════════════════
{thongbao}
════════════════ THÔNG TIN MEMBER ═══════════════════
➩ IP               : {ipv6}
➩ Thiết Bị         : {device_type}
➩ Loại Key         : Key Free
➩ Key Của Bạn      : {key}
➩ Ngày Hết Hạn     : {current_time}
═════════════════════════════════════════════════════"""
print(banner)

# Hàm cài đặt thư viện nếu chưa có
def install_package(package):
    if importlib.util.find_spec(package) is None:
        print("=" * 80)
        print("Vui lòng chờ, lần sau bạn sẽ không cần cài đặt lại.".center(80))
        print("=" * 80)
        subprocess.run(['pip', 'install', package, '-q'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        pass

# Cài đặt pyfiglet nếu chưa có
install_package('pyfiglet')

# Import thư viện sau khi đã cài
import pyfiglet

def create_ascii_art_all_fonts():
    text = input("Nhập văn bản bạn muốn tạo art logo (ví dụ : Herlys War): ")  # Văn bản cần tạo
    num_logos = int(input("Nhập số lượng logo bạn muốn tạo (ví dụ: 5): "))  # Số lượng logo muốn tạo
    
    fonts = pyfiglet.FigletFont.getFonts()  # Lấy danh sách tất cả font
    total_fonts = len(fonts)
    
    # Đảm bảo thư mục tồn tại
    folder_path = "/sdcard/HERLYSWAR/fontlogo"
    os.makedirs(folder_path, exist_ok=True)
    
    # Thông báo bắt đầu
    print(f"\nĐang tạo {num_logos} logo từ tổng số {total_fonts} font...\n")
    
    # Lưu từng font vào thư mục với tên file {text}{i}.txt và hiển thị ASCII art
    for i, font in enumerate(fonts[:num_logos], start=1):  # Giới hạn số lượng logo theo yêu cầu
        ascii_art = pyfiglet.figlet_format(text, font=font)  # Tạo chữ nghệ thuật
        file_name = f"{text}{i}.txt"  # Tạo tên file theo định dạng {text}{i}.txt
        file_path = os.path.join(folder_path, file_name)  # Đặt đường dẫn đầy đủ cho file
        
        # Lưu chỉ ASCII art vào file (không có dấu "====")
        with open(file_path, "w") as file:
            file.write(ascii_art)
        
        # Hiển thị ASCII art với định dạng đẹp
        print(ascii_art)  # Hiển thị ASCII art
    
    # Thông báo tất cả logo đã được lưu
    print("\nTất cả logo đã được tạo và lưu thành công vào thư mục:".center(80))
    print(f"\n{folder_path}\n")

# Gọi hàm
create_ascii_art_all_fonts()
