```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_621.jpeg
document_name: grid
page_number: 621
page_id: grid#page_621
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:27:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
}
}
}
```

## Overview

- Implements a `VirtualItem` class in VB.NET.
- Contains fields and properties for data management.
- Provides encapsulated access to private member variables through public properties.

## Content

### WinForms-specific conventions
The following VB.NET class example demonstrates a virtual item class with properties for managing data access and encapsulation.

```vb
[VB]

Public Class VirtualItem
    Private index_Renamed As Integer
    Private name_Renamed As String
    Private someValue_Renamed As Double
    Private otherValue_Renamed As Double

    Public Property Index() As Integer
        Get
            Return index_Renamed
        End Get
        Set
            index_Renamed = Value
        End Set
    End Property

    Public Property Name() As String
        Get
            Return name_Renamed
        End Get
        Set
            name_Renamed = Value
        End Set
    End Property

    Public Property SomeValue() As Double
        Get
            Return someValue_Renamed
        End Get
        Set
            someValue_Renamed = Value
        End Set
    End Property

    Public Property OtherValue() As Double
        Get
            Return otherValue_Renamed
        End Get
        Set
            otherValue_Renamed = Value
        End Set
    End Property
End Class
```

## API Reference (if applicable)

### Namespace: Unclear (Not specified)
- **Class**: `VirtualItem`
  - **Members**:
    - **Fields**:
      - `index_Renamed` (As Integer)
      - `name_Renamed` (As String)
      - `someValue_Renamed` (As Double)
      - `otherValue_Renamed` (As Double)
    - **Properties**:
      - `Index` (As Integer): Provides encapsulated access to `index_Renamed`.
      - `Name` (As String): Provides encapsulated access to `name_Renamed`.
      - `SomeValue` (As Double): Provides encapsulated access to `someValue_Renamed`.
      - `OtherValue` (As Double): Provides encapsulated access to `otherValue_Renamed`.

## Code Examples (multi-language supported)

### VB.NET Example

```vb
Public Class VirtualItem
    Private index_Renamed As Integer
    Private name_Renamed As String
    Private someValue_Renamed As Double
    Private otherValue_Renamed As Double

    Public Property Index() As Integer
        Get
            Return index_Renamed
        End Get
        Set
            index_Renamed = Value
        End Set
    End Property

    Public Property Name() As String
        Get
            Return name_Renamed
        End Get
        Set
            name_Renamed = Value
        End Set
    End Property

    Public Property SomeValue() As Double
        Get
            Return someValue_Renamed
        End Get
        Set
            someValue_Renamed = Value
        End Set
    End Property

    Public Property OtherValue() As Double
        Get
            Return otherValue_Renamed
        End Get
        Set
            otherValue_Renamed = Value
        End Set
    End Property
End Class
```

## Cross References

- This class is part of a broader discussion on implementing data virtualization in Syncfusion Grid for Windows Forms.
- Refer to the Syncfusion documentation for more details on Grid control and its features.

<!-- tags: [Syncfusion, WinForms, Grid, VirtualItem, data encapsulation, property management] keywords: [VirtualItem, Index, Name, SomeValue, OtherValue, data virtualization, encapsulation] -->
```