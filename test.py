from bs4 import BeautifulSoup

if __name__ == '__main__':
  message = 'dgfdh'
  soup = BeautifulSoup(message,'html.parser')

  print(soup.find_all())
  print(len(soup.find_all()))
  if len(soup.find_all()):
    print('test')