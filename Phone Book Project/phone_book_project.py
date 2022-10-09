import colorama
import mysql.connector
import sys
from colorama import Fore, Style
from  datetime import datetime
from tabulate import tabulate
colorama.init()

def registered_user_prompt():
    registered_user_choice = input("Are you a registered User[Yes/No]: ").lower()
    print()
    if registered_user_choice in ("yes","no"):
        return registered_user_choice
    else:
        print(Fore.RED+"Please Enter a Valid Choice !"+Style.RESET_ALL)
        registered_user()
        sys.exit()

def register():
    print(Fore.BLUE+"\n--------------------- Registration ----------------------------\n"+Style.RESET_ALL)
    register_user_name = input("Enter you name: ")
    register_user_email = input("Enter your email id: ")
    register_user_password = input("Enter a password: ")
    sql_user_already_exsists = """SELECT user_email
                                FROM authentication
                                WHERE user_email=%s
                                    """
    cursor.execute(sql_user_already_exsists, (register_user_email,))
    user_already_exsists_email_list = cursor.fetchall()
    if len(user_already_exsists_email_list) > 0:
        print(Fore.RED+"\nUser Already Exsists ! Please Login..."+Style.RESET_ALL)
        login()
    else:
        sql_register_user = """INSERT INTO authentication
                          VALUES(%s,%s,%s)
                              """
        cursor.execute(sql_register_user, (register_user_name, register_user_email, register_user_password))
        connection.commit()
        print(Fore.GREEN+"\nUser {},Registered Succesfully...\n".format(register_user_name)+Style.RESET_ALL)
        login()

def login_date_time():
    date_time_now=datetime.now()
    date_time_now_string=date_time_now.strftime("%a %b %d %X %Y")
    print(Fore.YELLOW+date_time_now_string+Style.RESET_ALL)

def login():
    print(Fore.BLUE + "\n--------------------- Login ----------------------------\n" + Style.RESET_ALL)
    user_email=input("Enter your email id: ")
    user_password=input("Enter your password: ")
    sql_user_authentication =  """  SELECT *
                                    FROM authentication
                                    WHERE user_email=%s """
    cursor.execute(sql_user_authentication, (user_email,))
    sql_user_authentication_result=cursor.fetchall()
    if len(sql_user_authentication_result)>0:
            if sql_user_authentication_result[0][2]==user_password:
                print(Fore.GREEN+"\nUser: {}, Logged in Successfully....".format(sql_user_authentication_result[0][0])+Style.RESET_ALL)
                login_date_time()
            else:
                print(Fore.RED+"\nPassowrd does not match with given User! "+Style.RESET_ALL)
                password_incorrect_choice=input("\nDo want to exit ?[Yes/No]: ").lower()
                print()
                if password_incorrect_choice=="no":
                    login()
                else:
                    phone_book_closed()
                    sys.exit()
    else:
        print(Fore.RED+"\nUser Not Found ! Please register..."+Style.RESET_ALL)
        login_failed_registration_choice=input("\nDo want to register ?[Yes/No]: ").lower()
        print()
        if login_failed_registration_choice == "yes":
            register()
        else:
            phone_book_closed()
            sys.exit()

def user_authentication():
    print(Fore.CYAN + "\nWelcome To The Digital PhoneBook \n" + Style.RESET_ALL)
    registered_user_choice = registered_user_prompt()
    if registered_user_choice == "yes":
        login()
    else:
        register()

def add_action():
    contact_first_name = input("Enter contact first name: ")
    contact_last_name = input("Enter contact last name: ")
    contact_email = input("Enter contact email: ")
    contact_phone_number = input("Enter contact phone number: ")
    sql_add_contact = """INSERT INTO contacts
                       VALUES(DEFAULT,%s,%s,%s,%s)
                        """
    cursor.execute((sql_add_contact), (contact_first_name, contact_last_name, contact_email, contact_phone_number))
    connection.commit()
    print(Fore.GREEN+"\nContact: {} {}, added Successfully....".format(contact_first_name,contact_last_name))

def view_action():
    user_contact_query = input("Enter Contact Name: ")
    sql_get_contact = """
                        SELECT *
                        FROM contacts
                        WHERE first_name=%s"""
    cursor.execute(sql_get_contact, (user_contact_query,))
    user_contact_result = cursor.fetchall()
    header_contacts=["ContactId","FirstName","LastName","EmailId","PhoneNumber"]
    print(tabulate(user_contact_result,headers=header_contacts, tablefmt='fancy_grid', missingval='N/A'))

