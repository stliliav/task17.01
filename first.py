class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def method(self):
        return ("Name of a book: " + self.title +"\nAuthor: " + self.author + "\nYear of publishing: "+ self.year)
chosen = (Book("Crime and Punishment", "Dostoevsky Fedor Mikhailovich", "1866"))
print(chosen.method())