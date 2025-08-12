```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_288.jpeg
document_name: edit
page_number: 288
page_id: edit#page_288
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:11:25Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Code Examples

### C#

```csharp
private void editControl_TextChanged(object sender, System.EventArgs e)
{
    // Do not start the timer as long as characters are being typed.
    if (this.timer1.Enabled == true) {
        this.timer1.Stop();
    }
    this.timer1.Start();
}

private void timer1_Tick(object sender, System.EventArgs e)
{
    this.ValidateText();
    
    this.timer1.Stop();
}

private void ValidateText()
{
    // Perform your validation logic here.
    MessageBox.Show(" Text Validated ");
}
```

### VB.NET

```vb
Private Sub editControl_TextChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles EditControl1.TextChanged
    ' Do not start the timer as long as characters are being typed.
    If Me.timer1.Enabled = True Then
        Me.timer1.Stop()
    End If
    Me.timer1.Start()
End Sub

Private Sub timer1_Tick(ByVal sender As Object, ByVal e As System.EventArgs) Handles timer1.Tick
    Me.ValidateText()
    
    Me.timer1.Stop()
End Sub

Private Sub ValidateText()
    ' Perform your validation logic here.
    MessageBox.Show(" Text validated ")
End Sub
```

## API Reference

### Methods

- `editControl_TextChanged`: Handles the `TextChanged` event of the `EditControl1` control.
- `timer1_Tick`: Handles the `Tick` event of the `timer1` control.
- `ValidateText`: Performs the validation logic after a delay.
- `MessageBox.Show`: Displays a message box with the specified text.

## Download Links

<a href="http://www.syncfusion.com/downloads">Download WinForms 11.4.0.26</a>

```html

<!-- tags: [syncfusion, windows forms, controls, edit control, timer, validation, C#, VB.NET, api, version: 11.4.0.26] -->
```