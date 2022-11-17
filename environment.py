from pages.sign_in_page import Sign_In_Page
from browser import Browser
from pages.forgot_password_page import Forgot_Password_Page
from pages.sign_up_page import Sign_Up_Page


def before_all(context):
    context.browser = Browser()
    context.sign_in_page = Sign_In_Page()
    context.forgot_pass = Forgot_Password_Page()
    context.sign_up_page = Sign_Up_Page()


def after_all(context):
    context.browser.close()

    # contextul e ca o cutiuta care contine cate un obiect de tipul fiecarei clase de pagini
    # de fiecare data cand adaugam o pagina noua in proiect, o vom adauga in context

    # before_all = nume de metoda standardizat care instruieste sistemul ca acele instructiuni trebuie executate intotdeauna
                    # inainte de excutarea unui scenariu