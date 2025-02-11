html_doc=""""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>
        PARAGRAF
    </h1>
    <ul>
        <li>Menu</li>
        <li>Menu</li>
        <li>Menu</li>
    </ul>
    <h2>
        METİN
    </h2>
    <ul>
        <li>Menu</li>
        <li>Menu</li>
        <li>Menu</li>
    </ul>
</body>
</html>
"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc,"html.parser")
result=soup.prettify()
result=soup.title
result=soup.head
result=soup.body

result=soup.title.name
result=soup.title.string

result=soup.h1
result=soup.h2
result=soup.find_all("li")
print(result)