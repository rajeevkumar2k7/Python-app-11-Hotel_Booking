from fpdf import FPDF
import pandas as pd

df = pd.read_csv(filepath_or_buffer='articles.csv', dtype={'id':str})
print(df)

class Articles:
    def __init__(self, item_id):
        self.item_id = item_id
        self.item_name = df.loc[df['id']==self.item_id]['name'].squeeze()
        self.price = df.loc[df['id']==self.item_id]['price'].squeeze()
    
    def item_qty(self):
        in_stock = df.loc[df['id']==self.item_id]['in stock'].squeeze()
        return in_stock
    
    def update_qty(self):
        df.loc[df['id']==self.item_id]['in stock'] -1
        df.to_csv(path_or_buf='articles.csv', index=False)



class Invoice:
    def __init__(self, item_id):
        self.item = item_id

    def generate(self):

        pdf = FPDF(orientation="portrait", unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font(family="Arial", style='b', size= 12)
        pdf.cell(w=30,h=12, txt=f'{self.item.item_id} : Invoice', align='left',ln=1)
        pdf.line(x1=10,x2=200, y1=20,y2=20)

        pdf.set_font(family="Times", style='', size= 10)
        pdf.cell(w=30,h=10, txt= f'Purchase item : {self.item.item_name}', align='left',ln=1)

        pdf.set_font(family="Times", style='i', size= 10)
        pdf.cell(w=30,h=10, txt=f'Total prcie: {self.item.price}', align='left',ln=1)
        pdf.output('item_invoice.pdf')



id = input('Enter item ID to purchase the item: ')

Item_ID = Articles(item_id=id)
qty = Item_ID.item_qty()

if qty > 0:
    Item_ID.update_qty()
    invoice = Invoice(item_id=Item_ID)
    invoice.generate()
else:
    print('Not Enough item to purchase')