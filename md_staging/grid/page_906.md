```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_906.jpeg
document_name: grid
page_number: 906
page_id: grid#page_906
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:51:17Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Grid Grouping control with Field Chooser

#### Overview
- This section discusses the Grid Grouping control feature along with the Field Chooser dialog box.
- The Field Chooser allows users to customize the columns visible in the Grid control.
- Sample demonstration includes a layout and explanation of how to use the Field Chooser.

#### Content
**Figure 327: Grid Grouping control with Field Chooser**

The image demonstrates the Grid Grouping control in use, showing a table with various fields such as `ProductID`, `CategoryID`, `QuantityPerUnit`, `UnitPrice`, `ReorderLevel`, and `Discontinued`. The Field Chooser dialog box is displayed, allowing users to select which columns to show or hide.

**For more details, refer the following sample:**
```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\WindowsGrid.Grouping.Windows\Samples\2.0\Grouping Grid Layout\Grid Field Chooser Demo
```

### Field Chooser Events

#### Overview
- Field Chooser events are used to customize the Field Chooser dialog box.
- These events allow users to modify the behavior of the Field Chooser dialog and customize its functionality.

#### Field Chooser Events
Field Chooser events include:
- **FieldChooserShowing**: Triggered before the Field Chooser dialog is shown.
- **FieldChooserShown**: Triggered after the Field Chooser dialog is shown.
- **FieldChooserClosing**: Triggered before the Field Chooser dialog is closed.
- **FieldChooserClosed**: Triggered after the Field Chooser dialog is closed.

**FieldChooser Events Table**

- **FieldChooserShowing**: Allows customization before the dialog is displayed.
- **FieldChooserShown**: Can perform operations after the dialog is displayed.
- **FieldChooserClosing**: Enables modifications before closing the dialog.
- **FieldChooserClosed**: Can handle cleanup or post-processing after closing.

### API Reference

#### Below is a summary of the events related to the Field Chooser:

- **FieldChooserShowing**
- **FieldChooserShown**
- **FieldChooserClosing**
- **FieldChooserClosed**

These events allow developers to customize the behavior and appearance of the Field Chooser dialog dynamically.

### Related Documentation

For more information on the Grid Grouping control and Field Chooser:
- Explore detailed documentation and samples in the Syncfusion WinForms SDK.
- Reference the sample provided for practical implementation and customization guidance.

<!-- tags: [Grid, WinForms, FieldChooser, EventHandling, Customization] keywords: [DataGrid, ColumnVisibility, UserInteraction, WindowsForms, ControlBehavior] -->
```