```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_771.jpeg
document_name: tools
page_number: 771
page_id: tools#page_771
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:45Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Null Value Settings

There are various settings that can be applied to the PercentTextBox control, when the value of the control is set to 'Null'. These settings are illustrated below.

| PercentTextBox Properties | Description |
|---------------------------|-------------|
| AllowNull                | Specifies if the NullString will be used when the value is Null. |
| NullString               | Specifies the string to be displayed when the DecimalValue is Null. |
| NullFormat               | Returns the NumberFormatInfo object for the null display. |

### C#
```csharp
this.percentTextBox1.NullString = "Null Value";
this.percentTextBox1.AllowNull = true;
```

### VB.NET
```vbnet
Me.percentTextBox1.NullString = "Null Value"
Me.percentTextBox1.AllowNull = True
```

![Figure: Null String Set](null_value_set.png)

### Min and Max Value Settings

The minimum and maximum values of the IntegerTextBox can be set using the below given properties.

| PercentTextBox Properties | Description |
|---------------------------|-------------|
| MaxValue                 | Gets / sets the maximum value that can be set through the PercentTextBox. The default value is set to '1'. |
| MinValue                 | Gets / sets the minimum value that can be set through the PercentTextBox. The default |
```