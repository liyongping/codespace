import requests
import hashlib


def md5(original_string):
    m2 = hashlib.md5()
    m2.update(original_string)
    return m2.hexdigest()


def fuck_login(username, password):
    proxies = {
        "http": "http://cn-proxy.jp.oracle.com:80"
    }

    heaeders = {
        "Host": "ilas.gzlib.com.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "http://ilas.gzlib.com.cn/opac/reader/login",
        "Cookie": "JSESSIONID=3C0983245CDD9EEFCA1D1B233544E6E5; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"rdid": username,
            "rdPasswd": md5(password),
            "returnUrl": None,
            "password": None
            }
    r = requests.post("http://ilas.gzlib.com.cn/opac/reader/doLogin", data=data, proxies=proxies, headers=heaeders, timeout=10)
    print r.request.body
    print r.headers
    print r.status_code

if __name__ == '__main__':
    user = "001486"
    fuck_login(user, user)


