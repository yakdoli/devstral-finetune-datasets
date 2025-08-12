```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_101.jpeg
document_name: grid
page_number: 101
page_id: grid#page_101
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:22:58Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains how to add a Virtual Grid to your Windows Forms application.
- Provides code examples demonstrating properties and methods related to the grid.
- Emphasizes the importance of not modifying certain properties like `RowCount` and `ColCount`.

## Content

### Properties and Methods

```vb
Return _rowCount
End Get
End Property

Public Overridable ReadOnly Property ColCount() As Integer
    Get
        Return _colCount
    End Get
End Property

Default Public Overridable Property Item(ByVal row As Integer, ByVal _
                  col As Integer) As Integer
    Get
        Return _data(row, col)
    End Get

    Set(ByVal Value As Integer)
        _data(row, col) = Value
    End Set
End Property
End Class
```

#### Adding Virtual Grid

##### 3.1.5.2 Adding Virtual Grid

To add a Virtual Grid to your application:

1. Select the form, open the toolbox and drag a **Grid** control onto your form.

**Note:** Do not change the values of the `RowCount` or `ColCount` properties for the grid. Let the default values remain as it is. These values will be provided dynamically as part of the virtual grid implementation.

## API Reference

### Properties

- **RowCount**: Gets the number of rows in the grid.
- **ColCount**: Gets the number of columns in the grid.
- **Item(row As Integer, col As Integer)**: A default property used to get or set the value at the specified row and column.

### Methods

- **Get**: Retrieves the value at the specified row and column.
- **Set**: Sets the value at the specified row and column.

## Code Examples

The provided code snippet demonstrates how to access and modify values in the grid using the `Item` property.

```vb
' Accessing a value
Dim value As Integer = grid.Item(row, col)

' Modifying a value
grid.Item(row, col) = newValue
```

## Page-level Navigation/TOC (if applicable)

This section provides guidance on incorporating a Virtual Grid into your Windows Forms application, with a focus on avoiding manual adjustments to `RowCount` and `ColCount`.

## Cross References

See also: 
- [Virtual Grid Documentation](#)
- [Grid Control Overview](#)

<!-- tags: virtual, windows forms, grids, properties, methods, winforms, grid control, essentialgrid, syncfusion -->
```