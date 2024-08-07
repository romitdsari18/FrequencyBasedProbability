# FrequencyBasedProbability

To create a program in Python that performs the following: 

1.Loads the ‘cars.csv’ file into a pandas DataFrame. 

2.For each aspiration type 𝑎, computes the conditional probability of that aspiration, given each of the makes: 𝑃 (𝑎𝑠𝑝𝑖𝑟𝑎𝑡𝑖𝑜𝑛 = 𝑎|𝑚𝑜𝑑𝑒𝑙 = 𝑚) 

3.Displays the conditional probabilities to the screen. 

4.Computes the probability of each make and outputs to the screen.

# Explanation:
1.Firstly, Imported the panda’s library using the import statement.

2.After that used the pd.read_csv() method for reading and storing the CSV file in a pandas DataFrame.

3.Then Created the lists for the unique values of make and aspiration to avoid repetition and increase efficiency. This is done by using the unique() and tolist() methods.

4.By using these lists for calculating the conditional probability of aspiration and make by using nested for loops to iterate over each unique make and aspiration value. The len() function is used for calculating the number of matching rows and total rows, and then the conditional probability is calculated by dividing the matching count and total count.

5.Calculating the probability of each unique make value by dividing the number of rows with that make value by the total number of rows in the DataFrame.

