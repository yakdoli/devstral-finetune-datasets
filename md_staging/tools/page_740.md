```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_740.jpeg
document_name: tools
page_number: 740
page_id: tools#page_740
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:31:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

**Figure 466: IntegerTextBox created Through Code**

![](image.png)

## Concepts and Features

The following Editors controls (DoubleTextBox, IntegerTextBox, PercentTextBox, and CurrencyTextBox) have been revamped. Click [here](#) to see the details of revamping.

### Display Settings

This section discusses the display settings of the IntegerTextBox control.

The IntegerTextBox provides a list of properties to set the display characteristics associated with the integer value.

| **IntegerTextBox Properties**       | **Description**                                                                 |
|--------------------------------------|--------------------------------------------------------------------------------|
| **NumberGroupSeparator**            | Gets / sets the separator to be used for grouping the digits.                |
| **NumberGroupSizes**                | Specifies the grouping of number digits in the IntegerTextBox.               |
| **NumberNegativePattern**           | Gets / sets the pattern to use when the value is negative.                   |
| **NegativeSign**                    | Gets / sets the sign that is to be used to indicate a negative value.         |

The grouping size of the number digits can be set using the **Int32 Collection Editor**, which will be displayed on selecting the **NumberGroupSizes** property in the property grid.

### VB.NET

```csharp
this.integerTextBox1.NumberGroupSeparator = "/";
this.integerTextBox1.NumberGroupSizes = new int[] { 5 };
this.integerTextBox1.NumberNegativePattern = 2;
```

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Class**: IntegerTextBox
- **Properties**:
  - **NumberGroupSeparator**: Type (string), Default ("")
  - **NumberGroupSizes**: Type (int[]), Default (null)
  - **NumberNegativePattern**: Type (int), Default (0)
  - **NegativeSign**: Type (string), Default ("-")

## Code Examples

### C#

```csharp
this.integerTextBox1.NumberGroupSeparator = "/";
this.integerTextBox1.NumberGroupSizes = new int[] { 5 };
this.integerTextBox1.NumberNegativePattern = 2;
```

### VB.NET

```vb
Me.integerTextBox1.NumberGroupSeparator = "/"
Me.integerTextBox1.NumberGroupSizes = New Integer() { 5 }
Me.integerTextBox1.NumberNegativePattern = 2
```

## Related Topics

- [More about IntegerTextBox](#)
- [General Properties and Methods](#)
- [Handling Events](#)

<!-- tags: [winforms, integer textbox, display settings, properties, negative values, grouping] -->
```