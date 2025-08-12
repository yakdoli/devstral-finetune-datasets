```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_115.jpeg
document_name: XlsIO
page_number: 115
page_id: XlsIO#page_115
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:55:56Z
fidelity: lossless
-->

## Text Alignment

Text has to be aligned inside the cells to properly fit in any data. This is done in Excel by using the Horizontal and Vertical alignment settings either through the Formatting toolbar or through the options provided by the Alignment tab in the Format Cells dialog box. In addition to the Left, Center, and Right alignments, Horizontal alignment option goes further and allows text to be justified. This can be especially useful if the text is significantly long. Vertical alignment option allows you to align the contents of a cell towards the Top, Middle, or Bottom area of a cell.

![Figure 36: Alignment Settings in MS Excel](36)

## Indentation

In some circumstances, you may neither want to center the text nor keep it left or right aligned. In such cases, indentation can be done. Indentation consists of "pushing" the text to the left or right, without aligning it to center. To indent a text, you need to specify the number of units in the Indent box.

## Alignment Settings in XlsIO

XlsIO supports alignment properties similar to Excel. The following code example illustrates the alignment settings that can be applied to the cells by using XlsIO.
```html
115 |
Page
© 2013 Syncfusion. All rights reserved.
```
```