```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_459.jpeg
document_name: grid
page_number: 459
page_id: grid#page_459
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:09Z
fidelity: lossless
-->

## Overview
- The document focuses on setting the style for Office 2007 scroll bars and defining scroll behavior when moving through frozen cells in a Windows Forms Grid.
- It includes both C# and VB.NET code examples for configuring scroll bar styles and scroll tips.
- The document explains how to set properties such as `Office2007ScrollBarsColorScheme`, `ScrollFrozen`, and `ScrollTipFormat`.

## Content

### Setting the Style for Office 2007 Scroll Bars

#### C#

```csharp
// Set the style for Office 2007 scroll bar.
this.gridControl1.Office2007ScrollBarsColorScheme = Office2007ColorScheme.Blue;
```

#### VB.NET

```vb
' Set the style for Office 2007 scroll bar.
Me.gridControl1.Office2007ScrollBarsColorScheme = Office2007ColorScheme.Blue
```

### ScrollFrozen Property

- **ScrollFrozen**: Defines scroll behavior when the user moves the current cell with arrow keys into frozen cells. The default value is `true`.
- The following code examples can be used to set this property.

#### C#

```csharp
// Define scroll behavior in frozen cells.
this.gridControl1.ScrollFrozen = true;
```

#### VB.NET

```vb
' Define scroll behavior in frozen cells.
Me.gridControl1.ScrollFrozen = True
```

### ScrollTipFormat Property

- **ScrollTipFormat**: Specifies the text to be displayed in the ScrollTip window with a placeholder for the scroll position.
- The following code examples can be used to set this property.

#### C#

```csharp
// Set the text to be displayed in the ScrollTip window with a placeholder for scroll position.
```

## API Reference (if applicable)

### Properties
- **Office2007ScrollBarsColorScheme**: Gets or sets the style of the Office 2007 scroll bars.
- **ScrollFrozen**: Gets or sets the scroll behavior when moving within frozen cells.
- **ScrollTipFormat**: Gets or sets the text displayed in the ScrollTip window.

## Code Examples

### Setting the Office 2007 Scroll Bar Style
```csharp
// C#
this.gridControl1.Office2007ScrollBarsColorScheme = Office2007ColorScheme.Blue;

' VB.NET
Me.gridControl1.Office2007ScrollBarsColorScheme = Office2007ColorScheme.Blue
```

### Configuring Scroll Behavior in Frozen Cells
```csharp
// C#
this.gridControl1.ScrollFrozen = true;

' VB.NET
Me.gridControl1.ScrollFrozen = True
```

### Customizing ScrollTip Text
```csharp
// C#
this.gridControl1.ScrollTipFormat = "Scroll position: {0}";
```

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Grid, ScrollBars, FrozenCells, ScrollTips, C#, VB.NET] keywords: [Office2007ScrollBarsColorScheme, ScrollFrozen, ScrollTipFormat, GridControl] -->
```