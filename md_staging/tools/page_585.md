```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_585.jpeg
document_name: tools
page_number: 585
page_id: tools#page_585
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:22Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Feature Comparison Table

| Feature                          | Column 1 | Column 2    | Column 3    | Column 4 |
|-----------------------------------|----------|--------------|--------------|----------|
| AutoComplete                     |          |              |              |          |
| Drop-Down List- Change Selection by Keys | No          | Yes:1        | Yes:2        | No          |
| Drop-Down List- Change Selection by Mouse Move | No          | No          | No          | No          |
| Drop-Down Close by Enter Key    | Yes:1    | No          | No          | No          |
| Drop-Down Close by Escape Key   | No          | No          | No          | No          |
| Drop-Down Close by Click       | Yes:1    | Yes:2        | Yes:3        | No          |
| Losing Focus                    | Yes:2 (in DropDownStyle.DropDownList (editable) mode only) | No          | No          | Yes:1        |
| Changing Text Property in Code   | Yes:1    | No          | No          | No          |



---

### Populating the ComboBoxAdv

#### 3.5.5.2.4.1 Populating the ComboBoxAdv

**To Populate the ComboBoxAdv containing predefined percent values with other percent values and allowing the text field of the ComboBoxAdv to behave like PercentTextBox**

1. Derive a new class from the existing Syncfusion ComboBoxAdv. Override as shown below and give a new definition for TextBox.

#### Code Example

```csharp
// Derive a new class from the existing Syncfusion ComboBoxAdv.
public class PercentComboBoxAdv : Syncfusion.Windows.Forms.Tools.ComboBoxAdv
{
    // Overrides the internal TextBox.
    protected override TextBox CreateTextBox()
    {
        Syncfusion.Windows.Forms.Tools.PercentTextBox ptb = new
```

---

## Page-level Navigation/TOC

- **3.5.5.2.4.1 Populating the ComboBoxAdv**

## Cross References

See also:
- Syncfusion.Windows.Forms.Tools.ComboBoxAdv
- Syncfusion.Windows.Forms.Tools.PercentTextBox

<!-- tags: [Syncfusion Winforms, ComboBoxAdv, PercentTextBox, Version 11.4.0.26] keywords: [Populating, ComboBoxAdv, Percentage values, TextBox, editable mode, Syncfusion] -->
```