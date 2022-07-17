import requests
import tkinter as tk

def getNews():
    api_key="7625bfd3db8c4f4f9067b502bd73e910"
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey="+api_key
    news=requests.get(url).json()
    articles=news["articles"]
    my_articles=[]
    my_news=" "
    for articles in articles:
        my_articles.append(articles["title"])
    for i in range(10):
        my_news=my_news+str(i+1)+". "+ my_articles[i]+"\n"
    label.config(text=my_news)
canvas=tk.Tk()
canvas.geometry("1100x600")
canvas.title("News App")
canvas.configure(bg='skyblue')

button=tk.Button(canvas,font=24,text="Reload",command=getNews, bg='pink')
button.pack(pady=20)
label=tk.Label(canvas,font=18,justify="left")
label.pack(pady=20)
getNews()
canvas.mainloop()

