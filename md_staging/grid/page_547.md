```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_547.jpeg
document_name: grid
page_number: 547
page_id: grid#page_547
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:23:42Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
al.Add(new Person("Mary", "Tucker"));
al.Add(new Person("Sue", "Gaskins"));
al.Add(new Person("John", "Jacobs"));
al.Add(new Person("Sam", "Garfunkel"));
al.Add(new Person("George", "Shepherd"));
al.Add(new Person("Becky", "Dunsford"));

this.gridDataBoundGrid1.DataSource = al;
}
```

#### [VB.NET]
```vb
' Create the Person object class.
Public Class Person
    Private fname As String
    Private lname As String

    Public Sub New(ByVal fname As String, ByVal lname As String)
        Me.fname = fname
        Me.lname = lname
    End Sub

    Public Property LastName()
        Get
            Return lname
        End Get
        Set(ByVal Value)
            lname = Value
        End Set
    End Property

    Public Property FirstName()
        Get
            Return fname
        End Get
        Set(ByVal Value)
            fname = Value
        End Set
    End Property
End Class

' Code within your Form_Load event handler.
Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
    Dim al As ArrayList = New ArrayList()
```

## API Reference (if applicable)
- **Namespace**: N/A (not specified in the code)
- **Class**: `Person`
  - **Properties**
    - `LastName`: String
    - `FirstName`: String
  - **Constructor**
    - `Public Sub New(ByVal fname As String, ByVal lname As String)`

## Code Examples (multi-language supported)

### C#
```csharp
// Example of adding Person objects to an ArrayList and setting it as the data source
al.Add(new Person("Mary", "Tucker"));
al.Add(new Person("Sue", "Gaskins"));
al.Add(new Person("John", "Jacobs"));
al.Add(new Person("Sam", "Garfunkel"));
al.Add(new Person("George", "Shepherd"));
al.Add(new Person("Becky", "Dunsford"));

this.gridDataBoundGrid1.DataSource = al;
```

### VB.NET
```vb
' Example of creating a Person object and handling Form_Load
Public Class Person
    Private fname As String
    Private lname As String

    Public Sub New(ByVal fname As String, ByVal lname As String)
        Me.fname = fname
        Me.lname = lname
    End Sub

    Public Property LastName()
        Get
            Return lname
        End Get
        Set(ByVal Value)
            lname = Value
        End Set
    End Property

    Public Property FirstName()
        Get
            Return fname
        End Get
        Set(ByVal Value)
            fname = Value
        End Set
    End Property
End Class

Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
    Dim al As ArrayList = New ArrayList()
    al.Add(New Person("Mary", "Tucker"))
    al.Add(New Person("Sue", "Gaskins"))
    al.Add(New Person("John", "Jacobs"))
    al.Add(New Person("Sam", "Garfunkel"))
    al.Add(New Person("George", "Shepherd"))
    al.Add(New Person("Becky", "Dunsford"))

    gridDataBoundGrid1.DataSource = al
End Sub
```

<!-- tags: [Essential Grid, Windows Forms, DataSource, ArrayList, Person Class, Person Object, Form_Load] keywords: [Essential Grid, Windows Forms, DataSource, ArrayList, Object Class, Form_Load, Person Object] -->
```