```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_054.jpeg
document_name: diagram
page_number: 054
page_id: diagram#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:12:00Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates how to create and configure a DiagramExplorer in both C# and VB.
- Highlights the use of the `Syncfusion.Windows.Forms.Diagram.Controls` namespace for diagram functionalities.

## Content

### Example Code in C#

The following code provides a concise example of setting up a `DocumentExplorer` instance and attaching it to a form:

```csharp
//Imports the Diagram control's namespace
using Syncfusion.Windows.Forms.Diagram.Controls;

//Creates a DocumentExplorer instance
DocumentExplorer documentExplorer = new DocumentExplorer();
documentExplorer.Dock = DockStyle.Left;

//Attach a diagram model to documentExplorer
documentExplorer.AttachModel(diagram1.Model);

//Add documentExplorer to the form
this.Controls.Add(documentExplorer);
```

### Example Code in VB

Here is an equivalent example in VB for creating and attaching a `DocumentExplorer` to a form:

```vb
'Imports the Diagram control's namespace
Imports Syncfusion.Windows.Forms.Diagram.Controls

'Creates a DocumentExplorer instance
Dim documentExplorer As New DocumentExplorer()
documentExplorer.Dock = DockStyle.Left

'Attach a diagram model to documentExplorer
documentExplorer.AttachModel(Diagram1.Model)

'Add documentExplorer to the form
Me.Controls.Add(documentExplorer)
```

### Explanation

1. **Imports**: The code imports the required namespace for the Diagram control.
2. **Instance Creation**: A `DocumentExplorer` instance is created and its docking property is set to `DockStyle.Left` to dock the explorer on the left side of the form.
3. **Model Attachment**: A diagram model is attached to the `DocumentExplorer` to display relevant content within it.
4. **Control Addition**: The `DocumentExplorer` is added to the form's controls collection to make it visible.

## API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Diagram.Controls`
- **Class**: `DocumentExplorer`
  - Method: `AttachModel(Model model)`
    - Description: Attaches a diagram model to the `DocumentExplorer`.
  - Property: `Dock`
    - Description: Determines the docking style of the control within the form.
    - Type: `DockStyle`

## Code Examples (Referenced Above)

### C# Code

```csharp
using Syncfusion.Windows.Forms.Diagram.Controls;
...
DocumentExplorer documentExplorer = new DocumentExplorer();
documentExplorer.Dock = DockStyle.Left;
documentExplorer.AttachModel(diagram1.Model);
this.Controls.Add(documentExplorer);
```

### VB Code

```vb
Imports Syncfusion.Windows.Forms.Diagram.Controls
...
Dim documentExplorer As New DocumentExplorer()
documentExplorer.Dock = DockStyle.Left
documentExplorer.AttachModel(Diagram1.Model)
Me.Controls.Add(documentExplorer)
```

## RAG Annotations
<!-- tags: [Diagram, Windows Forms, DocumentExplorer, DockStyle, Model, AttachModel, Syncfusion Windows Forms Diagram Controls] keywords: [DiagramExplorer, DockStyle, AttachModel, Diagram, Windows Forms, C#, VB, Control Configuration, Model Attachment] -->
```