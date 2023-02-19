import requests
import hashlib
import sys

def request_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    res = requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f'Unable to fetch data from api :{res.status_code}')
    return res

def get_pass_leaks(hashes, check_hash):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h==check_hash:
            return count
    return 0

def pass_check(password):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5 , tail = sha1pass[:5],sha1pass[5:]
    response = request_api_data(first5)
    return get_pass_leaks(response,tail)

def main(passwords):
    for pwd in passwords:
        count = pass_check(pwd)
        if count:
            print(f"Your Password {pwd} is not Secure. It has been found {count} times")
        else:
            print(f"Congrats!! Your password {pwd} is secure.")

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))