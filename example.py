import requests

class nmApi:
    def __init__(self):
        self.api_url = "https://bytedancesolutions.p.rapidapi.com"
        self.rapidapi_key = "" # Add your RapidAPI key here 
    
    def headers(self):
        return {
            "x-rapidapi-key": self.rapidapi_key,
            "x-rapidapi-host": "bytedancesolutions.p.rapidapi.com",
            "Content-Type": "application/json"
        }

    def encrypt_strData(self, str_data):
        endpoint = '/encrypt_strData'
        url = f"{self.api_url}{endpoint}"
        payload = {'strData': str_data}
        try:
            response = requests.post(url, headers=self.headers(), json=payload)
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

    def decrypt_strData(self, str_data):
        endpoint = '/decrypt_strData'
        url = f"{self.api_url}{endpoint}"
        payload = {'strData': str_data}
        try:
            response = requests.post(url, headers=self.headers(), json=payload)
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

    def web_signature(self, useragent, api_url, href, timestamp, canvas, data=""):
        endpoint = '/web_signature'
        url = f"{self.api_url}{endpoint}"
        payload = {
            "useragent": useragent,
            "url": api_url,
            "href": href,
            "timestamp": timestamp,
            "canvas": canvas,
            "data": data
        }
       
        try:
            response = requests.post(url, headers=self.headers(), json=payload)
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

    def decrypt_bogus(self, x_bogus):
        endpoint = '/decrypt_bogus'
        url = f"{self.api_url}{endpoint}"
        payload = {'x-bogus': x_bogus}
        try:
            response = requests.post(url, headers=self.headers(), json=payload)
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

    def decrypt_gnarly(self, x_gnarly):
        endpoint = '/decrypt_gnarly'
        url = f"{self.api_url}{endpoint}"
        payload = {'x-gnarly': x_gnarly}
        try:
            response = requests.post(url, headers=self.headers(), json=payload)
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

    def web_signature_v1(self, useragent, api_url, sdk_version, timestamp, canvas, data=""):
        endpoint = '/web_signature_v1'
        url = f"{self.api_url}{endpoint}"
        payload = {
            "useragent": useragent,
            "url": api_url,
            "sdk_version": sdk_version,
            "timestamp": timestamp,
            "canvas": canvas,
            "data": data
        }
        try:
            response = requests.post(url, headers=self.headers(), json=payload)
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

    def decrypt_mssdk_info(self, x_mssdk_info):
        endpoint = '/decrypt_mssdk_info'
        url = f"{self.api_url}{endpoint}"
        payload = {'x-mssdk-info': x_mssdk_info}
        try:
            response = requests.post(url, headers=self.headers(), json=payload)
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

    def encrypt_mssdk_info(self, plain_mssdk_info):
        endpoint = '/encrypt_mssdk_info'
        url = f"{self.api_url}{endpoint}"
        payload = {'plain-mssdk-info': plain_mssdk_info}
        try:
            response = requests.post(url, headers=self.headers(), json=payload)
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

    def generate_fpverify(self):
        endpoint = '/generate_fpverify'
        url = f"{self.api_url}{endpoint}"
        try:
            response = requests.get(url, headers=self.headers())
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

    def health_check(self):
        endpoint = '/health'
        url = f"{self.api_url}{endpoint}"
        try:
            response = requests.get(url, headers=self.headers())
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

