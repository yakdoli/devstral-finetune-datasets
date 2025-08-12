```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_108.jpeg
document_name: tools
page_number: 108
page_id: tools#page_108
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:25:38Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the use of `CommandBarDockState` to manage the behavior of a fonts toolbar in a Windows Forms application.
- Focuses on adjusting the visibility and position of controls in relation to the `CommandBar` state.
- Highlights dynamic changes to control properties based on the toolbar's docking or floating state.

## Content

### Managing Font Toolbar Visibility and Position
The following code snippet illustrates how to dynamically adjust the visibility, length, and position of the fonts toolbar panel (`szFontToolBarPanel`) and its child controls (`fontComboBox` and `fontSizeComboBox`) based on the docking state of the toolbar.

```csharp
Syncfusion.Windows.Forms.Tools.CommandBarDockState currentborder = this.commandBarFonts.DockState;
Syncfusion.Windows.Forms.Tools.CommandBarDockState newborder = arg.NewDockState;
if ((((currentborder == Syncfusion.Windows.Forms.Tools.CommandBarDockState.Top) ||
      (currentborder == Syncfusion.Windows.Forms.Tools.CommandBarDockState.Bottom) ||
      (currentborder == Syncfusion.Windows.Forms.Tools.CommandBarDockState.Float) ||
      (currentborder == Syncfusion.Windows.Forms.Tools.CommandBarDockState.None)) &&
     ((newborder == Syncfusion.Windows.Forms.Tools.CommandBarDockState.Left) ||
      (newborder == Syncfusion.Windows.Forms.Tools.CommandBarDockState.Right)))
{
    this.fontComboBox.Visible = false;
    this.fontSizeComboBox.Visible = false;
    this.commandBarFonts.MaxLength = this.commandBarFonts.CalcCommandBarMaxLength(this.szFontToolBarPanel.Width);
    // Move the panel containing the fonts toolbar to the (0,0) position of the commandbar panel.
    this.pnlFontsTB.Location = new Point(0, 0);
}
```

### Restoring Visibility and Position
When the Fonts CommandBar is being redocked or floated from the left or right borders, the following logic restores the visibility of the combo boxes and adjusts the position of the fonts toolbar panel to its original location.

```csharp
// If the Fonts CommandBar is being redocked / floated from the left or right borders, then
// increase the max length and restore combo box visibility.
if ((((currentborder == Syncfusion.Windows.Forms.Tools.CommandBarDockState.Left) ||
      (currentborder == Syncfusion.Windows.Forms.Tools.CommandBarDockState.Right)) &&
     ((newborder == Syncfusion.Windows.Forms.Tools.CommandBarDockState.Top) ||
      (newborder == Syncfusion.Windows.Forms.Tools.CommandBarDockState.Bottom) ||
      (newborder == Syncfusion.Windows.Forms.Tools.CommandBarDockState.Float) ||
      (newborder == Syncfusion.Windows.Forms.Tools.CommandBarDockState.None)))
{
    this.commandBarFonts.MaxLength = this.commandBarFonts.CalcCommandBarMaxLength(this.szFontCommandBarPanelSize.Width);
    // Move the fonts toolbar panel to its original position ie., after the two combo boxes.
    this.pnlFontsTB.Location = new Point(this.fontSizeComboBox.Right + 6, 0);
}
```

### Explanation
- **Visibility Management**: The combo boxes (`fontComboBox` and `fontSizeComboBox`) are hidden when the toolbar is docked or floated at the top, bottom, or is none. They are restored when the toolbar is redocked or floated from the left or right.
- **Position Adjustment**: The panel containing the fonts toolbar (`pnlFontsTB`) is dynamically moved to either the `0,0` position within the command bar panel or its original position, based on the docking state of the toolbar.
- **Dynamic Length Calculation**: The `commandBarFonts.MaxLength` is recalculated based on the width of the relevant panel to ensure proper layout and responsiveness.

## API Reference

### Members Used
- `CommandBarDockState`
- `DockState`
- `NewDockState`
- `CalcCommandBarMaxLength`

### Methods
- `commandBarFonts.MaxLength`: Adjusts the maximum length of the font bar.

## Code Examples

The complete code implementation includes:

```csharp
// [Example code illustrating the use of CommandBarDockState for managing toolbar states]
```

### Notes
- This example assumes the presence of the necessary UI elements (`fontComboBox`, `fontSizeComboBox`, `commandBarFonts`, `szFontToolBarPanel`, etc.).
- Adjustments to control visibility and position are crucial for ensuring a responsive and user-friendly interface.

<!-- tags: [Windows Forms, CommandBarDockState, CommandBar, Fonts Toolbar] keywords: [DockState, NewDockState, MaxLength, CommandBar, fonts toolbar, visibility management, position adjustment, UI elements] -->
```