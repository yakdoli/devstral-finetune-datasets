```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_270.jpeg
document_name: grid
page_number: 270
page_id: grid#page_270
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:05:27Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Counts the number of cells that are not empty.

## COUNTA

### Syntax

COUNTA(value1, value2, ...), where:

- **value1, value2, ...** are arguments representing the values you want to count. In this case, a value is any type of information, excluding empty cells.

### 4.1.4.6.6.45 COUNTBLANK

Counts empty cells in a specified range of cells.

#### Syntax

COUNTBLANK(range), where:

- **range** is the range from which you want to count the blank cells.

#### Remark

- Cells with formulas that return `""` (empty text) are also counted. Cells with zero values are not counted.

### 4.1.4.6.6.46 COUNTIF

Counts the number of cells within a range that meet the given criteria.

#### Syntax

COUNTIF(range, criteria), where:

- **range** is the range of cells from which you want to count cells.
- **criteria** is the criteria in the form of a number, expression, or text that defines which cells will be counted. For example, the criteria can be expressed as `">32"`.

## API Reference

### Methods
- **COUNTA** - Counts the number of cells that are not empty.
- **COUNTBLANK** - Counts empty cells in a specified range of cells.
- **COUNTIF** - Counts the number of cells within a range that meet the given criteria.

### Parameters
- **COUNTA**
  - **value1, value2, ...** - Arguments representing the values you want to count.
- **COUNTBLANK**
  - **range** - The range from which you want to count the blank cells.
- **COUNTIF**
  - **range** - The range of cells from which you want to count cells.
  - **criteria** - The criteria in the form of a number, expression, or text that defines which cells will be counted.

### Returns
- **COUNTA**: The number of non-empty cells.
- **COUNTBLANK**: The number of blank cells.
- **COUNTIF**: The number of cells that meet the specified criteria.

## Code Examples

C#
```csharp
// Example using COUNTA
int countNonEmpty = COUNTA(10, "text", null, 20); // Counts 3 non-empty cells

// Example using COUNTBLANK
int countBlank = COUNTBLANK(range); // Counts blank cells in the specified range

// Example using COUNTIF
int countMatching = COUNTIF(range, ">32"); // Counts cells greater than 32
```

<!-- tags: [counta, countblank, countif, windows forms, essential grid, syncfusion] keywords: [cell count, non-empty cells, blank cells, criteria count, windows forms sdk, designer] -->
```