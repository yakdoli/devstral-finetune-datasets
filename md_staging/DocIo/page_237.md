```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_237.jpeg
document_name: DocIo
page_number: 237
page_id: DocIo#page_237
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:43:53Z
fidelity: lossless
-->

# Essential DocIO

You can specify the style of the border line of the text box by using the `LineStyle` property. It provides the following options:

- Simple
- Double
- ThickThin
- ThinThick
- Triple

## Class Hierarchy

```
FormatBase
    |
    WTextBoxFormat
```

## Public Constructor

| Name | Description |
| --- | --- |
| `WTextBoxFormat.WTextBoxFormat(IWordDocument)` | Initializes a new instance of the `WTextBoxFormat` class. |

## Public Properties

| Name | Description |
| --- | --- |
| `FillColor` | Gets or sets fill color for textbox. |
| `Height` | Gets or sets the textbox height (in points). |
| `HorizontalAlignment` | Gets or sets horizontal alignment of textbox. |
| `HorizontalOrigin` | Gets or sets horizontal origin. |
| `HorizontalPosition` | Gets or sets the horizontal position of textbox (in points). |
| `LineColor` | Gets or sets line color. |
| `LineDashing` | Gets or sets line dashing for textbox. |
| `LineStyle` | Gets or sets linestyle of textbox. |

## API Reference (if applicable)

- **Namespace**: Syncfusion.DocIO
- **Class**: `WTextBoxFormat`
- **Properties**:
  - `FillColor`: Gets or sets the fill color of the textbox. Type: `Color`.
  - `Height`: Gets or sets the height of the textbox. Type: `float`.
  - `HorizontalAlignment`: Gets or sets the horizontal alignment of the textbox. Type: `HorizontalAlign`.
  - `HorizontalOrigin`: Gets or sets the horizontal origin of the textbox. Type: `int`.
  - `HorizontalPosition`: Gets or sets the horizontal position of the textbox. Type: `float`.
  - `LineColor`: Gets or sets the line color of the textbox. Type: `Color`.
  - `LineDashing`: Gets or sets the line dashing style of the textbox. Type: `LineDashing`.
  - `LineStyle`: Gets or sets the line style of the textbox. Type: `LineStyle`.

### Methods
- `WTextBoxFormat():` Initializes a new instance of the `WTextBoxFormat` class.
- `WTextBoxFormat(IWordDocument):` Initializes a new instance of the `WTextBoxFormat` class with a specified `IWordDocument`.

## Code Examples

```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.DLS;

// Example: Creating and configuring a textbox with specific styles
WordDocument document = new WordDocument();
WSection section = document.AddSection();
WTextBox textBox = new WTextBox(section);
textBox.Format.FillColor = Color.LightGray;
textBox.Format.LineColor = Color.Black;
textBox.Format.LineStyle = LineStyle.Double;
textBox.Format.HorizontalPosition = 100;
textBox.Format.HorizontalAlignment = HorizontalAlign.Left;
textBox.Format.Width = 200;
textBox.Format.Height = 100;

// Add more textbox content as needed
document.Save("Textboxes.docx");
```

## Cross References

See also:
- [DocIO User Guide](https://www.syncfusion.com/products/net/docio)
- `IWordDocument`
- `HorizontalAlign`
- `LineDashing`
- `LineStyle`

<!-- tags: [DocIO, WTextBox, WTextBoxFormat, LineStyle, .NET, .NET Framework, .NET Core, Syncfusion Winforms, 11.4.0.26] keywords: [WTextBox, LineStyle, Border, Textbox, Format, Properties, Constructors, DocIO, Syncfusion, Winforms] -->
```