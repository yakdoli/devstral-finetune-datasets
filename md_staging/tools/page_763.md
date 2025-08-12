```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_763.jpeg
document_name: tools
page_number: 763
page_id: tools#page_763
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:07Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the implementation of data binding for integer values using PercentTextBox controls.
- Explains the display settings for percentage values inPercentTextBox, including number grouping and formatting.

## Content

### Example Code: Data Binding for Integer Values in PercentTextBox

#### C# Code
```csharp
this.integerTextBox1.NullString = "";
this.integerTextBox1.AllowNull = true;
this.integerTextBox1.DataBindings.Add("BindableValue", boundView, "IntegerField");
```

#### VB.NET Code
```vb
Me.integerTextBox1.NullString = ""
Me.integerTextBox1.AllowNull = True
Me.integerTextBox1.DataBindings.Add("BindableValue", boundView, "IntegerField")
```

### 3.5.8.5 PercentTextBox

The `PercentTextBox` is a textbox-derived control that can display double data type values in percentage form.

#### Description
- **Figure 481: PercentTextBox Control**
  ![PercentTextBox Control](image_url)
- The `PercentTextBox` is derived from the Windows Forms framework textbox control.
- It supports displaying and collecting percentage values.
- It handles user keyboard input and percent formatting.
- It uses the globalization features of the .NET platform to provide locale-specific formatting.

### 3.5.8.5.1 Features

#### PercentTextBox Features
- Used to display percentage values.
- Provides the following features:

##### Display Settings
- The `display` settings involve setting the separator to be used to group numbers and the group size.
- Involves setting the pattern to be used for positive and negative numbers and the symbol to indicate the percent.

#### Summary
The `PercentTextBox` control is an essential tool for working with percentage values in Windows Forms applications. It provides advanced formatting and globalization capabilities, ensuring that percentage values are displayed and entered in a user-friendly manner.

---

## API Reference (if applicable)
- **Namespace:** Known namespaces related to windows forms.
- **Class:** PercentTextBox
- **Members:** Properties and methods specific toPercentTextBox.

## Code Examples (multi-language supported)
- Demonstrates data binding and display settings forPercentTextBox in both C# and VB.NET.

## Page-level Navigation/TOC (if applicable)
- Provides a structured overview ofPercentTextBox features and usage examples.

## Cross References
See also: [related controls and features in Syncfusion Winforms].

## RAG Annotations
<!-- tags: [Syncfusion Winforms, PercentTextBox, DataBinding, DisplaySettings] keywords: [PercentTextBox, NumberFormatting, Localization] -->
```