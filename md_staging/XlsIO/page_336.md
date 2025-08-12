```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_336.jpeg
document_name: XlsIO
page_number: 336
page_id: XlsIO#page_336
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:12:08Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Explains how the Automatic and Manual Calculation modes in Excel work and their impact on recalculating open workbooks.
- Describes the settings for Iteration, Workbook options, and manual calculation requests in the Options Dialog Box.
- Details scenarios where recalculations are particularly important or noticeable.

## Content

### Automatic Calculation

**Figure 120: Options Dialog Box- Calculation**

In the Automatic Calculation mode, Excel automatically recalculates all open workbooks at each and every change and whenever you open a workbook.

Usually when you open a workbook in Automatic mode, and recalculating is done, you will not be able to see the recalculating, because the changes will not be reflected until the workbook is saved. An exception is when you open a workbook in Excel 2000 that was saved by using Excel 97, or open a workbook by using Excel 2002/2003 saved by using Excel 2000. This is because Excel's calculation engines are different, and also because a Full calculation is done.

### Manual Calculation

In the Manual Calculation mode, Excel will only recalculate all open workbooks when you request it by pressing F9 or CTRL-ALT-F9, or when you Save a workbook. For workbooks taking more than a fraction of a second to recalculate, it is usually better to set the Calculation to "Manual".

Excel tells you when the workbook needs recalculating, by showing Calculate in the status bar.

## API Reference (if applicable)

None specified in this section.

## Code Examples (multi-language supported)

None specified in this section.

## Cross References

- Refer to the Syncfusion documentation for more details on Excel Calculation options and Automatic vs. Manual modes.

<!-- tags: [product, module, control, api, version?] keywords: [Excel, Calculation, Automatic, Manual, recalculate, workbook, Options Dialog Box, Update remote references, Excel 97, Excel 2000, Excel 2002/2003, Iteration, Maximum iterations, Maximum change] -->
```