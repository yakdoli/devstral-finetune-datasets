```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_144.jpeg
document_name: diagram
page_number: 144
page_id: diagram#page_144
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:15:34Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- The **SymmetricLayout** class is used for arranging diagrams with specific properties like model, vertical distance, spring factor, spring length, and maximum iteration count.
- Parameters and their descriptions are provided in detail.
- Programming examples in C# and VB.NET demonstrate how to create and assign a **SymmetricLayout** instance to a diagram.

## Content

The Model and Vertical Distance values are passed as parameters to the **SymmetricLayoutManager** class. The parameters and properties of Symmetric Layout Manager are listed below.

### Parameters of Symmetric Layout Manager

| Property               | Description                                                                 |
|------------------------|-------------------------------------------------------------------------------|
| **Model**              | Represents the model of the diagram, which has to be displayed as a directed tree. |
| **VerticalDistance**   | Defines the Graph Rotation angle. It accepts only integer values between 0 - 360. |
| **SpringFactor**       | Gets or sets the spring factor.                                             |
| **SpringLength**       | Defines the spring length.                                                   |
| **MaxIteration**       | Holds the maximum count of iteration.                                        |

Programmatically, the symmetric layout manager instance is created with the respective arguments, assigned to the **LayoutManager**, and updated as follows.

### Code Examples

#### C#

```csharp
SymmetricLayoutManager symmetricLayout = new SymmetricLayoutManager(diagram1.Model, 100);
symmetricLayout.SpringFactor = 0.442;
symmetricLayout.SpringLength = 100;
symmetricLayout.MaxIteration = 500;
this.diagram1.LayoutManager = symmetricLayout;
this.diagram1.LayoutManager.UpdateLayout(null);
```

#### VB.NET

```vb
Dim symmetricLayout As New SymmetricLayoutManager(diagram1.Model, 100)
symmetricLayout.SpringFactor = 0.442
symmetricLayout.SpringLength = 100
symmetricLayout.MaxIteration = 500
Me.diagram1.LayoutManager = symmetricLayout
Me.diagram1.LayoutManager.UpdateLayout(Nothing)
```

### Sample Diagrams

Sample Diagrams are as follows.

<!-- tags: [diagram, symmetriclayout, windowsforms, C#, VB.NET, SymmetricLayoutManager, springfactor, springlength, MaximumIteration] keywords: [diagramManager, verticalDistance, graphRotation, springFactor, springLength, maxIteration, model] -->
```