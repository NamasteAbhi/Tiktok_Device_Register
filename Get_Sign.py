import time
from urllib.parse import urlencode
import requests



Rapid_Key='' #Enter Your Rapid Key


devices={'is_activated': 'success', 'Device_Info': {'iid': '7331503474641291051', 'device_id': '7331503144294532650', 'passport-sdk-version': '19', 'device_type': 'XIAOMI_YOTH7', 'device_brand': 'xiaomi', 'os_api': '25', 'os_version': '7.1.2', 'openudid': 'f01a3daff6c0e557', 'sys_region': 'US', 'mcc_mnc': '3110', 'timezone_name': 'America/New_York', 'timezone_offset': '-18000', 'region': 'US', 'carrier_region': 'US', 'app_language': 'en', 'op_region': 'US', 'cdid': '58aa63a5-84e9-46c3-a093-8e11293e3ec2', 'support_webview': '1', 'user-agent': 'com.zhiliaoapp.musically/2023303020 (Linux; U; Android 7.1.2; en_US; XIAOMI_YOTH7; Build/N2G48H;tt-ok/3.12.13.4-tiktok)', 'Mssdk_Endpoint': 'mssdk16-platform-useast5.us.tiktokv.com', 'ac': 'wifi', 'channel': 'googleplay', 'aid': '1233', 'app_name': 'musical_ly', 'version_code': '330302', 'version_name': '33.3.2', 'device_platform': 'android', 'os': 'android', 'ab_version': '33.3.2', 'ssmix': 'a', 'language': 'en', 'manifest_version_code': '2023303020', 'resolution': '1080*1920', 'dpi': '320', 'update_version_code': '2023303020', 'app_type': 'normal', 'build_number': '33.3.2', 'uoo': '0', 'locale': 'en', 'ac2': 'wifi', 'host_abi': 'armeabi-v7a', 'okhttp_version': '4.2.137.48-tiktok', 'use_store_region_cookie': '1', 'google_aid': '918f2eb7-55ee-49a5-9e6f-50a666d18b72', 'clientuuid': '9eb1822c-0c30-488b-810f-d9897f6c172b', 'req_id': '3cad660c-29ae-481b-b451-db60ec5ab106'}, 'Cookies': {'store-idc': 'useast5', 'store-country-code': 'us', 'store-country-code-src': 'did', 'install_id': '7331503474641291051', 'ttreq': '1$7ba79f7160e931963a0a22a9bdda1eec7940002b'}, 'secDeviceIdToken': 'AXC19EKtvhrMvWpXKXIZHP9Nh', 'Seed_Algorithm': 12, 'Seed_Token': 'MDGiHJ/SrHIOIT8xgzw0k4PgnOd6GCVwVGco9vYPTEvRLhmLEmRpHQJ8R0n4f03r3+4BLwnOxRaT80KCSfDwAgPCmzeUSecBLcR+mk9F8XtqrJUJCunnonAUNSnd6oSeZfI=', 'Ri_Report': True}

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
            "resolution": "720*1280",
            "dpi": "240",
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
            "host_abi": "armeabi-v7a",
            "cdid":devices['Device_Info']["cdid"],
            "support_webview": "1",
            "okhttp_version": devices['Device_Info']["okhttp_version"],
            "use_store_region_cookie": "1"
        }).replace('%2A', '*')

Sig_Token=devices['secDeviceIdToken']
Seed_Token=devices['Seed_Token']
Seed_Algo=devices['Seed_Algorithm']

Payload=urlencode({
    'username': '707660773430333230333271706e6f33303134363330',
    'password': '3c67313033717c706e3233323330624424',
    'account_sdk_source': 'app',
    'mix_mode': '1',
    'multi_login': '1'
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

response = requests.post(url, json=data, headers=headers)

print(response.json())
