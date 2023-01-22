from bs4 import BeautifulSoup
import requests,openpyxl

excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="movie list"
sheet.append(['rank','movie','rating','year'])

try:
    response=requests.get("https://www.imdb.com/chart/top/")
    soup=BeautifulSoup(response.text,'html.parser')
    movies=soup.find('tbody',class_="lister-list").find_all("tr")

    for movie in movies:

        rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
        movie_name= movie.find('td', class_="titleColumn").a.text
        rate= movie.find('td', class_="ratingColumn").strong.text
        year=movie.find('td', class_="titleColumn").span.text.replace('(',"")
        year=year.replace(')',"")

        print(rank,movie_name,rate,year)
        sheet.append([rank,movie_name,rate,year])

except:
    print("e")


excel.save("movies.xlsx")

