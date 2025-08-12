```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_627.jpeg
document_name: tools
page_number: 627
page_id: tools#page_627
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:25:28Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to create and use a `PopupControlContainer` control to display popups for other controls.
- Explains enabling scrollbars for the `PopupControlContainer` control.

## Content

### Creating a `PopupControlContainer`

We can add child controls to the `PopupControlContainer` and associate it as a popup for other controls like `RichTextBox`. Refer to the topic **How to show `PopupControlContainer` as the popup for a `RichTextBox` control?**.

A sample illustrating how to create a custom `PopupControlContainer` and assign it to a control is available in the following sample installation location:

```
.. \My Documents\S y n c f u s i o n \ E s s e n t i a l S t u d i o \ Version Number\Windows\Tools.Windows\Samples\2 . 0 \Editors Package\Container controls\PopupContainer\PopupContainerDemo
```

#### See also

- **Concepts and Features**
  - **3.5.6.1.3 Concepts and Features**

The following topics will help you become more familiar in using the `PopupControlContainer` control.

#### Scroll Support

We can enable scrollbars automatically for the `PopupContainer` control when its items are shown beyond its size by setting `AutoScroll` to true. When `AutoScroll` is enabled for the control, we can set the margin and logical size for the autoscroll region by using the `AutoScrollMargin` and `AutoScrollMinSize` properties.

| **PopupControlContainer Properties** | **Description** |
| --- | --- |
| AutoScroll | It indicates whether Scrollbars will automatically appear if controls are placed outside the form's client area. |
| AutoScrollMargin | It sets the margin around the controls during AutoScroll. |
| AutoScrollMinSize | It sets the minimum logical size for the AutoScroll region. |

## API Reference

### Properties

- **AutoScroll**  
  Type: Boolean  
  Indicates whether Scrollbars will automatically appear if controls are placed outside the form's client area.

- **AutoScrollMargin**  
  Type: Size  
  Sets the margin around the controls during AutoScroll.

- **AutoScrollMinSize**  
  Type: Size  
  Sets the minimum logical size for the AutoScroll region.

## Code Examples

Example in VB.NET:

```vb
Me.popupControlContainer1 = New Syncfusion.Windows.Forms.PopupControlContainer()
Me.Controls.Add(Me.popupControlContainer1)
```

### Additional Notes

Ensure that the `AutoScroll` property is set to `True` when using the `PopupControlContainer` to enable automatic scrolling for the control's contents.

## Cross References

- **3.5.6.1.3 Concepts and Features**

<!-- tags: [syncfusion, winforms, popupcontrolcontainer, autoscroll, windows forms, controls, rich text box] keywords: [popupcontrolcontainer, autoscroll, autoScrollMargin, autoScrollMinSize, windows forms controls] -->
```