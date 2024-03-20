import requests
import datetime
from requests_html import HTML

now = datetime.datetime.now()
year = now.year
def url_to_txt (url,filename= f"web_scraping/urlText-{year}.html", save =False):
    r= requests.get(url)
    
    
    if r.status_code == 200:
            html_text=r.text
            if save:
                with open(filename, 'w', encoding="utf-8") as f:
                
                    f.write(html_text)
                
            return html_text
    return ""
        
            
            
url ="https://www.boxofficemojo.com/year/world/"
# r = requests.get(url)
# print(r.status_code)
# print(r.text)

html_text =url_to_txt(url)

r_html = HTML(html = html_text)
# print(r_html.find("table"))
# print(r_html.find("h1"))
# print(r_html.find("a"))
table_class= ".imdb-scroll-table"
r_table = r_html.find(table_class)


if len(r_table) == 1:
    print(r_table[0].text)