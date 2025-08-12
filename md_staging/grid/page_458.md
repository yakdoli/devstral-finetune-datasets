<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_458.jpeg
document_name: grid
page_number: 458
page_id: grid#page_458
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:17:33Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- This page discusses properties related to scroll bars in the Essential Grid for Windows Forms, focusing on toggling between standard and Office 2007 scroll bars and specifying their style.

## Content

### Figure 176: VerticalThumbTrack = "True"

![Figure 176: VerticalThumbTrack = "True"](image.png)

#### Office2007ScrollBars

Toggles between standard and Office 2007 scroll bars. Default value is set to `false`.

The following code examples can be used to set this property:

1. **Using C#**

   ```csharp
   // Toggle to Office 2007 scroll bar.
   this.gridControl1.Office2007ScrollBars = true;
   ```

2. **Using VB.NET**

   ```vb
   ' Toggle to Office 2007 scroll bar.
   Me.gridControl1.Office2007ScrollBars = True
   ```

#### Office2007ScrollBarsColorScheme

Specifies the style for Office 2007 scroll bars. Default value is set to `Blue`.

The following code examples can be used to set this property:

1. **Using C#**

   ```csharp
   // [C#]
   ```

## API Reference

### Properties

- **Office2007ScrollBars**
  - Type: `bool`
  - Description: Toggles between standard and Office 2007 scroll bars.
  - Default: `false`

- **Office2007ScrollBarsColorScheme**
  - Type: `ColorScheme`
  - Description: Specifies the style for Office 2007 scroll bars.
  - Default: `Blue`

## Code Examples

### Example: Enabling Office 2007 Scroll Bars

#### C#

```csharp
this.gridControl1.Office2007ScrollBars = true;
```

#### VB.NET

```vb
Me.gridControl1.Office2007ScrollBars = True
```

### Example: Setting Scroll Bar Style

#### C#

```csharp
this.gridControl1.Office2007ScrollBarsColorScheme = SfGrid.Office2007Colors.Green;
```

#### VB.NET

```vb
Me.gridControl1.Office2007ScrollBarsColorScheme = SfGrid.Office2007Colors.Green
```

## RAG Annotations
<!-- tags: [grid, windows forms, scroll bars, Office 2007, Syncfusion] keywords: [Office2007ScrollBars, Office2007ScrollBarsColorScheme, scroll bar style, C#, VB.NET] -->