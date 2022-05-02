class News:
    def __init__(self, author, title, description, url, urlToImage, date, content):
        '''
        Function to initialize News Objects
        It defines the properties each News object will hold.
        '''
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.date = date
        self.content = content