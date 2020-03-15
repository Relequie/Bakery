# Bakery
 School Mock Test on Flask Application (45min)
 
 ## Purpose
 Create a Flask application for filtering the goods (mainly bread, cake and mooncake) from different shops
 
 ## Database
 There are 4 tables: BakeryItem, Bread, Cake and Mooncake
 
 **BakeryItem has 6 columns:**
 - `ItemNumber`
 - `Name`
 - `ExpiryDate`
 - `Type` (Bread/Cake/Mooncake)
 - `Price`
 - `Source`
 
 **Bread has 2 columns:**
 - `ItemNumber` referencing `BakeryItem.Index`
 - `Subtype` (Yeast/White/Flatbread
 
 **Cake has 2 columns:**
 - `ItemNumber` referencing `BakeryItem.Index`
 - `Country` (where it came from)
 
 **Mooncake has 2 columns:**
 - `ItemNumber` referencing `BakeryItem.Index`
 - `Lard` (True/False, whether it contains lard)
 
 ## Text Files
 It contains all the raw data of bread, cake, mooncake.\
 In BREAD.txt, the datails are in the order of `ItemNumber`, `Name`, `ExpiryDate`, `Type`, `Price`, `Source`, `Subtype`.\
 In CAKE.txt, the details are in the order of `ItemNumber`, `Name`, `ExpiryDate`, `Type`, `Price`, `Source`, `Country`.\
 In MOONCAKE.txt, the details are in the order of `ItemNumber`, `Name`, `ExpiryDate`, `Type`, `Price`, `Source`, `Lard`.
 
 ## Task 1
 It is a sql file containing the sqlite3 commands to create the tables as specified in Database
 
 ## Task 2
 It is a python file using file operations to read the text files and insert them into the database
 
 ## Task 3
 It is a sql file with one sql query finding the `ItemNumber`, `Name`, `Source`, `Subtype` of all the bread
 
 ## Task 4
 It is a python file that handles the actual flask applications.
 **Templates**
 There are two html files.\
 The `search.html` renders a page that that request for a source.\
 The `display.html` renders a page that displays all the `BakeryItem` with the source inputted
