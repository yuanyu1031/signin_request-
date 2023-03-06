import os
import requests
import urllib.parse

def ParseCookiestr(cookie_str):
    cookielist = {}
    for item in cookie_str.split(';'):
        itemname=item.split('=')[0]
        iremvalue=item.split('=')[1]
        cookielist[itemname.strip()]=urllib.parse.unquote(iremvalue)
    return cookielist


headers = {
    'authority': 'glados.network',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': '74423511365535966705398523722820-720-1280',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://glados.network',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

json_data = {
    'token': 'glados.network',
}
if __name__ == "__main__":
    cookie_str1 = os.environ.get("COOKIE1", None)
    cookie_str2 = os.environ.get("COOKIE2", None)
    cookie_str3 = os.environ.get("COOKIE3", None)
    cookies1 = ParseCookiestr(cookie_str1)
    cookies2 = ParseCookiestr(cookie_str2)
    cookies3 = ParseCookiestr(cookie_str3)
    response1 = requests.post('https://glados.network/api/user/checkin', cookies=cookies1, headers=headers, json=json_data)
    response2 = requests.post('https://glados.network/api/user/checkin', cookies=cookies2, headers=headers, json=json_data)
    response3 = requests.post('https://glados.network/api/user/checkin', cookies=cookies3, headers=headers, json=json_data)
    cookie_str4 = os.environ.get("COOKIE4", None)
    cookies4 = ParseCookiestr(cookie_str4)
    response4 = requests.post('https://glados.network/api/user/checkin', cookies=cookies4, headers=headers, json=json_data)
