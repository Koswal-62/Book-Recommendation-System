import pickle
import streamlit as st
import requests
from warnings import filterwarnings

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeOptions

filterwarnings('ignore')

#check if we need the url from the site or csv file
#change the values where needed


def fetch_poster(bookurll):
    
    try:
        # Fetch HTML content of the Goodreads book page
        response = requests.get(bookurll)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the book cover image URL
        cover_img_tag = soup.find('meta', property='og:image')
        if cover_img_tag:
            cover_img_url = cover_img_tag['content']
            return cover_img_url
        else:
            return None

    except Exception as e:
        print(f"Error fetching book details: {e}")
        return None



#check the names of column used
def recommend(book):
    index=books[books['BookName']==book].index[0]
    simi_books=similarity[index]
    rcmd_book=[]
    rcmd_poster=[]
    rcmd_rating=[]
    rcmd_pages=[]
    rcmd_author=[]
    rcmd_language=[]
    for i in simi_books[0:5]:
        i=int(i)
        book_url=books.iloc[i]['bookurl']
        #b=books.iloc[i]['BookName']
        rcmd_poster.append(fetch_poster(book_url))
        rcmd_book.append(books.iloc[i]['BookName'])
        rcmd_rating.append(books.iloc[i]['Averagerating'])
        rcmd_pages.append(books.iloc[i]['pages'])
        rcmd_author.append(books.iloc[i]['Author'])
        rcmd_language.append(books.iloc[i]['Language'])

    return rcmd_language,rcmd_author,rcmd_book,rcmd_pages,rcmd_poster,rcmd_rating

st.markdown("""
    <style>
        body {
            background-color: #272727;
            color: #ffffff; /* Change text color to white for better visibility */
        }
    </style>
""", unsafe_allow_html=True)


st.header('BOOK RECOMMENDER APP')
books=pickle.load(open(r'E:\DS PROJECTS\SQL & FRONTEND\library\5.Final BookDetails\Book_Details1.pkl','rb'))
similarity=pickle.load(open(r'E:\DS PROJECTS\SQL & FRONTEND\library\Similarity\simi.pkl','rb'))

book_list=books['BookName'].values
selected_book=st.selectbox(
    'Type or select a movie to get recommendation',
    book_list
)

if st.button('Show recommendation'):
    rcmd_Language,rcmd_Author,rcmd_Book,rcmd_Pages,rcmd_Poster,rcmd_Rating=recommend(selected_book)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(rcmd_Book[0])
        st.image(rcmd_Poster[0])
        st.text(rcmd_Author[0])
        st.text(rcmd_Language[0])
        st.text(rcmd_Rating[0])
        st.text(rcmd_Pages[0])

    with col2:
        st.text(rcmd_Book[1])
        st.image(rcmd_Poster[1])
        st.text(rcmd_Author[1])
        st.text(rcmd_Language[1])
        st.text(rcmd_Rating[1])
        st.text(rcmd_Pages[1])

    with col3:
        st.text(rcmd_Book[2])
        st.image(rcmd_Poster[2])
        st.text(rcmd_Author[2])
        st.text(rcmd_Language[2])
        st.text(rcmd_Rating[2])
        st.text(rcmd_Pages[2])

    with col4:
        st.text(rcmd_Book[3])
        st.image(rcmd_Poster[3])
        st.text(rcmd_Author[3])
        st.text(rcmd_Language[3])
        st.text(rcmd_Rating[3])
        st.text(rcmd_Pages[3])

    with col5:
        st.text(rcmd_Book[4])
        st.image(rcmd_Poster[4])
        st.text(rcmd_Author[4])
        st.text(rcmd_Language[4])
        st.text(rcmd_Rating[4])
        st.text(rcmd_Pages[4])
