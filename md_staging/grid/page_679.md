```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_679.jpeg
document_name: grid
page_number: 679
page_id: grid#page_679
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:33:19Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains how to create and manage data objects for use in a grid control.
- Demonstrates object-oriented programming practices in VB.NET.
- Describes how to implement property getters and setters.

## Content

### Class Definition

The following VB.NET class `Data` is designed to manage data objects for grid controls in a Windows Forms application.

```vb
Public Sub New()
    Me.New("", "", "")
End Sub

Public Sub New(ByVal cat_Id As String, ByVal cat_Name As String, ByVal desc As String)
    Me.cat_Id = cat_Id
    Me.cat_Name = cat_Name
    Me.desc = desc
End Sub

Private cat_Name As String
Public Property CategoryName() As String
    Get
        Return Me.cat_Name
    End Get
    Set(ByVal value As String)
        Me.cat_Name = Value
    End Set
End Property

Private desc As String
Public Property Description() As String
    Get
        Return Me.desc
    End Get
    Set(ByVal value As String)
        Me.desc = Value
    End Set
End Property

Private cat_Id As String
Public Property CategoryID() As String
    Get
        Return Me.cat_Id
    End Get
    Set(ByVal value As String)
        Me.cat_Id = Value
    End Set
End Property
End Class
```

### Collection of Data Objects

1. Create an instance of `ArrayList` and add a list of `Data` type objects into it. This represents the collection of data to be displayed in the grid.

## Code Examples

```csharp
[C#]
```

## Cross References
- See also: [Using ArrayList in Windows Forms](#reference-link)

<!-- tags: [winforms, essential grid, datagrid, ArrayList, VB.NET, object-oriented programming] keywords: [data objects, property getters, setters, category name, description, category id] -->
```