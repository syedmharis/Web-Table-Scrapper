import pandas as pd
url = input("Enter your URL to Scrap : ")
mylist = pd.read_html(url)
if len(mylist)> 1:
    for i in range(len(mylist)):
        print(mylist[i])
else:
    print("Try another link such as 'https://www.w3schools.com/html/html_tables.asp'")