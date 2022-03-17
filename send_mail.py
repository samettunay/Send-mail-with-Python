import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"

# Your mail
sender_email = "samet.tunay12@gmail.com"  

# Receiver mail
receiver_email = "birtutamyazilim@gmail.com"

password = input("Your password: ")

message = "This email was sent via Python."

context = ssl.create_default_context()
server = smtplib.SMTP_SSL(smtp_server, port, context=context)
server.login(sender_email, password)
print("Login successful..")
server.sendmail(sender_email, receiver_email, message)
print("Email sent..")



