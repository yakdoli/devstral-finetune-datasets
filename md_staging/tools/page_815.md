```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_815.jpeg
document_name: tools
page_number: 815
page_id: tools#page_815
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:37:36Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
Me.currencyTextBox1.BorderSides = System.Windows.Forms.Border3DSide.All
```

![Figure: $125.12](image.png)

**Figure 517:** `BorderStyle = "FixedSingle"; Border3DStyle = "Flat"; BorderColor = "Magenta"`

### Setting Different Colors for Currency Values

We can set different colors for the different set of currency values, i.e., Colors can be set for positive currency values, negative currency values, and zero values by using the below properties. We can draw the background of Currency TextBox with colors when it is in read-only mode by using `ReadOnlyBackColor`.

| CurrencyTextBox Properties | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| PositiveColor              | Specifies Forecolor when the current value is positive.                |
| NegativeColor              | Specifies Forecolor when the current value is negative.                |
| ReadOnlyBackColor          | Specifies the color to be used for back color when the control is read only. Set `ReadOnly` to `true`. |
| ZeroColor                  | Specifies Forecolor when the current value is Zero.                    |

#### Code Examples

**[C#]**

```csharp
this.currencyTextBox1.PositiveColor = System.Drawing.Color.Blue;
this.currencyTextBox1.NegativeColor = System.Drawing.Color.Red;
this.currencyTextBox1.ReadOnlyBackColor = System.Drawing.Color.Linen;
this.currencyTextBox1.ZeroColor = System.Drawing.Color.DarkOrange;
```

**[VB.NET]**

```vb
Me.currencyTextBox1.PositiveColor = System.Drawing.Color.Blue
Me.currencyTextBox1.NegativeColor = System.Drawing.Color.Red
Me.currencyTextBox1.ReadOnlyBackColor = System.Drawing.Color.Linen
Me.currencyTextBox1.ZeroColor = System.Drawing.Color.DarkOrange
```

<!-- tags: [WinForms, CurrencyTextBox, BorderProperties, ColorSettings, ReadOnlyBackColor, PositiveColor, NegativeColor, ZeroColor] keywords: [currency, textbox, borderstyle, border3dstyle, bordercolor, colors, positive, negative, zero, read-only] -->
```