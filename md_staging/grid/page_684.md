```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_684.jpeg
document_name: grid
page_number: 684
page_id: grid#page_684
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:33:36Z
fidelity: lossless
-->

## Overview
- Describes the implementation of a `Books` class that inherits from `ArrayList` and implements the `ITypedList` interface.
- Explains the implementation of `GetItemProperties` and `GetListName` methods.
- Guides on creating an instance of `Books` and adding records to it.

## Content

### Creating the `Books` Class

#### Implementation Overview
The provided example demonstrates the creation of a `Books` class that inherits from `ArrayList` and implements the `ITypedList` interface. The class is designed to serve as a data store for a grouping grid. Below is the implementation in both C# and VB.NET.

#### C# Implementation

```csharp
public class Books : ArrayList, ITypedList
{
    public PropertyDescriptorCollection GetItemProperties(PropertyDescriptor[] listAccessors)
    {
        return TypeDescriptor.GetProperties(typeof(Book));
    }

    public string GetListName(PropertyDescriptor[] listAccessors)
    {
        return "Book";
    }
}
```

#### VB.NET Implementation

```vb
Public Class Books : Inherits ArrayList : Implements ITypedList
    Public Function GetItemProperties(ByVal listAccessors As PropertyDescriptor()) As PropertyDescriptorCollection Implements ITypedList.GetItemProperties
        Return TypeDescriptor.GetProperties(GetType(Book))
    End Function

    Public Function GetListName(ByVal listAccessors As PropertyDescriptor()) As String Implements ITypedList.GetListName
        Return "Book"
    End Function
End Class
```

### Adding Records to the `Books` Class

#### Step-by-Step Guide
1. **Create an Instance of `Books`**:
   - Instantiate the `Books` class to serve as a list to hold `Book` objects.
   
2. **Add Records**:
   - Populate the `Books` instance with various `Book` objects.

#### Example in C#

```csharp
// Create an instance of Books
Books bookList = new Books();

// Add records (Book objects) to the list
bookList.Add(new Book { Title = "Book1", Author = "Author1" });
bookList.Add(new Book { Title = "Book2", Author = "Author2" });
bookList.Add(new Book { Title = "Book3", Author = "Author1" });
```

#### Example in VB.NET

```vb
' Create an instance of Books
Dim bookList As New Books()

' Add records (Book objects) to the list
bookList.Add(New Book With {.Title = "Book1", .Author = "Author1"})
bookList.Add(New Book With {.Title = "Book2", .Author = "Author2"})
bookList.Add(New Book With {.Title = "Book3", .Author = "Author1"})
```

### Summary
This section outlines the process of creating a `Books` class that implements the `ITypedList` interface, which is essential for grouping grids in Windows Forms. The `GetItemProperties` and `GetListName` methods are implemented to describe the structure of the `Book` class. Finally, the creation of an instance and the addition of `Book` records demonstrate how to populate the grid with data.

## Code Examples

### C# Example
```csharp
// Class declaration
public class Books : ArrayList, ITypedList
{
    public PropertyDescriptorCollection GetItemProperties(PropertyDescriptor[] listAccessors)
    {
        return TypeDescriptor.GetProperties(typeof(Book));
    }

    public string GetListName(PropertyDescriptor[] listAccessors)
    {
        return "Book";
    }
}

// Using the Books class
Books bookList = new Books();
bookList.Add(new Book { Title = "Book1", Author = "Author1" });
```

### VB.NET Example
```vb
' Class declaration
Public Class Books : Inherits ArrayList : Implements ITypedList
    Public Function GetItemProperties(ByVal listAccessors As PropertyDescriptor()) As PropertyDescriptorCollection Implements ITypedList.GetItemProperties
        Return TypeDescriptor.GetProperties(GetType(Book))
    End Function

    Public Function GetListName(ByVal listAccessors As PropertyDescriptor()) As String Implements ITypedList.GetListName
        Return "Book"
    End Function
End Class

' Using the Books class
Dim bookList As New Books()
bookList.Add(New Book With {.Title = "Book1", .Author = "Author1"})
```

## RAG Annotations
<!-- tags: [syncfusion, windowsforms, grid, itypedlist, booksclass] keywords: [typedlist, groupinggrid, book, records, itemproperties, listname, csharp, vb.net] -->
```