```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_384.jpeg
document_name: grid
page_number: 384
page_id: grid#page_384
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:13:50Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Editing Named Ranges

### Overview
- Explanation of how to edit named ranges using the NamedRange Collection Editor.
- Ability to manipulate the title of the editor by handling the ShowingNamedRangesDialog event.

## Content

### Figure 138: Editing Named Ranges
The figure illustrates the NamedRange Collection Editor interface, where you can manage named ranges for "Car" as shown in the Key field, with "500" as its Value. Additional properties such as "Members" and "Car properties" are also present, providing control for adding, removing, and modifying named ranges.

#### Editing the Title of the Editor
You can also edit the title of this editor by handling the ShowingNamedRangesDialog event. The following code example demonstrates this:

#### Code Example in C#
```csharp
GridFormulaNamedRangesEditHelper.ShowingNamedRangesDialog += new ControlEventHandler(helper_ShowingNamedRangesDialog);

// Event handler to change the title of NamedRange Collection Editor dialog box.
private void helper_ShowingNamedRangesDialog(object sender, ControlEventArgs e)
{
    Form f = e.Control as Form;
    if (f != null)
    {
        // Set the title for the dialog box.
        f.Text = "CashFlow Inputs";
    }
}
```

##### APIs Used
- `GridFormulaNamedRangesEditHelper.ShowingNamedRangesDialog`: Event that allows customization of the NamedRange Collection Editor dialog box.
- `ControlEventArgs`: Event argument that contains the control being shown in the dialog box.

#### Code Example in VB.NET
Same functionality provided in VB.NET can be structured as follows, though the example in the image is cut off, indicating it continues in the next section.

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridFormulaNamedRangesEditHelper
- **Event**: ShowingNamedRangesDialog
  - **Parameters**:
    - `sender`: The source of the event.
    - `e`: ControlEventArgs, providing the control being shown in the dialog box.
  - **Returns**: None (void).
  - **Usage**: Subscribed to customize the NamedRange Collection Editor dialog box title.

## Code Examples (Multi-Language)

### C#
The provided C# example demonstrates how to change the title of the NamedRange Collection Editor dialog box to "CashFlow Inputs."

### VB.NET
Though not fully visible in the image, the equivalent functionality in VB.NET would involve similar event handling logic to update the dialog box title.

## Pages Navigation
- This section explains editing named ranges and modifying the editor title, which is part of the broader Grid functionality in Syncfusion Winforms.

### See also:
- Other related features and documentation in the Essential Grid for Windows Forms.

<!-- tags: [Syncfusion Winforms, Grid, NamedRange, Editor, Event, API] keywords: [named ranges, editor title, dialog box, C# example, VB.NET, control event handler, ShowingNamedRangesDialog, CashFlow Inputs] -->
```