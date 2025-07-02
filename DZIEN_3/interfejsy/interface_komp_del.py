class StorageBackend:
    def save(self, data):
        raise NotImplementedError

class FileStorage(StorageBackend):
    def save(self, data):
        with open("data.txt", "w") as f:
            f.write(data)

class App:
    def __init__(self, storage:StorageBackend):
        self.storage = storage

    def run(self):
        data = "Zapis danych z aplikacji"
        self.storage.save(data)

app = App(FileStorage())
app.run()
