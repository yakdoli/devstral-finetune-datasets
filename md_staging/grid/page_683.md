```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_683.jpeg
document_name: grid
page_number: 683
page_id: grid#page_683
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:33:32Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### WinForms Sample Code

#### C#

```csharp
this.author = author;
}
private string bookName;
public string BookName
{
    get
    {
        return this.bookName;
    }
    set
    {
        this.bookName = value;
    }
}
private string author;
public string Author
{
    get
    {
        return this.author;
    }
    set
    {
        this.author = value;
    }
}
}
```

#### VB.NET

```vb
Public Class Book
    Public Sub New(ByVal bname As String, ByVal auth As String)
        Me.bName = bname
        Me.authr = auth
    End Sub
    Private bname As String
    Public Property BookName() As String
        Get
            Return Me.bname
        End Get
        Set
            Me.bname = Value
        End Set
    End Property
    Private authr As String
End Class
```

### Description

The sample code demonstrates the implementation of a `Book` class in both C# and VB.NET to manage the properties of a book, such as its name and author. The class includes private fields for `bookName` and `author`, along with public properties (`BookName` and `Author`) that provide getter and setter methods for these fields. In VB.NET, the implementation also includes a constructor to initialize the book's name and author, showcasing how to handle object instantiation and property access in both languages.

### API Reference

#### C#

- **Class**: `Book`
  - **Fields**:
    - `private string bookName;`
    - `private string author;`
  - **Properties**:
    - `public string BookName`:
      - Getter: Returns the value of `bookName`.
      - Setter: Assigns a new value to `bookName`.
    - `public string Author`:
      - Getter: Returns the value of `author`.
      - Setter: Assigns a new value to `author`.

#### VB.NET

- **Class**: `Book`
  - **Fields**:
    - `Private bname As String`
    - `Private authr As String`
  - **Constructor**: `Public Sub New(ByVal bname As String, ByVal auth As String)`
    - Initializes the `bname` and `authr` fields.
  - **Properties**:
    - `Public Property BookName() As String`:
      - Getter: Returns the value of `bname`.
      - Setter: Assigns a new value to `bname`.

### Code Examples

#### C#

```csharp
Book myBook = new Book();
myBook.BookName = "1984";
myBook.Author = "George Orwell";
Console.WriteLine($"Book Name: {myBook.BookName}, Author: {myBook.Author}");
```

#### VB.NET

```vb
Dim myBook As New Book("1984", "George Orwell")
Console.WriteLine($"Book Name: {myBook.BookName}, Author: {myBook.Author}")
```

## Page-level Navigation/TOC

- **Overview**
- **WinForms Sample Code**
  - C#
  - VB.NET
- **Description**
- **API Reference**
  - C#
  - VB.NET
- **Code Examples**
  - C#
  - VB.NET

## Cross References

See also: [Essential Grid](#), [WinForms Controls](#), [C# and VB.NET Examples](#), [Property Accessors](#).

<!-- tags: [Essential Grid, WinForms, C#, VB.NET, Book Class, Property Accessors] keywords: [book, author, name, constructor, getter, setter, class, field, property] -->
```