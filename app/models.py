class News:
    def __init__(self, id, name, description, url, category, country, language):
        self.id=id
        self.name=name 
        self.description=description
        self.url=url
        self.category=category
        self.country=country
        self.language=language
        


class Articles:
    def __init__(self, id, title, author, description, url, urlToImage, publishAt):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishAt=publishAt
        
