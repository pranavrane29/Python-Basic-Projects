### ***# Project 5 — Inventory Management System***

### ***\*\*Made by:\*\* Pranav Rane***

### ***\*\*Language:\*\* Python 3.x***

### ***\*\*File:\*\* InventoryManagement.py***

\-----------------------------------------------------------------------



##### **## Project Overview**

The Inventory Management System is a comprehensive stock-control application built in 

Python. It tracks products by ID, name, category, price, and quantity. The system allows stock

in (restocking), stock-out (sales), generates low-stock alerts, and produces inventory reports 

with total stock value. It uses all core Python data structures and integrates basic file handling 

for persistent storage. 

\-----------------------------------------------------------------------

##### 

##### **## Data Structure Used**

\*Dictionary - A dictionary named inventory that stores all the data of the stocks in the key - value pair.(Important)

\*List - A transaction log list that keeps track of all transactions made.

\*Set - categories name set that stores the categories for final report

\----------------------------------------------------------------------



##### **## Functions Used**

• load\_inventory() — Read data from inventory.txt       

• save\_inventory() — Write data to inventory.txt       

• add\_product() — Register new product          

• stock\_in() — Add quantity to existing product             

• stock\_out() — Deduct quantity with validation            

• view\_inventory() — Display full formatted table

• low\_stock\_alert() — List products below reorder level      

• generate\_report() — Summary statistics and analytics      

• log\_transaction() — Append entry to transaction history      

• get\_total\_value() — Returns total inventory valuation       

\---------------------------------------------------------------------



##### **## Key Features**

\- Used dictionary to store data efficiently.

\- Data storing to another file inventory.txt.

\- Tracks the transaction log after every transaction made.

\- Duplicate pid prevention.

\- Stocks Guards for less stocks.

\- Low stock validation if stock is less than reorder quantity.

\- Gst calculation as per each category of items.

\- Input validation via try-except on all numeric inputs

\- Empty record guard on most methods.

\- Clean interface for report (maybe)

\------------------------------------------------------------------------



##### **## Bonus Feature — GST calculation**

Calculates Gst as 5%,12% or 18% as per the category of the 

product being added.

\------------------------------------------------------------------------



##### **## Resources Used**

\- \*\*Claude (Anthropic)\*\* — Debugging, code review, concept explanations

\- \*\*Python 3.x Official Documentation\*\* — Standard library reference

\- \*\*Assignment PDF\*\* — Project specification and evaluation criteria



\-------------------------------------------------------------------------

&#x09;

\*Submitted as part of Python Mini Project Assignment Book | 2025-26\*

