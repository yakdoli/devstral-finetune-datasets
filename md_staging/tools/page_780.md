```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_780.jpeg
document_name: tools
page_number: 780
page_id: tools#page_780
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:08Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Overflow Indicator ToolTip Text Set

The following properties are related to the visibility and functionality of the overflow indicator.

| Property | Description |
|----------|-------------|
| ShowOverflowIndicator | Gets / sets overflow indicator visibility. |
| ShowOverflowIndicatorToolTip | Indicates whether to show the overflow indicator tooltip. |

#### Example Code: C#

```csharp
this.percentTextBox1.OverflowIndicatorToolTipText = "Overflow";
this.percentTextBox1.ShowOverflowIndicator = true;
this.percentTextBox1.ShowOverflowIndicatorToolTip = true;
```

#### Example Code: VB.NET

```vb
Me.percentTextBox1.OverflowIndicatorToolTipText = "Overflow"
Me.percentTextBox1.ShowOverflowIndicator = True
Me.percentTextBox1.ShowOverflowIndicatorToolTip = True
```

**Figure 496: Overflow Indicator ToolTip Text Set**

![Figure 496: Overflow Indicator ToolTip Text Set](image.png)

### Banner Text Support

The PercentTextBox control can display banner text in the text field at runtime. A **BannerTextProvider Component** should be available for this purpose. Additionally, we need to set the following properties to make the banner text feature effective:

- **AllowNull**: Set to `true` to allow the text field to accept null values.
- **NullString**: Set to `""` (empty string) to define the string to display when the field is null.
- **Text**: Set to `""` (empty string) to initialize the text field.

#### Example Code: C#

```csharp
this.percentTextBox1.AllowNull = true;
this.percentTextBox1.NullString = "";
this.percentTextBox1.Text = "";
```

#### Example Code: VB.NET

```vb
Me.percentTextBox1.AllowNull = True
Me.percentTextBox1.NullString = ""
Me.percentTextBox1.Text = ""
```

## References

- **BannerTextProvider Component**: This component is essential for displaying banner text within the PercentTextBox control.
- **Properties**:
  - **AllowNull**: Determines whether the text field can accept null values.
  - **NullString**: Specifies the string to display when the field contains null.
  - **Text**: The initial or current text displayed in the text field.

<!-- tags: [overflow indicator, tooltip, banner text, percenttextbox, windows forms] keywords: [overflow indicator visibility, tooltip text, null string, banner text provider, percenttextbox properties] -->
```