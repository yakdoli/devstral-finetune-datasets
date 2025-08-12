```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_158.jpeg
document_name: diagram
page_number: 158
page_id: diagram#page_158
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:18:24Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Provides details on properties for controlling node editing in a diagram.
- Explains how to programmatically set these properties using C# and VB.NET.
- Discusses the use of the `EditStyle` properties to customize node editing behavior.

## Content

### EditStyle Properties

| Property             | Description                                                                                   |
|----------------------|-----------------------------------------------------------------------------------------------|
| AllowVertexEdit      | Specifies whether or not to edit the vertex. Default value is **True**.                      |
| HidePinPoint         | Specifies whether to show or hide the PinPoint. Default value is **False**.                 |
| HideRotationhandle   | Specifies whether to show or hide the RotationHandle in order to control the rotation of the node. Default value is **False**. |

### Setting Properties Programmatically

#### C#

```csharp
rect.EditStyle.AspectRatio = true;
rect.EditStyle.DefaultHandleEditMode = HandleEditMode.Resize;
rect.EditStyle.Enabled = true;
rect.EditStyle.AllowVertexEdit = true;
rect.EditStyle.DefaultHandleEditMode = HandleEditMode.Vertex;
rect.EditStyle.HidePinPoint = true;
rect.EditStyle.HideRotationHandle = true;
```

#### VB

```vb
rect.EditStyle.AspectRatio = True
rect.EditStyle.DefaultHandleEditMode = HandleEditMode.Resize
rect.EditStyle.Enabled = True
rect.EditStyle.AllowVertexEdit = True
rect.EditStyle.DefaultHandleEditMode = HandleEditMode.Vertex
rect.EditStyle.HidePinPoint = True
rect.EditStyle.HideRotationHandle = True
```

Thus, in the above code snippets, the properties are set to the Rectangular node (`rect`) created through the code.

## API Reference (if applicable)

### EditStyle Properties

#### AspectRatio
- Type: `bool`
- Description: Controls whether the node maintains aspect ratio during resizing. Default is `True`.
- Default: `True`

#### DefaultHandleEditMode
- Type: `HandleEditMode`
- Description: Specifies the default mode for handle editing. Default is `HandleEditMode.Resize`.
- Default: `HandleEditMode.Resize`

#### Enabled
- Type: `bool`
- Description: Enables or disables node editing. Default is `True`.
- Default: `True`

#### AllowVertexEdit
- Type: `bool`
- Description: Enables or disables vertex editing. Default is `True`.
- Default: `True`

#### HidePinPoint
- Type: `bool`
- Description: Determines whether to show or hide the PinPoint. Default is `False`.
- Default: `False`

#### HideRotationHandle
- Type: `bool`
- Description: Determines whether to show or hide the RotationHandle. Default is `False`.
- Default: `False`

## Code Examples (multi-language supported)

### Implemented Example in C#

Here is an example of how these properties can be set programmatically in a C# application:

```csharp
using Syncfusion.Windows.Forms.Diagram;

// Assume 'rect' is a Rectangular node
DiagramNode rect = new DiagramNode();

// Set the properties using EditStyle
rect.EditStyle.AspectRatio = true;
rect.EditStyle.DefaultHandleEditMode = HandleEditMode.Resize;
rect.EditStyle.Enabled = true;
rect.EditStyle.AllowVertexEdit = true;
rect.EditStyle.DefaultHandleEditMode = HandleEditMode.Vertex;
rect.EditStyle.HidePinPoint = true;
rect.EditStyle.HideRotationHandle = true;

// Add the node to the diagram
Diagram diagram = new Diagram();
diagram.Nodes.Add(rect);
```

### Implemented Example in VB.NET

Here is an example of how these properties can be set programmatically in a VB.NET application:

```vb
Imports Syncfusion.Windows.Forms.Diagram

' Assume 'rect' is a Rectangular node
Dim rect As New DiagramNode()

' Set the properties using EditStyle
rect.EditStyle.AspectRatio = True
rect.EditStyle.DefaultHandleEditMode = HandleEditMode.Resize
rect.EditStyle.Enabled = True
rect.EditStyle.AllowVertexEdit = True
rect.EditStyle.DefaultHandleEditMode = HandleEditMode.Vertex
rect.EditStyle.HidePinPoint = True
rect.EditStyle.HideRotationHandle = True

' Add the node to the diagram
Dim diagram As New Diagram()
diagram.Nodes.Add(rect)
```

In both examples, the properties are set to the Rectangular node (`rect`) created programmatically, demonstrating how to customize the editing behavior of the node in a diagram.

## RAG Annotations

<!-- tags: [WinForms, Diagram, Node Editing, Syncfusion, HandleEditMode, AspectRatio, RotationHandle, VertexEdit, PinPoint] 
keywords: [node, editing, aspect ratio, default handle, mode, rotation handle, pinpoint, vertex edit, control, customize] -->
```