```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_126.jpeg
document_name: XlsIO
page_number: 126
page_id: XlsIO#page_126
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:55:44Z
fidelity: lossless
-->

## Essential XlsIO

### Setting Number Format

The following example demonstrates how to set a custom number format using the `NumberFormat` property:

```csharp
sheet.Range("C4").NumberFormat = "$#,##0.00";
```

**Note:** You can also set custom formats such as Accounting by using the `NumberFormat` property as shown in the preceding code example.

### Entering Data in Text Format

The following code example illustrates entering data in the `Text` format.

#### C#

```csharp
sheet.Range["C4"].Text = "1.20";
```

#### VB.NET

```vb.net
sheet.Range("C4").Text = "1.20"
```

### Getting and Setting Data in Cells

XlsIO provides the following properties to get/set the data in the cells:

- **DisplayText**: Gets the text that is displayed in the cell. This is a read-only property, which returns a cell value that is displayed after the number format application.

- **Value**: Gets/sets the string from it. Since the user can assign different data types, the `Value` property parses the input string to determine which type was used. It sequentially checks whether it is an empty cell, formula, boolean, error, number, or date-time.

- **Value2**: This object returns/sets the cell value. It works in the following way: it first checks whether the specified object has the type known for it (DateTime, TimeSpan, Double, Int). If yes, then it uses the corresponding typed properties (DateTime, TimeSpan, Number). Otherwise, it calls the `Value` property with String data type.

#### Difference Between `Value2` and `Value`

The only difference between the `Value2` property and the `Value` property is that the `Value2` property does not use the Currency and Date data types. Additionally, it does not support `FormulaArray` values.

### Using `IsStringsPreserved` Property

The `IsStringsPreserved` property of `IWorksheet` is used to modify its behavior and return `bool`, `double`, or `datetime`. Otherwise, it returns the `Value` property.

#### Example Usage

```csharp
sheet.IsStringsPreserved = true;
sheet.Range[1, 1].Value = "1";
```

<!-- tags: [XlsIO, NumberFormat, TextFormat, DisplayText, Value, Value2, IsStringsPreserved, Syncfusion Winforms, 11.4.0.26] keywords: [number format, text format, data in cells, display text, value property, is strings preserved, essential xlsio, syncfusion winforms] -->
```