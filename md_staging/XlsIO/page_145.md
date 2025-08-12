```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_145.jpeg
document_name: XlsIO
page_number: 145
page_id: XlsIO#page_145
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:58:23Z
fidelity: lossless
-->

# Essential XlsIO

```vb
condition1.FirstFormula = "10"
condition1.SecondFormula = "20"

' Setting format properties.
condition1.Operator = ExcelComparisonOperator.Between
condition1.FormatType = ExcelCFType.CellValue
condition1.BackColor = ExcelKnownColors.Light_orange
condition1.IsBold = True
condition1.IsItalic = True

' Applying conditional formatting to "A3" for format type as CellValue(Equal).
Dim condition2 As IConditionalFormats = sheet.Range("A3").ConditionalFormats

' Adding formats to the IConditionalFormats collection.
Dim condition3 As IConditionalFormat = condition2.AddCondition()
sheet.Range("A3").Text = "Enter the Number as 1000"

' Setting format properties.
condition3.FormatType = ExcelCFType.CellValue
condition3.Operator = ExcelComparisonOperator.Equal
condition3.FirstFormula = "1000"
condition3.FontColor = ExcelKnownColors.Magenta

' Applying conditional formatting to "A5" for format type as CellValue(Not between).
Dim condition4 As IConditionalFormats = sheet.Range("A5").ConditionalFormats

' Adding formats to the IConditionalFormats collection.
Dim condition5 As IConditionalFormat = condition4.AddCondition()
sheet.Range("A5").Text = "Enter a Number not between 100 to 200"

' Setting format properties.
condition5.FormatType = ExcelCFType.CellValue
condition5.Operator = ExcelComparisonOperator.NotBetween
condition5.FirstFormula = "100"
condition5.SecondFormula = "200"
condition5.FillPattern = ExcelPattern.DarkVertical

' Applying conditional formatting to "A7" for format type as CellValue(LessOrEqual).
Dim condition6 As IConditionalFormats = sheet.Range("A7").ConditionalFormats

' Adding formats to the IConditionalFormats collection.
Dim condition7 As IConditionalFormat = condition6.AddCondition()
sheet.Range("A7").Text = "Enter a Number which is less than or equal to
```

## RAG Annotations
<!-- tags: [XlsIO, conditional formatting, cell value, format properties, Excel comparison operator, Excel known colors, font color, fill pattern] keywords: [ExcelComparisonOperator.Between, ExcelComparisonOperator.Equal, ExcelComparisonOperator.NotBetween, ExcelKnownColors.Light_orange, ExcelKnownColors.Magenta, ExcelPattern.DarkVertical, condition1, condition2, condition3, condition4, condition5, condition6, condition7] -->
```