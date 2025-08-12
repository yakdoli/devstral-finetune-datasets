```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_116.jpeg
document_name: grid
page_number: 116
page_id: grid#page_116
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:34:07Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This section discusses cell type conversion and handling for various cell types in the `Grid` control.
- Covers different cell types such as Number, Image, ComboBox/RichText, ProgressBar, and DateTime.

## Content

### 3.1.6.1.1.2 If format not specified
- The cell is checked whether it is a Number cell type by using the `CellType` property.
- If it is not a Number cell type, the format is skipped for all cell types.
- Finally, the `CellValue` is assigned to `Range`'s `Value2` property.
- Since the format is not specified, the `Value2` value is converted to its respective type and set to General Format.

### 3.1.6.1.1.3 Image Cell Conversion

#### If CellType specified
- The cell is checked whether it is an Image cell type by using the `CellType` property.
- If it is an Image cell type, the `CellValue` is converted to a bitmap and this bitmap is inserted into the sheet specifying the row and column.

#### If CellType not specified
- Not Applicable

### 3.1.6.1.1.4 ComboBox and RichText Cell Conversion

#### If CellType specified
- The cell is checked whether it is a ComboBox or RichText cell type by using the `CellType` property.
- If it is a ComboBox or RichText cell type, the `FormattedText` is stored in the `Range`'s `Text` property.

#### If CellType not specified
- Not Applicable

### 3.1.6.1.1.5 ProgressBar Cell Conversion

#### If CellType specified
- The cell is checked whether it is a ProgressBar cell type using the `CellType` property.
- If it is a ProgressBar cell type, the ProgressBar text style is checked whether it should be in percentage style.
- If the style is in percentage, then the percentage value is calculated and saved to `Range`'s `Number` property.
- The `Range`'s `NumberFormat` is saved as "0%".
- If there is no style specified, the `ProgressValue` is directly saved to `Range`'s `Number`.

#### If CellType not specified
- Not Applicable

### 3.1.6.1.1.6 DateTime Cell Conversion

#### If format specified
- The cell is checked whether it is a DateTime cell type using the `CellType` property.
- If it is a DateTime cell type, the format is skipped for all cell types and finally the `CellValue` is assigned to `Range`'s `DateTime` property.
- Since the format is specified, the `DateTime` value is converted to `DateTime` type and the format is set to the `DateTime` format in `Range`'s `Format`.

#### If format not specified
- The cell is checked whether it is a DateTime cell type using the `CellType` property.
- If it is not a DateTime cell type, the format is skipped for all cell types and finally the `CellValue` is assigned to `Range`'s `DateTime` property.
- Since the format is not specified, the `DateTime` value is converted to `DateTime` type and set to General Format.

## Code Examples

No code examples provided in this section.

## RAG Annotations
<!-- tags: [grid, windows forms, cell conversion, essential grid] keywords: [CellType, Value2, Image cell, ComboBox, RichText, ProgressBar, DateTime] -->
```