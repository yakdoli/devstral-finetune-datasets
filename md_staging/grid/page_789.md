```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_789.jpeg
document_name: grid
page_number: 789
page_id: grid#page_789
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:40:01Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

![Figure 316: Localized CompareOperatorListBox](./image.png)

## 4.3.4.3.4.2.3 Working with Filters

This section deals with different options to process the filter rows.

### Accessing FilteredRecords

If you want to work with the subset of the records being filtered from a grid table, then you can use FilteredRecords collection for that table. This is a read-only collection that manages the subset of records that has been filtered against a filter criteria.

#### [C#]

```csharp
GridTable table = this.grid.Table;
foreach (Record frec in table.FilteredRecords)
{
    Console.WriteLine("Record Info : " + frec);
}
```

#### [VB.NET]

```vb
Private table As GridTable = Me.grid.Table
For Each frec As Record In table.FilteredRecords
    Console.WriteLine("Record Info : " & frec)
Next frec
```

### Accessing the FilterBarString

## Global Footer
© 2013 Syncfusion. All rights reserved.
```