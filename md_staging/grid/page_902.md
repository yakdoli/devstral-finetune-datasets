```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_902.jpeg
document_name: grid
page_number: 902
page_id: grid#page_902
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:51:00Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Define `GridColumnSpanDescriptor` for each column to span across grid rows or columns, specifying the span range.
- Create a `GridColumnSetDescriptor` to store `ColumnSpans` to manage columns that need to be spanned.

## Content

### Step 1: Define `GridColumnSpanDescriptor` for Each Column

Define a `GridColumnSpanDescriptor` for each column to be spanned across grid rows or columns. Specify the range that the column spans. Rows and Columns are zero-based.

#### C#
```csharp
GridColumnSpanDescriptor csd0 = new GridColumnSpanDescriptor("EmployeeID");
csd0.Range = GridRangeInfo.Cells(0, 0, 1, 0);
GridColumnSpanDescriptor csd1 = new GridColumnSpanDescriptor("Address");
csd1.Range = GridRangeInfo.Cells(0, 1, 0, 2);
GridColumnSpanDescriptor csd2 = new GridColumnSpanDescriptor("City");
csd2.Range = GridRangeInfo.Cells(1, 1, 1, 1);
GridColumnSpanDescriptor csd3 = new GridColumnSpanDescriptor("Country");
csd3.Range = GridRangeInfo.Cells(1, 2, 1, 2);
```

#### VB.NET
```vbnet
Dim csd0 As GridColumnSpanDescriptor = New GridColumnSpanDescriptor("EmployeeID")
csd0.Range = GridRangeInfo.Cells(0, 0, 1, 0)
Dim csd1 As GridColumnSpanDescriptor = New GridColumnSpanDescriptor("Address")
csd1.Range = GridRangeInfo.Cells(0, 1, 0, 2)
Dim csd2 As GridColumnSpanDescriptor = New GridColumnSpanDescriptor("City")
csd2.Range = GridRangeInfo.Cells(1, 1, 1, 1)
Dim csd3 As GridColumnSpanDescriptor = New GridColumnSpanDescriptor("Country")
csd3.Range = GridRangeInfo.Cells(1, 2, 1, 2)
```

### Step 2: Create `GridColumnSetDescriptor` with `ColumnSpans`

Create a `GridColumnSetDescriptor` whose `ColumnSpans` property stores the information about the columns that need to be spanned. Hence, you need to initialize the `ColumnSpans` property with the `ColumnsSpanDescriptors` of the desired columns you want to spread.

#### C#
```csharp
GridColumnSetDescriptor csd = new GridColumnSetDescriptor();
csd.ColumnSpans.Add(csd0);
csd.ColumnSpans.Add(csd1);
csd.ColumnSpans.Add(csd2);
csd.ColumnSpans.Add(csd3);
```

<!-- tags: [grid, windows forms, columnspan, syncfusion] keywords: [GridColumnSpanDescriptor, GridColumnSetDescriptor, GridRangeInfo, Cells, EmployeeID, Address, City, Country] -->
```