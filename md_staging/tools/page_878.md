```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_878.jpeg
document_name: tools
page_number: 878
page_id: tools#page_878
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:40:38Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```vb
Public Sub New()
    For Each c As Control In Controls
        If TypeOf c Is TextBox Then
            itb.Location = c.Location
            itb.Size = c.Size
            itb.Dock = c.Dock
            itb.Anchor = c.Anchor
            Controls.Add(itb)
            itb.BringToFront()
            AddHandler itb.TextChanged, AddressOf itb_TextChanged
        End If
    Next
End Sub

Private Sub itb_TextChanged(ByVal sender As Object, ByVal e As EventArgs)
    ' Assigns the IntegerValue.
    Value = itb.IntegerValue
End Sub

Public Property NegativeColor() As System.Drawing.Color
    Get
        Return itb.NegativeColor
    End Get
    Set
        itb.NegativeColor = value
    End Set
End Property

Protected Overloads Overrides Sub OnValueChanged(ByVal e As EventArgs)
    itb.Text = Value.ToString()
End Sub
End Class
```

After deriving the new class, create an object for that class and set the required properties.

### Example: Creating an Object in C#

```csharp
NumericupdownnextDerived ud = new NumericupdownnextDerived();
ud.Location = new Point(200, 200);
ud.Minimum = -100;
ud.NegativeColor = Color.Red;
Controls.Add(ud);
```

### Example: Creating an Object in VB.NET

```vb
[VB.NET]
```
```汽油
<!-- tags: [Syncfusion, Windows Forms, Essential Tools, NumericupdownnextDerived, C#, VB.NET, Control Creation] keywords: [Windows Forms, controls, properties, event handling, color settings, numeric updown, derived class] -->
```