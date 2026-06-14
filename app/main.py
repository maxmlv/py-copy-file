import os.path


def copy_file(command: str) -> None:
    command_parts = command.split(" ")
    if len(command_parts) == 3:
        cp, original, copy = command_parts
        if cp == "cp" and os.path.exists(original) and original != copy:
            with open(original, "r") as file_in, open(copy, "w") as file_out:
                file_out.write(file_in.read())
