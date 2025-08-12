```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_150.jpeg
document_name: XlsIO
page_number: 150
page_id: XlsIO#page_150
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:57:24Z
fidelity: lossless
-->

## XlsIO

### Overview
- Demonstrates how to remove conditional formatting from an entire sheet.
- Explains the use of the `FormulaR1C1` property in conditional formatting.
- Provides examples in C# and VB.NET for setting conditional formatting formulas.

### Content

#### Removing Conditional Formatting Settings From Entire Sheet
```csharp
' Removing Conditional Formatting Settings From Entire Sheet.
sheet.UsedRange.Clear(ExcelClearOptions.ClearConditionalFormats)
```

#### Using FormulaR1C1 property in Conditional Formats

XlsIO returns or sets the formula for the conditional format by using R1C1-style notation. Following code example illustrates this.

**[C#]**
```csharp
// Using FormulaR1C1 property in Conditional Formatting
IConditionalFormats condition = worksheet.Range["E5:E18"].ConditionalFormats;
IConditionalFormat condition1 = condition.AddCondition();
condition1.FirstFormulaR1C1 = "=R[1]C[0]";
condition1.SecondFormulaR1C1 = "=R[1]C[1]";
```

**[VB.NET]**
```vbnet
' Using FormulaR1C1 property in Conditional Formatting
Dim condition As IConditionalFormats = sheet.Range("E5:E18").ConditionalFormats
Dim condition1 As IConditionalFormat = condition.AddCondition()
condition1.FirstFormulaR1C1 = "=R[1]C[0]"
condition1.SecondFormulaR1C1 = "=R[1]C[1]"
```

### Advanced Conditional Formatting

#### See Also
- [Cell Styles](#cell-styles)

### References

#### 4.1.1.6.2.1 Advanced Conditional Formatting

---

<!-- tags: [xlsio, conditionalfomatting, formulaR1C1, R1C1style, conditionalformattingadvanced] keywords: [xlsio, conditional formatting, formulaR1C1, R1C1 notation, advanced conditional formatting] -->

```