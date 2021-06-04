import smtplib
import _thread, time

class Execute_and_report():

    def send_email(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()


    def start_report(self):
        result = "Subject: Kto's PC is UP ! Report"
        self.send_email("nicenoob247@gmail.com", "nicenoob1234", result)


def s(t, d):
    while 1:
        time.sleep(d)
        print(t)


_thread.start_new_thread(s, ("waiting", 100))
time.sleep(150)

execute = Execute_and_report()
execute.start_report()


