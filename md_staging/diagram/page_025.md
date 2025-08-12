```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_025.jpeg
document_name: diagram
page_number: 025
page_id: diagram#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:09:03Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Demonstrates creating and configuring a Diagram control in a Windows Forms application using C# and VB.NET.
- Shows how to enable scroll bars, set size, and position the Diagram control.
- Focuses on initializing the Diagram control and configuring its basic properties.

## Content

The following examples illustrate how to create and configure a Diagram control in a Windows Forms environment.

### Using C#

#### Code Example
```csharp
// Imports the Diagram control’s namespaces
using Syncfusion.Windows.Forms.Diagram.Controls;
using Syncfusion.Windows.Forms.Diagram;

// Create an instance
Diagram diagram = new Diagram();

// Enable scroll bars
diagram.HScroll = true;
diagram.VScroll = true;

// Sizing the diagram
diagram.Size = new Size(400, 400);
// Positioning the diagram
diagram.Location = new Point(20, 5);
```

### Using VB.NET

#### Code Example
```vb
' Imports the Diagram control’s namespaces
Imports Syncfusion.Windows.Forms.Diagram
Imports Syncfusion.Windows.Forms.Diagram.Controls

' Create an instance
Dim diagram As New Diagram()

' Enable Scrollbars
diagram.HScroll = True
diagram.VScroll = True

' Sizing the diagram
diagram.Size = New Size(400, 400)
' Positioning the diagram
```

## Code Examples (multi-language supported)

The provided code examples demonstrate the initialization and basic configuration of the Diagram control in both C# and VB.NET. These examples cover essential aspects such as enabling scroll bars, setting the control’s size, and positioning it within the form.

### Key Properties Configured

- **HScroll**: Enables horizontal scrolling for the Diagram.
- **VScroll**: Enables vertical scrolling for the Diagram.
- **Size**: Sets the dimensions of the Diagram control.
- **Location**: Positions the Diagram control within the form.

## RAG Annotations

<!-- tags: [Syncfusion, WinForms, DiagramControl, HorizontalScroll, VerticalScroll, Size, Position] keywords: [Diagram config, Scroll bars, Control sizing, Control positioning, C# implementation, VB.NET implementation] -->
```