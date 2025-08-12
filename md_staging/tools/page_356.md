```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_356.jpeg
document_name: tools
page_number: 356
page_id: tools#page_356
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:07:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Introduction to using the ButtonEdit control in the Toolbox.
- Initial appearance of the ButtonEdit control when added to a form.
- Process to add buttons to the ButtonEdit control using the ButtonEditChildButton Collection Editor.

## Content

### Step 1: Accessing the ButtonEdit Control

The ButtonEdit control can be found in the Toolbox, specifically under the Syncfusion category.

**Figure 167: ButtonEdit Control in Toolbox**
![Figure 167: ButtonEdit Control in Toolbox](https://i.imgur.com/example_image.png)

### Step 2: Initial Appearance of ButtonEdit

When the control is initially added to the form, it appears like an edit control with no buttons.

**Figure 168: ButtonEdit Control in the Designer Form**
![Figure 168: ButtonEdit Control in the Designer Form](https://i.imgur.com/example_image.png)

### Step 3: Adding Buttons to ButtonEdit

We can add buttons to the control using the `ButtonEditChildButton Collection Editor`, which is invoked by the `ButtonEdit.Buttons` property. The editor can also be accessed using the Smart Tag option.

## API Reference

### Properties

- **ButtonEdit.Buttons**: This property is used to access the ButtonEditChildButton Collection Editor.

## Code Examples

### Example of Adding Buttons to ButtonEdit

```csharp
// Access the ButtonEdit control
var buttonEdit = new ButtonEdit();

// Access the Buttons collection
buttonEdit.Buttons.Add(new ButtonEditButton
{
    Text = "Add",
    Click += (sender, e) => MessageBox.Show("Add button clicked!")
});

// Add the ButtonEdit control to the form
this.Controls.Add(buttonEdit);
```

## Cross References

See also:
- Syncfusion's official documentation for more details on ButtonEdit controls.
- Additional examples and tutorials in the Syncfusion WinForms User Guide.

<!-- tags: [Syncfusion Winforms, ButtonEdit Control, Toolbox, Designer Form] keywords: [ButtonEdit, Buttons, ButtonEditChildButton, ToolBox, designer, control editor, smart tag] -->
```