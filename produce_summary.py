def gets_melon_totals(file, daynum):
    """Given a file name and number of the day, prints delivery summary including
    total number of melons delivered and their cost."""

    # opens file with data and saves as variable
    delivery_report = open(file)
    
    # loops over each line in the file
    for line in delivery_report:
        # removes trailing characters from the right of each line, splits line into 
        # words on pipe
        fields = line.rstrip().split("|")

    # use list unpacking to quickly assign variables to each index. "fields" is
    # on the right side of the equation because it is evaluated 1st. if swapped
    # it would reassign the variable name
    melon_name, melon_count, amount = fields

    # returns string containing summary of info
    return f"Day {daynum}: Delivered {melon_count} {melon_name}s for total of ${amount}"
    
    # closes file
    file.close()

# calls function and prints results
print(gets_melon_totals("um-deliveries-20140519.txt", 1))
print(gets_melon_totals("um-deliveries-20140520.txt", 2))
print(gets_melon_totals("um-deliveries-20140521.txt", 3))