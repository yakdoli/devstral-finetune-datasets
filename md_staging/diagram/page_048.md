```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_048.jpeg
document_name: diagram
page_number: 048
page_id: diagram#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:09:45Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Guide on integrating the PropertyEditor control into a Windows Forms application.
- Instructions on dragging the PropertyEditor control from the toolbox to the designer.
- Explanation of the addition of dependent assemblies upon dragging the control to the Designer Form window.

## Content

### Using the PropertyEditor Control in a Diagram

The following image (Figure 24) illustrates the process of dragging the PropertyEditor control to the designer:

#### Figure 24: Dragging PropertyEditor to the Designer

- **Toolbox**: The image shows the Toolbox in Visual Studio with various Syncfusion controls listed.
- **PropertyEditor**: A specific control highlighted with a tooltip indicating its version and purpose.
  - **Tooltip**: PropertyEditor control for nodes in a Diagram.
  - **Action**: The arrow points to "Drag PropertyEditor and drop it to the designer."
  
The PropertyEditor control will be added to the designer and its dependent assemblies will be added to the project once you drop it to the Designer Form window.

## Code Examples

The process of adding the PropertyEditor control programmatically can be illustrated with the following C# code example:

```csharp
using System.Windows.Forms;
using Syncfusion.Windows.Forms.Diagram.Controls;

public class PropertyEditorExample : Form
{
    public PropertyEditorExample()
    {
        InitializeComponent();

        // Create an instance of PropertyEditor
        PropertyEditor propertyEditor = new PropertyEditor();

        // Add PropertyEditor to the form
        this.Controls.Add(propertyEditor);
    }

    private void InitializeComponent()
    {
        // Designer-generated code...
    }
}
```

This example demonstrates how to programmatically add the PropertyEditor control to a Windows Forms application.

## API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Diagram.Controls`
- **Class**: `PropertyEditor`
- **Properties** (relevant to the context):
  - `Version` - Specifies the version of the PropertyEditor control.
  - `Diagram` - Indicates the diagram instance to which the PropertyEditor is associated.

## Cross References

- For more information on other components and controls, refer to the Syncfusion WinForms documentation.
- See also: DiagramControl, DiagramNode, and other related controls in the syncfusion-sdk documentation.

<!-- tags: [winforms, propertyeditor, designer, diagram, syncfusion, windows forms] keywords: [PropertyEditor, DiagramControl, Designer Form, dependent assemblies, Windows Forms, syncfusion-sdk] -->
```