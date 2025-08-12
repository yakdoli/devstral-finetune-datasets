```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_144.jpeg
document_name: XlsIO
page_number: 144
page_id: XlsIO#page_144
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:58:39Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
// Setting format properties.
condition5.FormatType = ExcelCFType.CellValue;
condition5.Operator = ExcelComparisonOperator.NotBetween;
condition5.FirstFormula = "100";
condition5.SecondFormula = "200";
condition5.FillPattern = ExcelPattern.DarkVertical;

// Applying conditional formatting to "A7" for format type as CellValue(LessOrEqual).
IConditionalFormats condition6 = sheet.Range["A7"].ConditionalFormats;

// Adding formats to IConditionalFormats collection
IConditionalFormat condition7 = condition6.AddCondition();
sheet.Range["A7"].Text = "Enter a Number which is less than or equal to 1000";

// Setting format properties.
condition7.FormatType = ExcelCFType.CellValue;
condition7.Operator = ExcelComparisonOperator.LessOrEqual;
condition7.FirstFormula = "1000";
condition7.BackColor = ExcelKnownColors.Light_green;

// Applying conditional formatting to "A9" for format type as CellValue(NotEqual).
IConditionalFormats condition8 = sheet.Range["A9"].ConditionalFormats;

// Adding formats to the IConditionalFormats collection.
IConditionalFormat condition9 = condition8.AddCondition();
sheet.Range["A9"].Text = "Enter a Number which is not equal to 1000";

// Setting format properties.
condition9.FormatType = ExcelCFType.CellValue;
condition9.Operator = ExcelComparisonOperator.NotEqual;
condition9.FirstFormula = "1000";
condition9.BackColor = ExcelKnownColors.Lime;
```

### [VB.NET]

```vb
' Applying conditional formatting to "A1" for format type as CellValue(Between).
Dim condition As IConditionalFormats = sheet.Range("A1").ConditionalFormats

' Adding formats to the IConditionalFormats collection.
Dim condition1 As IConditionalFormat = condition.AddCondition()
sheet.Range("A1").Text = "Enter a Number between 10 to 20"
```

## API Reference

- **Namespace:**  
  The code snippets use objects and methods from the `Excel` namespace, such as `ExcelCFType`, `ExcelComparisonOperator`, and `ExcelPattern`.

- **Class методы/свойства:**
  - `ExcelCFType.CellValue`
  - `ExcelComparisonOperator.{NotBetween, LessOrEqual, NotEqual}`
  - `ExcelPattern.DarkVertical`
  - `ExcelKnownColors.{Light_green, Lime}`
  - `IConditionalFormats.ConditionalFormats`
  - `IConditionalFormat.AddCondition()`
  - `Range.Text`

### Parameters

- `FirstFormula` and `SecondFormula`: Used to define the range or threshold for conditional formatting.
- `Operator`: Specifies the type of comparison to be applied.

### Returns

The methods and properties return `IConditionalFormats` and `IConditionalFormat` objects that can be further formatted using the properties mentioned above.

### Exceptions

The code snippets do not explicitly handle any exceptions, but ensure error handling is in place when implementing these functionalities.

## Code Examples

The provided examples demonstrate how to apply conditional formatting in various scenarios:
- Setting a fill pattern for values not between 100 and 200.
- Applying a background color for values less than or equal to 1000.
- Formatting a background color when a value is not equal to 1000.

<!-- tags: [syncfusion, winforms, xlsio, conditional formatting, cell value, comparison operator, formatting options, v11.4.0.26] keywords: [ExcelCFType, ExcelComparisonOperator, ExcelPattern, ExcelKnownColors, IConditionalFormats, IConditionalFormat] -->
```