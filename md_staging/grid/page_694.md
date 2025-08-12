```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_694.jpeg
document_name: grid
page_number: 694
page_id: grid#page_694
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:35:06Z
fidelity: lossless
-->

## Content

### Visual Basic (.NET) Code Example

The following Visual Basic (.NET) code example demonstrates the implementation of properties for managing and raising notifications when changes occur in user details such as FirstName, LastName, Address, and City.

```vb
End Property

Public Property FirstName() As String
    Get
        Return first_name
    End Get
    Set(ByVal value As String)
        If first_name <> value Then
            first_name = value
            RaisePropertyChanged("FirstName")
        End If
    End Set
End Property

Public Property LastName() As String
    Get
        Return last_name
    End Get
    Set(ByVal value As String)
        If last_name <> value Then
            last_name = value
            RaisePropertyChanged("LastName")
        End If
    End Set
End Property

Public Property Address() As String
    Get
        Return addr
    End Get
    Set(ByVal value As String)
        If addr <> value Then
            addr = value
            RaisePropertyChanged("Address")
        End If
    End Set
End Property

Public Property city() As String
    Get
        Return cityname
    End Get
    Set(ByVal value As String)
        If cityname <> value Then
            cityname = value
            RaisePropertyChanged("City")
        End If
    End Set
End Property
```

This implementation provides a mechanism to track changes in the properties of an object, which can be essential for binding these properties to a visual grid or UI element, ensuring updates are reflected appropriately.

## API Reference

### Properties
- **FirstName() As String**: Retrieves or sets the first name of the user. Includes logic to notify about changes using `RaisePropertyChanged`.
- **LastName() As String**: Retrieves or sets the last name of the user, similar to `FirstName`.
- **Address() As String**: Retrieves or sets the address details, with change notification support.
- **city() As String**: Retrieves or sets the city name, handling updates with `RaisePropertyChanged`.

### Methods
- **RaisePropertyChanged(propertyName As String)**: Raises the PropertyChanged event for the specified property, ensuring UI bindings are updated.

## Code Examples

The provided code snippet exemplifies how to implement properties with change notification mechanisms in a .NET environment using Visual Basic. This approach is particularly useful for data-binding scenarios where properties need to update UI components dynamically, ensuring a lengthened and enriched user experience.

<!-- tags: data-binding, property-change-notification, .NET, Visual Basic, UI updates, Syncfusion Winforms keywords: firstName, lastName, address, city -->
```