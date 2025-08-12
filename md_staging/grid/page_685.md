```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_685.jpeg
document_name: grid
page_number: 685
page_id: grid#page_685
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:32:29Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Demonstrates how to bind a collection that implements `ITypedList` to the Grouping Grid in a Windows Forms application.
- Sample code provided in both C# and VB.NET.
- Explanation of assigning the list to the grid's `DataSource`.

## Content

### Binding a Collection to the Grouping Grid

#### Step 1: Creating the Collection
The following code snippets show how to create a list of books, where each book has a name and an author:

```csharp
[C#]

Books MyBooks = new Books();
MyBooks.Add(new Book("Computer Networks", "Tanenbaum"));
MyBooks.Add(new Book("Data Structures", "Tremblay and Sorenson"));
MyBooks.Add(new Book("Database Management", "Alexis Leon"));
```

```vbnet
[VB.NET]

Dim MyBooks As Books = New Books()
MyBooks.Add(New Book("Computer Networks", "Tanenbaum"))
MyBooks.Add(New Book("Data Structures", "Tremblay and Sorenson"))
MyBooks.Add(New Book("Database Management", "Alexis Leon"))
```

#### Step 2: Assigning the DataSource
The list of books is then assigned to the `DataSource` property of the Grouping Grid.

```csharp
[C#]

this.gridGroupingControl.DataSource = MyBooks;
```

```vbnet
[VB.NET]

Me.GridGroupingControl1.DataSource = MyProducts
```

#### Step 3: Running the Sample
Running the sample results in a Grouping Grid displaying the books with their respective authors.

**Figure 273: Binding a Collection that implements ITypedList to the Grouping Grid**
![Grouping Grid Sample Screenshot](https://i.imgur.com/TowbX.png)

<figcaption>
Figure 273: Binding a Collection that implements ITypedList to the Grouping Grid
</figcaption>

## API Reference

### Namespace: Syncfusion.Windows.Forms.Grid

#### Property: `DataSource`
- **Type**: Object
- **Description**: Gets or sets the data source for the grid.
- **Default**: `null`
- **Parameters**: None
- **Returns**: The current data source object.

## Code Examples

### C#

```csharp
Books MyBooks = new Books();
MyBooks.Add(new Book("Computer Networks", "Tanenbaum"));
MyBooks.Add(new Book("Data Structures", "Tremblay and Sorenson"));
MyBooks.Add(new Book("Database Management", "Alexis Leon"));

this.gridGroupingControl.DataSource = MyBooks;
```

### VB.NET

```vbnet
Dim MyBooks As Books = New Books()
MyBooks.Add(New Book("Computer Networks", "Tanenbaum"))
MyBooks.Add(New Book("Data Structures", "Tremblay and Sorenson"))
MyBooks.Add(New Book("Database Management", "Alexis Leon"))

Me.GridGroupingControl1.DataSource = MyProducts
```

## RAG Annotations
<!-- tags: [grouping grid, windows forms, data binding, ITypedList, Syncfusion, grid control] keywords: [books, author, gridGroupingControl, DataSource, Grouping Grid, data source, binding] -->
```