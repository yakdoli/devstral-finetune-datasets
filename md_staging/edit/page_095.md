```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_095.jpeg
document_name: edit
page_number: 095
page_id: edit#page_095
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:59:22Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Explains how to customize the appearance of indentation guidelines and bracket highlighting in Windows Forms.
- Details properties to specify custom colors for indentation and bracket highlighting.
- Demonstrates the difference between bracket highlighting with and without indentation guidelines.

## Content

### Bracket Highlighting with Indentation Guidelines

```csharp
public Form1()
{
    // Required for Windows Form Designer support
    InitializeComponent();
    
    this.editControl1.LoadFile("..\..\Form1.cs");
    this.editControl1.IndentLineColor = Color.Khaki;
}
```

**Figure 26: Bracket Highlighting with Indentation Guidelines**

### Bracket Highlighting without Indentation Guidelines

```csharp
public Form1()
{
    // Required for Windows Form Designer support
    InitializeComponent();
    
    this.editControl1.LoadFile("..\..\Form1.cs");
    this.editControl1.IndentLineColor = Color.Khaki;
}
```

**Figure 27: Bracket Highlighting without Indentation Guidelines**

### Customizing the Appearance

It is possible to specify custom colors for the indentation guidelines and bracket highlighting blocks by using the below given properties.

#### Edit Control Properties

| Edit Control Property                   | Description                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------|
| `IndentLineColor`                      | Specifies the color of the indent line.                                   |
| `IndentBlockHighlightingColor`         | Specifies the color of the indent block start and end.                    |
| `IndentationBlockBackgroundBrush`      | Gets / sets the brush for the indentation block background.               |
| `IndentationBlockBorderColor`          | Specifies the color of the indentation block border line.                |

## Page-level Navigation/TOC
- Bracket Highlighting with Indentation Guidelines
- Bracket Highlighting without Indentation Guidelines
- Customizing the Appearance

## Cross References
- See also: Windows Forms Designer support, indentation guidelines, bracket highlighting.

<!-- tags: [product, windows forms, edit control, customization, indentation, bracket highlighting] keywords: [indentation guidelines, bracket highlighting, custom colors, windows forms] -->
```