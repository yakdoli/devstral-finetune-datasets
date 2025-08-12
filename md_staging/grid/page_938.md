<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_938.jpeg
document_name: grid
page_number: 938
page_id: grid#page_938
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:53:23Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### 4.3.4.8 Serialization

In this section, we will discuss how to serialize and deserialize grouping grid schema information. **Serialization** is the process of saving the object state into a stream of bytes for further use. The reverse process is **Deserialization**. Through serialization, the objects are made portable so that they can be serialized at one end and then transferred to the other end of a network where they will again be deserialized into its original form for use.

#### Grid Grouping control supports two forms of serialization.

##### 4.3.4.8.1 Xml Serialization

## Appendix

### Figure 347: Retrieving Information about Selected Records by using the SelectedRanges Collection

The following figure illustrates how to retrieve information about selected records using the SelectedRanges collection:

| EmployeeID | LastName  | FirstName | Title                    | BirthDate | HireDate           |
|------------|-----------|-----------|--------------------------|-----------|--------------------|
| 1          | Davolio    | Nancy     | Sales Representative     | 12/8/1968 | 5/1/1992          |
| 2          | Fuller     | Andrew    | Vice President, Sales    | 2/19/1952 | 8/14/1992         |
| 3          | Leverling  | Janet     | Sales Representative     | 8/30/1963 | 4/1/1992 1:00 AM  |
| 4          | Peacock    | Margaret  | Sales Representative     | 9/19/1958 | 5/3/1993          |
| 5          | Buchanan   | Steven    | Sales Manager           | 3/4/1955  | 10/17/1993        |
| 6          | Suyama     | Michael   | Sales Representative     | 7/2/1963  | 10/17/1993        |
| 7          | King       | Robert    | Sales Representative     | 5/29/1960 | 1/2/1994          |
| 8          | Callahan   | Laura     | Inside Sales Coordinator | 1/9/1958  | 3/5/1994          |
| 9          | Dodsworth  | Anne      | Sales Representative     | 7/2/1969  | 11/15/1994        |

The output of the selected records is as follows:

- (GridRecord): EmployeeID = 3, LastName = Leverling, FirstName = Janet, Title = Sales Representative, BirthDate = 8/30/1963, HireDate = 4/1/1992 1:00 AM
- (GridRecord): EmployeeID = 4, LastName = Peacock, FirstName = Margaret, Title = Sales Representative, BirthDate = 9/19/1958, HireDate = 5/3/1993
- (GridRecord): EmployeeID = 5, LastName = Buchanan, FirstName = Steven, Title = Sales Manager, BirthDate = 3/4/1955, HireDate = 10/17/1993
- (GridRecord): EmployeeID = 6, LastName = Suyama, FirstName = Michael, Title = Sales Representative, BirthDate = 7/2/1963, HireDate = 10/17/1993

## RAG Annotations

<!-- tags: [Syncfusion Winforms, Serialization, Deserialization, Grid Grouping] keywords: [SelectedRanges, Xml Serialization, Object State, Portable Objects] -->