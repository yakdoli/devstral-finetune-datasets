<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: grouping
page_number: 031
page_id: grouping#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:25Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- This section demonstrates how to group data in a `MyObject` class using the `GroupingEngine` in Syncfusion Winforms.
- Focuses on grouping by a specific property, `C`, and sorting the grouped data accordingly.

## Content

**Note:** Here, the columns correspond to the public properties in our sample `MyObject` class, `A`, `B`, `C`, and `D`.

We will now continue using the same sample created in the **previous** section and add the corresponding code at the bottom of the `Main` method.

### Step 1: Grouping the Data

To group the `MyObject` `ArrayList` by a particular property, say property `C`, you have to add only the property name (`"C"`) to the `groupingEngine.TableDescriptor.GroupedColumns` collections. Add the following code snippet to the bottom of the `Main` method.

#### C# Implementation

```csharp
// Group on property C.
groupingEngine.TableDescriptor.GroupedColumns.Add("C");

// Display the records in the engine after grouping.
foreach (Record rec in groupingEngine.Table.Records)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}
```

#### VB.NET Implementation

```vb
' Group on property C.
groupingEngine.TableDescriptor.GroupedColumns.Add("C")

' Display the records in the engine after grouping.
For Each rec In groupingEngine.Table.Records
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec
```

### Step 2: Observing the Grouped Data

After running the code from step 1, a screen similar to the one below will be displayed. Note that the bottom list displayed is now sorted by **column C**. This is a one side effect of grouping by column `C`.

## Result

The grouped data is now sorted by the specified column, `C`, and the output reflects this sorting. This ensures that the grouped data is organized and displayed as intended.

## Code Examples

### C# Example
```csharp
using Syncfusion.GroupingEngine;

void Main()
{
    // Setup groupingEngine and MyObject data
    GroupingEngine groupingEngine = new GroupingEngine();

    // Populate MyObject objects in ArrayList

    // Group on property C.
    groupingEngine.TableDescriptor.GroupedColumns.Add("C");

    // Display the results
    foreach (Record rec in groupingEngine.Table.Records)
    {
        MyObject obj = rec.GetData() as MyObject;
        if (obj != null)
        {
            Console.WriteLine(obj);
        }
    }
}
```

### VB.NET Example
```vb
Imports Syncfusion.GroupingEngine

Sub Main()
    ' Setup groupingEngine and MyObject data
    Dim groupingEngine As New GroupingEngine()

    ' Populate MyObject objects in ArrayList

    ' Group on property C.
    groupingEngine.TableDescriptor.GroupedColumns.Add("C")

    ' Display the results
    For Each rec In groupingEngine.Table.Records
        Dim obj As MyObject = CType(rec.GetData(), MyObject)
        If Not (obj Is Nothing) Then
            Console.WriteLine(obj)
        End If
    Next rec
End Sub
```

## API Reference

- **GroupingEngine**: The main class responsible for handling grouping operations.
- **TableDescriptor.GroupedColumns**: Property to specify the columns to group by.
- **Record.GetData()**: Method to retrieve the data object from a record.

## Page-level Navigation/TOC
- [Essential Grouping](#essential-grouping)
  - Overview
  - Content
    - Step 1: Grouping the Data
    - Step 2: Observing the Grouped Data
  - Result
  - Code Examples
    - C# Example
    - VB.NET Example
  - API Reference

## Tags and Keywords

<!-- tags: [syncfusion, winforms, grouping, groupingengine, tabledescriptor, groupedcolumns] keywords: [grouping, property grouping, column sorting, data grouping, engine, table descriptor, grouped columns] -->