```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_023.jpeg
document_name: diagram
page_number: 023
page_id: diagram#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:08:17Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This section provides guidance on creating the Diagram control and other related components such as PaletteGroupBar, PaletteGroupView, Overview, PropertyEditor, and DocumentExplorer in a Windows Forms application.
- It focuses on using the Visual Studio designer to incorporate these controls into a .NET Windows Forms application.

## Content

### 3.2 Essential Diagram in Windows Forms Application
This section helps you to create the Diagram, PaletteGroupBar, PaletteGroupView, Overview, PropertyEditor, and DocumentExplorer controls through the designer and code in a Windows Forms application.

#### 3.2.1 Diagram

##### 3.2.1.1 Creating a Diagram Control through Designer
This section depicts the step-by-step procedure to create a Diagram control through the Visual Studio designer in a .NET Windows Forms application.

To create a Diagram control using the designer:

1. Create a new Windows Forms application.
2. Open the Designer Form window.
3. Drag Diagram from the Toolbox window and drop it to the Designer Form window.

**Figure 10: Dragging Diagram to the Designer**

![](attachment:Syncfusion-Windows-4.0-vs2010-Toolbox-10.2.0...-image.png)

*Drag Diagram and drop it to the designer*

The Diagram control will be added to the designer and its dependent assemblies will be added to the project once you dropped it to the Designer Form window.

## API Reference

### Namespaces and Classes
- **Namespace**: Syncfusion.Windows.Forms.Diagram
- **Class**: Diagram

### Methods
- OnLoad()
- OnPaint()

### Properties
- DiagramDirection
- Title

### Events
- Load
- Paint

## Code Examples

### Example: Adding Diagram Control in Windows Forms

```csharp
using System;
using System.Windows.Forms;
using Syncfusion.Windows.Forms.Diagram;

namespace DiagramExample
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Add Diagram to the form
            Diagram diagram = new Diagram();
            Controls.Add(diagram);
        }
    }
}
```

## Cross References
- Refer to the documentation for more information on PaletteGroupBar, PaletteGroupView, Overview, PropertyEditor, and DocumentExplorer controls.

<!-- tags: [Windows Forms, Diagram, Control, Designer, Visual Studio, .NET] keywords: [Diagram control, PaletteGroupBar, PaletteGroupView, Overview, PropertyEditor, DocumentExplorer, Visual Studio designer, Windows Forms application, .NET] -->
```