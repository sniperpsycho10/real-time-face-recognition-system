from src.database_manager import (
    DatabaseManager
)


def main():

    database = (
        DatabaseManager()
    )

    print(
        "\n===== ATTENDANCE SEARCH =====\n"
    )

    print(
        "1. Search By Name"
    )

    print(
        "2. Search By Date"
    )

    choice = input(
        "\nChoice: "
    )

    if choice == "1":

        name = input(
            "Enter Name: "
        )

        results = (
            database.search_by_name(
                name
            )
        )

    elif choice == "2":

        date = input(
            "Enter Date (YYYY-MM-DD): "
        )

        results = (
            database.search_by_date(
                date
            )
        )

    else:

        print(
            "Invalid Choice"
        )

        return

    print(
        "\n===== RESULTS =====\n"
    )

    if len(results) == 0:

        print(
            "No Records Found"
        )

    else:

        for record in results:

            print(
                record
            )

    database.close()


if __name__ == "__main__":
    main()