import random
from urllib.parse import urlencode
import httpx
import hashlib
import time
import ssl

ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS)
CIPHERS = 'ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES'
ctx.set_ciphers(CIPHERS)
ctx.set_alpn_protocols(["h2", "http/2.0"])


Rapid_Key='' #Enter Your Rapid Key


devices={"is_activated": "success", "Device_Info": {"iid": "7331530235232061230", "device_id": "7331529932814206507", "passport-sdk-version": "19", "device_type": "HONOR_VUM2U", "device_brand": "honor", "os_api": "27", "os_version": "8.1.0", "openudid": "d3f138db14bb0726", "sys_region": "US", "mcc_mnc": "310540", "timezone_name": "America/New_York", "timezone_offset": "-18000", "region": "US", "carrier_region": "US", "app_language": "en", "op_region": "US", "cdid": "73467f85-ca58-4b97-be27-1409326f25fb", "support_webview": "1", "user-agent": "com.zhiliaoapp.musically/2023303020 (Linux; U; Android 8.1.0; en_US; HONOR_VUM2U; Build/N2G48H;tt-ok/3.12.13.4-tiktok)", "Mssdk_Endpoint": "mssdk16-platform-useast5.us.tiktokv.com", "ac": "wifi", "channel": "googleplay", "aid": "1233", "app_name": "musical_ly", "version_code": "330302", "version_name": "33.3.2", "device_platform": "android", "os": "android", "ab_version": "33.3.2", "ssmix": "a", "language": "en", "manifest_version_code": "2023303020", "resolution": "1080*1920", "dpi": "320", "update_version_code": "2023303020", "app_type": "normal", "build_number": "33.3.2", "uoo": "0", "locale": "en", "ac2": "wifi", "host_abi": "armeabi-v7a", "okhttp_version": "4.2.137.48-tiktok", "use_store_region_cookie": "1", "google_aid": "8ed9ae2d-d941-480f-9727-dd30fc71a29b", "clientuuid": "c4146720-ecb5-4997-b36e-1037aa1bdce0", "req_id": "7e59e64f-b714-4120-bf26-9349b91da23a"}, "Cookies": {"store-idc": "useast5", "store-country-code": "us", "store-country-code-src": "did", "install_id": "7331530235232061230", "ttreq": "1$18237b6d6da904100cfe29d650d54aafb2ccb925"}, "secDeviceIdToken": "Au6vK_bZGe7k-beNTkYFhak3T", "Seed_Algorithm": 16, "Seed_Token": "MDGkHp/TrnIFIzp1yTA2lobgx70pFCcgBDcupPtdTR2ELB6GR2wxQVV0QR29NQmm2ekHIQDGxhucuA7OUPahUgCUwzOKVrpRfYxnmkVF6DQx+MNHFr/hri0VOC3c6tPNX/E=", "Ri_Report": True}

Endpoint='api16-normal-useast5.us.tiktokv.com'  #Different Endpoints For Different Country

Params=urlencode({
            "passport-sdk-version": "19",
            "iid": devices['Device_Info']["iid"],
            "device_id": devices['Device_Info']["device_id"],
            "ac": "wifi",
            "channel": devices['Device_Info']["channel"],
            "aid": devices['Device_Info']["aid"],
            "app_name": "musical_ly",
            "version_code": devices['Device_Info']["version_code"],
            "version_name": devices['Device_Info']["version_name"],
            "device_platform": "android",
            "os": "android",
            "ab_version": devices['Device_Info']["ab_version"],
            "ssmix": "a",
            "device_type": devices['Device_Info']["device_type"],
            "device_brand": devices['Device_Info']["device_brand"],
            "language":devices['Device_Info']["language"],
            "os_api": devices['Device_Info']["os_api"],
            "os_version": devices['Device_Info']["os_version"],
            "openudid": devices['Device_Info']["openudid"],
            "manifest_version_code": devices['Device_Info']["manifest_version_code"],
            "resolution": devices['Device_Info']["resolution"],
            "dpi": devices['Device_Info']["dpi"],
            "update_version_code": devices['Device_Info']["update_version_code"],
            "_rticket": str(round(time.time() * 1000)),
            "app_type": "normal",
            "sys_region":  devices['Device_Info']["sys_region"],
            "mcc_mnc": devices['Device_Info']["mcc_mnc"],
            "timezone_name": devices['Device_Info']["timezone_name"],
            "ts": str(round(time.time())),
            "timezone_offset": devices['Device_Info']["timezone_offset"],
            "build_number":devices['Device_Info']["build_number"],
            "region":  devices['Device_Info']["region"],
            "carrier_region": devices['Device_Info']["carrier_region"],
            "uoo": "0",
            "app_language":  devices['Device_Info']["app_language"],
            "locale": devices['Device_Info']["locale"],
            "op_region":  devices['Device_Info']["op_region"],
            "ac2": "wifi",
            "host_abi":devices['Device_Info']["host_abi"],
            "cdid":devices['Device_Info']["cdid"],
            "support_webview": "1",
            "okhttp_version": devices['Device_Info']["okhttp_version"],
            "use_store_region_cookie": "1"
        }).replace('%2A', '*')

Sig_Token=devices['secDeviceIdToken']
Seed_Token=devices['Seed_Token']
Seed_Algo=devices['Seed_Algorithm']

Payload=urlencode( {
    'password': '7f6163737f637363736163736163677f67',
    'account_sdk_source': 'app',
    'username': '7f6163737f736163737f616373636173',
    'mix_mode': '1',
    'multi_login': '1',
})

Cookies='; '.join([f'{key}={value}' for key, value in devices['Cookies'].items()])

url = "https://tiktok-device-registeration.p.rapidapi.com/Get_Sign/"

data={
    "Params": Params,
    "Payload": Payload,
    "Sig_Token": Sig_Token,
    "Cookies":Cookies,
    "Bd_Lanusk": "", #This data Comes in response headers after login tiktok account like this  #vqj9gCzgfSa0PaRvV/oiwGJ5lAO9VjDgLYBWp533J1ALNvAsld3tDLOZb5kTXd7Q9OM7ZhobWkDWyQAn
    "Bd_Kmsv": "", # Same Comes in response headers after login like this 0 int value
    "Seed_Token": Seed_Token,
    "Seed_Algorithm": Seed_Algo
}
headers = {
    "content-type": "application/json",
    "Content-Type": "application/json",
    "X-RapidAPI-Key": Rapid_Key,
    "X-RapidAPI-Host": "tiktok-device-registeration.p.rapidapi.com"
}

response = httpx.post(url, json=data, headers=headers)
print(response.json())

headers_1= {
    'connection': 'Keep-Alive',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'host': Endpoint,
    'passport-sdk-version': '19',
    'pns_event_id': str(random.randint(100,250)),
    'sdk-version': '2',
    'user-agent': devices['Device_Info']['user-agent'],
    'x-argus': response.json()['X-Argus'],
    'x-gorgon':response.json()['X-Gorgon'],
    'x-khronos': response.json()['X-Khronos'],
    'x-ladon':  response.json()['X-Ladon'],
    'x-ss-req-ticket': str(int(response.json()['X-Khronos'])*1000),
    'x-ss-stub': hashlib.md5(Payload.encode()).hexdigest().upper(),
    'x-tt-bypass-dp': '1',
    'x-tt-dm-status': 'login=0;ct=0;rt=7',
    'x-vc-bdturing-sdk-version': '2.3.5.i18n',
}



re=httpx.post(f'https://{Endpoint}/passport/user/login/?{Params}',headers=headers_1,data=Payload,cookies=devices['Cookies'],verify=ctx).text
print(re)



