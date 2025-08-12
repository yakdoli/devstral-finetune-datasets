```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_054.jpeg
document_name: HTMLUI
page_number: 054
page_id: HTMLUI#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:06:11Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```csharp
// HTML element MouseEnter event definition.
private void textElement_MouseEnter( object sender, EventArgs e )
{
    Console.WriteLine("MouseDown Event Handled");
}
```

```vbnet
' Object declaration for the textarea element in the html document rendered in the control.
Private Sub htmluiControl1_LoadFinished(ByVal sender As Object, ByVal e As System.EventArgs)
    Dim hmlelements As Hashtable = Me.htmluiControl1.Document.GetElementsByIdHash()
    Dim textElement As BaseElement = CType(IIf(TypeOf hmlelements("text1") Is BaseElement, hmlelements("text1"), Nothing), BaseElement)

    ' Event handlers declaration for the events on the html elements.
    AddHandler textElement.Click, AddressOf textElement_Click
    AddHandler textElement.KeyDown, AddressOf textElement_KeyDown
    AddHandler textElement.MouseEnter, AddressOf textElement_MouseEnter
End Sub

' HTML element Click event definition.
Private Sub textElement_Click(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("Click Event Handled")
End Sub

' HTML element KeyDown event definition.
Private Sub textElement_KeyDown(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("KeyDown Event Handled")
End Sub

' HTML element MouseEnter event definition.
Private Sub textElement_MouseEnter(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("MouseDown Event Handled")
End Sub
```

Another important feature of the HTMLUI is its **Bubbling Event** architecture. With this architecture, a single common event handler defined for a particular event of the parent can be used for all the Child Elements bound to that parent while executing the same event.

```html
[HTML]

<html>
    <body>
        <input type="button" id="button1"/>
        <br/>
        <input type="button" id="button2"/>
    </body>
</html>
```

## Cross References

See also: [Unclear]

<!-- tags: [syncfusion-sdk, HTMLUI, Windows Forms, Bubbling Event, WinForms, .NET] keywords: [HTML elements, event handling, controls, inheritance, event bubbling] -->
```