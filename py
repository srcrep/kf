import config

api_key = "config.api_key"
api_secret = "config.api_secret"
api_passphrase = "config.api_passphrase"
url = ''
now = int(time.time() * 1000)
str_to_sign = str(now) + 'GET' + '/api/v1/position?symbol=XBTUSDM'
signature = base64.b64encode(
    hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
passphrase = base64.b64encode(hmac.new(api_secret.encode('utf-8'), api_passphrase.encode('utf-8'), hashlib.sha256).digest())
headers = {
    "KC-API-SIGN": signature,
    "KC-API-TIMESTAMP": str(now),
    "KC-API-KEY": api_key,
    "KC-API-PASSPHRASE": passphrase,
    "KC-API-KEY-VERSION": "2"
}
