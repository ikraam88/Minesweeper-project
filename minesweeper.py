# create the grid as a 2D array
grid = [["-", "-", "-", "#", "#"], ["-", "#", "-", "-", "-"], ["-", "-", "#", "-", "-"], ["-", "#", "#", "-", "-"], ["-", "-", "-", "-", "-"]]
# count the number of rows and number of columns using the len() function
num_rows = len(grid)
num_cols = len(grid[num_rows-1])

# create a function that will print the grid
def grid_display():
    # iterate through the grid
    for row in grid:
        print(row)
print("\nBEFORE MINING\n")
# call the function to display the grid
grid_display()
# define a function for counting mines
# take the row index and the column index as arguments
def count_mines(r_index, col_index):
    # intitialise the number of mines
    num_mines = 0
    # create if statements for the row index and column index
    # check the first row using nested if statements
    if row_index == 0:
        if column_index == 0:
        # check if the first columns have mines (hashes) - (3 checks)
            if grid[r_index][col_index+1] == "#":
                    num_mines+=1
            if grid[r_index+1][col_index+1] == "#":
                num_mines+=1
            if grid[r_index+1][col_index] == "#":
                num_mines+=1  
        # check the last column have mines (hashes) - (3 checks)
        elif row_index == 0 and (column_index== num_cols -1):
            if grid[r_index][col_index-1] == "#":
                num_mines+=1
            if grid[r_index+1][col_index-1] == "#":
                num_mines+=1
            if grid[r_index+1][col_index] == "#":
                num_mines+=1
        # check the middle columns have mines (hashes) - (5 checks)
        else:
            if grid[r_index][col_index-1] == "#":
                num_mines+=1
            if grid[r_index][col_index+1] == "#":
                num_mines+=1
            if grid[r_index+1][col_index-1] == "#":
                num_mines+=1
            if grid[r_index+1][col_index] == "#":
                num_mines+=1
            if grid[r_index+1][col_index+1] == "#":
                num_mines+=1

    # check the bottom row using nested if statements
    elif (row_index == num_rows - 1):
        # check if the first columns have mines (hashes) - (3 checks) 
        if column_index == 0:
            if grid[r_index-1][col_index] == "#":
                num_mines+=1
            if grid[r_index-1][col_index+1] == "#":
                num_mines+=1
            if grid[r_index][col_index+1] == "#":
                num_mines+=1
        # check if the last columns have mines (hashes) - (3 checks)
        elif (column_index == num_cols - 1):
            if grid[r_index-1][col_index-1] == "#":
                num_mines+=1
            if grid[r_index-1][col_index] == "#":
                num_mines+=1
            if grid[r_index][col_index-1] == "#":
                num_mines+=1
        #check if the middle columns have mines (hashes) - (5 checks)
        else:
            if grid[r_index-1][col_index-1] == "#":
                num_mines+=1
            if grid[r_index-1][col_index] == "#":
                num_mines+=1
            if grid[r_index-1][col_index+1] == "#":
                num_mines+=1
            if grid[r_index][col_index-1] == "#":
                num_mines+=1
            if grid[r_index][col_index+1] == "#":
                num_mines+=1
    # check the middle row using nested if statements
    else:
        #check if the first columns have mines (hashes) - (5 checks)
        if column_index == 0:
            if grid[r_index-1][col_index] == "#":
                num_mines+=1
            if grid[r_index-1][col_index+1] == "#":
                num_mines+=1
            if grid[r_index][col_index+1] == "#":
                num_mines+=1
            if grid[r_index+1][col_index] == "#":
                num_mines+=1
            if grid[r_index+1][col_index+1] == "#":
                num_mines+=1
        # check if the last columns have mines (hashes) - (5 checks)
        elif column_index == num_cols - 1:
            if grid[r_index-1][col_index-1] == "#":
                num_mines+=1
            if grid[r_index-1][col_index] == "#":
                num_mines+=1
            if grid[r_index][col_index-1] == "#":
                num_mines+=1
            if grid[r_index+1][col_index-1] == "#":
                num_mines+=1
            if grid[r_index+1][col_index] == "#":
                num_mines+=1
        #check if the middle columns have mines (hashes) - (8 checks)
        else:
            if grid[r_index-1][col_index-1] == "#":
                num_mines+=1
            if grid[r_index-1][col_index] == "#":
                num_mines+=1
            if grid[r_index-1][col_index+1] == "#":
                num_mines+=1
            if grid[r_index][col_index-1] == "#":
                num_mines+=1
            if grid[r_index][col_index+1] == "#":
                num_mines+=1
            if grid[r_index+1][col_index-1] == "#":
                num_mines+=1
            if grid[r_index+1][col_index] == "#":
                num_mines+=1
            if grid[r_index+1][col_index+1] == "#":
                num_mines+=1
    # return the number of mines
    return num_mines
# print the message for the enumerated data
print("\n Row and Column Indexes\n")
# iterate through each element in the enumerated grid into 2 variables
for row_index, row_data in enumerate(grid):
# iterate through the elements in the row data
# display each element in the arrays as enumerated rows and columns
    for column_index, column_data in enumerate(row_data):
    # check if the column data is a dash
    # if so it will change the dashes to numbers
        if column_data == "-":
            print(f"{column_data}[row = {row_index}] [column = {column_index}]")
            grid[row_index][column_index] = count_mines(row_index, column_index)
# print final display message
print("\nMINING RESULTS\n")
# call the grid_display function to display the final grid
grid_display()



