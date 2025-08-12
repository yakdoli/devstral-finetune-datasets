```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_209.jpeg
document_name: edit
page_number: 209
page_id: edit#page_209
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:07:26Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Introduction to the Selection Margin feature in the Edit Control.
- Explanation of how the Selection Margin allows users to select content by clicking on the corresponding margin area.
- Customization options for the Selection Margin using specific properties.

## Content

### Selection Margin Feature
The Selection Margin is a thin vertical strip along the left side of the Edit Control that enables you to select the contents of the entire line on the Edit Control by simply clicking on the corresponding selection margin area of the line.

### Properties for Customizing the Selection Margin
The `ShowSelectionMargin` property allows you to show or hide this selection margin. The following properties are used to customize the margin:

| Edit Control Property                  | Description                                    |
|-----------------------------------------|------------------------------------------------|
| `SelectionMargin ForegroundColor`      | Gets or sets the foreground color of the selection margin. |
| `SelectionMargin BackgroundColor`      | Gets or sets the background color of the selection margin. |
| `SelectionMargin Width`                | Sets the width of the selection margin.       |

### Code Examples

#### C#
```csharp
this.editControl1.SelectionMargin ForegroundColor = Color.Gray;
this.editControl1.SelectionMargin BackgroundColor = Color.IndianRed;
this.editControl1.SelectionMargin Width = 100;
```

#### VB.NET
```vb
Me.editControl1.SelectionMargin ForegroundColor = Color.Gray
Me.editControl1.SelectionMargin BackgroundColor = Color.IndianRed
Me.editControl1.SelectionMargin Width = 100
```

## API Reference

### Properties
- `SelectionMargin ForegroundColor`: Gets or sets the foreground color of the selection margin.
- `SelectionMargin BackgroundColor`: Gets or sets the background color of the selection margin.
- `SelectionMargin Width`: Sets the width of the selection margin.

## Code Examples (if applicable)
No additional code examples provided.

## Page-level Navigation/TOC
- Selection Margin Feature
- Properties for Customizing the Selection Margin
- Code Examples

## Cross References
No cross references provided.

## RAG Annotations
<!-- tags: windows-forms, edit-control, selection-margin, customization, foreground-color, background-color, width -->
<!-- keywords: selection margin, edit control, foreground color, background color, width, showselectionmargin, properties -->
```