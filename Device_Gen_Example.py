import requests

url = "https://tiktok-device-registeration.p.rapidapi.com/Tiktok_Device_Gen/"

rapid_key='' 

querystring = {
  "Proxy":"username:password@host:port",
  "Country":"us"
}

headers = {
	"Content-Type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": rapid_key,
	"X-RapidAPI-Host": "tiktok-device-registeration.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())


#{"is_activated": "success", "Device_Info": {"iid": "7280522761154561834", "device_id": "7280522557017884206", "passport-sdk-version": "19", "ac": "wifi", "channel": "googleplay", "aid": "1233", "app_name": "musical_ly", "version_code": "2023103030", "version_name": "31.3.3", "device_platform": "android", "os": "android", "ab_version": "31.3.3", "ssmix": "a", "device_type": "wiko", "device_brand": "WIKO_QYGPU", "language": "en", "os_api": "31", "os_version": "12", "openudid": "a0f94634068ad15b", "manifest_version_code": "2023103030", "resolution": "720*1280", "dpi": "240", "update_version_code": "2023103030", "app_type": "normal", "sys_region": "US", "mcc_mnc": "310240", "timezone_name": "America/New_York", "timezone_offset": -14400, "build_number": "31.3.3", "region": "US", "carrier_region": "US", "uoo": "0", "app_language": "en", "locale": "en", "op_region": "US", "ac2": "wifi", "host_abi": "armeabi-v7a", "cdid": "d0476399-dcfc-448c-b3d4-76267e8434e0", "support_webview": "1", "okhttp_version": "4.2.152.10-tiktok", "use_store_region_cookie": "1"}, "Cookies": {"store-idc": "useast5", "store-country-code": "us", "store-country-code-src": "did", "install_id": "7280522761154561834", "ttreq": "1$0b0a98bbd96a14f30dde1ccc8d1b0ba6da974ade"}, "secDeviceIdToken": "AqTsJsVFEWZ6_daXzvUni_KDd", "Seed_Algorithm": 10, "Seed_Token": "MDGnGJraqnIBIDd+yTwxwdWwx+B7Tn5yATB8pKsHSUmDIRbTETVtFlcqEBy9NQSm2egOIwHEyhqZuQ7OUKWmUQHGxzCKVrQFLdtnmhNLujRq/McdFrrprn0TNCuIu4SaAvE=", "Ri_Report": true}

