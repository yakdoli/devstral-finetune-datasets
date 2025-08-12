```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_738.jpeg
document_name: tools
page_number: 738
page_id: tools#page_738
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:31:53Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The document outlines the use of the `IntegerTextBox` control in Windows Forms applications. It covers both the design-time and programmatic approaches to incorporating this control into an application. 

## Content

### IntegerTextBox in Toolbox

The `IntegerTextBox` control is available in the Windows Forms toolbox. Figure 464 displays the `IntegerTextBox` control being selected from the list of available tools.

**Figure 464: IntegerTextBox in Toolbox**

### Designer Approach

1. **Run the application.** The `IntegerTextBox` that allows you to enter only integer values will be displayed as shown below.

**Figure 465: IntegerTextBox created Through Designer**

### Through Programmatical Approach

The `IntegerTextBox` control can also be created programmatically in code.

#### Creating IntegerTextBox Programmatically

The IntegerTextBox control can be created programmatically through code as detailed below.

1. **Include the required namespace.**

```csharp
using Syncfusion.Windows.Forms.Tools;
```

---

## API Reference

### Namespace

- `Syncfusion.Windows.Forms.Tools`

### Class

- `IntegerTextBox`

### Properties
- **Value**: Gets or sets the integer value in the control.
- **Format**: Specifies the format in which the integer should be displayed.

### Methods
- **OnValueChanged**: Triggered when the value in the `IntegerTextBox` changes.

### Events
- **ValueChanged**: Triggered when the value in the control is changed.

---

## Code Examples

### C#

```csharp
using Syncfusion.Windows.Forms.Tools;

public class Form1 : Form
{
    private IntegerTextBox integerTextBox;

    public Form1()
    {
        integerTextBox = new IntegerTextBox();
        integerTextBox.Location = new Point(50, 50);
        integerTextBox.Size = new Size(100, 20);

        this.Controls.Add(integerTextBox);
    }
}
```

---

## Page-level Navigation/TOC

- Essential Tools for Windows Forms
  - IntegerTextBox in Toolbox
  - Designer Approach
  - Through Programmatical Approach

---

## Cross References

See also:
- Other Windows Forms controls in the Syncfusion library.

---

<!-- tags: [tools, integertextbox, windowsforms, designertime, programmatically, syncfusion, 11.4.0.26] keywords: [tools, integer textbox, windows forms, design as drag-drop, design from code] -->
```