```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_412.jpeg
document_name: chart
page_number: 412
page_id: chart#page_412
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:40:04Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### 4.6.9 Axis Title

Essential Chart provides properties to set custom titles for the axes. Set the title text for an axis using the `Title` property. Customize this text using `TitleColor` and `TitleFont` properties.

| Chart Axis Property | Description |
|----------------------|-------------|
| `TitleColor`        | Sets the color for the title text of the axis. |
| `TitleFont`         | Sets the font style for the title text.      |

#### C#

```csharp
// Sets custom title for x-axis.
this.chartControl1.PrimaryXAxis.Title = "x-axis";
this.chartControl1.PrimaryXAxis.TitleColor = Color.Red;
this.chartControl1.PrimaryXAxis.TitleFont = new Font("Arial", 10);
// Set custom title for y-axis in the similar method.
```

#### VB

```vb
' Sets custom title for x-axis.
Me.chartControl1.PrimaryXAxis.Title = "x-axis"
Me.chartControl1.PrimaryXAxis.TitleColor = Color.Red
Me.chartControl1.PrimaryXAxis.TitleFont = New Font("Arial", 10)
' Set custom title for y-axis in the similar method.
```

#### Multiline Chart Axes Title

You can now wrap the axes titles and display them as multiline text. Set multiline title text in the `Axis.Title` property through the designer as follows. Press ENTER key to begin a new line. Press CTRL+ENTER to set the text entered.

---

<!-- tags: [Syncfusion Winforms, Chart, Axis Title, Essential Chart] keywords: [chart, axis, title, titlecolor, titlefont, multiline, text, designer] -->
```