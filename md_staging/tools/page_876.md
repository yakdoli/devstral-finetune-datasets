```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_876.jpeg
document_name: tools
page_number: 876
page_id: tools#page_876
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:40:05Z
fidelity: lossless
-->

## Foreground Color

The foreground color of the control can be set using the properties given below.

| NumericUpDownExt Property | Description |
|---------------------------|-------------|
| ForeColor                 | Gets / sets the foreground color of the spin box (also known as an up-down control). |

### Setting Foreground Color

[C#]

```csharp
this.numericUpDownExt1.ForeColor = System.Drawing.Color.DodgerBlue;
```

[VB.NET]

```vb
Me.numericUpDownExt1.ForeColor = System.Drawing.Color.DodgerBlue
```

![Figure 556: Foreground Color set for the NumericUpDownExt Control](https://i.imgur.com/5OjSv.png)

### Using Foreground Color to Indicate Negative Values

**3.5.8.9.3.3.2.1**  
Applying Foreground Color to Negative ValuesIt is a good behavior in a NumericUpDownExt control to indicate negative values using a separate color. The IntegerTextBox and DoubleTextBox controls also exhibit the same behavior.

![Figure 557: Derived NumericUpDownExt showing Negative Values in Different Color](https://i.imgur.com/5OjSv.png)

**To add this feature to the NumericUpDown control, we need to derive the control. For this, we need to include the below given code snippet in the derived class.**

[C#]

```csharp
class NumericudownextDerived : NumericUpDownExt
{
    private IntegerTextBox itb = new IntegerTextBox();
    public integerupdow()
    {
```

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations
<!-- tags: [foreground color, numericupdownext, syncfusion winforms, numericudownextderived] keywords: [numericupdownext, forecolor, negative values, derived control] -->
```