# -*- coding: utf-8 -*-
#MADE BY : AYKAN UGUR WITH LOTS OF LOVE AND A LITTLE PYHTON KNOWLEDGE
# This code defines a class hierarchy for different types of archive items (Book, Article, Podcast)
class ArchiveItem():
    def __init__(self,uid,title,year):
        self.uid = uid
        self.title = title
        self.year = year
        
    def __str__(self):
        return f"ArchiveItem(uid={self.uid}, title={self.title}, year={self.year})"
    
    def __eq__(self, other):
        pass
    
    def is_recent(self,n):
        return self.year >= (2025-n)

class Book(ArchiveItem):
    def __init__(self,uid,title,year,author,pages):
        super().__init__(uid,title,year)
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{super().__str__()}, author={self.author}, pages={self.pages}"

class Article(ArchiveItem):
    def __init__(self,uid,title,year,journal,doi):
        super().__init__(uid,title,year)
        self.journal = journal
        self.doi = doi
        
        
    def __str__(self):
        return f"{super().__str__()}, journal={self.journal}, doi={self.doi}"
        
class Podcast(ArchiveItem):
    def __init__(self,uid,title,year,host,duration):
        super().__init__(uid,title,year)
        self.host = host
        self.duration = duration
    
    def __str__(self):
        return f"{super().__str__()}, host={self.host}, duration={self.duration}"


def save_to_file(items, filename):
    with open(filename, 'w') as f:
        for item in items:
            if isinstance(item, Book):
                f.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
            elif isinstance(item, Article):
                f.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
            elif isinstance(item, Podcast):
                f.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n")

def load_from_file(filename):
    items = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if parts[0] == 'Book':
                items.append(Book(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
            elif parts[0] == 'Article':
                items.append(Article(parts[1], parts[2], int(parts[3]), parts[4], parts[5]))
            elif parts[0] == 'Podcast':
                items.append(Podcast(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
    return items



ArchiveItems = []

book1 = Book("B1","Book 1",2023,"Author 1",300)
book2 = Book("B2","Book 2",2024,"Author 2",250)
article1 = Article("A1","Article 1",1900,"Journal 1","doi:10.1000/xyz123")
article2 = Article("A2","Article 2",2023,"Journal 2","doi:10.1000/xyz456")
Podcast1 = Podcast("P1","Podcast 1",2023,"Host 1",60)
Podcast2 = Podcast("P2","Podcast 2",2024,"Host 2",45)

ArchiveItems.append(book1)
ArchiveItems.append(book2)
ArchiveItems.append(article1)
ArchiveItems.append(article2)
ArchiveItems.append(Podcast1)
ArchiveItems.append(Podcast2)
print("################NO FILTER PRINT #################")


save_to_file(ArchiveItems, 'archive_items.txt')
loaded_items = load_from_file('archive_items.txt')
Value = 1
for item in loaded_items:
    if item.uid[0] == "B":
        print(f"{Value} :  book title is {item.title}, book year is {item.year}, book author is {item.author}, book pages is {item.pages}")
    elif item.uid[0] == "A":
        print(f"{Value} :article title is {item.title}, article year is {item.year}, article journal is {item.journal}, article doi is {item.doi}")
    elif item.uid[0] == "P":
        print(f"{Value} :podcast title is {item.title}, podcast year is {item.year}, podcast host is {item.host}, podcast duration is {item.duration}")
        Value += 1
    Value += 1
Value = 1
print("################FILTER PRINT BY YEAR 5 #################")
for item in loaded_items:
    if item.is_recent(5):
        if item.uid[0] == "B":
            print(f"{Value} :  book title is {item.title}, book year is {item.year}, book author is {item.author}, book pages is {item.pages}")
        elif item.uid[0] == "A":
            print(f"{Value} :article title is {item.title}, article year is {item.year}, article journal is {item.journal}, article doi is {item.doi}")
        elif item.uid[0] == "P":
            print(f"{Value} :podcast title is {item.title}, podcast year is {item.year}, podcast host is {item.host}, podcast duration is {item.duration}")
            Value += 1
        Value += 1

print("################FILTER PRINT BY DOI starts with 10.1234 #################")
for item in loaded_items:
    if  item.uid[0] == "A" and item.doi.startswith("10.1234"):
        if item.uid[0] == "B":
            print(f"{Value} :  book title is {item.title}, book year is {item.year}, book author is {item.author}, book pages is {item.pages}")
        elif item.uid[0] == "A":
            print(f"{Value} :article title is {item.title}, article year is {item.year}, article journal is {item.journal}, article doi is {item.doi}")
        elif item.uid[0] == "P":
            print(f"{Value} :podcast title is {item.title}, podcast year is {item.year}, podcast host is {item.host}, podcast duration is {item.duration}")
            Value += 1
        Value += 1
print("################PRINTS ARE END#################")
    