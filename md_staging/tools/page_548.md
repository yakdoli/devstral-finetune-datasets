```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_548.jpeg
document_name: tools
page_number: 548
page_id: tools#page_548
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:19:57Z
fidelity: lossless
--> 

## Essential Tools for Windows Forms

### Overview

- Configuring the ComboBox dropdown to utilize a `TreeView` control as its dropdown content.
- Associating the `PopupControl` property of `ComboBox` to the `TreeView` instance.
- Tips for setups involving the interaction between the combo and treeview controls.

### Content

#### Configuring TreeView as Pop-Up in ComboDropDown

1. **Step 1: Associating TreeView as Pop-Up**
   - Set the `ComboDropDown`'s `PopupControl` property to the desired `TreeView` instance.
   
   **Figure 337: Associating TreeView control as Pop-Up of ComboDropDown Control**
   ![TreeView Association](ComboDropDown_Training_DOCUMENTATION_IMAGE.JPG)

2. **Note:** It is possible to include code to set up the interaction between the combo and the treeview control. Refer to [Setting Interaction between ComboDropDown and TreeView](#setting-interaction).

##### Setting Interaction between ComboDropDown and TreeView

Include code to handle interactions between the `ComboDropDown` and `TreeView` to manage selection and navigation.

---

### See also

- [Concepts and Features](#concepts-and-features)
- [Through Code](#through-code)

#### 3.5.5.1.2.2 Through Code

1. **Step 1: Drag and Drop TreeView**
   - Drag and drop the `TreeView` control to be used in the drop-down portion of the `ComboDropDown` control.

2. **Step 2: Include the Required Namespace**

   **C#**
   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```

   **VB.NET**
   ```vb
   Imports Syncfusion.Windows.Forms.Tools
   ```

---

### API Reference

- **Properties**
  - `PopupControl`: Reference to the `TreeView` instance used as the dropdown for `ComboDropDown`.
  - `NumberOnly`: Boolean to restrict the dropdown to show only numeric data.
  - `WritableDatabase`: Boolean to determine if the dropdown data is editable.

### Code Examples

**C# Example: Setting up the TreeView as Pop-Up**

```csharp
using Syncfusion.Windows.Forms.Tools;

public class Form1 : Form
{
    public Form1()
    {
        // Create and initialize TreeView control
        TreeView treeNode = new TreeView();
        treeNode.Nodes.Add("Node 0");
        treeNode.Nodes[0].Nodes.Add("Node 1");
        treeNode.Nodes[0].Nodes[0].Nodes.Add("Node 2");

        // Create and initialize ComboDropDown control
        ComboDropDown comboDropDown = new ComboDropDown();
        comboDropDown.PopupControl = treeNode;

        // Add controls to the form
        this.Controls.Add(comboDropDown);
    }
}
```

---

### Cross References

**See also:**

- [Concepts and Features](#concepts-and-features)
- [Through Code](#through-code)

---

<!-- tags: [Syncfusion Winforms, ComboBox, TreeView, PopUpControl, Windows Forms] keywords: [ComboDropDown, TreeView, Pop-Up, Windows Forms, Essential Tools, Development Guide] -->
```