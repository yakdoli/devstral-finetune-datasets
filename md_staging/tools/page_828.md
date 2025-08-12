```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_828.jpeg
document_name: tools
page_number: 828
page_id: tools#page_828
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:37:12Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Provides an overview of essential tools for Windows Forms.
- Includes properties and events for Button, TextBox, and ListBox controls.
- Covers AutoScroll and DockPadding features with explanations and code examples.

## Content

### Controls

| Control       | Description                                                                                                                                                                                                 |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Button        | It includes the properties and events present in the windows Button.                                                                                                                                       |
| TextBox       | It includes the properties and events present in the windows TextBox.                                                                                                                                      |
| ListBox       | The ListBox property of editable list, expands and allows the user to set various appearance and behavior properties of the EditableList.                                                                    |

### AutoScroll

#### Description
You can enable scrollbars automatically for the EditableList control when its items are shown beyond its size by setting `AutoScroll` to true. When `AutoScroll` is enabled for the control, you can set the margin and logical size for the autoscroll region by using the `AutoScrollMargin` and `AutoScrollMinSize` properties.

#### EditableList Properties

| Property                   | Description                                                                                                                                                                                                                                                      |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **AutoScroll**             | It indicates whether Scrollbars will automatically appear if controls are placed outside the form's client area.                                                                                                                                            |
| **AutoScrollMargin**       | It sets margin around the controls during AutoScroll.                                                                                                                                                                                                           |
| **AutoScrollMinSize**      | It sets the minimum logical size for the AutoScroll region.                                                                                                                                                                                                     |

#### Code Examples

##### C#

```csharp
this.editableList1.AutoScroll = true;
this.editableList1.AutoScrollMargin = new System.Drawing.Size(2, 2);
this.editableList1.AutoScrollMinSize = new System.Drawing.Size(3, 3);
```

##### VB.NET

```vb
Me.editableList1.AutoScroll = True
Me.editableList1.AutoScrollMargin = New System.Drawing.Size(2, 2)
Me.editableList1.AutoScrollMinSize = New System.Drawing.Size(3, 3)
```

### Dock Padding

#### Description
Dock padding determines the size of the border for the docked controls.

## Page-level Navigation/TOC (if applicable)

- [AutoScroll](#autoscroll)
- [Dock Padding](#dock-padding)

## Cross References

See also:
- Properties: AutoScroll, AutoScrollMargin, AutoScrollMinSize
- Controls: Button, TextBox, ListBox

<!-- tags: [syncfusion, windowsforms, autoscroll, dockpadding, editablelist] keywords: [properties, controls, scrollbars, margin, minimum size, border, windows forms, tools] -->
```