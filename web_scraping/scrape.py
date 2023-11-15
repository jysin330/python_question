import requests
import datetime
now = datetime.datetime.now()
year = now.year
def url_to_file (url,filename= f"web_scraping/urlText-{year}.html"):
    r= requests.get(url)
    if r.status_code == 200:
        html_text=r.text
        with open(filename, 'w', encoding="utf-8") as f:
           
            f.write(html_text)
            
        return html_text
    return ""
        
            
            
url ="https://www.boxofficemojo.com/year/world/"
# r = requests.get(url)
# print(r.status_code)
# print(r.text)

url_to_file(url)