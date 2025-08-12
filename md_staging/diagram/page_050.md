```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: diagram
page_number: 050
page_id: diagram#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:11:42Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates the integration and use of the PropertyEditor control in a Windows Forms application.
- Explains how to create, configure, and add the PropertyEditor to the form using both C# and VB.NET.

## Content

### Creating and Configuring the PropertyEditor

#### C#
```csharp
//Imports the Diagram control's namespace
using Syncfusion.Windows.Forms.Diagram.Controls;

//Creates a PropertyEditor instance
PropertyEditor propertyEditor = new PropertyEditor();
propertyEditor.Dock = DockStyle.Left;
propertyEditor.ShowCombo = true;

//Set the diagram reference to propertyEditor
propertyEditor.Diagram = diagram1;

//Add propertyEditor to the form
this.Controls.Add(propertyEditor);
```

#### VB.NET
```vb
'Imports the Diagram control's namespace
Imports Syncfusion.Windows.Forms.Diagram.Controls

'Creates a PropertyEditor instance
Dim propertyEditor As New PropertyEditor()
propertyEditor.Dock = DockStyle.Left
propertyEditor.ShowCombo = True

'Set the diagram reference to propertyEditor
propertyEditor.Diagram = Diagram1

'Add propertyEditor to the form
Me.Controls.Add(propertyEditor)
```

### Explanation
- **Imports**: Both the C# and VB.NET code samples import the necessary namespace for the Syncfusion Diagram control.
- **PropertyEditor Instance**: A new `PropertyEditor` instance is created.
- **Docking**: The `DockStyle.Left` property is set, ensuring the PropertyEditor is docked to the left side of the form.
- **Combo Box**: The `ShowCombo` property is set to `true` to display a combo box in the PropertyEditor.
- **Diagram Reference**: The `Diagram` property is set to reference the specific diagram (e.g., `diagram1` or `Diagram1`).
- **Adding to the Form**: The `Controls.Add` method is used to add the `PropertyEditor` to the form.

## API Reference

### Members
- **PropertyEditor**: The control that provides an interface for editing properties of diagram objects.
- **DockStyle**: Enumerates possible values for positioning controls within a form (e.g., `DockStyle.Left`).
- **Diagram**: Property that associates the PropertyEditor with a specific diagram.
- **ShowCombo**: Boolean property that determines whether a combo box is displayed in the PropertyEditor.

## Code Examples

### C#
The C# example demonstrates creating and configuring a `PropertyEditor` and adding it to the form. It includes:
- Importing the necessary namespace.
- Creating the `PropertyEditor` instance.
- Setting up docking and display properties.
- Binding the `PropertyEditor` to the diagram.
- Adding the `PropertyEditor` to the form controls.

### VB.NET
The VB.NET example is functionally identical to the C# example, with equivalent syntax for creating and integrating the `PropertyEditor` into the Windows Forms application.

## Page-level Navigation/TOC (if applicable)
- None specified on this page.

## Cross References
- See also: Other sections related to Windows Forms controls and Diagram customization.

### RAG Annotations
<!-- tags: [Syncfusion, Windows Forms, Diagram, PropertyEditor] keywords: [PropertyEditor, DockStyle, Diagram, ShowCombo, Controls.Add] -->
```