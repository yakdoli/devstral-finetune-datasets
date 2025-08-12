```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_069.jpeg
document_name: edit
page_number: 069
page_id: edit#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:58:23Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- This page discusses the use of Underline, StrikeThrough, and formatting options in the Edit Control.
- It covers how to specify underline styles, including Color, Weight, and Underline parameters.
- Demonstrates the functionality of different underline styles and strike-through operations on text.

## Content

### Underline Parameters
The `LineColor`, `Weight`, and `Underline` parameters are used to specify the type of underlining to be used.

#### Code Example
```csharp
private System.Windows.Forms.RadioButton radioButton1;
private System.Windows.Forms.RadioButton radioButton2;
private System.Windows.Forms.RadioButton radioButton3;
private System.Windows.Forms.GroupBox groupBox1;
private System.Windows.Forms.GroupBox groupBox2;
```

**Figure 18: Text with Double Solid Style, Double Dot Style, Wave Style Underlines**

A sample which demonstrates this feature is available in the below location.

### ..\My Documents\Syncfusion\EssentialStudio\[Version Number]\Windows\Edit.Windows\Samples\2.0\Advanced Editor Functions\UnderlinesDemo

### Striking Through Text

The `StrikeThrough` method allows you to perform strikethrough operation on the text contained in the Edit Control. This is a very useful feature in denoting text that was deleted from the original document or highlighting offending code. You can also specify any custom color for the strikethrough line.

#### C# Example
```csharp
// Strikeout the current line.
this.editControl1.StrikeThrough(this.editControl1.CurrentLine, Color.IndianRed);

// Strikeout the selected text.
this.editControl1.StrikeThrough(this.editControl1.Selection.Top, this.editControl1.Selection.Bottom, Color.Navy);

// Strikeout the text in the specified text range.
this.editControl1.StrikeThrough(startCoordinatePoint, endCoordinatePoint, Color.Aqua);
```

#### VB.NET Example
```vb
' Strikeout the current line.
```

---

## API Reference

### Methods
- `StrikeThrough`:
  - **Parameters**:
    - `lineNumberOrRange`: Specifies the line or range of lines for the strikethrough effect.
    - `color`: Specifies the color of the strikethrough line.

### Properties
- `LineColor`: Specifies the color of the underline.
- `Weight`: Specifies the thickness of the underline.
- `Underline`: Specifies the type of underline style.

---

## Code Examples

#### C#
```csharp
this.editControl1.StrikeThrough(this.editControl1.CurrentLine, Color.IndianRed);
this.editControl1.StrikeThrough(this.editControl1.Selection.Top, this.editControl1.Selection.Bottom, Color.Navy);
this.editControl1.StrikeThrough(startCoordinatePoint, endCoordinatePoint, Color.Aqua);
```

#### VB.NET
```vb
' Strikeout the current line.
```

---

<!-- tags: [Essential Edit, Windows Forms, Underline, StrikeThrough, Syncfusion Winforms, Version 11.4.0.26] keywords: [underline styles, text formatting, strike-through, text decoration, underlining, strikethrough lines, advanced editor features, text control, edit control, line color, weight, text range] -->
```