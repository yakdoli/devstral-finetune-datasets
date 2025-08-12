```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_120.jpeg
document_name: edit
page_number: 120
page_id: edit#page_120
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:56Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

### Content

A sample which demonstrates the above feature is available in the following sample installation path.

- \My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Edit.Windows\Samples\2.0\Advanced Editor Functions\BordersDemo

#### Figure 40: Text Borders in Edit Control

```csharp
{
    case "Dash" :
        this.borderstyle = FrameBorderStyle.Dash;
        break;
    case "DotDash" :
        this.borderstyle = FrameBorderStyle.DashDot;
        break;
    case "Dot" :
        this.borderstyle = FrameBorderStyle.Dot;
        break;
    case "Solid" :
        this.borderstyle = FrameBorderStyle.Solid;
        break;
    case "Wave" :
        this.borderstyle = FrameBorderStyle.Wave;
        break;
    case "None" :
        this.borderstyle = FrameBorderStyle.None;
        break;
}
```

### See Also

- Underlines, Wavelines and StrikeThrough

## 4.4.12.3 Encoding Text

Edit Control facilitates saving the contents of a file in any desired encoding and new line style. This can be accomplished by using the below given method.

### Edit Control Method: SaveFile

| Edit Control Method | Description          |
|---------------------|----------------------|
| SaveFile           | Saves content to the specified file. |

<!-- tags: [Essential Edit, Windows Forms, Text Borders, Encoding Text, SaveFile] keywords: [Essential Edit, Windows Forms, Text Borders, Encoding Text, SaveFile, FrameBorderStyle, Dash, DotDash, Dot, Solid, Wave, None] -->
```