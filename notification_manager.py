import smtplib
import os

# import environmental variables
HOST_EMAIL = os.environ.get('my_email')
PASSWORD = os.environ.get("email_password")


class NotificationManager:

    """
        This class allows text messages to be email to users.
    """

    @staticmethod
    def email_user(first_name, last_name, email, message):

        """
            Email user a message.
                Parameter:
                    first_name (str): First name of flight club user.
                    last_name (str): Last name of flight club user.
                    email (str): Email address of flight club user.
                    message (str): Flight deal message.
        """

        with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:
            connection.starttls()
            connection.login(user=HOST_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=HOST_EMAIL,
                                to_addrs=email,
                                msg=f"Subject:Flight Club member {first_name} {last_name}, we've found you and amazing"
                                    f" flight deal!\n\n{message}")
