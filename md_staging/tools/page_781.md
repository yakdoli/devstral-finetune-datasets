```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_781.jpeg
document_name: tools
page_number: 781
page_id: tools#page_781
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:33:31Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

A sample which demonstrates the Text, Text Align and Overflow Indicator features of the PercentTextBox control is available in the below sample installation path.

### Sample Installation Path
- `..My Documents\Syncfusion\EssentialStudio\VersionNumber\Windows\Tools.Windows\Samples\2.0\Editors Package\EditorControls`

### 3.5.8.5.3.5 Appearance Settings: Background Settings

The Background settings of the PercentTextBox control are discussed below.

#### Background Color

The background color of the control can be set using the properties given below.

| PercentTextBox Properties                  | Description                                                                           |
|--------------------------------------------|---------------------------------------------------------------------------------------|
| BackColor                                  | Specifies the background color of the component.                                    |
| ReadOnlyBackColor                         | Specifies the backcolor to be used when the control is in the ReadOnly mode.        |

#### Code Examples

##### C#

```csharp
this.percentTextBox1.BackColor = System.Drawing.Color.LightCyan;
this.percentTextBox1.ReadOnly = true;
this.percentTextBox1.ReadOnlyBackColor = System.Drawing.Color.Pink;
```

##### VB.NET

```vb
Me.percentTextBox1.BackColor = System.Drawing.Color.LightCyan
Me.percentTextBox1.[ReadOnly] = True
Me.percentTextBox1.ReadOnlyBackColor = System.Drawing.Color.Pink
```

### Figure 497: PercentTextBox with Background Color Set
\[IMAGE: PercentTextBox with a light blue background displaying "25%".\]

## API Reference

- **BackColor**: Specifies the background color of the component.
- **ReadOnlyBackColor**: Specifies the backcolor to be used when the control is in the ReadOnly mode.

## Code Examples

See the C# and VB.NET examples above for setting the background color of the PercentTextBox control.

## Page-level Navigation/TOC

### Structure of the Page
1. **Introduction**
   - Sample Installation Path
   - Overview of Appearance Settings
   - Focus on Background Settings

2. **Background Color**
   - Explanation of Properties
   - Code Examples (C# and VB.NET)

3. **Visual Example**
   - Figure 497: PercentTextBox with Background Color Set

## Cross References

- **Related Controls**: Refer to the documentation for other features and controls of the PercentTextBox in the Editors Package.
- **Sample Path**: Ensure to access the sample at the specified installation path for practical demonstrations.

## RAG Annotations

<!-- tags: [PercentTextBox, Windows Forms, Syncfusion, Background Color, ReadOnly, C#, VB.NET] keywords: [PercentTextBox control, Background settings, ReadOnly mode, appearance settings, Color.LightCyan, Color.Pink] -->
```