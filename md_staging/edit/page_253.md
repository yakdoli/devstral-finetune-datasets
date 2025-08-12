```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_253.jpeg
document_name: edit
page_number: 253
page_id: edit#page_253
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:53Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview

- Explanation of two events related to the indicator margin in the Windows Forms Edit control.
- Members such as `Bookmark` and `LineIndex` explained.
- Code samples provided in C# and VB.NET for handling these events.

## Content

### IndicatorMarginClick Event

| Member      | Description                           |
|-------------|---------------------------------------|
| Bookmark    | Gets clicked custom bookmark if available. |
| LineIndex   | Gets clicked line index.            |

**C#**
```csharp
private void editControl1_IndicatorMarginClick(object sender,
                                             Syncfusion.Windows.Forms.Edit.IndicatorClickEventArgs e)
{
    Console.WriteLine(" IndicatorMarginClick event is raised ");
}
```

**VB.NET**
```vbnet
Private Sub editControl1_IndicatorMarginClick(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.IndicatorClickEventArgs)
    Console.WriteLine(" IndicatorMarginClick event is raised ")
End Sub
```

#### 4.14.10.2 IndicatorMarginDoubleClick Event

This event is raised when the user double-clicks on the indicator margin area. The event handler receives an argument of type `IndicatorClickEventArgs`. The following `IndicatorClickEventArgs` members provide information specific to this event.

| Member      | Description                           |
|-------------|---------------------------------------|
| Bookmark    | Gets clicked custom bookmark if available. |
| LineIndex   | Gets clicked line index.            |

**C#**
```csharp
private void editControl1_IndicatorMarginDoubleClick(object sender,
                                                   Syncfusion.Windows.Forms.Edit.IndicatorClickEventArgs e)
{
    Console.WriteLine(" IndicatorMarginDoubleClick event is raised ");
}
```
```