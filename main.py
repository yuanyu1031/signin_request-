import requests

cookies = {
    '_ga': 'GA1.2.1521371181.1674981853',
    '_gid': 'GA1.2.887338355.1674981853',
    'koa:sess': 'eyJ1c2VySWQiOjIxMTUwMywiX2V4cGlyZSI6MTcwMDkwMTk4NzgyNywiX21heEFnZSI6MjU5MjAwMDAwMDB9',
    'koa:sess.sig': 'CRiYvfARpzojEuw6i9JIi_Oif3s',
}

headers = {
    'authority': 'glados.network',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': '74423511365535966705398523722820-720-1280',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': '_ga=GA1.2.1521371181.1674981853; _gid=GA1.2.887338355.1674981853; koa:sess=eyJ1c2VySWQiOjIxMTUwMywiX2V4cGlyZSI6MTcwMDkwMTk4NzgyNywiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=CRiYvfARpzojEuw6i9JIi_Oif3s',
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

response = requests.post('https://glados.network/api/user/checkin', cookies=cookies, headers=headers, json=json_data)