import csv


def main():
    with open('AB_NYC_2019.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)

        count = 0
        biggest = 0
        biggest_data = []
        ten_percentage_of_total_data = 488.9

        rows = ([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], int(row[9]), row[10], row[11],
                 row[12], row[13], row[14], row[15]] for row in csv_reader)

        for line in rows:

            count += 1
            total_data = count * 0.1

            if total_data < ten_percentage_of_total_data:

                price = int(line[9])

                if price > biggest:

                    biggest = price
                    biggest_data = line

        print(header)
        print(biggest_data)


if __name__ == "__main__":
    main()

    print("")

    print("Created By Min Khant Soe (HakHak)")

    input("")
