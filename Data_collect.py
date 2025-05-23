from bs4 import BeautifulSoup
import os
import pandas as pd

Smartphone_specs = {'Title': [],'Display': [],'Storage':[],'Camera':[],'Processor':[],'Battery':[]}

for file in os.listdir("Smartphone_flipkart"):
    try: 
        with open (f"Smartphone_flipkart/{file}") as f:
            html_doc = f.read()    
        soup = BeautifulSoup(html_doc, 'html.parser')
        t =  soup.find('div',class_='KzDlHZ')
        title = t.get_text() #type: ignore
        u= soup.find_all('li',class_="J+igdf")

        p1 = u[0].get_text()
        
        p2 = u[1].get_text()
        p3 = u[2].get_text()
        p4 = u[3].get_text()
        p5 = u[4].get_text()
    

        Smartphone_specs["Title"].append(title)
        Smartphone_specs["Storage"].append(p1)
        Smartphone_specs["Display"].append(p2)
        Smartphone_specs["Camera"].append(p3)
        Smartphone_specs["Battery"].append(p4)
        Smartphone_specs["Processor"].append(p5)
       
    except Exception as  e :
        print(e)

df = pd.DataFrame(data = Smartphone_specs)
df.to_csv("Flipkart_Smartphoneslist.csv")

print("Csv file Done")
    
    
   


 