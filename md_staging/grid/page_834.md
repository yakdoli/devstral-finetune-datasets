```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_834.jpeg
document_name: grid
page_number: 834
page_id: grid#page_834
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:46:45Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Code Example

```vb
Public Property Field1() As String
    Get
        Return f1
    End Get
    Set(ByVal value As String)
        If f1 <> value Then
            f1 = value
            RaisePropertyChanged("Field1")
        End If
    End Set
End Property

Public Property Field2() As String
    Get
        Return f2
    End Get
    Set(ByVal value As String)
        If f2 <> value Then
            f2 = value
            RaisePropertyChanged("Field2")
        End If
    End Set
End Property

Public Property Field3() As Integer
    Get
        Return f3
    End Get
    Set(ByVal value As Integer)
        If f3 <> value Then
            f3 = value
            RaisePropertyChanged("Field3")
        End If
    End Set
End Property

Public ReadOnly Property Child() As BindingList(Of ChildObj)
    Get
        Return childObj
    End Get
End Property

Sub RaisePropertyChanged(ByVal name As String)
    RaiseEvent PropertyChanged(Me, New PropertyChangedEventArgs(name))
End Sub
```

### References

- **See also**: Property Changed EventArgs, BindingList, Child Object Management

<!-- tags: [Essential Grid, WinForms, Property Changed, BindingList] keywords: [field, property, event, windows forms] -->
```