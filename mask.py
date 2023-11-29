import requests, random, platform, urllib, sys, os

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[0;33m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    LITBU = '\033[94m'
    YELLOW = '\033[3;33m'
    CYAN = '\033[0;36'

def cls():
  if sys.platform == 'win32':
    # clear in windows, java
    os.system('cls')
  else:
    # clear in linux, android, ubuntu
    os.system('clear')

os.system('python src/serv.py')
cls()
print(bcolors.FAIL + '''
 ███▄ ▄███▓ ▄▄▄        ██████  ██ ▄█▀   █    ██  ██▀███   ██▓
▓██▒▀█▀ ██▒▒████▄    ▒██    ▒  ██▄█▒    ██  ▓██▒▓██ ▒ ██▒▓██▒
▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ▓███▄░   ▓██  ▒██░▓██ ░▄█ ▒▒██░
▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒▓██ █▄   ▓▓█  ░██░▒██▀▀█▄  ▒██░
▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒▒██▒ █▄  ▒▒█████▓ ░██▓ ▒██▒░██████▒
░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒  ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▓  ░
░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒ ▒░  ░░▒░ ░ ░   ░▒ ░ ▒░░ ░ ▒  ░
░      ░     ░   ▒   ░  ░  ░  ░ ░░ ░    ░░░ ░ ░   ░░   ░   ░ ░
       ░         ░  ░      ░  ░  ░        ░        ░         ░  ░''')

print('''\033[95m
1. cutt.ly   -    Developer: misha korzhik
2. clck.ru   -    https://github/mishakorzik
3. is.gd     -    Version: 1.1.0 stable
4. da.gd     -    Tranks for installing!
5. Exit      -    Exit utility ...''')

op = input(bcolors.WARNING + 'Options: ')

if op == '1':
  domain = 'https://cutt.ly/'
  protocol = 'https://'
  print(bcolors.WARNING + 'Example: google.com')
  MYURL = input(str(bcolors.LITBU +'While url link: '))
  name = input(bcolors.LITBU +'Come up with a name: ')
  cuttly = ['b5bd33bc62505a97a122827ee9a4336c48230', 'eb13dab99e34c37ef75484c64a2991f9a895e', '3fa41af6e314f5d664105ea6b447437278bdd']
  key = random.choice(cuttly)
  url = urllib.parse.quote(protocol+MYURL)
  r1 = requests.get('http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(key, url, name))
  r = (r1.text)
  if r == '{"url":{"status":1}}':
    print(bcolors.FAIL + 'This link is abbreviated!')
  elif r == '{"url":{"status":2}}':
    print(bcolors.FAIL + 'The entered link is not a link!')
  elif r == '''{"url":{"status":3}}''':
    print(bcolors.FAIL + 'The preferred link name is already taken!')
  elif r == '{"url":{"status":4}}':
    print(bcolors.FAIL + 'Api key error! Please try again later.')
  elif r == '{"url":{"status":5}}':
    print(bcolors.FAIL + 'The link has not passed the validation.')
  elif r == '{"url":{"status":6}}':
    print(bcolors.FAIL + 'The link provided is from a blocked domain!')
  else:
    print(bcolors.OKGREEN + 'Link succesfully created! url: '+domain+name)

elif op == '4':
  domain = 'https://'
  print(bcolors.WARNING + 'Example: google.com')
  MYURL = input(str(bcolors.LITBU +'While url link: '))
  link = domain + MYURL
  r1 = requests.get('https://da.gd/s/?url='+link).text
  print(bcolors.LITBU + 'Link succesfully created!')
  print(bcolors.OKGREEN + 'url: ' + r1)

elif op == '3':
  domain = 'https://'
  print(bcolors.WARNING + 'Example: google.com')
  MYURL = input(str(bcolors.LITBU +'While url link: '))
  link = domain + MYURL
  r1 = requests.get(f"https://is.gd/create.php?format=json&url="+link).json()['shorturl']
  print(bcolors.LITBU + 'Link succesfully created!')
  print(bcolors.OKGREEN + 'url: ' + r1)

elif op == '2':
  domain = 'https://'
  print(bcolors.WARNING + 'Example: google.com')
  MYURL = input(str(bcolors.LITBU +'While url link: '))
  url = domain + MYURL
  r1 = requests.get('https://clck.ru/--?url=google.com').text
  print(bcolors.LITBU + 'Link succesfully created!')
  print(bcolors.OKGREEN + 'url: ' + r1)
else:
  os.execl(sys.executable, sys.executable, *sys.argv)
