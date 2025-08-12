```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_091.jpeg
document_name: edit
page_number: 091
page_id: edit#page_091
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:59:08Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Allow setting a pause at a specified location in the Edit Control using the Break Points feature.
- Combine Line Background and Custom Indicator features to achieve this functionality.
- Handle the `IndicatorMarginClick` event to insert a break point.

## Content

### Using Break Points in Essential Edit

Essential Edit allows you to set a pause at some specified location in the Edit Control by using the **Break Points** feature. This is done by combining the **Line Background** and **Custom Indicator** features. The `IndicatorMarginClick` event can be handled to insert a break point.

#### Example Code: C#

```csharp
private void editControl1_IndicatorMarginClick(object sender, Syncfusion.Windows.Forms.Edit.IndicatorClickEventArgs e)
{
    // Set breakpoint indicator.
    this.editControl1.SetCustomBookmark(e.LineIndex, new BookmarkPaintEventHandler(CustomBookmarkPainter));

    // Highlight the relevant line.
    IBackgroundFormat format =
        this.editControl1.RegisterBackColorFormat(color, Color.Transparent);
    this.editControl1.SetLineBackColor(e.LineIndex, true, format);
}
```

#### Example Code: VB.NET

```vb
Private Sub editControl1_IndicatorMarginClick(sender As Object, e As Syncfusion.Windows.Forms.Edit.IndicatorClickEventArgs) Handles editControl1.IndicatorMarginClick
    ' Set breakpoint indicator.
    Me.editControl1.SetCustomBookmark(e.LineIndex, New BookmarkPaintEventHandler(AddressOf CustomBookmarkPainter))

    ' Highlight the relevant line.
    Dim format As IBackgroundFormat =
        Me.editControl1.RegisterBackColorFormat(color, Color.Transparent)
    Me.editControl1.SetLineBackColor(e.LineIndex, True, format)
End Sub
```

## Page-level Navigation/TOC (if applicable)
- Essential Edit
  - Break Points Feature Overview
  - Implementing Break Points
    - Handling `IndicatorMarginClick` Event
  - Custom Indicator and Line Background Combining
  - Example Code in C# and VB.NET

## Cross References
- Refer to the Event handling section in Syncfusion's documentation for more details on handling `IndicatorMarginClick` events.

<!-- tags: [Essential Edit, Break Points, Windows Forms, Syncfusion Windows Forms] keywords: [Break Points, Line Background, Custom Indicator, IndicatorMarginClick, C#, VB.NET] -->
```