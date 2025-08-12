```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: diagram
page_number: 049
page_id: diagram#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:10:43Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Describes the functionality of the PropertyEditor control in Syncfusion Diagram.
- Highlights creating a PropertyEditor control both in the designer and through code.
- Explains step-by-step procedures for programmatic creation of PropertyEditor.

## Content

### WinForms Designer Form with PropertyEditor Control

#### Figure 25: Designer Form Window with PropertyEditor Control
![Diagram showing the Designer Form Window with highlighted PropertyEditor, Smart Tag, and Diagram references.](image)

### 3.2.5.2 Creating a PropertyEditor Control through Code

#### Overview
This section shows the step-by-step procedure to create a PropertyEditor control programmatically in a .NET Windows Forms application.

#### Steps to Create a PropertyEditor Control Using Code:

1. **Create a new Windows Forms application.**
2. **Add the following basic dependent Syncfusion assemblies to the project:**
   - Syncfusion.Core.dll
   - Syncfusion.Diagram.Base.dll
   - Syncfusion.Diagram.Windows.dll
   - Syncfusion.Shared.Base.dll
3. **Create a PropertyEditor control using the following code.**

#### Code Example:
```csharp
// Example C# Code for creating PropertyEditor control
using Syncfusion.Windows.Forms.Diagram.Controls;
using Syncfusion.Windows.Forms.Diagram;
using System.Windows.Forms;

public class MyForm : Form
{
    public MyForm()
    {
        var diagram = new Diagram();
        var propertyEditor = new PropertyEditor();
        
        // Attach the diagram to the PropertyEditor
        propertyEditor.Dia = diagram;
        
        // Add the PropertyEditor to the form
        this.Controls.Add(propertyEditor);
    }
}
```

### Additional Notes
- Ensure all required Syncfusion assemblies are referenced in the project.
- The PropertyEditor control should be attached to a Diagram object for proper functionality.

### See also:
- Documentation on using Syncfusion Diagram controls in Windows Forms applications.
- Reference to related控件

## API Reference

### Classes
- **PropertyEditor**: A control used to edit properties of diagram objects.

### Methods/Properties
- **Diagram:** Gets or sets the Diagram object the PropertyEditor is attached to.
- **Dock:** Gets or sets the docking behavior of the PropertyEditor.

## RAG Annotations
<!-- tags: [syncfusion, winforms, diagram, propertyeditor, creating controls, code example] keywords: [PropertyEditor, Syncfusion.Windows.Forms.Diagram.Controls, Syncfusion.Diagram, C#, windows forms] -->
``` 
