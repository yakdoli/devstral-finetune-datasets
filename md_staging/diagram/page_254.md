```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_254.jpeg
document_name: diagram
page_number: 254
page_id: diagram#page_254
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:13Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
return 0;
}
}
}
```

### VB.NET
```vbnet
' Derived Diagram
Public Class MyDiagram
    Inherits Syncfusion.Windows.Forms.Diagram.Controls.Diagram
    Public Overrides Function CreateModel() As Model
        Return New QuickStart.MainForm.MyModel()
    End Function 'CreateModel
End Class

' Derived Model where the new property is added
Public Class MyModel
    Inherits Syncfusion.Windows.Forms.Diagram.Model
    Public Overrides Sub SetDefaultPropertyValues()
        MyBase.SetDefaultPropertyValues()
        Me.SetPropertyValue("MyCustomProperty", 0)
    End Sub 'SetDefaultPropertyValues
    Public ReadOnly Property MyCustomProperty() As Integer
        Get
            Dim value As Object = Me.GetPropertyValue("MyCustomProperty")
            If Not (value Is Nothing) Then
                Return Fix(value)
            End If
            Return 0
        End Get
    End Property
End Class 'MyModel
```

## 5.2 How To Add Ports To A Custom Symbol

The following code snippet illustrates how ports can be added to a custom symbol.

### C#
```csharp
private CirclePort leftport;
private CirclePort rightport;
```

<!-- tags: [Syncfusion Winforms, diagram, custom symbol, ports, C#, VB.NET] keywords: [add ports, custom symbol, diagram, syncfusion, windows forms, model properties] -->
```