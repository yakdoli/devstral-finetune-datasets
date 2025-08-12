```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_833.jpeg
document_name: grid
page_number: 833
page_id: grid#page_833
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:42:30Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Implementation of properties with `INotifyPropertyChanged` interface.
- Usage of `BindingList<T>` for maintaining child objects.
- Property change notifications for binding functionality.

## Content

The following C# and VB.NET code examples illustrate the implementation of a `ParentObj` class that implements `INotifyPropertyChanged`. This class includes various properties such as `Field1`, `Field2`, `Field3`, and a `BindingList` of child objects.

### C#

```csharp
public int Field3 {
    get { return f3; }
    set {
        if (f3 != value) {
            f3 = value;
            RaisePropertyChanged("Field3");
        }
    }
}

public BindingList<ChildObj> Child {
    get { return childObj; }
}

void RaisePropertyChanged(string name) {
    if (PropertyChanged != null)
        PropertyChanged(this, new PropertyChangedEventArgs(name));
}

public event PropertyChangedEventHandler PropertyChanged;
```

### VB.NET

```vb
Public Class ParentObj : Implements INotifyPropertyChanged

    Private f1, f2 As String
    Private f3 As Integer
    Private childObj As BindingList(Of ChildObj) = New BindingList(Of ChildObj)()

    Public Sub New(ByVal f1 As String, ByVal f2 As String, ByVal f3 As Integer, ByVal ParamArray c As ChildObj())
        Me.f1 = f1
        Me.f2 = f2
        Me.f3 = f3
        For Each i As ChildObj In c
            childObj.Add(i)
        Next i
    End Sub
End Class
```

### Explanation

- **INotifyPropertyChanged**: The `ParentObj` class implements this interface to notify other objects when its properties change. The `PropertyChanged` event is raised whenever a property value changes, using the `RaisePropertyChanged` method.
- **Field3 Property**: This property includes a setter that compares the new value with the current value. If they differ, it updates the field and raises a `PropertyChanged` event.
- **Child Property**: This property provides access to a `BindingList` of child objects, which is useful for maintaining a list of items that automatically support binding.
- **Constructor**: The VB.NET example shows a constructor that initializes the `ParentObj` class with string and integer parameters, along with an array of child objects.

## API Reference

### Methods

- **RaisePropertyChanged**
  - **Description**: Notifies any object subscribed to the `PropertyChanged` event that a property value has changed.
  - **Signature**:
    ```csharp
    void RaisePropertyChanged(string name)
    ```
  - **Parameters**:
    - `name`: The name of the property that has changed.

### Properties

- **Field3**
  - **Type**: `int`
  - **Getter**: Returns the current value of `f3`.
  - **Setter**: Updates the value of `f3` and raises a `PropertyChanged` event if the value changes.

- **Child**
  - **Type**: `BindingList<ChildObj>`
  - **Getter**: Returns the instance of the `BindingList` containing child objects.

## Code Examples

The provided examples demonstrate how to handle property changes and maintain a collection of child objects using `INotifyPropertyChanged` and `BindingList<T>`.

## Conclusion

This section illustrates how to implement binding-ready properties and maintain a collection of child objects in a `ParentObj` class using `INotifyPropertyChanged` and `BindingList<T>`. This is especially relevant for binding scenarios in Windows Forms applications.

<!-- tags: [product, winforms, grid, binding, propertychange] keywords: [INotifyPropertyChanged, BindingList, property changed, child objects, event, c#, vb.net] -->
```