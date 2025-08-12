```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_113.jpeg
document_name: grid
page_number: 113
page_id: grid#page_113
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:31:16Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Type Conversions

You will notice that in the `GridSaveCellInfo` method, you had made use of the `int.Parse` method to convert the string value in the `GridStyleInfo` object to the integer you needed for the external data source. You can instead make use of the more general `Convert` class provided by Essential Grid, to handle conversions between various data types. This class, for example, can convert the value in a `CellValue` property to a `DateTime` object, or to a `Color` object, depending upon the need. The following code example illustrates how to use this Convert class.

### [C#]

```csharp
// Convert a value in CellValue property to 'int' (as required by our data source) by using Convert class.
this._extData[e.RowIndex - 1, e.ColIndex - 1] =
    (int)GridCellValueConvert.ChangeType(e.Style.CellValue, typeof(int), null);
```

### [VB.NET]

```vb
' Convert a value in CellValue property to 'int' (as required by our data source) by using Convert class.
Me._extData(e.RowIndex - 1, e.ColIndex - 1) =
    CInt(GridCellValueConvert.ChangeType(e.Style.CellValue, GetType(Integer), Nothing))
```

---

### Note: This conversion problem may occur when the value that is stored in the style object is a string. This happens when the `CellValueType` property is not explicitly set on the style object in your `GridQueryCellInfo` method. But when this is set to "int", then you can cast the `CellValue` in `SaveCellInfo` to an int, and do not have to worry about conversions.

---

## Lesson 5: Excel Export

### Overview
- Export to Excel is a common functionality required in the .NET world.
- The Essential Grid control provides built-in support for Excel Export.
- Download the data from the Grid or related controls into an Excel spreadsheet for offline use.

### Content

Export to Excel is one of the most common functionalities that are required in the .NET world. The Essential Grid control has built-in support for Excel Export. You can download the data from the Grid control or Grid Data Bound Grid or Grouping Grid control into an Excel spreadsheet for offline verification and/or computation. This can be achieved by making use of the `GridExcelConverter` and `GroupingGridExcelConverter` classes. This section will step you through the conversion of the contents of the grid to an Excel file, as well as discuss the various converter options.

In this lesson, you will learn about the following topics.

## Code Examples

### C# Example

```csharp
this._extData[e.RowIndex - 1, e.ColIndex - 1] =
    (int)GridCellValueConvert.ChangeType(e.Style.CellValue, typeof(int), null);
```

### VB.NET Example

```vb
Me._extData(e.RowIndex - 1, e.ColIndex - 1) =
    CInt(GridCellValueConvert.ChangeType(e.Style.CellValue, GetType(Integer), Nothing))
```

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Grid, Excel Export, Data Conversion, Converter, GridExcelConverter, GroupingGridExcelConverter] 
keywords: [GridView Export, Grid Data Export, Grid Export to Excel, Excel Conversion, Type Conversion, CellValue, GridQueryCellInfo, GridSaveCellInfo] -->
```
