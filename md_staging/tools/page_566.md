```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_566.jpeg
document_name: tools
page_number: 566
page_id: tools#page_566
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:12Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The section discusses the ComboBoxAdv control, its programmatically created example, and the concepts and features related to its usage.

## Content

### Figure 349: ComboBoxAdv Created Programmatically

![Figure 349: ComboBoxAdv Created Programmatically](https://via.placeholder.com/600x400?text=Figure+349%3A+ComboBoxAdv+Created+Programmatically)

#### See Also

- **Concepts and Features**
- `3.5.5.2.3 Concepts and Features`

The following topics will help you become more familiar in using the ComboBoxAdv control.

#### 3.5.5.2.3.1 ComboBoxAdv

The `ComboBoxAdv` control has a textbox which is the edit portion of the control and a dropdown. This section will discuss these components in detail in the below topics.

##### 3.5.5.2.3.1.1 TextBox

The `ComboBoxAdv` control has properties which change the appearance and behavior of the textbox or the edit portion of the control.

### Text Appearance

The below properties customize the text in the `ComboBoxAdv` control.

#### ComboBoxAdv TextBox Properties

| ComboBoxAdv TextBox Properties | Description |
|----------------------------------|-------------|
| Text                            | Sets text for the textbox. The text can be set to null to clear the text in the textbox. |
| TextAlign                       | Sets the alignment of the text in the textbox. |
| ForeColor                       | Sets the foreground color for the text entered in the edit portion of the control. |

## API Reference

### Properties

- **Text**: Sets text for the textbox. The text can be set to null to clear the text in the textbox.
- **TextAlign**: Sets the alignment of the text in the textbox.
- **ForeColor**: Sets the foreground color for the text entered in the edit portion of the control.

## Code Examples

The `ComboBoxAdv` control can be customized using various properties to alter its appearance and behavior.

#### C# Example

```csharp
ComboBoxAdv comboBox = new ComboBoxAdv();
comboBox.Text = "Sample Text";
comboBox.TextAlign = HorizontalAlignment.Center;
comboBox.ForeColor = Color.Red;
```

#### VB.NET Example

```vb
Dim comboBox As New ComboBoxAdv()
comboBox.Text = "Sample Text"
comboBox.TextAlign = HorizontalAlignment.Center
comboBox.ForeColor = Color.Red
```

## Cross References

See also:

- **Concepts and Features**
- `3.5.5.2.3 Concepts and Features`
- `3.5.5.2.3.1 ComboBoxAdv`
- `3.5.5.2.3.1.1 TextBox`

### Text Appearance

The following properties customize the text in the `ComboBoxAdv` control.

<!-- tags: [ComboBoxAdv, Text Appearance, text properties, WinForms, Syncfusion, text formatting, control customization] keywords: [ComboBoxAdv, textbox, dropdown, text, text alignment, text color, customization, properties, appearance] -->
```