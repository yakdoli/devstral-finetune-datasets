```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_605.jpeg
document_name: tools
page_number: 605
page_id: tools#page_605
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:22:47Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```csharp
Syncfusion.Windows.Forms.Tools.MultiColumnComboBox();
this.Controls.Add(this.multiColumnComboBox1);
```

```vb
Private multiColumnComboBox1 As
Syncfusion.Windows.Forms.Tools.MultiColumnComboBox
Me.multiColumnComboBox1 = New
Syncfusion.Windows.Forms.Tools.MultiColumnComboBox()

Me.Controls.Add(Me.multiColumnComboBox1)
```

After creating `MultiColumnComboBox`, you can bind them using a data source. Refer to [Databinding](Databinding).

### See also

- **Concepts and Features**

#### 3.5.5.4.3 Concepts and Features

The following topics will help you become more familiar with using the `MultiColumnComboBox` control.

#### 3.5.5.4.3.1 Multiple Columns

The `MultiColumnComboBox` control is a `ComboBoxAdv` control with multiple columns. Multiple columns will be enabled by default. To disable this, set the `MultiColumn` property to false. We can display the headers for the columns using the `ShowColumnHeader` property.

![Control displaying Multiple Columns](https://www.example.com/figure374.png)

---

Figure 374: Control displaying Multiple Columns

---

<!-- tags: [Syncfusion, WinForms, MultiColumnComboBox, ComboBoxAdv, MultiColumn] keywords: [MultiColumnComboBox, ComboBoxAdv, WinForms, multiple columns, column headers, data binding, Databinding, Syncfusion Winforms, version 11.4.0.26] -->
```