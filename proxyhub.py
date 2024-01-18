from urllib.request import urlopen, Request
import random

proxies = []  # Will contain proxies [ip, port]

# Main function
def main():
    # Retrieve proxies from the provided URL
    proxies_url = 'https://raw.githubusercontent.com/casals-ar/proxy-list/main/https'
    proxies_doc = urlopen(proxies_url).read().decode('utf8')

    # Save proxies in the array
    for line in proxies_doc.split('\n'):
        if line.strip():  # Ignore empty lines
            proxy = line.strip().split(':')
            if len(proxy) == 2:
                ip, port = proxy
                proxies.append({'ip': ip, 'port': port})

    # Choose a random proxy
    proxy_index = random_proxy()
    proxy = proxies[proxy_index]

    for n in range(1, 100):
        req = Request('https://icanhazip.com')
        req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'https')

        # Every 10 requests, generate a new proxy
        if n % 5 == 0:
            proxy_index = random_proxy()
            proxy = proxies[proxy_index]

        # Make the call
        try:
            my_ip = urlopen(req).read().decode('utf8')
            print('#' + str(n) + ': ' + my_ip)
        except:  # If error, delete this proxy and find another one
            del proxies[proxy_index]
            print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' deleted.')
            proxy_index = random_proxy()
            proxy = proxies[proxy_index]

# Retrieve a random index proxy (we need the index to delete it if not working)
def random_proxy():
    return random.randint(0, len(proxies) - 1)

if __name__ == '__main__':
    main()
