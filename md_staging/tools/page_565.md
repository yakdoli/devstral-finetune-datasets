```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_565.jpeg
document_name: tools
page_number: 565
page_id: tools#page_565
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:20:13Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Using ComboBoxAdv

#### Imports

```csharp
Imports Syncfusion.Windows.Forms.Tools
```

#### Creating and Adding ComboBoxAdv to the Form

```csharp
[C#]
private Syncfusion.Windows.Forms.Tools.ComboBoxAdv comboBoxAdv1;
this.comboBoxAdv1 = new ComboBoxAdv();
```

```vbnet
[VB.NET]
Private comboBoxAdv1 As Syncfusion.Windows.Forms.Tools.ComboBoxAdv
Me.comboBoxAdv1 = New ComboBoxAdv()
```

#### Adding Items to ComboBoxAdv

Items can be added to `ComboBoxAdv` through the `Items.Add` method, similar to the Windows `ComboBox` control.

```csharp
[C#]
this.comboBoxAdv1.Items.Add(100);
this.comboBoxAdv1.Items.Add(200);
this.comboBoxAdv1.Items.Add(300);
```

```vbnet
[VB.NET]
Me.comboBoxAdv1.Items.Add(100)
Me.comboBoxAdv1.Items.Add(200)
Me.comboBoxAdv1.Items.Add(300)
```

#### Adding ComboBoxAdv to the Form

Finally, add `ComboBoxAdv` to the form using the `Controls.Add` method.

```csharp
[C#]
this.Controls.Add(this.comboBoxAdv1);
```

```vbnet
[VB.NET]
this.Controls.Add(this.comboBoxAdv1);
```
```