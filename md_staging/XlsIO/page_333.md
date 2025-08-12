```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_333.jpeg
document_name: XlsIO
page_number: 333
page_id: XlsIO#page_333
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:11:14Z
fidelity: lossless
-->

### XlsIO

#### Overview
- This section describes properties that indicate the type of data or formula present in a range of cells.
- It highlights Read-Only properties for various formula types, numbers, strings, rich text, style, and error options.
- Explains how to use Array formulas in Excel through the FormulaArray property.

#### Content

| Property             | Description                                                                                                                                                   |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HasFormula           | True if all cells in the range contain formulas; False if at least one of the cells in the range doesn't contain a formula. This is a Read-Only property. |
| HasFormulaArray      | Indicates whether range contains array-entered formula. This is a Read-Only property.                                                                      |
| HasFormulaBoolValue  | Indicates if current range has formula bool value. This is a Read-Only property.                                                                        |
| HasFormulaDateTime   | Indicates if current range has formula value formatted as DateTime. This is a Read-Only property.                                                          |
| HasFormulaErrorValue | Indicates if current range has formula error value. This is a Read-Only property.                                                                      |
| HasNumber            | Indicates whether the range contains number. This is a Read-Only property.                                                                                  |
| HasRichText          | Indicates whether cell contains formatted rich text string.                                                                                  |
| HasString            | Indicates whether the range contains String. This is a Read-Only property.                                                                         |
| HasStyle             | Indicates whether range has default style. False means default style. This is a Read-Only property.                                                       |
| IgnoreErrorOptions   | Represents various **ignore error options** in Excel.                                                                                                    |

### 4.4.1.1 Array Formula

#### Overview
Array Formula is a special type of formula in Excel. It works with an array or series of data values, rather than a single data value. XlsIO supports the usage of Array formula through the FormulaArray property.

#### Description
Following code example explains how an array of values, from Named Range, is used for computation. For more details on Named Ranges, please refer to [Defined Names](#). 

#### Code Example
```csharp
[C#]
```

#### Footer
© 2013 Syncfusion. All rights reserved.

#### RAG Annotations
<!-- tags: [xlsio, array formulas, read-only properties, formula types, rich text, style, error options, named ranges] keywords: [syncfusion sdk, xlsio, arrayformula, hasformula, hasformulaboolvalue, hasformuladatetime, hasformulaerrorvalue, hasnumber, hasrichtext, hasstring, hasstyle, ignoreerroroptions] -->
```