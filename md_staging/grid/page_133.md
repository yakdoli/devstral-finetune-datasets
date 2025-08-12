```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_133.jpeg
document_name: grid
page_number: 133
page_id: grid#page_133
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:45:26Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This section provides a step-by-step procedure to create a Grid control through the Designer and through a programmatical approach in a .NET application.
- Highlights the use of the GridControl and its properties for customization.

## Content

### 4.1.1 Creating Grid Control

This section will provide the step-by-step procedure to create a Grid control through designer and through programmatical approach in a .NET application.

#### 4.1.1.1 Through Designer

To make the task of designing the Grid control easier on a cell level, a new Designer Editor has been added. With the editor, the grid can be modified and saved (and loaded) to XML formatted files, or Soap formatted templates. There is also no longer a Toggle Interactive Mode design verb that was present in versions prior to 4.1.

**To add a Grid Control to the Application**

Following steps illustrate how to add a Grid control to your application.

1. **Drag the GridControl component from the toolbox onto the form.**

   ![Grid Control](Form1.png "Figure 70: Grid Control")
   
2. **To edit the cell level properties of the grid (and also general Grid control properties), right-click anywhere in the Grid control and select Edit.**

## API Reference

- **GridControl**: The main component for creating grid controls in Windows Forms.
- **Designer Editor**: A tool for modifying GridControl properties in a visually friendly manner.

## Code Examples

Basic Code Example (C#):
```csharp
using Syncfusion.Windows.Forms.Grid;
// Drag and drop GridControl from toolbox onto your WinForms designer.
// Additional code for further customization can follow.
```

<!-- tags: [GridControl, Designer Editor, Syncfusion Windows Forms, .NET application] keywords: [Grid, control, designer, programming, application, tutorial, step-by-step, Windows Forms] -->
```