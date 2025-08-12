```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_165.jpeg
document_name: XlsIO
page_number: 165
page_id: XlsIO#page_165
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:36Z
fidelity: lossless
-->

## Copying/Moving Range

### Overview

- Support for copying and moving cells in Excel worksheets.
- The `CopyTo` method for transferring cells from one range to another.
- Options to copy cell formats, styles, and other elements using the `ExcelCopyRangeOptions` enumerator.

### Content

Moving and copying cells is a very common procedure when you are creating or editing your worksheets. XlsIO provides support to copy a range of cells from one end to another. The `CopyTo` method enables copying a range of cells from the source to the destination. It has an option to copy all the formats or only specific formats to the destination range by using the `ExcelCopyRangeOptions` enumerator. The following values can be set for the `ExcelCopyRangeOptions`:

| **Member Name**          | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| None                     | No flags.                                                                      |
| UpdateFormulas           | Indicates whether to update formulas during copy. WARNING: you should always specify this flag if your operations could change the position of an Array formula. |
| UpdateMerges             | Indicates whether to update merges during copy.                                                        |
| CopyStyles               | Indicates that we have to copy styles during range copy.                                             |
| CopyShapes               | Indicates that we have to copy shapes during range copy.                                              |
| CopyErrorIndicators      | Indicates that we have to copy error indicators during range copy.                                   |
| CopyConditionalFormats   | Indicates that we have to copy conditional formats during range copy.                                |
| All                      | All flags.                                                                     |

The following code example illustrates how to copy a range of cells from the source to the destination, preserving only cell styles.

```csharp
[C#]

// Copying a Range.
Dim source As IRange = sheet.Range("A1")
Dim des As IRange = sheet.Range("A5")
source.CopyTo(des)
```

### API Reference

#### Methods

- **CopyTo** (`destination As IRange`, `options As Enum.ExcelCopyRangeOptions`)
  - **Parameters:**
    - `destination`: The destination range where the source range is to be copied.
    - `options`: The options for copying (e.g., `CopyStyles`, `UpdateFormulas`, etc.).
  - **Returns:** None
  - **Description:** Copies the specified range to the destination range with the specified options.

### Code Examples

#### Example: Copying a Range with Cell Styles

```csharp
[C#]

// Copying a Range.
Dim source As IRange = sheet.Range("A1")
Dim des As IRange = sheet.Range("A5")
source.CopyTo(des)
```

<!-- tags: [XlsIO, Syncfusion Winforms, copying cells, ExcelCopyRangeOptions, copying cells with styles, C# code examples] keywords: [copyto, rangecopy, styles, cell formatting, conditional formats, error indicators, cell merging, formula updates] -->
```