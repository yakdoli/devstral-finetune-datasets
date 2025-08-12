```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_146.jpeg
document_name: XlsIO
page_number: 146
page_id: XlsIO#page_146
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:57:07Z
fidelity: lossless
-->

**Essential XlsIO**

```csharp
1000"

' Setting format properties.
condition7.FormatType = ExcelCFTYPE.CellValue
condition7.Operator = ExcelComparisonOperator.LessOrEqual
condition7.FirstFormula = "1000"
condition7.BackColor = ExcelKnownColors.Light_green

' Applying conditional formatting to "A9" for format type as CellValue(NotEqual).
Dim condition8 As IConditionalFormats = sheet.Range("A9").ConditionalFormats

' Adding formats to the IConditionalFormats collection.
Dim condition9 As IConditionalFormat = condition8.AddCondition()
sheet.Range("A9").Text = "Enter a Number which is not equal to 1000"

' Setting format properties.
condition9.FormatType = ExcelCFTYPE.CellValue
condition9.Operator = ExcelComparisonOperator.NotEqual
condition9.FirstFormula = "1000"
condition9.BackColor = ExcelKnownColors.Lime
```

![Microsoft Excel - Sample](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZAAAAC8CAYAAAA8zrfsAAAABHRFWHRTb2Z0d2FzcyB2ZWN0b3MSGdhdG93bgAAEAAQ5GKGAAAAZ0lEQVR4nO2dwysAQAhFXjd5/xkABBQ3CCCCCCCh///////8ABQ0G+///////DFfA0SBvQhggrs8rfa83pxkgoAEB既可以ccccccBAAndAAAA䄩0́ğGgJPAzEnEpesAwSAeSeAqZIZ//AuahQfTFYAwSEqFeAwQGxNIEwAEGhOBTGhOFTeAlIFBbCHWgNMZjLHN7AEICIAEISaQwCESACBQDBBSoBDIGBIDogLRIqDwCwRABABSoBDIGBIDogLRIqDwCwRABABSoBDIGBIDogLRIqDwCwRABABSoBDIF currentPageAEGkوبةdTIFIFCAFEXJScgHEROHgABRQqOEEOhSAAAAADNZVVX5fISsZlisXCicYfKttlfFymYQvOsMXJ0uAEIEbVsG3pAewBaBkgGK1SBIQIIwQQIIEQAEioEIAQQIIEwSpCrXI/XVgGc1KCfihxTuLDDDbg4pGtW6zKwQIIEEa1gmg AguZxRhkRiFwqpxQhAKKExGCEMC_ylabelX=####Embedded image####🙅‍♀️ MVP