import requests
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

platforms = [
    "https://www.instagram.com/{}/",
    "https://twitter.com/{}/",
    "https://www.facebook.com/{}/",
    "https://www.tiktok.com/@{}/",
    "https://www.reddit.com/user/{}/",
    "https://m.youtube.com/@{}/",
    "https://www.pinterest.com/{}/",
    "https://www.tumblr.com/{}/",
    "https://github.com/{}/",
    "https://discord.com/users/{}/",
    "https://steamcommunity.com/id/{}/",
    "https://open.spotify.com/user/{}/",
    "https://www.twitch.tv/{}/",
    "https://wa.me/{}/",
    "https://vk.com/{}/",
    "https://www.flickr.com/photos/{}/",
    "https://medium.com/@{}/",
    "https://www.snapchat.com/{}/"
]

def check_username(username):
    print(f"{Fore.YELLOW}Procurando o nome de usuário: {username}")
    for platform in platforms:
        url = platform.format(username)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{Fore.GREEN}[+] O nome de usuário '{username}' está registrado no site: {url}")
            elif response.status_code == 404:
                print(f"{Fore.RED}[-] O nome de usuário '{username}' não foi encontrado no site: {url}")
            else:
                print(f"{Fore.YELLOW}[!] Não foi possível verificar {url}. Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[!] Erro ao acessar {url}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Verifique a disponibilidade do nome de usuário em várias plataformas sociais.")
    parser.add_argument("username", type=str, help="Nome de usuário para procurar nas plataformas")
    args = parser.parse_args()
    
    check_username(args.username)

if __name__ == "__main__":
    main()
