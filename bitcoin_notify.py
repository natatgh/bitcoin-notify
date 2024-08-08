import ctypes
import requests
import time
from datetime import datetime
from plyer import notification
import plyer.platforms.win.notification  # Import explícito para garantir que PyInstaller inclua esta dependência

# Função para obter o preço atual do Bitcoin
def get_bitcoin_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,brl')
    data = response.json()
    return data['bitcoin']['usd'], data['bitcoin']['brl']

# Função para enviar notificação
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

# Função para mudar o ícone do console
def set_console_icon(icon_path):
    icon_flags = 0x00000010  # LR_LOADFROMFILE
    icon_handle = ctypes.windll.user32.LoadImageW(0, icon_path, 1, 0, 0, icon_flags)
    if icon_handle == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0:
        ctypes.windll.user32.SendMessageW(hwnd, 0x80, 0, icon_handle)

# Caminho para o ícone
icon_path = 'D:\\OneDrive\\Documentos\\Códigos\\bitcoin-notify\\src\\ico\\bitcoin-logo-1-1.ico'
set_console_icon(icon_path)

# Pergunta ao usuário a quantidade de bitcoins
btc_amount = float(input("Digite a quantidade de Bitcoins que você possui: "))

# Loop para atualizar o valor do Bitcoin periodicamente
while True:
    try:
        current_price_usd, current_price_brl = get_bitcoin_price()
        current_value_usd = btc_amount * current_price_usd
        current_value_brl = btc_amount * current_price_brl
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = (
            f'💰 Valor Atual do Bitcoin\n'
            f'USD: ${current_price_usd:.2f}\n'
            f'💵 Seu saldo de BTC:\n'
            f'BRL: R${current_value_brl:.2f}'
        )

        send_notification(f'⚠️ Atualização do Bitcoin | ⏳ Data e Hora {now}\n', message)

        message = (
            f'📅 Data e Hora: {now}\n\n'
            f'💰 Valor Atual do Bitcoin\n'
            f'USD: ${current_price_usd:.2f}\n'
            f'BRL: R${current_price_brl:.2f}\n\n'
            f'💵 Seu saldo de BTC:\n'
            f'USD: ${current_value_usd:.2f}\n'
            f'BRL: R${current_value_brl:.2f}'
        )

        print(f'Data e Hora {now}\n{message}')

        # Espera por 30 minutos (1800 segundos) antes de verificar novamente
        time.sleep(1800)

    except Exception as e:
        print(f"Erro ao obter o preço do Bitcoin: {e}")
        time.sleep(60)  # Em caso de erro, espera 1 minuto antes de tentar novamente
