```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_143.jpeg
document_name: XlsIO
page_number: 143
page_id: XlsIO#page_143
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:57:30Z
fidelity: lossless
-->

# Essential XlsIO

## Overview

- XlsIO allows you to create conditional formats by using `IConditionFormats`, with various conditions set via its properties.
- Supports applying more than three conditional formats in the same cell in the `.xlsx` format.

## Content

XlsIO provides the capability to create and apply conditional formats using the `IConditionFormats` interface. The following code demonstrates how to apply various conditional formats in XlsIO.

### Applying Conditional Formats

```csharp
// Applying conditional formatting to "A1" for format type as CellValue(Between).
IConditionFormats condition = sheet.Range["A1"].ConditionalFormats;

// Adding formats to IConditionFormats collection.
IConditionalFormat condition1 = condition.AddCondition();
sheet.Range["A1"].Text = "Enter a Number between 10 to 20";
condition1.FirstFormula = "10";
condition1.SecondFormula = "20";

// Setting format properties.
condition1.Operator = ExcelComparisonOperator.Between;
condition1.FormatType = ExcelCFTypes.CellValue;
condition1.BackColor = ExcelKnownColors.Light_orange;
condition1.IsBold = true;
condition1.IsItalic = true;

// Applying conditional formatting to "A3" for format type as CellValue(Equal).
IConditionFormats condition2 = sheet.Range["A3"].ConditionalFormats;

// Adding formats to the IConditionFormats collection.
IConditionalFormat condition3 = condition2.AddCondition();
sheet.Range["A3"].Text = "Enter the Number as 1000";

// Setting format properties.
condition3.FormatType = ExcelCFTypes.CellValue;
condition3.Operator = ExcelComparisonOperator.Equal;
condition3.FirstFormula = "1000";
condition3.FontColor = ExcelKnownColors.Magenta;

// Applying conditional formatting to "A5" for format type as CellValue (Not between).
IConditionFormats condition4 = sheet.Range["A5"].ConditionalFormats;

// Adding formats to the IConditionFormats collection.
IConditionalFormat condition5 = condition4.AddCondition();
sheet.Range["A5"].Text = "Enter a Number not between 100 to 200";
```

<!-- tags: [xlsio, conditional formatting, IConditionFormats] keywords: [cells, conditional formatting, between, equal, not between, properties, text, column, row, ExcelComparisonOperator, ExcelKnownColors, Italic, Bold, FontColor, BackColor] -->
```