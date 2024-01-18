from urllib.request import urlopen, Request
import random

proxies = []  # Contendrá proxies [ip, port]

# Función principal
def main():
    global proxies

    # Obtener proxies desde la URL proporcionada
    proxies_url = 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt'
    # proxies_url = 'https://raw.githubusercontent.com/casals-ar/proxy-list/main/https'
    proxies_doc = urlopen(proxies_url).read().decode('utf8')

    # Guardar proxies en el array
    for line in proxies_doc.split('\n'):
        if line.strip():  # Ignorar líneas vacías
            proxy = line.strip().split(':')
            if len(proxy) == 2:
                ip, port = proxy
                proxies.append({'ip': ip, 'port': port})

    for n in range(1, 100):
        # Elegir un proxy aleatorio
        proxy_index = random_proxy()
        proxy = proxies[proxy_index]

        req = Request('https://icanhazip.com')
        req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'https')

        # Realizar la llamada
        try:
            my_ip = urlopen(req).read().decode('utf8')
            print('#' + str(n) + ': ' + my_ip)
        except Exception as e:
            print(f'Error en la solicitud #{n}: {e}')

# Obtener un índice de proxy aleatorio
def random_proxy():
    return random.randint(0, len(proxies) - 1)

if __name__ == '__main__':
    main()
