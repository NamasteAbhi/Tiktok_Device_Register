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


devices={"is_activated": "success", "Device_Info": {"iid": "7280628010981984006", "device_id": "7280626767643543045", "passport-sdk-version": "19", "ac": "wifi", "channel": "googleplay", "aid": "1233", "app_name": "musical_ly", "version_code": "310303", "version_name": "31.3.3", "device_platform": "android", "os": "android", "ab_version": "31.3.3", "ssmix": "a", "device_type": "lg", "device_brand": "LG_RDJZ1", "language": "en", "os_api": "24", "os_version": "7.0", "openudid": "1cfeedc94f096fbe", "manifest_version_code": "2023103030", "resolution": "720*1280", "dpi": "240", "update_version_code": "2023103030", "app_type": "normal", "sys_region": "PA", "mcc_mnc": "71420", "timezone_name": "America/Panama", "timezone_offset": -18000, "build_number": "31.3.3", "region": "PA", "carrier_region": "PA", "uoo": "0", "app_language": "en", "locale": "en", "op_region": "PA", "ac2": "wifi", "host_abi": "armeabi-v7a", "cdid": "3384ccd4-d3f7-481d-a6d5-554bec1cee41", "support_webview": "1", "okhttp_version": "4.2.152.10-tiktok", "use_store_region_cookie": "1"}, "Cookies": {"install_id": "7280628010981984006", "store-country-code": "pa", "store-country-code-src": "did", "store-idc": "maliva", "ttreq": "1$38169af7102f365c0143503fcbcb2d158a4f95e7"}, "secDeviceIdToken": "ApgtHUP1J5Zr81i5BHZSrZG5T", "Seed_Algorithm": 10, "Seed_Token": "MDGvHZXRq3oCLDwxhj9pwYLinbcvHXBwA2J48PdcSR2BLEmDRjBsQVZ6E0j4fE3r3ucCJwXFwRec80KCHK38V1SXkjuUSrRSfcR+mENL8Xtr+MUJDLPkpX5EN36K7tDOZfI=", "Ri_Report": 'true'}

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

Payload=urlencode({
    'username': '707660773430333230333271706e6f33303134363330',
    'password': '3c67313033717c706e3233323330624424',
    'account_sdk_source': 'app',
    'mix_mode': '1',
    'multi_login': '1'
})


url = "https://tiktok-device-registeration.p.rapidapi.com/Get_Sign/"

data = {
    "Params": Params,
    "Payload": Payload,
    "Sig_Token": Sig_Token
}
headers = {
    "content-type": "application/json",
    "Content-Type": "application/json",
    "X-RapidAPI-Key": Rapid_Key,
    "X-RapidAPI-Host": "tiktok-device-registeration.p.rapidapi.com"
}

response = httpx.post(url, json=data, headers=headers)

headers_1=response.json()| {
    'Host':'api16-normal-c-useast1a.tiktokv.com',
    'X-Ss-Stub': hashlib.md5(Payload.encode()).hexdigest().upper(),
    'Accept-Encoding': 'gzip, deflate',
    'Sdk-Version': '2',
    "X-Ss-Req-Ticket": str(int(response.json()['X-Khronos'])*1000),
    'Passport-Sdk-Version': '19',
    'X-Tt-Dm-Status': 'login=0;ct=0;rt=7',
    'X-Tt-Bypass-Dp': '1',
    'X-Vc-Bdturing-Sdk-Version': '2.3.2.i18n',
    'User-Agent': f'com.zhiliaoapp.musically/{devices["Device_Info"]["update_version_code"]}0(Linux; U; Android {devices["Device_Info"]["os_version"]}; en; {devices["Device_Info"]["device_type"]}; Build/PI;tt-ok/3.12.13.1)',
    'X-Ladon': response.json()['X-Ladon'],
    'X-Gorgon':response.json()['X-Gorgon'],
    'X-Khronos':response.json()['X-Khronos'],
    'X-Argus':response.json()['X-Argus'],
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}


re=httpx.post(f'https://api16-normal-c-useast1a.tiktokv.com/passport/user/login/?{Params}',headers=headers_1,data=Payload,cookies=devices['Cookies'],verify=ctx).text
print(re)




