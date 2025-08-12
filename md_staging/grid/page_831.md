```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_831.jpeg
document_name: grid
page_number: 831
page_id: grid#page_831
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:43:20Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the implementation of property change notification using `INotifyPropertyChanged` interface.
- Highlights the use of `RaisePropertyChanged` method to notify UI elements of changes.
- Provides an example implementation of a class with properties that trigger event notifications.

## Content

### Implementation of `INotifyPropertyChanged`

The following code snippet shows how to implement the `INotifyPropertyChanged` interface to notify changes in property values.

```vb
    f3 = value
    RaisePropertyChanged("Field3")
End If
End Set
End Property

Sub RaisePropertyChanged(ByVal name As String)
    RaiseEvent PropertyChanged(Me, New PropertyChangedEventArgs(name))
End Sub

Public Event PropertyChanged As PropertyChangedEventHandler Implements INotifyPropertyChanged.PropertyChanged
```

### Key Components
- **Property Changed Notification**: The `RaisePropertyChanged` method is called whenever a property value changes to notify the UI about the change.
- **Event Raising**: The `PropertyChanged` event is raised with the property name to notify subscribed listeners.
- **Implementation of Interface**: The class implements `INotifyPropertyChanged` and exposes the `PropertyChanged` event to notify bindings or UI components.

### Example Usage
In this example, when the value of a property (e.g., `Field3`) changes, the `RaisePropertyChanged` method is called to notify the subscribers that the property value has been updated. This is crucial for maintaining data synchronization in scenarios like MVVM.

## API Reference

### Methods
- `RaisePropertyChanged(ByVal name As String)`
  - **Parameters**:
    - `name As String`: The name of the property that has been changed.
  - **Description**: This method raises the `PropertyChanged` event with the name of the property that has changed, notifying all subscribed listeners.
  - **Returns**: None.

### Events
- `PropertyChanged As PropertyChangedEventHandler`
  - **Description**: This event is raised when a property value changes. It is used by the `INotifyPropertyChanged` interface to inform bindings and other listeners about property changes.

## Code Examples

The provided code snippet includes an example implementation of a class with a property change mechanism. This example ensures that any changes to a property trigger the notification process, adhering to the principles of data binding and synchronization.

## RAG Annotations
<!-- tags: [property change, property binding, INotifyPropertyChanged, MVVM, Windows Forms] keywords: [RaisePropertyChanged, PropertyChanged, INotifyPropertyChanged, property change event, data binding, synchronization, WinForms] -->
```