API_TOKEN: str = "961019773:AAF271xwgF8lskKr8x7exxMgzfgNGOioUuY"

class REDIS:
    PREF = "redis://"
    DB = "0"
    SERVER = "locahost"
    PORT = 6379
    SERVER_PORT = f"{PREF}{SERVER}:{PORT}/{DB}"


WEBHOOK: bool = False
URL = "https://www.digitalocean.com"
HEADERS = {
    "Accept": "*/*",
}