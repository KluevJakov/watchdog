import telebot
import psutil
from datetime import datetime
import sys

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

arguments = sys.argv[1:]

if len(arguments) == 0:
    print('Укажите API токен')
    exit()

bot = telebot.TeleBot(arguments[0])
jafix_chat = -1001999614605

#current time
bt = datetime.now()
ct_str = bt.strftime("%d.%m.%Y // %H:%M:%S")

# СPU
cpu = "["
temperatures = psutil.sensors_temperatures()
if 'coretemp' in temperatures:
    cpu_temperatures = temperatures['coretemp']
    for entry in cpu_temperatures:
        cpu += f"{entry.current}, "

cpu = cpu[:-2] + "]"

# RAM
memory_info = psutil.virtual_memory()
ram_str = f"{get_size(memory_info.used)}/{get_size(memory_info.total)}"

# boot time
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
bt_str = bt.strftime("%d.%m.%Y // %H:%M:%S")

# uptime
uptime_dt = datetime.now() - bt
uptime_str = (datetime(1, 1, 1) + uptime_dt).strftime("%H:%M:%S")

# disks
disk_info = psutil.disk_usage('/')
total_gb = disk_info.total
used_gb = disk_info.used
disks_str = f"{get_size(used_gb)}/{get_size(total_gb)}"

info_msg = f"""<pre>⚡ PULSE SYSTEM: {ct_str} ⚡
⚡ CPU: {psutil.cpu_percent()}% | {cpu} °C ⚡
⚡ RAM: {ram_str} ⚡
⚡ DISKS: {disks_str} ⚡
⚡ BOOT: {bt_str} ⚡
⚡ UPTIME: {uptime_str} ⚡
</pre>"""


bot.send_message(jafix_chat, text=info_msg, parse_mode='HTML')
