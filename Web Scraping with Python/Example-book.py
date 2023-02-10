import requests
import lxml
import bs4

#website -> http://books.toscrape.com/catalogue/category/books/classics_6/index.html
print('1. Get title of all books with ratnig 3')

#after analysis , url to use -> https://books.toscrape.com/catalogue/category/books_1/page-2.html
#logic is to change the 2(digit) in page-2.html programatically

page_num = 0
base_url = 'https://books.toscrape.com/catalogue/category/books_1/page-{}.html'

#res = requests.get(base_url.format(51))  <head><title>404 Not Found</title></head>

books_with_rating_3 = []

#loop through pages
i = 1
while True:

    #request url and convert to soup object
    res = requests.get(base_url.format(i))
    soup = bs4.BeautifulSoup(res.text,'lxml')

    #check if page is awailable
    if soup.select('title')[0].getText() == '404 Not Found':
        break
    #get all books on the page
    else:
        book_on_page = soup.select('.product_pod')

        #loop through books on page
        #rating 3 condition
        for b in book_on_page:
            if b.select('.star-rating.Three'):
                title = b.select('h3 > a')[0]['title']
                #print(title)
                books_with_rating_3.append(title)
                #append to the list
    #print(f'page {i} done')
    i += 1

total_books = len(books_with_rating_3)
print(f'total number of book with rating 3 are = {total_books}, below is the list')

i = 1
for b in books_with_rating_3:
    print(f'{i}. {b}')
    i += 1




