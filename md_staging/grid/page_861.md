```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_861.jpeg
document_name: grid
page_number: 861
page_id: grid#page_861
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:44:30Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- Demonstrates the customized appearance of grid columns.
- Explains how to enhance header cells by rendering images along with header text.
- Provides use case scenarios for rendering images in header cells.

### Content

#### Customized Appearance of Grid Columns
**Figure 333: Customized Appearance of Grid Columns**

| ProductID | ProductName                            | SupplierID | CategoryID | QuantityPerUnit         |
|-----------|----------------------------------------|------------|------------|--------------------------|
| 1         | Chai                                    | 1          | 1          | 10 boxes x 20 bags      |
| 2         | Chang                                   | 1          | 1          | 24 - 12 oz bottles      |
| 3         | Aniseed Syrup                          | 1          | 2          | 12 - 550 ml bottles     |
| 4         | Chef Anton's Cajun Seasoning           | 2          | 2          | 48 - 6 oz jars          |
| 5         | Chef Anton's Gumbo Mix                 | 2          | 2          | 36 boxes                |
| 6         | Grandma's Boysenberry Spread           | 3          | 2          | 12 - 8 oz jars          |
| 7         | Uncle Bob's Organic Dried Pears        | 3          | 7          | 12 - 1 lb pkgs.         |
| 8         | Northwoods Cranberry Sauce             | 3          | 2          | 12 - 12 oz jars         |
| 9         | Mishi Kobe Niku                         | 4          | 6          | 18 - 500 g pkgs.        |
| 10        | Ikura                                   | 4          | 8          | 12 - 200 ml jars        |
| 11        | Queso Cabrales                          | 5          | 4          | 1 kg pkg.               |
| 12        | Queso Manchego La Pastora               | 5          | 4          | 10 - 500 g pkgs.        |
| 13        | Konbu                                   | 6          | 8          | 2 kg box                |

**Note:** For more details, refer the following browser sample:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Appearance\Column Style Demo
```

#### Render Images in Header Cells
**4.3.4.5.1.4 Render Images in Header Cells**

Header cells are enhanced to render images along with their header text to represent the data more clearly. The user can align the images as desired.

##### Use Case Scenarios
In a payroll application, the images in the header cells help the user understand the nature of the data type in which the column is supposed to be bound.

**Figure 334: Header Cells with Images**

```html
<table>
  <thead>
    <tr>
      <th>Employees</th>
      <th style="text-align: center;">Drag a column header here to group by that column.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="background-color: #00BFFF; color: white;"><img alt="EmployeeID" src="EmployeeID_icon.png"/> EmployeeID</td>
      <td style="background-color: #00BFFF; color: white;"><img alt="LastName" src="LastName_icon.png"/> LastName</td>
      <td style="background-color: #00BFFF; color: white;"><img alt="FirstName" src="FirstName_icon.png"/> FirstName</td>
      <td style="background-color: #00BFFF; color: white;"><img alt="Title" src="Title_icon.png"/> Title</td>
      <td style="background-color: #00BFFF; color: white;">BirthDate <img alt="Calendar" src="Calendar_icon.png"/></td>
    </tr>
    <tr>
      <td>1</td>
      <td>Davolio</td>
      <td>Nancy</td>
      <td>Sales Representative</td>
      <td>12/8/1968 12:00:00 AM</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Fuller</td>
      <td>Andrew</td>
      <td>Vice President, Sales</td>
      <td>2/19/1952 12:00:00 AM</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Leverling</td>
      <td>Janet</td>
      <td>Sales Representative</td>
      <td>8/30/1963 12:00:00 AM</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Peacock</td>
      <td>Margaret</td>
      <td>Sales Representative</td>
      <td>9/19/1958 12:00:00 AM</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Buchanan</td>
      <td>Steven</td>
      <td>Sales Manager</td>
      <td>3/4/1955 12:00:00 AM</td>
    </tr>
  </tbody>
</table>
```

**Core: 2013 Syncfusion. All rights reserved.**

## RAG Annotations
<!-- tags: [grid, windows forms, header cells, images, payroll application] keywords: [customized appearance, product id, product name, category id, quantity per unit, employee id, last name, first name, title, birthdate] -->
```