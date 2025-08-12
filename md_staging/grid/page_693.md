<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_693.jpeg
document_name: grid
page_number: 693
page_id: grid#page_693
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:33:02Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates implementing the `INotifyPropertyChanged` interface in C# and VB.NET.
- Focuses on raising property change notifications when a property's value is updated.
- Includes code examples for handling property changes in classes.

## Content

### Implementing INotifyPropertyChanged in C#

```csharp
set
{
    if (city != value)
    {
        city = value;
        RaisePropertyChanged("City");
    }
}

void RaisePropertyChanged(string name)
{
    if (PropertyChanged != null)
        PropertyChanged(this, new PropertyChangedEventArgs(name));
}

// INotifyPropertyChanged Members.
public event PropertyChangedEventHandler PropertyChanged;
```

### Implementing INotifyPropertyChanged in VB.NET

```vb
Public Class CustomClass : Implements INotifyPropertyChanged
    Dim cusid As Integer
    Dim first_name As String, last_name As String, addr As String, cityname As String

    Public Sub New(ByVal id As Integer, ByVal fname As String, ByVal lname As String, ByVal addr As String, ByVal city As String)
        Me.cusid = id
        Me.first_name = fname
        Me.last_name = lname
        Me.addr = addr
        Me.cityname = city
    End Sub

    Public Property ID() As Integer
        Get
            Return cusid
        End Get
        Set(ByVal value As Integer)
            If cusid <> value Then
                cusid = value
                RaisePropertyChanged("ID")
            End If
        End Set
    End Property
End Class
```

### Explanation

The `INotifyPropertyChanged` interface is used to notify clients, typically a binding infrastructure like the Windows Forms or WPF data binding engine, that a property value has changed. This is particularly useful in scenarios where the UI needs to reflect the updated property values in real-time.

In the provided C# example:
- The `RaisePropertyChanged` method is used to notify any subscribers when a property value changes.
- The `PropertyChanged` event is defined as part of the `INotifyPropertyChanged` interface.

In the VB.NET example:
- The class `CustomClass` implements the `INotifyPropertyChanged` interface.
- The `ID` property includes logic to check if the property value has changed before raising the `PropertyChanged` event.

### Key Concepts
- **PropertyChange Notification**: Essential for updating the UI when property values change.
- **Event Handlers**: Used to handle property change events in code.
- **Binding Framework**: Typically leverages such notifications to keep UI elements synchronized with the data.

## API Reference

### INotifyPropertyChanged

```csharp
public interface INotifyPropertyChanged
{
    event PropertyChangedEventHandler PropertyChanged;
}
```

- **PropertyChanged**: Event that other classes can subscribe to in order to be notified when a property value changes.

#### Members

- **PropertyChangedEventHandler**: Delegate type used for handling property change events.

### PropertyChangedEventArgs

```csharp
public class PropertyChangedEventArgs : EventArgs
{
    public PropertyChangedEventArgs(string propertyName);
}
```

- **propertyName**: The name of the property that changed.

## Code Examples

### C# Example

```csharp
using System.ComponentModel;

public class Person : INotifyPropertyChanged
{
    private string _city;

    public event PropertyChangedEventHandler PropertyChanged;

    public string City
    {
        get { return _city; }
        set
        {
            if (_city != value)
            {
                _city = value;
                OnPropertyChanged("City");
            }
        }
    }

    protected void OnPropertyChanged(string propertyName)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}
```

### VB.NET Example

```vb
Imports System.ComponentModel

Public Class Person
    Implements INotifyPropertyChanged

    Private _city As String

    Public Event PropertyChanged As PropertyChangedEventHandler Implements INotifyPropertyChanged.PropertyChanged

    Public Property City As String
        Get
            Return _city
        End Get
        Set(ByVal value As String)
            If _city <> value Then
                _city = value
                OnPropertyChanged("City")
            End If
        End Set
    End Property

    Protected Sub OnPropertyChanged(ByVal propertyName As String)
        RaiseEvent PropertyChanged(Me, New PropertyChangedEventArgs(propertyName))
    End Sub
End Class
```

## Summary

Implementing `INotifyPropertyChanged` allows for dynamic updates in UI components when underlying data properties change. This is crucial for maintaining synchronization between the UI and the data model, enhancing the responsiveness and user experience of applications built with WinForms.

---

<!-- tags: [Syncfusion Winforms, INotifyPropertyChanged, Property Binding, Property Change Notification, C#, VB.NET] keywords: [INotifyPropertyChanged, PropertyChangedEventArgs, Property Binding, Property Change Notification, Windows Forms, Data Binding] -->