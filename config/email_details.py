import os

email_host = 'smtp.gmail.com'
email_port = '587'
email_host_user = os.environ['EMAIL_ADD']
email_host_password = os.environ['EMAIL_PASS']
default_from_email = os.environ['EMAIL_ADD']

