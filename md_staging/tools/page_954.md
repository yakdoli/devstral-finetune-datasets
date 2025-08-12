```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_954.jpeg
document_name: tools
page_number: 954
page_id: tools#page_954
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:45:01Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Illustrates how to create a `CheckBoxAdv` control via the designer.
- Step-by-step guide including adding the control to the form and setting properties.
- Includes examples of both designer-based and code-based creation.

## Through Designer

### Content

The following steps illustrate how to create a `CheckBoxAdv` control through designer.

- Create or open a Windows Forms project.
- Add a `CheckBoxAdv` control from the toolbox onto the form by dragging and dropping it onto the form or double-clicking the control.

![](./image.png)
*Figure 612: CheckBoxAdv in Toolbox*

- Set the desired properties for the control through the `Property` grid.
- Run the application.

![](./image-1.png)
*Figure 613: CheckBoxAdv created Through Designer*

### See Also

- **Through Code**
- **3.5.11.1.2.2 Through Code**

The `CheckBoxAdv` control can be created programmatically as detailed below:

---

## Code Examples

### WinForms-specific conventions
- For steps on how to create and customize `CheckBoxAdv` controls programmatically, consider the following example:

```csharp
// Programmatically creating a CheckBoxAdv control
using Syncfusion.Windows.Forms.Tools;
using System.Windows.Forms;

public class CheckBoxAdvExample
{
    public void CreateCheckBoxAdv()
    {
        // Create a new CheckBoxAdv control
        CheckBoxAdv checkBoxAdv = new CheckBoxAdv();
        
        // Set properties programmatically
        checkBoxAdv.Text = "Sample CheckBoxAdv";
        checkBoxAdv.Size = new System.Drawing.Size(200, 50);
        checkBoxAdv.Location = new System.Drawing.Point(50, 50);
        
        // Add the CheckBoxAdv to the form
        this.Controls.Add(checkBoxAdv);
    }
}
```

...

## References

- All rights reserved. The guide is provided by Syncfusion for the Windows Forms product version 11.4.0.26.

<!-- tags: [syncfusion, windows forms, checkboxadv, designer, control, toolbox, property grid, programmatically, tools] keywords: [checkboxadv, designer, syncfusion windows forms, toolbox, property, control, programmatically] -->
```