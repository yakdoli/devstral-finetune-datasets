```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_025.jpeg
document_name: grouping
page_number: 025
page_id: grouping#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:22Z
fidelity: lossless
-->

## Overview

- Essential Grouping functionality demonstrated using a custom `MyObject` class.
- Example code demonstrates initializing the `MyObject` class with specific properties and how they are set.

## Content

### Example Code

```vb
Sub Main()
End Sub

Public Class MyObject
    Private aValue As String
    Private bValue As String
    Private cValue As String
    Private dValue As String

    Public Sub New(ByVal i As Integer)
        aValue = String.Format("a{0}", i)

        ' Use digit only.
        bValue = String.Format("{0}", i)
        cValue = String.Format("c{0}", i Mod 3)
        dValue = String.Format("d{0}", i Mod 2)
    End Sub

    Public Property A() As String
        Get
            Return aValue
        End Get
        Set(ByVal Value As String)
            aValue = Value
        End Set
    End Property

    Public Property B() As String
        Get
            Return bValue
        End Get
        Set(ByVal Value As String)
            bValue = Value
        End Set
    End Property

    Public Property C() As String
        Get
            Return cValue
        End Get
        Set(ByVal Value As String)
            cValue = Value
        End Set
    End Property

    Public Property D() As String
        Get
            Return dValue
        End Get
    End Property
End Class
```

<!-- tags: [syncfusion, winforms, essential grouping, myobject] keywords: [essential grouping, myobject class, property initialization, modulo operation, string formatting] -->
```