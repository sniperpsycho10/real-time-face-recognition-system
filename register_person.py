import os


def register_person():

    print(
        "\n===== PERSON REGISTRATION =====\n"
    )

    person_name = input(
        "Enter Person Name: "
    ).strip()

    if not person_name:

        print(
            "\nInvalid Name"
        )

        return

    folder_path = os.path.join(
        "data",
        "known_faces",
        person_name
    )

    if os.path.exists(
        folder_path
    ):

        print(
            f"\nPerson '{person_name}' already exists."
        )

        print(
            f"Folder: {folder_path}"
        )

        return

    os.makedirs(
        folder_path
    )

    print(
        f"\n✓ Person Registered Successfully"
    )

    print(
        f"✓ Folder Created: {folder_path}"
    )


if __name__ == "__main__":

    register_person()