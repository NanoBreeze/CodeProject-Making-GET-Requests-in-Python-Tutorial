from urllib.request import urlopen
from bs4 import BeautifulSoup
codeProjectHtml = urlopen("http://www.codeproject.com/")
bsInstance = BeautifulSoup(codeProjectHtml.read(), "html.parser")

memberMenu = bsInstance.find("div", {"id" : "ctl00_MemberMenu_GenInfo"})
print (memberMenu.get_text())


codeProjectPythonSearchHtml = urlopen("http://www.codeproject.com/search.aspx?q=python")
bsInstance = BeautifulSoup(codeProjectPythonSearchHtml.read(), "html.parser")
firstArticle = bsInstance.find("a", {"id": "ctl00_MC_Results_ctl00_DocTitle"})
print (firstArticle.get_text())



