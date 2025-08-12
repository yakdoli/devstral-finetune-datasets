```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_012.jpeg
document_name: PivotGrid
page_number: 012
page_id: PivotGrid#page_012
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:03Z
fidelity: lossless
-->

# Getting Started

## Creating PivotGrid through Visual Studio

To create the PivotGrid through Visual Studio:

1. Open the Start menu, and then click Microsoft Visual Studio 2008.
2. On the File menu, click New Project. The New Project dialog box appears as follows.

![New Project Dialog Box](https://example.com/image-url-for-dialog-box.png "Figure 4: New Project Dialog Box")

3. Select WindowsForms Application, and then click OK.
4. Drag the PivotGridControl control from the Toolbox to the Design page.

## Overview
- Describes the initial setup process for creating a PivotGrid application using Visual Studio.
- Guides users through selecting project templates and dragging controls to the design surface.

## Content
### WinForms-specific conventions
The instructions detail how to use Visual Studio 2008 for setting up a PivotGrid project in the Windows Forms environment. This involves creating a new Windows Forms application and adding the PivotGridControl to the design surface.

• **Project Creation**:
    1. Open Microsoft Visual Studio 2008.
    2. Initiate a new project by navigating through the Start menu and selecting "New Project."

• **Template Selection**:
    - Choose "Windows Forms Application" from the available project templates.

• **Design Surface Integration**:
    - Drag and drop the PivotGridControl from the Toolbox onto the Design page to begin building the application interface.

## API Reference (if applicable)
- Namespace: `Syncfusion.Windows.Forms.PivotGrid`
- Class: `PivotGridControl`
- Properties: `DataSource`, `ColumnHeaders`, `RowHeaders`
- Methods: `LoadDataSource()`, `SetEmptyString()`
- Events: `DataBound`, `CellDoubleClick`

## Code Examples (multi-language supported)
```csharp
using Syncfusion.Windows.Forms.PivotGrid;

// Initialize the PivotGridControl
PivotGridControl pivotGrid = new PivotGridControl();
pivotGrid.DataSource = yourDataSource;
pivotGrid.loadDataSource();
```

```vb
Imports Syncfusion.Windows.Forms.PivotGrid

' Initialize the PivotGridControl
Dim pivotGrid As New PivotGridControl()
pivotGrid.DataSource = yourDataSource
pivotGrid.loadDataSource()
```

<!-- tags: PivotGrid, WindowsForms, VisualStudio2008, SyncfusionWinforms, control, properties, methods, events -->
```