def view_all_action():
    sql_get_all_contact = """
                        SELECT *
                        FROM contacts"""
    cursor.execute(sql_get_all_contact, ())
    all_contacts = cursor.fetchall()
    header_contacts=["ContactId","FirstName","LastName","EmailId","PhoneNumber"]
    print(tabulate(all_contacts,headers=header_contacts, tablefmt='fancy_grid', missingval='N/A'))

def update_action():
    contact_id = input("Enter Contact Id: ")
    print("What do you want to Update? ")
    print("{}    -->   to update first name\n{}     -->   to update last name\n{}         -->   to update email\n{}  -->   to update phone number  ".format(Fore.YELLOW+"[first-name]"+Style.RESET_ALL,Fore.YELLOW+"[last-name]"+Style.RESET_ALL,Fore.YELLOW+"[email]"+Style.RESET_ALL,Fore.YELLOW+"[phone-number]"+Style.RESET_ALL))
    user_contact_update_choice = input("\nEnter what do you want to update >>>")
    if user_contact_update_choice == "first-name":
        column_value = "first_name"
        contact_update_value = input("Enter new first name: ")
    elif user_contact_update_choice == "last-name":
        column_value = "last_name"
        contact_update_value = input("Enter new last name: ")

    elif user_contact_update_choice == "email":
        column_value = "email_id"
        contact_update_value = input("Enter new email id: ")

    elif user_contact_update_choice == "phone-number":
        column_value = "phone_number"
        contact_update_value = input("Enter new phone number: ")

    else:
        print("Please Select a Valid Field !")
        return None
    cursor.execute("UPDATE contacts SET %s='%s' WHERE contact_id=%s" % (column_value, contact_update_value, contact_id))
    connection.commit()
    print(Fore.GREEN+"\nContact Details Updated Successfully..."+Style.RESET_ALL)

def delete_action():
    contact_id = input("Enter contact id: ")
    sql_contact_delete = """
                            DELETE
                            FROM contacts
                            WHERE contact_id=%s"""
    cursor.execute(sql_contact_delete, (contact_id,))
    connection.commit()
    print(Fore.GREEN+"\nContact Deleted Successfully...."+Style.RESET_ALL)

def delete_all_action():
    sql_delete_all = """TRUNCATE contacts"""
    cursor.execute(sql_delete_all)
    connection.commit()
    print(Fore.GREEN+"\nAll Contacts Deleted Successfully.... "+Style.RESET_ALL)

def user_action():
    print("\nWhat do you want to do?")
    print(
        "{}           --->     to add contact \n{}          --->     to view a contact\n{}      --->     to view all contacts\n{}        --->     to update a contact\n{}        --->     to delete a contact\n{}    --->     to delete all contacts".format(Fore.CYAN+"[add]"+Style.RESET_ALL,Fore.CYAN+"[view]"+Style.RESET_ALL,Fore.CYAN+"[view-all]"+Style.RESET_ALL,Fore.CYAN+"[update]"+Style.RESET_ALL,Fore.CYAN+"[delete]"+Style.RESET_ALL,Fore.CYAN+"[delete-all]"+Style.RESET_ALL))
    user_action_choice = input("\nEnter Action you want to perform >>> ")
    print()
    if user_action_choice == "add":
        add_action()
    elif user_action_choice == "view":
        view_action()
    elif user_action_choice == "view-all":
        view_all_action()
    elif user_action_choice == "update":
        update_action()
    elif user_action_choice == "delete":
        delete_action()
    elif user_action_choice == "delete-all":
        delete_all_action()
    else:
        print(Fore.RED+"Please Select a Valid Action !"+Style.RESET_ALL)
    more_actions=input("\nDo you want to perform more Actions?[Yes/No]  ").lower()
    if more_actions=="yes":
        user_action()
    else:
        phone_book_closed()

def digital_phone_book():
    try:
        user_authentication()
        user_action()
    except Exception:
        print(Fore.RED+"There is some issue while performing given action !"+Style.RESET_ALL)
        print(Fore.GREEN+"Restarting your Phone Book ....."+Style.RESET_ALL)
        user_action()

def phone_book_closed():
    if connection.is_connected():
        connection.close()
        cursor.close()
        print(Fore.GREEN+"Phone Book closed..."+Style.RESET_ALL)

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='phone_book',
                                         user='root',
                                         password='root')
    cursor = connection.cursor()
    digital_phone_book()
except mysql.connector.Error:
    print(Fore.RED+"Your Phone Book is temporarily unavailable ..."+Style.RESET_ALL)
finally:
    phone_book_closed()