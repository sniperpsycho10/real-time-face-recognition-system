from src.database_builder import DatabaseBuilder


def main():

    builder = DatabaseBuilder()

    builder.build_database(
        "data/known_faces"
    )

    builder.save_database(
        "embeddings/face_database.pkl"
    )


if __name__ == "__main__":
    main()