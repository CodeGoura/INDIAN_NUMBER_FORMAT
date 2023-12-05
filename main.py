'''Method 1 Change the local currency to en_IN'''
import locale
locale.setlocale(locale.LC_MONETARY,'en_IN')
def money(user_money):
    '''Print formated Number'''
    fr_money = locale.currency(user_money,grouping=True)
    print(f"Formated Money is : \t {fr_money}")
user_num = int(input("Please Enter The Amount To Be formated : \n"))
money(user_num)
