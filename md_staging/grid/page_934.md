```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_934.jpeg
document_name: grid
page_number: 934
page_id: grid#page_934
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:53:04Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates using selected record in nested tables.
- Explains how to perform record search using the SelectedRecords collection.

## Content

### Record Selection in Nested Tables
To select multiple records in nested tables, use the `SelectedRecords` collection. The following code snippet shows how to add records to the `SelectedRecords` collection:

```csharp
Me.gridGroupingControl1.GetTable("Orders").SelectedRecords.Add(or1)
Me.gridGroupingControl1.GetTable("Orders").SelectedRecords.Add(or2)
```

**Figure 346: Record Selection in Nested Tables**

![Figure 346: Record Selection in Nested Tables](#)  
*Explanation: The image illustrates multi-record selection in a child table and parent table selections.*

### Record Search
To search for a particular record, the `SelectedRecords` collection provides a method called `FindRecord()`. This method searches for the occurrences of the specified record and returns a zero-based index of the occurrence found. If no such record is found, it returns -1. The method comes in two versions:
- One accepts the whole record as its parameter.
- The other accepts the position of the record in the underlying datasource.

#### Implementation Example
[C#]

```csharp
Record rec = this.gridGroupingControl1.Table.Records[2];

// Search for the record 'rec'.
int index = this.gridGroupingControl1.Table.SelectedRecords.FindRecord(rec);

// Search for the record with index 2.
int index2 = this.gridGroupingControl1.Table.SelectedRecords.FindRecord(2);
```

#### Equivalent in VB.NET
```vb
[VB.NET]
```

## API Reference
### Methods
- **FindRecord()**  
  - **Parameters**:  
    - `record`: Type `Record` (the record to search for).  
    - `index`: Type `int` (the index of the record in the datasource).  
  - **Returns**: `int` - The zero-based index of the occurrence found. Returns -1 if no such record is found.

## Code Examples
### C# Example
```csharp
Record rec = this.gridGroupingControl1.Table.Records[2];

// Search for the record 'rec'.
int index = this.gridGroupingControl1.Table.SelectedRecords.FindRecord(rec);

// Search for the record with index 2.
int index2 = this.gridGroupingControl1.Table.SelectedRecords.FindRecord(2);
```

### VB.NET Example
```vb
[VB.NET]
```

## RAG Annotations
<!-- tags: [record selection, nested tables, record search, gridGroupingControl, SelectedRecords, FindRecord] keywords: [multi-record selection, parent table, child table, selected record, occurrence index, search methods] -->
```