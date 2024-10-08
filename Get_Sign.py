import requests

Rapid_Key = ''  # Enter Your Rapid Key

url = "https://bytedancesolutions.p.rapidapi.com/getsign"

payload = {
    "querystring": "user_id=7304926335365104645&sec_user_id=MS4wLjABAAAAmJxZE4VCnvOSKvIyGgvyMAvtmB_hxmsKjdgBGmzXSPaXx87UGJAN1Q1Vbr3eRHE9&type=1&channel_id=0&from=13&from_pre=13&item_id=7402065520150859013&enter_from=homepage_hot&action_time=1728214227154&is_network_available=true&iid=7422269625251202822&device_id=7413249597273605675&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=360704&version_name=36.7.4&device_platform=android&os=android&ab_version=36.7.4&ssmix=a&device_type=RMX2117&device_brand=realme&language=en&os_api=30&os_version=11&openudid=e1d7059e31fa2e99&manifest_version_code=2023607040&resolution=1080*2158&dpi=480&update_version_code=2023607040&_rticket=1728214227168&is_pad=0&app_type=normal&sys_region=US&last_install_time=1728213879&timezone_name=Asia%2FKolkata&app_language=en&ac2=wifi5g&uoo=0&op_region=US&timezone_offset=19800&build_number=36.7.4&host_abi=arm64-v8a&locale=en&region=US&ts=1728214224&cdid=da8a97a5-143b-4402-9282-4e58c38ffe6b",
    "x_ss_stub": "00000000000000000000000000000000",
    "sessionid": "00000000000000000000000000000000",
    "Sig_Token": "AKLtyIKTPC2UZSe0rqTNO7kfQ",
    "Seed_Token": "MDGiGJjQqXEPITp9yW1mkoG0nLN7SHV3WDdz8PhdSEyDKknTGmxqFwcqQka2NQWm2ekFLgLHwRqSvA7OUKCkUAaUkDeJVrAOKoxnmkYXvzQx/cQUFunprnpHZS2N4N6WBvE=",
    "Seed_Algo": 8,
    "Bd_Kmsv": "0",
    "Bd_Lanusk": "#0a2EKUVGM6QN/NUrrwUdQjcwpyAOrmzzITN5QPfQQZpX4T07bbhGuw2Yj1xNQVVjm0Usd10EOQ5jPMz+",
    "msAppID": "1233",
    "deviceID": "7413249597273605675",
    "licenseID": "2142840551",
    "appVersion": "36.7.4",
    "sdkVersionStr": "v05.00.07-ov-android",
    "sdkVersion": 83887904,
    "appVersionConstant": 67138560,
    "phoneInfo": "RMX2117",
    "channel": "googleplay"
}
headers = {
    "x-rapidapi-key": Rapid_Key,
    "x-rapidapi-host": "bytedancesolutions.p.rapidapi.com",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())

# Example Response
"""
{
  "X-Argus": "nIBDGeOKLfl/yP6GgTk8HfgDE3EUDaqLVDKgADWY8/oxT/ugNjtubQ1cpD1tZT5suKjsf6Dz1AV1BWxm9rtQomYKuQz7rPiluVe8e/KedfBo9nUKoRzvyrC5aSezXx/+dHD8yYlv823WyJNGJPp1uy1J1p8qbhz1s4IEMplkg5lfT0BvkPTuaBBnxNqL7uDZiFUwL3zeWigbosG0bHosLg101cyGUDXXSCEcDIeXdB+1bKnpd8RZbw+StCOEOaaMErkJE8e7xQ1kpVJYWu5aw2tHCRhibpGX057l4yYDoIhRHeg9625id0WrLf6UG73KTP6tRK72hG00kp3c/pVwvcQjtAaXNREc5iyFAXJsI8UVwrcacJ9qXi5QATnwHbozG6xwoavMSP7FYzg9F/EuZOEeMeDWigR7Mrar2OXZgNBDxdTK99pLjfKQZjMaPHH2BTLwEsuT6SReVIzzeUaGlgjGzOe+yLy8GJbkqTfpAIZ0xMp/pCbuC7LV04UzzFdsY0CSp84AS+V6geRVPamUEfFgXMn6AjtK5xM1XzdVDKxTkMKweo4T07C2G7Jd6/oFa7OE4slAERmGxXZdC+hTIOMqQbxCjFOI/uOPAW85MkSGP+atpOnfI9scpT9LCU1CacM=",
  "X-Gorgon": "8404637d0000bddb453792a6df2af1208d7bdcbc84253d0c992a",
  "X-Khronos": "1728420715",
  "X-Ladon": "nF5UkreYpHI8mLBR1Do9YXz05cZFbmD1zQbMUGBGqr7pUzdO"
}
"""
