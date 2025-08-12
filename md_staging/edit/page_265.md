```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_265.jpeg
document_name: edit
page_number: 265
page_id: edit#page_265
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:30Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## 4.14.19 RegisteringKeyCommands Event

This event is discussed in the **Keystroke - Action Combinations Binding** topic.

## 4.14.20 Save Events

This section discusses the below given events that are generated when the user saves files and streams with data loss.

### 4.14.20.1 SaveFileWithDataLoss Event

This event is raised when user tries to save files with data loss.

The event handler receives an argument of type **SaveWithDataLosingEventArgs**. The following **SaveWithDataLosingEventArgs** members provide information, specific to this event.

| Member            | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| SaveWithLoss      | Gets / sets value that indicates whether data has to be saved with loss. |
| UserHandling      | Gets / sets value that indicates whether user handled the event.         |

#### Code Examples

```csharp
[C#]

private void editControl_SaveFileWithDataLoss(object sender, Syncfusion.Windows.Forms.Edit.SaveWithDataLosingEventArgs e)
{
    e.SaveWithLoss = true;
    e.UserHandling = true;
}
```

```vb
[VB.NET]

Private Sub editControl_SaveFileWithDataLoss(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.SaveWithDataLosingEventArgs)
    e.SaveWithLoss = True
    e.UserHandling = True
End Sub
```

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Edit
- **Class**: SaveWithDataLosingEventArgs
- **Properties**:
  - **SaveWithLoss**: Type: bool, Gets / sets value that indicates whether data has to be saved with loss.
  - **UserHandling**: Type: bool, Gets / sets value that indicates whether user handled the event.

<!-- Page-level Navigation/TOC (if applicable) -->
<!-- None -->

<!-- Cross References -->
- See also: SaveEvents, Keystroke - Action Combinations Binding

<!-- tags: [Syncfusion Winforms, SaveEvents, SaveFileWithDataLoss, EditControl] keywords: [save files, data loss, event handling, Syncfusion, Windows Forms, Save, Data Loss] -->
```