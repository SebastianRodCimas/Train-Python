import mariadb
import sys


def print_contacts(cur):
     """Retrieves the list of contacts from the database and prints to stdout"""


     contacts = []


     cur.execute("SELECT first_name, last_name, email FROM test.contacts")


     for (first_name, last_name, email) in cur:
        contacts.append(f"{first_name} {last_name} <{email}>")


     print("\n".join(contacts))

try:
     conn = mariadb.connect(
        user="connpy_test",
        password="passwd",
        host="192.0.2.1",
        port=3306)


     cur = conn.cursor()

     print_contacts(cur)


     conn.close()

except mariadb.Error as e:
      print(f"Error connecting to MariaDB Platform: {e}")
      sys.exit(1)

