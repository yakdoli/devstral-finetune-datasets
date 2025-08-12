```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_349.jpeg
document_name: XlsIO
page_number: 349
page_id: XlsIO#page_349
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:12:25Z
fidelity: lossless
-->

## Error Checking Options in XlsIO

### Overview
- This page details the error-checking features provided by XlsIO, including options to ignore errors and remove green indicators. These features are accessible through the `IgnoreErrorOptions` property of the `IRange` interface.
- The `ExcelIgnoreError` enumerator allows setting specific error indicators that can be ignored.
- Key error-checking rules include evaluating to error values, handling text dates with two-digit years, and detecting formulas that omit cells or contain inconsistent references.

### Content

#### Error Checking Options Dialog Box
- Figure 127 illustrates the `Options Dialog Box - Error Checking`, showing various settings and rules for error checking.
- **Settings**:
  - Enable background error checking (checked).
  - Error Indicator Color: Automatic.
  - **Rules**:
    - Evaluates to error value (checked).
    - Text date with 2 digit years (checked).
    - Number stored as text (checked).
    - Inconsistent formula in region (checked).
    - Formula omits cells in region (checked).
    - Unlocked cells containing formulas (checked).
    - Formulas referring to empty cells (unchecked).
    - List data validation error (checked).

#### Ignoring Errors in XlsIO
- **IgnoreErrorOptions**:
  - XlsIO provides functionality to ignore specified errors and remove green indicators.
  - This can be achieved using the `IgnoreErrorOptions` property of the `IRange` interface.
  - The `ExcelIgnoreError` enumerator lists the values that can be set for ignoring specific error indicators.

#### Values for `ExcelIgnoreError`
Below is a table summarizing the values that can be set for the `IgnoreError` option through the `ExcelIgnoreError` enumerator:

| Member name             | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| None                    | Represents None flag of excel ignore error indicator.                        |
| EvaluateToError        | Represents EvaluateToError flag of excel ignore error indicator.             |
| EmptyCellReferences    | Represents EmptyCellReferences flag of excel ignore error indicator.         |
| NumberAsText           | Represents NumberAsText flag of excel ignore error indicator.                |
| OmittedCells           | Represents OmittedCells flag of excel ignore error indicator.                 |
| InconsistentFormula    | Represents InconsistentFormula flag of excel ignore error indicator.          |
| TextDate                | Represents TextDate flag of excel ignore error indicator.                    |

### API Reference
The `ExcelIgnoreError` enumerator is used to specify which error indicators to ignore. The following values can be used:

- **None**: No error indicators are ignored.
- **EvaluateToError**: Errors due to formula evaluation are ignored.
- **EmptyCellReferences**: Reference errors due to empty cells are ignored.
- **NumberAsText**: Errors where numbers are stored as text are ignored.
- **OmittedCells**: Errors due to omitted cells in formulas are ignored.
- **InconsistentFormula**: Inconsistent formulas within a region are ignored.
- **TextDate**: Errors due to two-digit year text dates are ignored.

### Code Example
Here is an example of using the `IgnoreErrorOptions` property:

```csharp
// Example: Ignoring specific error indicators
using Syncfusion.XlsIO;

// Initialize Excel engine and load workbook
IWorkbook workbook = new Workbook();
IWorksheet worksheet = workbook.Worksheets[0];

// Set ignore error options for a range
IRange range = worksheet.Range["A1:B10"];
range.IgnoreErrorOptions = ExcelIgnoreError.NumberAsText | ExcelIgnoreError.TextDate;
```

### Cross References
- See also: Error Checking in Excel, Workbook Settings, IRange Interface Documentation.

### RAG Annotations
<!-- tags: XlsIO, error checking, background error checking, ExcelIgnoreError, IRange, error indicators keywords: error checking rules, ignore errors, error indicators, ExcelIgnoreError values, IRange interface, formula evaluation errors, two-digit year dates -->
```