class Author(object):
    def __init__(self, name):
        self.name = name

class Bucket(object):
    def __init__(self, author, message):
        self.author = author
        self.message = message

    def get_bucket(self):
        return {"author": self.author.name, "message": self.message}

