```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_111.jpeg
document_name: edit
page_number: 111
page_id: edit#page_111
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:37Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview

- Demonstrates configuration of text wrapping for the `EditControl` in a Windows Forms application.
- Includes setting text area width, offset for wrapped lines, and specifying column boundaries for word wrapping.
- Provides C# and VB.NET examples for implementation.

## Content

### Text Area Configuration for Edit Control

```csharp
// Set the width of the EditControl's text area.
this.editControl1.TextAreaWidth = 300;

// Specifies offset for the wrapped lines.
this.editControl1.WrappedLinesOffset = 10;
```

### [VB.NET]

```vbnet
' Sets the WordWrap mode.
Me.editControl1.WordWrapMode = Syncfusion.Windows.Forms.Edit.Enums.WordWrapMode.WordWrapMargin

' Sets font that is used while calculating the position of the WordWrap column.
Me.editControl1.WordWrapColumnMeasuringFont = New System.Drawing.Font("Arial", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (CType((0), Byte)))

' Specifies column for wrapping text.
Me.editControl1.WordWrapColumn = 125

' Set the width of the EditControl's text area.
Me.editControl1.TextAreaWidth = 300

' Specifies offset for the wrapped lines.
Me.editControl1.WrappedLinesOffset = 10
```

### Illustration Overview

The following illustration shows the Edit Control with the WordWrappingMode and WordWrapType properties set.

### API Reference

#### Properties

- `WordWrapMode`: Configures the wrapping behavior of the text in the EditControl.
- `WordWrapColumn`: Specifies the column at which the text should wrap when the WordWrapMode is set.
- `WordWrapColumnMeasuringFont`: Defines the font used for calculating the wrapping column based on its font metrics.
- `TextAreaWidth`: Sets the maximum width of the text area in the EditControl.
- `WrappedLinesOffset`: Sets the horizontal offset for wrapped lines within the text area.

### Code Examples

- **C#:**
  
  ```csharp
  // Configure word wrapping properties.
  this.editControl1.WordWrapMode = Syncfusion.Windows.Forms.Edit.Enums.WordWrapMode.WordWrapMargin;
  this.editControl1.WordWrapColumnMeasuringFont = new System.Drawing.Font("Arial", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (Convert.ToByte(0)));
  this.editControl1.WordWrapColumn = 125;
  this.editControl1.TextAreaWidth = 300;
  this.editControl1.WrappedLinesOffset = 10;
  ```

- **VB.NET:**
  
  ```vbnet
  ' Configure word wrapping properties.
  Me.editControl1.WordWrapMode = Syncfusion.Windows.Forms.Edit.Enums.WordWrapMode.WordWrapMargin
  Me.editControl1.WordWrapColumnMeasuringFont = New System.Drawing.Font("Arial", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (CType((0), Byte)))
  Me.editControl1.WordWrapColumn = 125
  Me.editControl1.TextAreaWidth = 300
  Me.editControl1.WrappedLinesOffset = 10
  ```

## Page-level Navigation/TOC (if applicable)

- Essential Edit for Windows Forms
  - Text Area Configuration for Edit Control
  - VB.NET Example
  - Illustration Overview
  - API Reference
  - Code Examples

<!-- tags: [EditControl, Windows Forms, TextWrapping, WordWrapMode, VB.NET, C#] keywords: [EditControl, TextAreaWidth, WordWrapColumn, WordWrapMode, WrappedLinesOffset, WordWrapColumnMeasuringFont] -->
```