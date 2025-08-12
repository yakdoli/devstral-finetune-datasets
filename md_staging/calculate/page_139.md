```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_139.jpeg
document_name: calculate
page_number: 139
page_id: calculate#page_139
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:31Z
fidelity: lossless
-->

# Essential Calculate

| Ztest | Returns the P-value of a z-test. |
|-------|------------------------------------|

## Inside CalcEngine

### 4.6 Inside CalcEngine

Following are the topics discussed in this section.

#### 4.6.1 Tracking the Information

To track information used during calculations, CalcEngine manages several hash tables. Here is a table of the public hash tables in CalcEngine and a description of their keys and values:

### Table 12: Hash Table

| Hash Table            | Key                    | Value                  | Description                                                      |
|-----------------------|------------------------|------------------------|------------------------------------------------------------------|
| FormulaInfoTable      | Cell reference         | FormulaInfo object     | Tracks formula/value information for this cell.                  |
| DependentCells        | Cell reference         | Hashtable object       | Tracks cells that depend on this cell.                           |
| DependentFormulaCells | Formula cell reference | Hashtable object       | Tracks cells that the formula cell depends upon.                 |
| NamedRanges           | Name string            | Value string           | Associates the named range with its value.                       |
| LibraryFunctions      | Function name          | LibraryFunction delegate | Associates the function name with its method.                   |

Within CalcEngine, all data is assumed to be part of a rectangular array reference through cell coordinates like A1, C18, and so on. Even CalcQuickBase does not require or use such cell-type notation internally on the user side. When it communicates with CalcEngine, it converts its [name]-type notation into cell references that CalcEngine can understand. It is these cell references that are used as keys for the first three listed hash tables.

### 4.6.2 Parsing

## API Reference (if applicable)
- None explicitly detailed in this section.

## Code Examples (multi-language supported)
- None explicitly detailed in this section.

<!-- tags: [syncfusion-sdk, calcengine, ztest, hash-table, calculation-engine, dependent-cells, named-ranges, library-functions] keywords: [formula-info-object, hashtable, cell-reference, named-range, function-name, method] -->
```