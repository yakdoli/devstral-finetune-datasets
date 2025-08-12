```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_735.jpeg
document_name: grid
page_number: 735
page_id: grid#page_735
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:36:48Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Manage property changes in the grid for specific properties like "Appearance," "Width," "ReadOnly," "HeaderText," and "AllowFilter."
- Handle different actions such as item property changes, removals, and movements.

## Content

### Property Change Handling

```csharp
if (le.Action == ListPropertyChangedType.ItemPropertyChanged)
{
    if (le.Property == "Appearance" || le.Property == "Width"
        || le.Property == "ReadOnly" || le.Property == "HeaderText"
        || le.Action == ListPropertyChangedType.Remove
        || le.Action == ListPropertyChangedType.Move
        || le.Property == "AllowFilter")
    {
        return;
    }
}
else if (e.PropertyName == "Appearance")
{
    // Base class will end edit mode, which is not necessary.
    return;
}
base.Engine_PropertyChanging(sender, e);
```

#### VB.NET Implementation

```vb
Protected Overrides Sub Engine_PropertyChanging(ByVal sender As Object, ByVal e As DescriptorPropertyChangedEventArgs)
    If e.PropertyName = "TableDescriptor" Then
        Dim tableDescriptor As TableDescriptor = CType(sender, Engine).TableDescriptor
        e = CType(e.Inner, DescriptorPropertyChangedEventArgs)
    End If

    If e.PropertyName = "Relations" Then
        e = e.GetNestedChildTableDescriptorEvent(tableDescriptor)
    End If

    If e.PropertyName = "Columns" Then
        Dim le As ListPropertyChangedEventArgs = CType(e.Inner, ListPropertyChangedEventArgs)
        If le.Action = ListPropertyChangedType.ItemPropertyChanged Then
            If le.Property = "Appearance" OrElse le.Property = "Width" _
                OrElse le.Property = "ReadOnly" OrElse le.Property = "HeaderText" _
                OrElse le.Action = ListPropertyChangedType.Remove _
                OrElse le.Action = ListPropertyChangedType.Move OrElse le.Property = "AllowFilter" Then
                Return
            End If
        End If
    End If
End Sub
```

### Summary
- The code ensures that certain property changes are intercepted to prevent unwanted behavior, such as the base class ending edit mode unnecessarily.
- The VB.NET section provides an alternative implementation with similar functionality, handling nested events and specific property changes.

## API Reference

### Events
- `Engine_PropertyChanging`: Triggered when a property is about to change.
- `ListPropertyChangedEventArgs`: Contains details about the property change action.

### Properties
- `Property`: Specifies the name of the property being changed.
- `Action`: Indicates the type of property change action (e.g., item property changed, removal, movement).

### Methods
- `GetNestedChildTableDescriptorEvent`: Retrieves nested table descriptor events based on the parent table descriptor.

### Classes
- `TableDescriptor`: Represents a table descriptor object used in the grid.
- `DescriptorPropertyChangedEventArgs`: Encapsulates event arguments for property changes.

## Code Examples

### C# Example

```csharp
if (e.Action == ListPropertyChangedType.ItemPropertyChanged && e.Property == "Width")
{
    // Handle width change
}
```

### VB.NET Example

```vb
If e.Action = ListPropertyChangedType.ItemPropertyChanged AndAlso e.Property = "Width" Then
    ' Handle width change
End If
```

## Cross References
- See also: Property change events, nested table descriptors, grid customization.

<!-- tags: [grid, property change, nested table descriptor, syncfusion, essential grid, windows forms] keywords: [property, change, action, appearance, width, read-only, header text, allow filter, table descriptor, relations, columns, events] -->
```