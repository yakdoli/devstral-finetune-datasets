```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_847.jpeg
document_name: tools
page_number: 847
page_id: tools#page_847
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:30Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```csharp
Me.maskedTextBox1.DataGroups.Add(Me.maskEditDataGroupInfo2)

' Defining maskedEditDataGroupInfo1.
Me.maskedEditDataGroupInfo1.DataGroupAlignment = 
Syncfusion.Windows.Forms.Tools.MaskGroupAlignment.Left
Me.maskedEditDataGroupInfo1.DataGroupName = "One"
Me.maskedEditDataGroupInfo1.DataGroupSize = 3

' Defining maskedEditDataGroupInfo2.
Me.maskedEditDataGroupInfo2.DataGroupAlignment = 
Syncfusion.Windows.Forms.Tools.MaskGroupAlignment.None 
Me.maskedEditDataGroupInfo2.DataGroupName = "Two"
Me.maskedEditDataGroupInfo2.DataGroupSize = 4
```

### Displaying Characters as Substitutes for User Input

We can display different characters as substitutes for the user input. This can be done using the below given properties.

| **MaskedTextBox Properties** | **Description** |
|-------------------------------|------------------|
| Sequentially                 | Indicates whether the control can sequentially display mask characters. |
| PasswordChar                 | Indicates the character to display for password input for single-line edit controls. |

The MaskedTextBox.Sequentially property indicates whether the control can sequentially display mask characters. After setting the Sequentially property to 'True', you can use the PasswordChar property in order to set the character, that is to be displayed as a substitute for the user input.

#### Code Examples

##### C#

```csharp
private void Form1_Load(object sender, System.EventArgs e)
{
    this.maskedTextBox1.Sequentially = true;
    this.maskedTextBox1.PasswordChar = '$';
}
```

##### VB.NET

```vb
Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.maskedTextBox1.Sequentially = True
End Sub
```
<!-- tags: Windows Forms, MaskedTextBox, SyncfusionSDK, MaskGroupAlignment, Substitutes, User Input, Sequential, PasswordChar, C#, VB.NET, version:11.4.0.26 -->
```