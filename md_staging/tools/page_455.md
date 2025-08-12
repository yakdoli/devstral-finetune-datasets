```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_455.jpeg
document_name: tools
page_number: 455
page_id: tools#page_455
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:14:07Z
fidelity: lossless
-->

## Content

### Overview
- This section explains how to modify the days displayed in the calendar using the **PrepareViewStyleInfo** event of the Grid control embedded in the **MonthCalendarAdv** control.

### WinForms Code Examples

#### C#

```csharp
private void Form1_Load(object sender, EventArgs e)
{
    foreach (Control ctl in this.monthCalendarAdv1.Controls)
    {
        GridControl grid = ctl as GridControl;
        if (grid != null)
        {
            grid.PrepareViewStyleInfo += new 
                GridPrepareViewStyleInfoEventHandler(grid_PrepareViewStyleInfo);

            break;
        }
    }
}

void grid_PrepareViewStyleInfo(object sender, GridPrepareViewStyleInfoEventArgs e)
{
    if (e.Style.Text == "1")
    {
        e.Style.Text = "a";
    }
}
```

#### VB.NET

```vb
Private Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    For Each ctl As Control In Me.monthCalendarAdv1.Controls
        Dim grid = CType(IIf(TypeOf ctl Is GridControl, ctl, Nothing), GridControl)
        
        ' Add grid.PrepareViewStyleInfo handler if needed.
    Next
End Sub
```

#### Additional Example Code

```csharp
' if not Monday
If e.ColIndex <> 2 Then
    e.Style.Clickable = False
    e.Style.Enabled = False
End If
```

---

### How to change the days displayed in the calendar

To customize the days displayed in the calendar, you need to handle the **PrepareViewStyleInfo** event of the Grid control within the **MonthCalendarAdv** control. This event allows you to modify the cell styles, such as the text displayed for specific dates.

#### Steps to Change the Days Displayed

1. **Access the GridControl**:
   - Iterate through the controls within the **monthCalendarAdv1** instance and find the instance of the **GridControl**.

2. **Attach the Event Handler**:
   - Use the `PrepareViewStyleInfo` event to modify the style of grid cells.

3. **Modify the Cell Text**:
   - In the event handler, check the current cell's style text and modify it as required.

#### Example: Changing "1" to "a"

The provided C# example demonstrates how to change the text "1" to "a" for a specific grid cell. This can be extended to modify any other cells or apply different conditions based on the grid's content.

---

### Implementation Details

#### Handling the Event

The `grid_PrepareViewStyleInfo` method is triggered for each cell being prepared for rendering. By checking the `e.Style.Text` property, you can determine the current text of the cell and update it accordingly.

#### Conditional Updates

The example checks if the cell's text is "1" and updates it to "a". You can extend this logic to handle other conditions or manipulate different properties such as color, font, or visibility.

---

### Summary

By handling the **PrepareViewStyleInfo** event of the Grid control within the **MonthCalendarAdv** control, you can customize the appearance and content of the calendar displayed in your Windows Forms application. This approach provides fine-grained control over how individual cells are styled and displayed.

---

### Footer

© 2013 Syncfusion. All rights reserved. 455 | Page

---

<!-- tags: [syncfusion, winforms, tools, calendar, grid, control, prepareviewstyleinfo, event, customization, monthcalendaradv, version:11.4.0.26] keywords: [gridcontrol, eventhandler, cellstyle, textmodification, calendar, tools, windowsforms, syncfusion] -->
```