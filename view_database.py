from src.database_manager import (
    DatabaseManager
)


def main():

    database = (
        DatabaseManager()
    )

    records = (
        database.fetch_all_records()
    )

    print(
        "\n===== DATABASE RECORDS =====\n"
    )

    for record in records:

        print(record)

    database.close()


if __name__ == "__main__":
    main()