if __name__ == "__main__":
    nm_api = nmApi()
    # Example usage

    print(nm_api.encrypt_strData("Hello World!"))
    print(nm_api.decrypt_strData('3QNcZH9PI7YePO9Gkn2NmIoCGJZIFtSBE3b6xD67Wir9Nqt4eGXcO4IroTTYBu5x0oZpn5nLKSaJvPyVDc4i'))

    signature = {
        "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "url": "https://login-no1a.www.tiktok.com/passport/web/send_code/?multi_login=1&did=7488765656987565294&aid=1459&account_sdk_source=web&sdk_version=2.1.5-tiktokbeta.1&language=en&verifyFp=verify_PoiK1wtd_LkjijSVb_Poik_9IjB_Uyty_gWMkjHLuGQJH&target_aid=&standalone_aid=&shark_extra=%7B%22aid%22:1459,%22app_name%22:%22Tik_Tok_Login%22,%22channel%22:%22tiktok_web%22,%22device_platform%22:%22web_pc%22,%22device_id%22:%227489957315023734294%22,%22region%22:%22FR%22,%22priority_region%22:%22%22,%22os%22:%22windows%22,%22referer%22:%22%22,%22cookie_enabled%22:true,%22screen_width%22:1536,%22screen_height%22:864,%22browser_language%22:%22en-US%22,%22browser_platform%22:%22Win32%22,%22browser_name%22:%22Mozilla%22,%22browser_version%22:%225.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F135.0.0.0+Safari%2F537.36%22,%22browser_online%22:true,%22verifyFp%22:%22verify_PoiK1wtd_LkjijSVb_Poik_9IjB_Uyty_gWMkjHLuGQJH%22,%22app_language%22:%22en%22,%22webcast_language%22:%22en%22,%22tz_name%22:%22Asia%2FCalcutta%22,%22is_page_visible%22:true,%22focus_state%22:true,%22is_fullscreen%22:false,%22history_len%22:2,%22user_is_login%22:false,%22data_collection_enabled%22:true%7D&msToken=fUQc1oKFCBGHv94I8QsYaI2u_1E56sSCpkcx35z0TVQuIxNzpbvj2ZwpOWENpolkC8YVZJqgU-g6IU586pwOoFH_LzM=",
        "href": "https://www.tiktok.com/",
        "canvas": 1487651046,
        "data": {
            "mix_mode": "1",
            "mobile": "2e3636253d323063633698787678",
            "type": "3731",
            "aid": "1459",
            "is_sso": "false",
            "account_sdk_source": "web",
            "region": "FR",
            "language": "en",
            "did": "7488765656987565294",
            "is6Digits": "1",
            "fixed_mix_mode": "1"
        },
        "timestamp": 1745257292
        }
    print(nm_api.web_signature( useragent=signature["useragent"],
                                api_url=signature["url"],
                                href=signature["href"],
                                timestamp=signature["timestamp"], canvas=signature["canvas"],data=signature["data"]))
    



    signature_v1 = {
        "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "url": "https://login-no1a.www.tiktok.com/passport/web/send_code/?multi_login=1&did=7488765656987565294&aid=1459&account_sdk_source=web&sdk_version=2.1.5-tiktokbeta.1&language=en&verifyFp=verify_PoiK1wtd_LkjijSVb_Poik_9IjB_Uyty_gWMkjHLuGQJH&target_aid=&standalone_aid=&shark_extra=%7B%22aid%22:1459,%22app_name%22:%22Tik_Tok_Login%22,%22channel%22:%22tiktok_web%22,%22device_platform%22:%22web_pc%22,%22device_id%22:%227489957315023734294%22,%22region%22:%22FR%22,%22priority_region%22:%22%22,%22os%22:%22windows%22,%22referer%22:%22%22,%22cookie_enabled%22:true,%22screen_width%22:1536,%22screen_height%22:864,%22browser_language%22:%22en-US%22,%22browser_platform%22:%22Win32%22,%22browser_name%22:%22Mozilla%22,%22browser_version%22:%225.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F135.0.0.0+Safari%2F537.36%22,%22browser_online%22:true,%22verifyFp%22:%22verify_PoiK1wtd_LkjijSVb_Poik_9IjB_Uyty_gWMkjHLuGQJH%22,%22app_language%22:%22en%22,%22webcast_language%22:%22en%22,%22tz_name%22:%22Asia%2FCalcutta%22,%22is_page_visible%22:true,%22focus_state%22:true,%22is_fullscreen%22:false,%22history_len%22:2,%22user_is_login%22:false,%22data_collection_enabled%22:true%7D&msToken=fUQc1oKFCBGHv94I8QsYaI2u_1E56sSCpkcx35z0TVQuIxNzpbvj2ZwpOWENpolkC8YVZJqgU-g6IU586pwOoFH_LzM=",
        "sdk_version": "5.1.0",
        "canvas": 1487651046,
        "data": {
            "mix_mode": "1",
            "mobile": "2e3636253d987836333635353535",
            "type": "3731",
            "aid": "1459",
            "is_sso": "false",
            "account_sdk_source": "web",
            "region": "FR",
            "language": "en",
            "did": "7488765656987565294",
            "is6Digits": "1",
            "fixed_mix_mode": "1"
        },
        "timestamp": 1745257292
        }
    print(nm_api.web_signature_v1( useragent=signature_v1["useragent"],
                                api_url=signature_v1["url"],
                                sdk_version=signature_v1["sdk_version"],
                                timestamp=signature_v1["timestamp"], canvas=signature_v1["canvas"],data=signature_v1["data"]))
    

    print(nm_api.decrypt_bogus("DFSzswVLfja9/KSxCasZKV6HQhY4"))
    print(nm_api.decrypt_gnarly("MwFLEcT1L12BkCDPScCcVVgZFU-DenHMLWzJ6yAUSq72eYD/Ts6GdxdfiS7vb5Ionv2s1L7TSYcFoLfX6yeqQNn8oC4GfUP4HLqk82ZjOBkweeg/2SOO979iORAQTJ3xo5x0wpdyBBqqvf0xVFSkVJErxMEdg0Ym5dH-5/rk3inSrRsFsKzoWla-MVY60/cizAY8561r7g7UsyckQLrKyNatakzBfvi8GBWsCfub4YgPOmNBpeP0a5PK40KusXtDPP3oq09kKR-m"))
    
    print(nm_api.encrypt_mssdk_info("hello_world"))
    print(nm_api.decrypt_mssdk_info('KTsBbIuBvkbVUg9ADCUpoQOdQQ=='))

    