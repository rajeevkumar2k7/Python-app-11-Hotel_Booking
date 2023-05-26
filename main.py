import pandas as pd

df = pd.read_csv(filepath_or_buffer='hotels.csv', dtype={"id":str})
card_df = pd.read_csv(filepath_or_buffer='cards.csv', dtype=str).to_dict(orient='records')
card_sec_df = pd.read_csv(filepath_or_buffer='card_security.csv', dtype=str)
print(card_df)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id']==self.hotel_id]['name'].squeeze()
        self.city = df.loc[df['id']==self.hotel_id]['city'].squeeze()

    def book(self):
        
        df.loc[df['id']==self.hotel_id, 'available']='no'
        df.to_csv(path_or_buf='hotels.csv', index=False)

    def available(self):
        availablity = df.loc[df['id'] == self.hotel_id]['available'].squeeze()
        if availablity == "yes":
            return True
        else:
            return False


class CreditCard:
    def __init__(self, number):
        self.number = number
    
    def validate(self, expiration, cvc, name):
        card_detail = {'number':self.number, 'expiration':expiration,
                       'cvc':cvc, 'holder':name}
        if card_detail in card_df:
            return True
        else:
            return False
        
class CradSecurity(CreditCard):
    def Authenticate(self, credit_pwd):
        password = card_sec_df.loc[card_sec_df['number']==self.number]['password'].squeeze()
        if password == credit_pwd:
            return True
        else:
            False



class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f'''
        Thank you for the booking
        Here is the detail of the Hotel booking
        Customer name = {self.customer_name}
        Hotel Name = {self.hotel.name}
        City = {self.hotel.city}
        '''
        print(content)

class SpaReservation(ReservationTicket):
    def generate(self):
        content = f'''
        Thank you for the booking
        Here is the detail of the SPA booking
        Customer name = {self.customer_name}
        Hotel Name = {self.hotel.name}
        City = {self.hotel.city}
        '''
        print(content)


print(df)

hotel_ID = input("Enter the Id of the hotel:")
hotel = Hotel(hotel_id=hotel_ID)

if hotel.available():
    hotel.book()

    name = input("Enter your name: ")
    cred_num = input('Enter Credit card number: ')
    credit_card= CradSecurity(number=cred_num)
    exp_dt = input("Enter expiry date: ")
    cvc_num = input("Enter cvc Number: ")
    user_pwd = input("Enter password: ")

    if credit_card.validate(expiration=exp_dt, cvc=cvc_num,name=name):
        if credit_card.Authenticate(credit_pwd=user_pwd):
            spa_reservation = input("Do you want to book spa? yes or no: ")
            if spa_reservation == "no":
                reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
                reservation_ticket.generate()
            else:
                spa_ticket = SpaReservation(customer_name=name, hotel_object=hotel)
                spa_ticket.generate()
        else:
            print('Credit card is not valid')
    else:
        print("Authentication failed")
else:
    print("Hotel is not free")  