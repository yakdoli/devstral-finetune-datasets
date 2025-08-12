```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_587.jpeg
document_name: tools
page_number: 587
page_id: tools#page_587
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:22:46Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the setup and usage of a custom control derived from PercentComboBoxAdv in both C# and VB.NET.
- Guides through the initialization, event handling, and data population for the control.
- Explains how to display selected values in Percent format upon the SelectedValueChanged event.

## Content
```csharp
System.EventHandler(this.PercentComboBoxAdv1_SelectedValueChanged);
```

```vbnet
[VB.NET]

' Do the initialization.
Private PercentComboBoxAdv1 As PercentComboBoxAdv
Me.PercentComboBoxAdv1 = New PercentComboBoxAdv()
Me.PercentComboBoxAdv1.Location = New System.Drawing.Point(Me.Width/4, Me.Height/3)
Me.Controls.Add(Me.PercentComboBoxAdv1)
Me.PercentComboBoxAdv1.SelectedValueChanged+= New System.EventHandler(Me.PercentComboBoxAdv1_SelectedValueChanged)
```

2. **You can populate the derived control with values using the `Items` property.**

```csharp
[C#]

private void Form1_Load(object sender, System.EventArgs e)
{
    // Populating the control with items.
    this.PercentComboBoxAdv1.Items.Add (78.9);
    this.PercentComboBoxAdv1.Items.Add (67.9);
    this.PercentComboBoxAdv1.Items.Add (75.9);
    this.PercentComboBoxAdv1.Items.Add (23.6);
    this.PercentComboBoxAdv1.Items.Add (34.7);
    this.PercentComboBoxAdv1.Items.Add (56.8);
}
```

```vbnet
[VB.NET]

Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)

    ' Populating the control with items.
    Me.PercentComboBoxAdv1.Items.Add (78.9)
    Me.PercentComboBoxAdv1.Items.Add (67.9)
    Me.PercentComboBoxAdv1.Items.Add (75.9)
    Me.PercentComboBoxAdv1.Items.Add (23.6)
    Me.PercentComboBoxAdv1.Items.Add (34.7)
    Me.PercentComboBoxAdv1.Items.Add (56.8)

End Sub
```

3. **In the `SelectedValueChanged` event, you can display the corresponding selected value in Percent Format.**

## API Reference
- Namespace: `Syncfusion.Windows.Forms.Tools`
- Class: `PercentComboBoxAdv`
- Event: `SelectedValueChanged`
- Method: `Items.Add`

## Code Examples
### C#
```csharp
private void PercentComboBoxAdv1_SelectedValueChanged(object sender, EventArgs e)
{
    var selectedValue = PercentComboBoxAdv1.SelectedValue;
    MessageBox.Show($"Selected Value: {selectedValue:P}");
}
```

### VB.NET
```vbnet
Private Sub PercentComboBoxAdv1_SelectedValueChanged(ByVal sender As Object, ByVal e As EventArgs)
    Dim selectedValue As Object = PercentComboBoxAdv1.SelectedValue
    MessageBox.Show($"Selected Value: {selectedValue:P}")
End Sub
```

## Page-level Navigation/TOC
- [ ] Initialization
- [ ] Data Population
- [ ] Event Handling

## Cross References
- See also: percent formatting in custom controls, event handling in windows forms, Syncfusion control usage.

<!-- tags: [Syncfusion, WinForms, PercentComboBoxAdv, Windows Forms Controls, Event Handling, Data Population] keywords: [PercentComboBoxAdv, SelectedValueChanged, Items.Add, Percent Format, Initialization, Data Population, Event Handling, Windows Forms] -->
```
