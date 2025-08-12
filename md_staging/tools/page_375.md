```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_375.jpeg
document_name: tools
page_number: 375
page_id: tools#page_375
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:09:45Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```markdown
e.ClickedButton.ButtonAlign = ButtonAlignment.Left
```
**End Sub**

## Border Events

The below table lists the events that are raised for border changes.

| ButtonEdit Properties         | Description                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------|
| Border3DStyleChanged         | Raised when Border3DStyle property of ButtonEdit control is changed.                  |
| BorderSidesChanged           | Raised when BorderSides property of ButtonEdit control is changed.                   |

### C#

```csharp
private void buttonEdit1_Border3DStyleChanged(object sender, EventArgs e)
{
    Console.WriteLine("3D border styles is changed");
}

private void buttonEdit1_BorderSidesChanged(object sender, EventArgs e)
{
    Console.WriteLine(" Border sides is changed");
}
```

### VB.NET

```vb
Private Sub buttonEdit1_Border3DStyleChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("3D border styles is changed")
End Sub

Private Sub buttonEdit1_BorderSidesChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" Border sides is changed")
End Sub
```

## ButtonEditChildButton Events

The below table lists the events that are available for the ButtonEdit Child Buttons control.

<!-- tags: [Syncfusion, Windows Forms, ButtonEdit, Border Events, ButtonEditChildButton Events, Border3DStyleChanged, BorderSidesChanged, C#, VB.NET] keywords: [border changes, button edit properties, event handling, 3D border styles, border sides] -->
```