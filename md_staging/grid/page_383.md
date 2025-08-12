```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_383.jpeg
document_name: grid
page_number: 383
page_id: grid#page_383
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:13:43Z
fidelity: lossless
-->

## Named Range Editing in Essential Grid

You can edit the named ranges by using the **NamedRange Collection Editor**. The following code uses the `ShowNamedRangesDialog` method to display the editor.

### Code Examples

#### C#

```csharp
GridFormulaNamedRangesEditHelper.ShowNamedRangesDialog(this.engine);
```

#### VB.NET

```vb
GridFormulaNamedRangesEditHelper.ShowNamedRangesDialog(Me.engine)
```

### NamedRange Collection Editor

![](attachment://image.png)

**Figure 137: NamedRange Collection Editor**

In the above dialog box, you will notice the named ranges (Members) are displayed in the left pane and their corresponding properties to the right pane (Properties). You can select a Named Range and edit its value as follows.

## Summary

This section explains how to edit named ranges in the Essential Grid using the NamedRange Collection Editor. The `ShowNamedRangesDialog` method is utilized to display the editor, allowing modifications to named ranges and their properties.

## API Reference

- **GridFormulaNamedRangesEditHelper**:
  - `ShowNamedRangesDialog(engine): void`
    - **Parameters**:
      - `engine`: The engine instance to which the named ranges belong.
    - **Description**: Displays the NamedRange Collection Editor dialog for editing named ranges.

## Code Examples (Detailed)

#### C#

```csharp
using Syncfusion.Windows.Forms.Grid;
using Syncfusion.Windows.Forms.Grid.Formula;

// Example usage
public class NamedRangeEditorExample : Form
{
    private readonly GridControl grid = new GridControl();

    public NamedRangeEditorExample()
    {
        this.Load += OnFormLoad;
    }

    private void OnFormLoad(object sender, EventArgs e)
    {
        // Initialize grid and engine
        GridFormulaEngine engine = new GridFormulaEngine();
        GridFormulaNamedRangesEditHelper.ShowNamedRangesDialog(engine);
    }
}
```

#### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Grid
Imports Syncfusion.Windows.Forms.Grid.Formula

Public Class NamedRangeEditorExample
    Inherits Form
    Private WithEvents grid As New GridControl()

    Public Sub New()
        AddHandler Me.Load, AddressOf OnFormLoad
    End Sub

    Private Sub OnFormLoad(sender As Object, e As EventArgs)
        ' Initialize grid and engine
        Dim engine As New GridFormulaEngine()
        GridFormulaNamedRangesEditHelper.ShowNamedRangesDialog(engine)
    End Sub
End Class
```

## Cross References

- Refer to the GridFormulaEngine documentation for more details on managing named ranges and formulas.

<!-- tags: [grid, namedrange, editor, syncfusion, winforms] keywords: [named range, collection editor, shownamedrangesdialog, gridformulaenginedialog] -->
```