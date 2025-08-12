```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_823.jpeg
document_name: grid
page_number: 823
page_id: grid#page_823
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:42:43Z
fidelity: lossless
-->

## Content

### Essential Grid for Windows Forms

Here are code examples demonstrating the use of predefined classes and properties within a Windows Forms application, specifically focusing on `Country` class implementations:

#### Country Class Implementation

```vb
Return countries
End Function

Public Overrides ReadOnly Property IsReadOnly() As Boolean
Get
    Return True
End Get
End Property

Public Overrides ReadOnly Property IsFixedSize() As Boolean
Get
    Return True
End Get
End Property
End Class

' Country Class.
<Serializable()> _
Public Class Country
    Private _code As String
    Private _name As String

    Public Sub New()
    End Sub

    Public Sub New(strCode As String, strName As String)
        Me._code = strCode
        Me._name = strName
    End Sub

    <Browsable(True)> _
    Public Property CountryCode() As String
        Get
            Return _code
        End Get
        Set
            _code = value
        End Set
    End Property

    <Browsable(True)> _
    Public Property Name() As String
        Get
            Return _name
        End Get
    End Property
End Class
```

## API Reference

### Class: Country

#### Properties

- **CountryCode**
  - Type: `String`
  - Description: Getter and setter for the country code.
  - Attributes: `<Browsable(True)>`

- **Name**
  - Type: `String`
  - Description: Getter and setter for the country name.
  - Attributes: `<Browsable(True)>`

#### Constructors

- **Public Sub New()**
  - Description: Default constructor.

- **Public Sub New(strCode As String, strName As String)**
  - Parameters:
    - `strCode`: Type `String`, represents the country code.
    - `strName`: Type `String`, represents the country name.
  - Description: Constructor to initialize the `Country` object with provided values.

## Code Examples

The provided code demonstrates how to define and use a `Country` class with properties that are both browsable and serializable. The implementation includes a default constructor and an overloaded constructor for initializing the class with specific values.

## Cross References

For more details on `Country` class usage and properties in Windows Forms, refer to the official Syncfusion documentation on Essential Grid for Windows Forms.

## Additional Notes

The `Serializable` attribute marks the class as serializable, and the `Browsable` attribute controls the visibility of properties in property grids.

<!-- tags: [syncfusion, windows forms, essential grid, country class, properties, constructor, serialization, version 11.4.0.26] keywords: [CountryCode, Name, Browsable, Serializable, default constructor, overloaded constructor, property grid, windows forms, essential grid, windows forms] -->
```