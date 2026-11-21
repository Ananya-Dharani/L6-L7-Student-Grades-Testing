def average_marks(marks_csv):
    if not isinstance(marks_csv, str):
        raise TypeError("marks_csv must be a string")

    parts = [part.strip() for part in marks_csv.split(",")]
    if not parts or any(part == "" for part in parts):
        raise ValueError("marks_csv must contain comma-separated integers")

    try:
        marks = [int(part) for part in parts]
    except (TypeError, ValueError) as exc:
        raise ValueError("marks_csv must contain comma-separated integers") from exc

    return round(sum(marks) / len(marks), 2)


def parse_srn(srn):
    if not isinstance(srn, str):
        raise TypeError("srn must be a string")

    srn = srn.strip()
    if len(srn) < 10:
        raise ValueError("srn must contain a campus, year, and department")

    year = srn[6:8]
    if not year.isdigit():
        raise ValueError("srn year must contain two digits")

    return srn[:4], int(year), srn[8:10]


def short_name(full_name):
    if not isinstance(full_name, str):
        raise TypeError("full_name must be a string")

    name_parts = full_name.split()
    if len(name_parts) < 2:
        raise ValueError("full_name must contain a first and last name")

    first = name_parts[0]
    last = name_parts[-1]
    return first[0].upper() + ". " + last.capitalize()

def main():
    print("==== Running average_marks ====")
    user_input = input("Enter marks as CSV (e.g. 78,85,92): ")
    result = average_marks(user_input)
    print("Average Marks:", result)

    print("\n==== Running parse_srn ====")
    user_input = input("Enter an SRN (e.g. PES1UG23CS123): ")
    result = parse_srn(user_input)
    print("Campus, Year and Dept:", result)

    print("\n==== Running short_name ====")
    user_input = input("Enter first and last name (e.g. ravi kumar): ")
    result = short_name(user_input)
    print("Short Name:", result)

if __name__ == "__main__":
    main()
