```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_674.jpeg
document_name: grid
page_number: 674
page_id: grid#page_674
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:33:42Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The dataset acts like a memory resident cache to hold the data. It represents a complete set of data including the tables that organize the data and relationships between the tables. The dataset is designed to help manage data in memory and to support disconnected operations on data. It can be populated by calling the Fill method of the DataAdapter.

## The Command Object

Commands contain the information that is submitted to a database, and are represented by provider-specific classes such as SqlCommand. A command can be a stored procedure call, an UPDATE statement, or a statement that returns results.

## The DataReader Object

This is a suitable object when you want, to only get the stream of data for reading. The data returned from a data reader is a fast forward-only stream of data. This means that you can only pull the data from the stream in a sequential manner. This is good for speed, but if you need to manipulate data, then a DataSet is a better object to work with.

## Data Binding Methods

To bind the grid to a database, you can use any one of the following methods.

### 1. Binding At Design Time

- **Binding to a database at Design time using VS2003**
- **Binding to a database at Design time using VS2005**

### 2. Binding At Run Time

- **Binding to an MDB file at run time**
- **Binding to a manually created datasource**

### 4.3.4.2.2 Binding to XML Data

Grid Grouping Control can be bound to data from XML files. To do this, a DataSet object is required which provides the necessary methods that will let you read the Xml data into the dataset. After loading the data, you can bind the grouping grid to this dataset by setting the data binding properties, the DataSource and the DataMember to the dataset and the table name respectively. It is also possible to save the changes back to the Xml file.
```