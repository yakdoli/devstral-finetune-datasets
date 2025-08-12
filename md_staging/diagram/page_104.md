```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_104.jpeg
document_name: diagram
page_number: 104
page_id: diagram#page_104
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:13:13Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

The Property Editor in Essential Diagram displays properties of the currently selected object(s) in the diagram. It is a windows forms control that can be added to the Visual Studio .NET toolbox. It also allows the users to set or modify various properties of the objects or the model. The Property Editor provides an easy interface, to set and view various property settings.

## Overview
- The Property Editor displays properties for selected objects in the diagram.
- It is a windows forms control integrated into the Visual Studio .NET toolbox.
- Allows users to modify properties of objects and the diagram model.
- Provides an easy interface for setting and viewing properties.

## Content

### Property Editor Properties

The following table lists the properties of the Property Editor. The important property of the Property Editor is the **Diagram** property.

| Property       | Description                                                                                                             |
|----------------|-------------------------------------------------------------------------------------------------------------------------|
| Diagram        | It contains a reference to the diagram that this property editor is attached to. The property editor receives events from the diagram when the current selection changes. It updates the currently displayed object in the property editor. |
| Product Name  | Gets the product name of the assembly containing the control.                                                          |
| ProductVersion | Gets the version of the assembly containing the control.                                                              |
| PropertyGrid   | Gets the reference to the PropertyGrid object contained by this property editor.                                      |
| ShowCombo      | Determines if combo box is visible.                                                                                  |

#### Setting Properties Programmatically

Programmatically, the properties can be set as follows.

```csharp
this.propertyEditor.PropertyGrid.BackColor = System.Drawing.Color.FromArgb(((System.Byte)(227)), ((System.Byte)(239)), ((System.Byte)(255)));
this.propertyEditor.PropertyGrid.CommandsBackColor = System.Drawing.Color.FromArgb(((System.Byte)(227)), ((System.Byte)(239)), ((System.Byte)(255)));
this.propertyEditor.PropertyGrid.CommandsForeColor= System.Drawing.Color.MidnightBlue;
this.propertyEditor.PropertyGrid.Font = new System.Drawing.Font("Arial", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));
this.propertyEditor.PropertyGrid.HelpBackColor = System.Drawing.Color.FromArgb(((System.Byte)(227)), ((System.Byte)239)), ((System.Byte)(255)));
```

## RAG Annotations
<!-- tags: [SyncfusionWinforms, PropertyEditor, DiagramControl, WindowsForms, Properties, PropertyGrid] keywords: [Property Editor, Diagram, PropertyGrid, Windows Forms, control properties, programmatically, essential diagram] -->
```