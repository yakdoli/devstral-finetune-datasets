```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_524.jpeg
document_name: grid
page_number: 524
page_id: grid#page_524
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:21:49Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
this.gridControl1.Model.CutPaste.CutRange(GridRangeInfo.Row(4), false);
```

- **Using VB.NET**

```vb
Me.gridControl1.Model.CutPaste.CutRange(GridRangeInfo.Row(4), False)
```

- **CanPaste** - This method checks for the most recent content in the clipboard that can be pasted into the grid. The return type of this method is Boolean. If it returns true, it indicates that the contents in the clipboard can be pasted into the grid. If there is no content available in the clipboard to paste, this method returns false.

  The following code examples show how to call this method:

  - **Using C#**

  ```csharp
  this.gridControl1.Model.CutPaste.CanPaste();
  ```

  - **Using VB.NET**

  ```vb
  Me.gridControl1.Model.CutPaste.CanPaste()
  ```

- **Paste** - This method pastes the content from the clipboard into the grid at the current selected range or current cell.

  **Note:** It is not mandatory to call this method after the CanPaste method. If there is no content in the clipboard to be pasted, this method will not respond.

  The following code examples show how to call this method:

  - **Using C#**

  ```csharp
  this.gridControl1.Model.CutPaste.Paste();
  ```

  - **Using VB.NET**

  ```vb
  Me.gridControl1.Model.CutPaste.Paste()
  ```

---

## API Reference

### Methods

- **CanPaste()**
  - **Return Type:** Boolean
  - **Description:** Checks if the contents in the clipboard can be pasted into the grid.
  - **Parameters:** None

- **Paste()**
  - **Return Type:** None
  - **Description:** Pastes the content from the clipboard into the grid at the current selected range or current cell.

---

## Code Examples

### C# Example

```csharp
// Check if content can be pasted
bool canPaste = this.gridControl1.Model.CutPaste.CanPaste();

if (canPaste)
{
    // Paste the content
    this.gridControl1.Model.CutPaste.Paste();
}
```

### VB.NET Example

```vb
' Check if content can be pasted
Dim canPaste As Boolean = Me.gridControl1.Model.CutPaste.CanPaste()

If canPaste Then
    ' Paste the content
    Me.gridControl1.Model.CutPaste.Paste()
End If
```

<!-- tags: [Essential Grid, Windows Forms, clipboard operations, paste, can paste, grid control] -->
keywords: [CanPaste, Paste, clipboard, grid, Windows Forms, content, clipboard operations]
```