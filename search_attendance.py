from src.database_manager import (
    DatabaseManager
)


def main():

    database = (
        DatabaseManager()
    )

    name = input(
        "Enter Name: "
    )

    records = (
        database.fetch_all_records()
    )

    found = False

    print(
        "\n===== RESULTS =====\n"
    )

    for record in records:

        if (
            record[1]
            .lower()
            ==
            name.lower()
        ):

            print(record)

            found = True

    if not found:

        print(
            "No Records Found"
        )

    database.close()


if __name__ == "__main__":
    main()