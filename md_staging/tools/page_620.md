```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_620.jpeg
document_name: tools
page_number: 620
page_id: tools#page_620
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:24:33Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Example Code

```csharp
this.afterDropDown = false;
str = "";
}
```

### VB.NET Code

```vb
Private Sub multiColumnComboBox1_SelectedIndexChanged(ByVal sender As Object, ByVal e As System.EventArgs)
    If Me.afterDropDown = True Then
        Dim i As Integer = 1

        Do While i <= Me.multiColumnComboBox1.ListBox.Grid.ColCount
            If i = 1 Then
                ' do nothing for the hidden columns
            Else
                str += Me.multiColumnComboBox1.ListBox.Grid(Me.multiColumnComboBox1.SelectedIndex + 1, i).Text & " "
            End If
            i += 1
        Loop

        Console.WriteLine(str)
        Me.multiColumnComboBox1.Text = str
    End If

    Me.afterDropDown = False
    str = ""
End Sub
```

### Figure 381: Multiple Members displayed in the Text Area

![Multiple Members displayed in the Text Area](https://i.imgur.com/9P66j.png)

## Page-level Navigation/TOC (if applicable)
- [Essential Tools for Windows Forms](#essential-tools-for-windows-forms)
- [Example Code](#example-code)
- [VB.NET Code](#vb.net-code)
- [Figure 381: Multiple Members displayed in the Text Area](#figure-381-multiple-members-displayed-in-the-text-area)

<!-- tags: [winforms, tools] keywords: [windows forms, essential tools, dropdown, multi-column combo box, event handling, text display, selected index changed] -->
```