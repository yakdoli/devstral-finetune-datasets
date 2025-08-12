```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_830.jpeg
document_name: grid
page_number: 830
page_id: grid#page_830
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:46:28Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the implementation of the `INotifyPropertyChanged` interface in a `ChildObj` class.
- Highlights property handling with raising property change notifications.
- Focuses on managing string and integer fields with corresponding public properties.

## Content

### Implementation of INotifyPropertyChanged

The following code example shows how to implement the `INotifyPropertyChanged` interface in a VB.NET class named `ChildObj`. This class manages three fields: two strings (`f1`, `f2`) and one integer (`f3`). It raises property changed events for each property when a change occurs.

```vb
Public Class ChildObj : Implements INotifyPropertyChanged

    Private f1, f2 As String
    Private f3 As Integer

    Public Sub New(ByVal f1 As String, ByVal f2 As String, ByVal f3 As Integer)
        Me.f1 = f1
        Me.f2 = f2
        Me.f3 = f3
    End Sub

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

End Class
```

### Explanation

- **Fields**: The class has three private fields: `f1`, `f2` (strings), and `f3` (integer).
- **Constructor**: The constructor initializes these fields with the provided values.
- **Properties**:
  - `Field1`, `Field2`, and `Field3` are public properties for accessing and modifying the corresponding fields.
  - Each property includes a `Get` method to return the field value and a `Set` method to update the value and raise a property changed event if the value has changed.
- **INotifyPropertyChanged Implementation**: The `RaisePropertyChanged` method is called within each `Set` method to notify any binding framework that the property has changed.

### Purpose
This implementation is particularly useful in scenarios where properties of objects need to be bound to UI elements in a way that reflects changes in real-time. The `INotifyPropertyChanged` interface is a common requirement for maintaining data-binding compatibility in Windows Forms applications.

## RAG Annotations

<!-- tags: [windows forms, inotifypropertychanged, property binding] keywords: [childobj, string, integer, field, property change, vb.net, data binding] -->
```