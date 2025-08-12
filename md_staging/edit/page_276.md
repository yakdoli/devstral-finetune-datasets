```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_276.jpeg
document_name: edit
page_number: 276
page_id: edit#page_276
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:25Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview

- Demonstrates handling the UpdateBookmarkTooltip event and setting the bookmark tooltip text for a specific line.
- Shows how to add a bookmark at the specified line and customize its tooltip display.

## Content

### Event Handling and Tooltip Customization

The following code demonstrates how to handle the `UpdateBookmarkTooltip` event, set the bookmark tooltip text, and specify the bookmark location:

#### Properties
| Property | Description |
|----------|-------------|
| **Image** | Gets / sets image associated with the tooltip. |
| **Line** | Index of the bookmarked line. |
| **Text** | Text of the tooltip. |
| **X** | Mouse X coordinate in client coordinates. |
| **Y** | Mouse Y coordinate in client coordinates. |

---

### C# Code Example

```csharp
// Handle the UpdateBookmarkToolTip event.
this.editControl.UpdateBookmarkToolTip += new
Syncfusion.Windows.Forms.Edit.UpdateBookmarkTooltipEventHandler(editControl_UpdateBookmarkToolTip);

// Set the bookmark at the specified line.
this.editControl.BookmarkAdd(this.editControl.CurrentLine);

// Specify whether bookmark tooltip should be shown.
this.editControl.ShowBookmarkTooltip = true;

private void editControl_UpdateBookmarkToolTip(object sender,
Syncfusion.Windows.Forms.Edit.UpdateBookmarkTooltipEventArgs e)
{
    // Set the bookmark tooltip text.
    e.Text = " Introduction to Essential Edit ";
}
```

---

### VB.NET Code Example

```vb
' Handle the UpdateBookmarkToolTip event.
AddHandler Me.editControl.UpdateBookmarkToolTip, AddressOf editControl_UpdateBookmarkToolTip

' Set the bookmark at the specified line.
Me.editControl.BookmarkAdd(Me.editControl.CurrentLine)

' Specify whether bookmark tooltip should be shown.
Me.editControl.ShowBookmarkTooltip = True

Private Sub editControl_UpdateBookmarkToolTip(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.UpdateBookmarkTooltipEventArgs)
    ' Set the bookmark tooltip text.
    e.Text = " Introduction to Essential Edit "
End Sub
```

---

## API Reference

### Event: UpdateBookmarkTooltip

- **Handler Type:** `UpdateBookmarkTooltipEventHandler`
- **Parameters:**
  - `object sender`: The source of the event.
  - `UpdateBookmarkTooltipEventArgs e`: Event data containing properties like `Text`, `Image`, `Line`, `X`, and `Y`.

### Properties

#### ShowBookmarkTooltip
- **Type:** `bool`
- **Description:** Specifies whether the bookmark tooltip should be shown.

#### BookmarkAdd
- **Method**: `void BookmarkAdd(int line)`
- **Description**: Adds a bookmark at the specified line.

## Code Examples

The provided code examples in **C#** and **VB.NET** demonstrate how to add a bookmark, configure its tooltip, and update the tooltip text dynamically.

## Cross References

- See also: `BookmarkManager`, `EditControl`, `UpdateBookmarkTooltipEventArgs`.

---

<!-- tags: [syncfusion, essential edit, windows forms, bookmark, tooltip, c#, vb.net] keywords: [updatebookmarktooltip, bookmarktooltip, tooltip text, client coordinates, editcontrol, event handling] -->
```