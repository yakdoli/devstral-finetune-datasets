```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_675.jpeg
document_name: grid
page_number: 675
page_id: grid#page_675
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:32:59Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The following table lists some important methods provided by the dataset that allows you to manipulate Xml data. In this, the XmlSchema represents the type of the data stored in the Xml file.

## Overview

- Lists methods for reading and writing Xml data.
- Emphasizes the use of XmlSchema for data type definition.
- Provides examples for binding datasets to grids with Xml data.

## Content

### Methods for Manipulating Xml Data

| Method Name       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| ReadXml           | Reads the Xml Schema and the data into the dataset using the specified Xml file. |
| ReadXmlSchema     | Reads the Xml Schema from the specified file into the dataset.                 |
| WriteXml          | Writes the current data, and optionally the schema, for the dataset into the specified Xml file. |
| WriteXmlSchema    | Writes the dataset structure as an Xml schema into the specified file.      |

The following code example illustrates the binding process.

### C# Example

```csharp
// Create a Data Set.
DataSet XmlData = new DataSet();

// Populate it with data from an XML file.
XmlData.ReadXml("C:\\Data\\Customers_Orders.xml");

// Bind the grid to the Data Set.
gridGroupingControl1.DataSource = XmlData;
gridGroupingControl1.DataMember = XmlData.Tables[0];
```

### VB.NET Example

```vb
' Create a Data Set.
Dim XmlData As New DataSet()

' Populate it with data from an XML file
XmlData.ReadXml("C:\\Data\\Customers_Orders.xml")

' Bind the grid to the Data Set.
gridGroupingControl1.DataSource = XmlData
gridGroupingControl1.DataMember = XmlData.Tables(0)
```

## API Reference

- **Namespace**: `System.Data`
- **Class**: `DataSet`
- **Methods**:
  - `ReadXml`: Method for reading Xml data into the dataset.
  - `ReadXmlSchema`: Method for reading Xml Schema into the dataset.
  - `WriteXml`: Method for writing dataset contents to an Xml file.
  - `WriteXmlSchema`: Method for writing Xml Schema to a file.

## Code Examples

### C# Binding Example

```csharp
// Example code for binding to a grid using dataset with Xml data.
DataSet XmlData = new DataSet();
XmlData.ReadXml("C:\\Data\\Customers_Orders.xml");
gridGroupingControl1.DataSource = XmlData;
gridGroupingControl1.DataMember = XmlData.Tables[0];
```

### VB.NET Binding Example

```vb
' Example code for binding to a grid using dataset with Xml data.
Dim XmlData As New DataSet()
XmlData.ReadXml("C:\\Data\\Customers_Orders.xml")
gridGroupingControl1.DataSource = XmlData
gridGroupingControl1.DataMember = XmlData.Tables(0)
```

### Documentation Footer

© 2013 Syncfusion. All rights reserved.

<!-- tags: [syncfusion, winforms, dataset, xml, essential grid, code examples] keywords: [dataset, xmlschema, readxml, writexml, bind, grid, xml data, code example] -->
```