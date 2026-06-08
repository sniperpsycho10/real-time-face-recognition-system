from src.database_manager import DatabaseManager


def main():

    database = DatabaseManager()

    print("\n===== ATTENDANCE SEARCH =====\n")

    choice = input(
        "Search By:\n"
        "1. Name\n"
        "2. Date\n\n"
        "Choice: "
    )

    print()

    if choice == "1":

        name = input(
            "Enter Name: "
        )

        records = (
            database.search_by_name(
                name
            )
        )

    elif choice == "2":

        date = input(
            "Enter Date (YYYY-MM-DD): "
        )

        records = (
            database.search_by_date(
                date
            )
        )

    else:

        print(
            "Invalid Choice"
        )

        database.close()

        return

    print(
        "\n===== RESULTS =====\n"
    )

    if not records:

        print(
            "No Records Found"
        )

    else:

        for record in records:

            print(record)

    database.close()


if __name__ == "__main__":

    main()