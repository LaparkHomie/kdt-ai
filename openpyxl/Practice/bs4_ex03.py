from bs4 import BeautifulSoup
from bs4 import XMLParsedAsHTMLWarning
import warnings

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

fp = open("joins.xml", "r", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

for line in soup.find_all('item'):
    print("title:", line.title.string)
    print("description:", line.description.string)
