print()
#i = 0
largest_book = ""
largest = 0
with open("books_and_chapters.txt") as scriptures:
    for scripture in scriptures:
        #i = i + 1
        cleanline = scripture.strip()
        books = cleanline.split(":")
        separate_line = books[2]
        book = books[0]
        chapters = int(books[1])
        #if i > 66:
            #print(book)
        if chapters > largest:
            largest = chapters
            largest_book = book
        #print(f"Scripture: {separate_line}, book: {book}, chapter: {chapters}")
    print(f"The largest book is: {largest_book}, chapters: {largest}")
8:24
print()
i = 0
largest_book = ""
largest = 0
volume = input("""which volume of scriptures they would like
to learn about? (for example, Old Testament, New Testament,
Book of Mormon, Doctrine and Covenants, Pearl of Great Price): """)
print()
with open("books_and_chapters.txt") as scriptures:
    for scripture in scriptures:
        i = i + 1
        cleanline = scripture.strip()
        books = cleanline.split(":")
        separate_line = books[2]
        book = books[0]
        chapters = int(books[1])
        if volume.lower() == "book of mormon":
            if i > 66:
                if i < 82:
                    print(book)
                    if chapters > largest:
                        largest = chapters
    print()
    print(f"The largest book in the Book of Mormon is: {largest}")
    print()