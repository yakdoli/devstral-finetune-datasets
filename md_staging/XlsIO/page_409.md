```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_409.jpeg
document_name: XlsIO
page_number: 409
page_id: XlsIO#page_409
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:16:32Z
fidelity: lossless
-->

## Essential XlsIO

### Scroll Bar

You may allow the users to view a particular worksheet, but hide the content in the last part of the worksheet from them. This can be done by hiding the scrollbars, by turning off either scrollbar checkbox, in the View tab of the Options dialog box.

XlsIO allows to control the visibility of these horizontal and vertical scrollbars in a workbook by using the IsHScrollBarVisible and IsVScrollBarVisible properties of IWorkbook as follows.

#### Code Example

```csharp
// Hides Horizontal scroll bar and show the vertical scroll bar
workbook.IsHScrollBarVisible = false;
workbook.IsVScrollBarVisible = true;
```

```vb
' Hides Horizontal scroll bar and show the vertical scroll bar
workbook.IsHScrollBarVisible = False
workbook.IsVScrollBarVisible = True
```

### Sheet Tabs

Excel allows to show/hide the workbook tabs, to prevent users from switching between sheets through sheet tabs, and focus their attention on a particular sheet.
```