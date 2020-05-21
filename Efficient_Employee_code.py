# Code to Find the Most Efficient Employee
# Our Task is to print out the name, Salary and Gender of the most Efficient Employee
# The column for Resources_used and work_done is in one CSV File
# The column for Salary and Gender is in another CSV File

# The code is as follows:

file1 = open("d:/Efficient Employee/word.csv", "r")               # Opens 1st CSV file/ you can also use "with open" to open the file
lst = file1.readlines()
file1.close()

file2 = open("d:/Efficient Employee/word2.csv", "r")              # Opens 2nd CSV file
lst1 = file2.readlines()
file2.close()

ratio = []                                                        # Contains ratio info
for i in range(1, len(lst)):                                      # Iterate or loop through each element of the lst
    z = lst[i].split(",")                                         # split the values of each element of list via space, store it in variable z
    ratio.append((int(z[2]) / int(z[1]), z[0]))                   # append the calculated ratios along with the name to ratio list

s_list = sorted(ratio, key=lambda t: t[0])                        # Sort the ratio list with the ascending order of the ratio

result = []                                                       # result list contains final ratio info
for i in range(1, len(lst)):
    z = lst[i].split(",")
    if z[0] == s_list[-1][1]:                                     # finds the name of the fastest worker from sorted list
        result.extend(z)							              # adds the speed of that worker into the result list

for j in range(1, len(lst1)):
    k = lst1[j].split(",")
    if k[0] == s_list[-1][1]:                                    # finds the name of the fastest worker from sorted list
        result.extend((k[1],k[2]))							     # adds the speed of that worker into the result list

print("{0} is the most efficient worker, {0} has done {1} units of Work , using {2} unit resources, worker's Salary is: {3}K and gender is : {4}".format(result[0], result[1], result[2], result[3], result[4]))

#The final line Prints out the Name, Salary and Gender of the most Efficient Employee

