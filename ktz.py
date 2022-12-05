import requests
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main():
    count = 0
    i = 0
    #file = open("emails.txt", "r")
    emails = ["aydana.aydos@inbox.ru", "saya_maratova@bk.ru", "asel_makulbekova_90@inbox.ru", "saylybekov00@bk.ru",
              "zhanpeisov.abay@bk.ru", "rusik_br@inbox.ru", "zhantemir_r@mail.ru", "alibek.shaymardanov@bk.ru",
              "alpamys_s61@mail.ru", "serikbaysazanbaev@gmail.com", "sildinov@internet.ru", "zharaspaeva.dias@bk.ru",
              "aynur-1994@internet.ru", "gulnar-71@internet.ru", "zhanat1969@internet.ru", "babaeva.aruzhan@mail.ru",
              "asema.muhina@mail.ru", "aygul63@internet.ru", "nurkhasym@internet.ru", "dusenova.777@mail.ru",
              "hadiya200@mail.ru", "tashev707@mail.ru", "bastemiev707@mail.ru", "rizabek717@mail.ru",
              "tolegenovadd@mail.ru", "tugaeva.lazzat@mail.ru", "kydyrsikhanova@bk.ru", "yesimbekov90@list.ru",
              "kadraliyevaa98@bk.ru", "mamyr76@list.ru", "dyusenova.94@bk.ru", "zholkenova99@bk.ru",
              "zhandos.zhanerke@bk.ru", "usenova.tomiris@bk.ru", "botbaybek84@bk.ru", "kkuntuar@list.ru", "abzib@bk.ru",
              "zhazybayeva03@bk.ru", "zhumabekova.ayya@bk.ru", "kumisbekova.zarina@bk.ru", "kelimbetova96@inbox.ru",
              "marat_abay@inbox.ru", "sarsembayev98@inbox.ru", "sarsembayeva_a@internet.ru", "shorzhanovaa@bk.ru",
              "akylbay93@list.ru", "mukhanova.87@internet.ru", "tyshkanbayeva90@bk.ru", "uzhmanova@inbox.ru",
              "makulbayev90@inbox.ru", "tturgynbekov@bk.ru", "shikbayeva@inbox.ru", "nemadjan_1979@mail.ru",
              "kos.pvl@mail.ru", "kostya03_89@mail.ru", "grandfu00@mail.ru", "sadykovasaira@mail.ru",
              "karavantranzit@bk.ru", "translogistik777@inbox.ru", "megatranss@bk.ru", "askhat.kara@mail.ru",
              "azamat.saniyazov@mail.ru", "maha.zhuma@mail.ru", "ken.luiza@mail.ru", "zbusakova@list.ru",
              "kairkenovss@mail.ru", "tugayevnazimbek@mail.ru"]
    for user in emails:
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                      '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/107.0.0.0 Safari/537.36 "
        }
        if(user == "askhat.kara@mail.ru" or user == "kos.pvl@mail.ru"):
            data = {
                'login': user,
                'password': "Fastroad1122"
            }
        elif(user == "karavantranzit@bk.ru" or user == "translogistik777@inbox.ru" or user == "megatranss@bk.ru"):
            data = {
                'login': user,
                'password': "Izikatka228uuu*"
            }
        elif(user == "nemadjan_1979@mail.ru"):
            data = {
                'login': user,
                'password': "izikatka228uuu*"
            }
        else:
            data = {
                'login': user,
                'password': "kazahstan013"
            }

        url = 'https://new.fastroad.kz/api/auth/signin'
        base_url = "https://new.fastroad.kz/api/user/orders"
        try:
            response = requests.post(url, data=data, headers=header).json()
            myToken = response['accessToken']
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                          '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/107.0.0.0 Safari/537.36",
                'x-access-token': myToken
            }

            response = requests.get(base_url, headers=headers).json()
            max_id = -999
            message = "Заявки:"

            for order in response:
                if max_id < order['id']:
                    max_id = order['id']

            for order in response:
                if order['id'] == max_id and order['status'] == 'pending':
                    message += f"У пользователя {user} номер заявки {max_id} был согласован\n"

        except Exception:
            print(Exception)

        count = count + 1
        print(str(count) + " " + user + " : " + message)


       # time.sleep(60)

        if message != "Заявки:":
            send_email(message)
    main()



def send_email(message):
    fromaddr = "rizabek717@mail.ru"
    toaddr = "rizabekiitu@gmail.com"
    toaddr1 = "rusik_br@inbox.ru"
    mypass = "TuztWTYQ3PNpy48FKAE8"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Order has been accepted"

    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr1, text)
    server.quit()


if __name__ == "__main__":
    main()
