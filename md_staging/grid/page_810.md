```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_810.jpeg
document_name: grid
page_number: 810
page_id: grid#page_810
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:44:54Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
Public Class USState
    Private _code As String
    Private _name As String

    Public Sub New()
        End Sub

    Public Sub New(key As String, name As String)
        Me._code = key
        Me._name = name
        End Sub

    <Browsable(True)> _
    Public Property Key() As String
        Get
            Return _code
        End Get
        Set
            _code = value
        End Set
    End Property

    <Browsable(True)> _
    Public Property Name() As String
        Get
            Return _name
        End Get
        Set
            _name = value
        End Set
    End Property

    Public Overrides Function ToString() As String
        Return Me._name + "(" + Me._code + ")"
    End Function
End Class
```

## Content

2. Create an object of USStates and add this object into the SourceListSet with a lookup name.

### Example Code

```csharp
USStatesCollection usStates = USStatesCollection.CreateDefaultCollection();
this.gridGroupingControl.Engine.SourceListSet.Add("USStates", usStates);
```

<!-- tags: [product, windows forms, essential grid, usstates, source list set, object creation] keywords: [create object, add to source list set, lookup name] -->
```