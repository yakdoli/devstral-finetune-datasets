```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_447.jpeg
document_name: grid
page_number: 447
page_id: grid#page_447
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:17:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates setting border settings for the grid using both C# and VB.NET.
- Explains how to specify the color of frozen grid lines using the `FixedLinesColor` property.
- Provides code examples for configuring print properties in the Grid.

## Content

### Setting Border Settings for the Grid

Using C#

```csharp
// Set border settings for the grid.
this.gridControl1.TableStyle.Borders.All = new
GridBorder(BorderStyle.Solid, Color.SteelBlue);
```

Using VB.NET

```vb
' Set border settings for the grid.
Me.gridControl1.TableStyle.Borders.All = New
GridBorder(BorderStyle.Solid, Color.SteelBlue)
```

### Specification of `FixedLinesColor`

- **FixedLinesColor**: Specifies the color of frozen grid lines (for example, row or column headers). Default value is set to `ActiveCaption`.

#### Using C#

```csharp
// Set the color of frozen grid lines.
this.gridControl1.Properties.FixedLinesColor = Color.YellowGreen;
```

#### Using VB.NET

```vb
' Set the color of frozen grid lines.
Me.gridControl1.Properties.FixedLinesColor = Color.YellowGreen
```

A sample demonstrating these properties is available under the following sample installation path:

`<Install Location>\Syncfusion\EssentialStudio\Version Number\Windows\Grid.Windows\Samples\2.0\Grid Properties Demo`

### 4.1.4.13.4.2 Print Properties

The following properties are associated with printing in Grid. They are generally referred to as Print Styles.

## API Reference

甲醛提到的属性未具体涉及API细节，因此这里没有具体的API定义。

## Code Examples

- The document includes examples for configuring grid borders and frozen grid line colors in both C# and VB.NET.

## Page-level Navigation/TOC

- Border Settings for the Grid
- Configuration of `FixedLinesColor`
- Print Properties

## Cross References

- Additional examples may refer to grid customization in other sections of the user guide.

<!-- tags: [Syncfusion, Winforms, Grid, Print Properties, Frozen Grid Lines, Border Settings] keywords: [FixedLinesColor, Grid Borders, Print Styles, C#, VB.NET] -->
```