```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_516.jpeg
document_name: tools
page_number: 516
page_id: tools#page_516
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:18:05Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page discusses properties and methods related to handling selected colors and groups in WinForms.
- It includes handling events such as ColorSelected, which is triggered upon selecting a color from a Color Group.

## Content

### Color Selection and Group Handling

#### SelectedColor and SelectedColorGroup
The figure below illustrates the selection of a color from a predefined group.

**Figure 302: SelectedColor = "OrangeRed"; SelectedColorGroup = "StandardColors"**

![Figure 302](https://syncfusion.com/docs/user-guide/windowsforms/tools-images/image302.png)

*Note: These property settings can be reset using `ResetSelectedColorGroup()` and `ResetSelectedColor()` methods.*

- **See Also**
  - [Color Groups](Color Groups)

### 3.5.4.2 Event Handling

This section covers the following event:

#### 3.5.4.2.1 ColorSelected Event

This event is triggered when a color from a Color Group is selected. The example below demonstrates how to close the ColorUI displayed in a Popup Menu using this event.

In the `ColorSelected` event, the following coding ensures that the popupControlContainer containing the ColorUI Control is closed once a color is selected.

```csharp
private void colorUIControl_ColorSelected(object sender, System.EventArgs e)
{
    // Ensures that the PopupControlContainer is closed after the selection of a color.
    Syncfusion.Windows.Forms.ColorUIControl cuicontrol = sender as Syncfusion.Windows.Forms.ColorUIControl;
    Syncfusion.Windows.Forms.PopupControlContainer pcc = cuicontrol.Parent as Syncfusion.Windows.Forms.PopupControlContainer;
}
```

---
**© 2013 Syncfusion. All rights reserved.**
```