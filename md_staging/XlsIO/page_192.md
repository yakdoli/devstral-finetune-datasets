```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_192.jpeg
document_name: XlsIO
page_number: 192
page_id: XlsIO#page_192
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:01:44Z
fidelity: lossless
--> 

# Essential XlsIO

```csharp
// Scrolls to 40th row
sheet.TopVisibleRow = 40

// Scrolls to 7 column when opening
sheet.LeftVisibleColumn = 7
```

This is especially useful when the spreadsheet has a large number of records, and the user wants to view a particular row/column that has some details, without scrolling to that row/column after opening it. Note that these row and column indexes are "one-based."

## Hide/Unhide Worksheet

### Overview
- Excel provides options for hiding or unhiding worksheets.
- These actions can be performed using the context menu or APIs in XlsIO.

### Content
#### Excel's Context Menu Option
Excel has the sheet tab bar that appears at the bottom of the screen with tab scrolling buttons displayed on the left side. Excel provides an option to show/hide a sheet from the user view. This is done by selecting the "Hide" item in the context menu of the sheet.

![](Figure_67_Hiding_a_Worksheet.png)
*Figure 67: Hiding a Worksheet*

#### Hiding and Unhiding a Worksheet in XlsIO
XlsIO also allows you to hide/unhide worksheets by using the `Visibility` property. The following APIs are used to hide/unhide worksheets.

### Code Examples

```csharp
// C#
sheet.Visibility = WorksheetVisibility.Hidden;
```

```vb
' VB.NET
sheet.Visibility = WorksheetVisibility.Hidden;
```
```