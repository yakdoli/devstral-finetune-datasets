```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_451.jpeg
document_name: grid
page_number: 451
page_id: grid#page_451
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:17:37Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- The page explains how to configure print properties for the Grid control in C# and VB.NET.
- It includes examples for setting `PrintVertLines` and `CenterHorizontal` properties for grid printing.
- Demonstrates how to align grids horizontally during printing.

## Content

[C#]

```csharp
// Specify if vertical lines of the grid should be printed.
this.gridControl.Properties.PrintVertLines = true;
```

### 2. Using VB.NET

[VB.NET]

```vbnet
' Specify if vertical lines of the grid should be printed.
Me.gridControl1.Properties.PrintVertLines = True
```

- **CenterHorizontal**—specifies if a grid should be centered horizontally while printing.

The following code examples illustrate how to set this property in the Grid control.

### C#

```csharp
// Specify if the grid should be centered horizontally while printing.
this.gridControl.Properties.CenterHorizontal = true;
```

### VB.NET

```vbnet
' Specify if the grid should be centered vertically while printing.
Me.gridControl1.Model.Properties.CenterHorizontal = False
```

A sample demonstrating these properties is available under the following sample installation path:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0\Print
```

### 4.1.4.13.4.3 Scroll Bar Properties

Essential Grid provides support to control the functionalities and appearance of the grid scroll bars.

## Page-level Navigation/TOC (if applicable)

- Concepts and examples related to configuring grid print options.
- Instructions on setting properties such as `PrintVertLines` and `CenterHorizontal`.
- Path to sample project for demonstration.

## Cross References

See also:
- Print options in Syncfusion Grid controls.
- Miscellaneous grid control properties.

<!-- tags: [syncfusion, winforms, grid, print, scrollbars, version:11.4.0.26] keywords: [printVertLines, centerHorizontal, gridControl, print options, scroll bar properties, Syncfusion Winforms] -->
```