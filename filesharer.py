

class FileSharer:

    def __init__(self, filepath, api_key="aosdfja234odw0asdoj23e0j"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
