```html
<!--source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_522.jpeg
document_name: tools
page_number: 522
page_id: tools#page_522
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:18:41Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- User interfaces for color selection.
- Features of ColorPickerButton and ColorUIControl.
- Steps to create ColorPickerButton, both visually and programmatically.

---

### Content

#### Features

**ColorPickerButton** drops down a **ColorUIControl** and provides a standard user interface for selecting colors.

- **ColorPicker button** can be created programmatically.
- The **ColorPickerButton** allows setting the **ColorGroups** from which the color can be selected.
- The selected color of **ColorPickerButton** can be set as the **Button's backcolor** and **Button's Text value**.

#### Creating ColorPickerButton

**ColorPickerButton** is available to the designer by just dragging and dropping the **ColorPickerButton** from the toolbox onto the form.

![Figure 308: ColorPickerButton in Toolbox](https://i.imgur.com/Syncfusion_Toolbox.png)

It can be created programmatically as discussed below.

1. **Include the required namespace.**

   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```

---

### API Reference

#### Namespaces

- **Syncfusion.Windows.Forms.Tools**
  - **ColorPickerButton**
  - **ColorUIControl**
  - **ColorGroups**

---

### Code Examples

Example: Creating a **ColorPickerButton** programmatically.

```csharp
using Syncfusion.Windows.Forms.Tools;

// Create a new instance of ColorPickerButton
ColorPickerButton colorPickerButton = new ColorPickerButton();

// Set the ColorGroups
colorPickerButton.ColorPicker.ColorGroups = new string[] { "CustomColors", "StandardColors" };

// Add the button to the form
form.Controls.Add(colorPickerButton);
```

### Cross References

- **See also**
  - **ColorUIControl**

---

<!-- tags: [syncfusion, winforms, colorpickerbutton, coloruicontrol] keywords: [windows forms, color selection, programmatically, designer, toolbox, namespace, controlcreation, api, visual studio] -->
```