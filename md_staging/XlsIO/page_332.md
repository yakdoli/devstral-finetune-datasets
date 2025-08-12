```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_332.jpeg
document_name: XlsIO
page_number: 332
page_id: XlsIO#page_332
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:11:53Z
fidelity: lossless
-->

## Overview
- Properties related to formulas in Excel.
- Handling of formula values, including boolean, date/time, and string evaluations.
- Validation and hidden formula properties.

## Content

### WinForms-specific conventions
- The table below provides a detailed overview of the properties related to formulas in Excel.

#### Properties and Descriptions

| Property                | Description                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| Formula                 | Returns or sets the object's formula in A1-style notation and in the language of the macro. <br> Read/write Variant. |
| FormulaArray            | Represents array-entered formula. <br> Visit `http://www.cpearson.com/excel/array.htm` for more information.          |
| FormulaArrayR1C1       | Returns or sets the formula array for the range by using R1C1-style notation.                                      |
| FormulaBoolValue       | Returns the calculated value of the formula as a boolean.                                                       |
| FormulaDateTime        | Gets/sets formula DateTime value contained by this cell. DateTime.MinValue if not all cells of the range have the same DateTime value. |
| FormulaErrorValue      | Returns the calculated value of the formula as a string.                                                        |
| FormulaHidden          | True if the formula will be hidden when the worksheet is protected; False if at least part of formula in the range is not hidden. |
| FormulaNumberValue     | Gets/sets number value evaluated by formula.                                                                    |
| FormulaR1C1            | Returns or sets the formula for the range by using R1C1-style notation.                                         |
| FormulaStringValue     | Gets/sets string value evaluated by formula.                                                                    |
| HasDataValidation      | Indicates whether the specified range object has data validation. <br> If Range is not a single cell, then returns True only if all cells have data validation. This is a Read-Only property. |
| HasDateTime            | Indicates whether the range contains DateTime value. This is a Read-Only property.                               |
| HasExternalFormula     | Indicates if the current range has an external formula. This is a Read-Only property.                            |

## Cross References
- For more information on formula arrays, refer to: [http://www.cpearson.com/excel/array.htm](http://www.cpearson.com/excel/array.htm).

## RAG Annotations
<!-- tags: [XlsIO, formulas, WinForms, properties, Excel] keywords: [Formula, FormulaArray, FormulaArrayR1C1, FormulaBoolValue, FormulaDateTime, FormulaErrorValue, FormulaHidden, FormulaNumberValue, FormulaR1C1, FormulaStringValue, HasDataValidation, HasDateTime, HasExternalFormula] -->
```