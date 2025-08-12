```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_452.jpeg
document_name: tools
page_number: 452
page_id: tools#page_452
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:13:50Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes how to set diagonal columns BackColor to "Green" in a calendar control.
- Demonstrates how to add icons to data cells using the DateCellQueryInfo event.

---

## Content

### Visual Demonstration
![Figure 249: Diagonal Columns BackColor = "Green"](https://via.placeholder.com/500x300?text=Figure+249:+Diagonal+Columns+BackColor+%3D+%22Green%22)

### Setting Icons for the Data Cells

Using the `DateCellQueryInfo` event, we can add icons to the data cells.

#### Code Examples

- **C#**
  ```csharp
  private void monthCalendarAdv1_DateCellQueryInfo(object sender, Syncfusion.Windows.Forms.Tools.DateCellQueryInfoEventArgs e)
  {
      if (e.RowIndex == 3)
      {
          e.Style.ImageList = this.imageList1;
          e.Style.ImageIndex = 1;
      }
  }
  ```

- **VB.NET**
  ```vbnet
  Private Sub monthCalendarAdv1_DateCellQueryInfo(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Tools.DateCellQueryInfoEventArgs)
      If e.RowIndex == 3 Then
          e.Style.ImageList = this.imageList1;
          e.Style.ImageIndex = 1;
      End If
  End Sub
  ```

---

## API Reference

- **Event**: `DateCellQueryInfo`
  - **Namespace**: `Syncfusion.Windows.Forms.Tools`
  - **EventArgs**: `DateCellQueryInfoEventArgs`
  - **Parameters**:
    - `sender`: The object that triggered the event.
    - `e`: Event data containing properties and methods to manipulate the style and appearance of the date cell.

---

## Cross References
- [Unclear]

---

<!-- tags: [Syncfusion Winforms, DateCellQueryInfo, Set Icons, MonthCalendar] keywords: [Set Icons, DateCellQueryInfo, Visual Demonstration, C#, VB.NET, BackColor, Diagonal Columns] -->
```