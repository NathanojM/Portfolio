title=input("Title: ")
pic=input("Picture: ")
size=input("Size: ")
url=input("URL: ")
hashtags=input("#: ")

text=f"[{title}]({url})<br>[![[{pic}|{size}]]]({url})<br>#{hashtags}"
print(text)