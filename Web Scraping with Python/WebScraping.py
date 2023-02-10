print('WEB SCRAPING')

#import libraries
import requests
import bs4
import lxml

print('1. Grabbing the page Title and other tags')

#using example.com  -> https://example.com/

result = requests.get("http://www.example.com/")

print(type(result))
#print(result.text)

soup = bs4.BeautifulSoup(result.text,"lxml")
#print(soup)

#since soup.select returns a 'list' of all tags , we can traverse throut it using index 
#and getText method helps to get the text out of it
site_title = soup.select("title")[0].getText()
print(f'title is  -> {site_title}')

site_para = soup.select("p")[0].getText()
print(f'site paragraph is -> {site_para}')


print('\n1. Grabbing the Class elements')
result1 = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper#Places')

soup1 = bs4.BeautifulSoup(result1.text,'lxml')

table_of_contents = soup1.select('.vector-toc-text')

print(f'table of content has below elements : \n\n{table_of_contents[0].text}')

#for text in table_of_contents:
#    print(text.getText())


print('\n2. Grabbing the Image elements')

images = soup1.select('.image > img')
#print(f'images -> {images}')

computor = images[0]
print(f'images -> {computor}')
#grab url
image_url = computor['src']
print(f"images url -> {image_url}")
#write to computor
img = requests.get('https:'+image_url)
f = open('myImage.jpg','wb')
f.write(img.content)