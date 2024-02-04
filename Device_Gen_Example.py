import requests
import os
import uuid

url = "https://tiktok-device-registeration.p.rapidapi.com/Tiktok_Device_Gen/"

rapid_key='' #Enter Your RapidApi_Key

querystring = {
  "Proxy":"username:password@host:port",
  "Country":"us",
 'Openudid': os.urandom(8).hex(), #Use Your Same Old Device Data For Reactivate Your Old Devices
 'Req_id': str(uuid.uuid4()),
 'Cdid':  str(uuid.uuid4()),
 'Clientuuid': str(uuid.uuid4()),
 'Google_aid':  str(uuid.uuid4()),
}

headers = {
	"Content-Type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": rapid_key,
	"X-RapidAPI-Host": "tiktok-device-registeration.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())


#{'Cookies': {'install_id': '7331528878471153454', 'store-country-code': 'us', 'store-country-code-src': 'did', 'store-idc': 'useast5', 'ttreq': '1$0f19d7c50fc0eb3093a52a300802452de901de35'}, 'Device_Info': {'Mssdk_Endpoint': 'mssdk16-normal-useast8.us.tiktokv.com', 'ab_version': '33.3.2', 'ac': 'wifi', 'ac2': 'wifi', 'aid': '1233', 'app_language': 'en', 'app_name': 'musical_ly', 'app_type': 'normal', 'build_number': '33.3.2', 'carrier_region': 'US', 'cdid': 'ff806113-c87f-4540-a330-a226d44fb098', 'channel': 'googleplay', 'clientuuid': '15775b02-475e-4074-9c55-c3b6001fb6ad', 'device_brand': 'realme', 'device_id': '7331528586270688810', 'device_platform': 'android', 'device_type': 'REALME_BRWST', 'dpi': '320', 'google_aid': '1c523255-5ca8-4bc8-a49e-30a56d1bd358', 'host_abi': 'armeabi-v7a', 'iid': '7331528878471153454', 'language': 'en', 'locale': 'en', 'manifest_version_code': '2023303020', 'mcc_mnc': '310650', 'okhttp_version': '4.2.137.48-tiktok', 'op_region': 'US', 'openudid': '53e32ad2028c24b9', 'os': 'android', 'os_api': '32', 'os_version': '12', 'passport-sdk-version': '19', 'region': 'US', 'req_id': '5474deec-ee9c-4a7f-8575-02454134ff1d', 'resolution': '1080*1920', 'ssmix': 'a', 'support_webview': '1', 'sys_region': 'US', 'timezone_name': 'America/New_York', 'timezone_offset': '-18000', 'uoo': '0', 'update_version_code': '2023303020', 'use_store_region_cookie': '1', 'user-agent': 'com.zhiliaoapp.musically/2023303020 (Linux; U; Android 12; en_US; REALME_BRWST; Build/N2G48H;tt-ok/3.12.13.4-tiktok)', 'version_code': '330302', 'version_name': '33.3.2'}, 'Ri_Report': True, 'Seed_Algorithm': 10, 'Seed_Token': 'MDGnEpnXqHIHLHMuhTpow4SxnLB4GyRwATUrq/taHhrUfRyBEDc/Qgd+QQOxNQDt2OkHJgTAxBLWvw7MHqf8UAWXwS6PSOYCYt0plxVeviA2rdwWWrnhpXoSYnmN7ICsZPM=', 'is_activated': 'success', 'secDeviceIdToken': 'AZoWhheN-3RAfIQzmqB4_icaj'}
