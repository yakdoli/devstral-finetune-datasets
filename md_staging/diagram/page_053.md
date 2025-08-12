```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: diagram
page_number: 053
page_id: diagram#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:10:58Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Describes the step-by-step procedure to create a DocumentExplorer control programmatically in a .NET Windows Forms application.
- Highlights the necessary Syncfusion assemblies to be added for utilizing the DocumentExplorer control.
- Includes an overview of properties and settings relevant to configuring the DocumentExplorer control.

## Content

### 3.2.6.2 Creating a DocumentExplorer Control through Code
This section shows the step-by-step procedure to create a DocumentExplorer control programmatically in a .NET Windows Forms application.

To create a DocumentExplorer control using code:

1. Create a new Windows Forms application.

2. Add the following basic dependent Syncfusion assemblies to the project:
   - Syncfusion.Core.dll
   - Syncfusion.Diagram.Base.dll
   - Syncfusion.Diagram.Windows.dll
   - Syncfusion.Shared.Base.dll

3. Create a DocumentExplorer control using the following code.

---

### Figure: Designer Form Window Added with DocumentExplorer Control
![Image of Designer Form Window Added with DocumentExplorer Control](#)

*Figure 27: Designer Form Window Added with DocumentExplorer Control*

### Detailed Steps for Creating a DocumentExplorer Control

#### Step 1: Create a New Windows Forms Application
- Initialize a new Windows Forms project in Visual Studio.
- Ensure that the project is set up to use the .NET framework compatible with the required Syncfusion assemblies.

#### Step 2: Add the Required Syncfusion Assemblies
- Download and reference the following Syncfusion assemblies from the official source:
   - Syncfusion.Core.dll
   - Syncfusion.Diagram.Base.dll
   - Syncfusion.Diagram.Windows.dll
   - Syncfusion.Shared.Base.dll
- Add these DLLs to the project's references to enable the use of Syncfusion’s Diagram features.

#### Step 3: Programmatically Create the DocumentExplorer Control
- Use the following code to create and initialize the DocumentExplorer control in your Windows Forms application.
- Attach properties, such as `LineColor`, `Location`, and `Nodes`, to configure the control's appearance and functionality.

### Notes:
- The `DocumentExplorer` control provides an easy way to display hierarchical data in tree-like structures.
- Ensure that all required dependencies and configurations are correctly set to avoid runtime errors.

### Cross References
- See also: Documentation for additional properties and methods related to the DocumentExplorer control.
- Reference: Overview of Syncfusion’s Windows Forms Diagram control for further customization options.

<!-- tags: [WinForms, DocumentExplorer, Control, SyncfusionDiagram, Version11.4.0.26] keywords: [DocumentExplorer, Windows Forms, Syncfusion, Control, Programmatically, Assembly] -->
```