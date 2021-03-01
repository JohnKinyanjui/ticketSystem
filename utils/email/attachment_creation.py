import csv


def create_file():
    row_list = [["TicketId", "Priority", "Department", "Ref No", "Longitude", "Latitude"],
                ["", "Linus Torvalds", "Linux Kernel", "", "", ""],
                ["", "Tim Berners-Lee", "World Wide Web", "", "", ""],
                ["", "Guido van Rossum", "Python Programming", "", "", ""]]
    with open('protagonist.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)
