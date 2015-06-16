def send_email():
   import smtplib
   import subprocess
   import time
   from os import path

   from cronos import cronos

   c = cronos.Cronos()
   today = time.strftime("%m/%d/%Y")

   p = subprocess.Popen('ls log/ |sort', shell=True, stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT)
   logfile = path.join('log', p.stdout.readlines()[-1].strip())
   body = ''
   with open(logfile, 'r') as f:
       body = f.read()
   gmail_user = c.get('gmail_user')
   gmail_pwd = c.get('gmail_pwd')
   FROM = c.get('from')
   TO = ['jvesuna314@gmail.com'] #must be a list
   SUBJECT = 'LD {0}'.format(today)
   TEXT = body

   message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
   """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
   try:
       server = smtplib.SMTP("smtp.gmail.com", 587)
       server.ehlo()
       server.starttls()
       server.login(gmail_user, gmail_pwd)
       server.sendmail(FROM, TO, message)
       server.close()
       print 'successfully sent the mail'
   except:
       print "failed to send mail"

def main():
    send_email()

if __name__ == '__main__':
    main()
