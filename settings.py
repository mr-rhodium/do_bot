API_TOKEN: str = ""

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