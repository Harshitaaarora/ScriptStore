# Get Script Transcribed- GST
import requests
from bs4 import BeautifulSoup

url = "http://shakespeare.mit.edu/romeo_juliet/full.html"

r= requests.get(url)

soup=BeautifulSoup(r.text,"html.parser")
dialogue=soup.find("body")
script_text=dialogue.get_text(separator='\n', strip=True)

# print(script_text)
with open("GST.txt","w") as f:
    f.write(script_text)
  
print("Done")