import pickle


class DatabaseLoader:

    def __init__(
        self,
        database_path
    ):

        self.database_path = database_path

    def load_database(self):

        with open(
            self.database_path,
            "rb"
        ) as file:

            database = pickle.load(
                file
            )

        print(
            "\nDatabase Loaded Successfully"
        )

        print(
            f"Known People: {list(database.keys())}"
        )

        return database