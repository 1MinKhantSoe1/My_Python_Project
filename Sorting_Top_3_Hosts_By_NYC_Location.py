import csv


def main():

    with open('AB_NYC_2019.csv', encoding='utf-8') as csv_file:  # csv file location and encoding utf-8 format
        csv_reader = csv.reader(csv_file)   # Read the csv file using csv.reader
        header = next(csv_reader)   # Read for header

        new_data = []  # 1 step
        count = 0   # 1 step

        """10% of total data"""
        ten_percentage_of_total_data = 488.9    # 1 step

        top_3 = 1   # 1 step

        """Read the csv file row by row sign to rows"""
        rows = [[row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], int(row[9]), row[10], row[11],
                 row[12], row[13], row[14], row[15]] for row in csv_reader]  # 2n + n step

        for row in range(len(rows)):  # n step

            count += 1  # 1 step

            total_data = count * 0.1  # 2n steps                  # Filter the total data to 10%

            if total_data < ten_percentage_of_total_data:   # n step

                new_data.append([rows[row][0], rows[row][1], rows[row][2], rows[row][3], rows[row][4], rows[row][5],
                                rows[row][6], rows[row][7], rows[row][8], rows[row][9], rows[row][10], rows[row][11],
                                rows[row][12], rows[row][13], rows[row][14], rows[row][15]])  # 2n steps

        for row in range(1, len(new_data)):  # n step                       # Insertion sort all data by price

            temporary_data = new_data[row]  # 2n steps
            c = row  # 1 step

            while c > 0 and new_data[c-1][9] > temporary_data[9]:  # 2n^2 steps
                new_data[c] = new_data[c-1]  # 2n^2 steps
                c -= 1  # 1 step
            new_data[c] = temporary_data    # 2n^2 steps
        new_data.reverse()  # Reverse all the data from the list

        print(header)
        for row in new_data:  # n step                                       # Final Top-3 host by location Result

            location = row[4]   # 2n steps

            if location == "Brooklyn":  # 2n steps                          # The data will show only in Brooklyn

                while top_3 <= 3:   # 2n^2

                    print(row)
                    top_3 += 1      # 1 step
                    break


if __name__ == "__main__":
    main()

    print("")

    print("Created By Min Khant Soe (HakHak)")

    input("")
