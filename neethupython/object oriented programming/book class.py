class Book:
    def __init__(self,library_name,book_name,author,pages):
        self.library_name=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
        print(self.library_name,"\n",self.book_name,"\n",self.author,"\n",self.pages)
b=Book("kichoos","paathummayude aadu","basheer",200)