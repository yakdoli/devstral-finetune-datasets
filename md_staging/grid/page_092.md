```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_092.jpeg
document_name: grid
page_number: 092
page_id: grid#page_092
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:21:59Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Load a dataset with records.
- Support the updation of data in the database.
- Apply special column formats using the GridBoundColumn collection.

## Content

### Updating Data in the Database

To support updation of the data in your database, you will need to call the `Update` command on the `SQLDataAdapter`. Double-click the Update button on the design surface to add a Click Handler. Then add the following line of code to the handler:

#### Code in VB.NET
```vb
' Load dataset with records.
Me.sqlDataAdapter1.Fill(Me.dataSet1)
```

#### Code in C#
```csharp
// Save Changes (if any) back to the database.
this.sqlDataAdapter1.Update(this.dataSet1);
```

#### Code in VB.NET
```vb
' Save Changes (if any) back to the database.
Me.sqlDataAdapter1.Update(Me.dataSet1);
```

Now when you click the Update button, it will post any changes that you have made back to your database.

### 3.1.4.2 Applying Special Column Formats

The **GridBoundColumn** collection property of the Grid Data Bound Grid is used to set column properties. This collection will let you control the columns that are displayed as well as their order. For each column that you want displayed, add a Grid Bound Column. In this Grid Bound Column, you must set the **MappingName** property; the other properties such as **HeaderText** and the **Style** are optional. Under the **Style** property, you will have access to the normal **GridStyleInfo** properties that you can apply to this column such as **BackColor**, **CellType**, and **Font**.
```html
```html
<!-- tags: [syncfusion, winforms, grid, gridboundcolumn, mappingname, style, gridstyleinfo] keywords: [boundingcolumn, mappingname, header, dropdowncheckboxcolumn, dropdowncurrencymanage, dropdownimagecolumn, dropdownvaluecolumn, dropdowntextcolumn, dropdownlistcolumn, dropdowncheckboxcolumn, dropdowncurrencymanage, dropdownimagecolumn, dropdownvaluecolumn, dropdowntextcolumn, dropdownlistcolumn] -->
```