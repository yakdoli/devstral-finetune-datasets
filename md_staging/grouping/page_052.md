```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_052.jpeg
document_name: grouping
page_number: 052
page_id: grouping#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:40Z
fidelity: lossless
-->

# Essential Grouping

## Overview

- Demonstrates how to perform custom sorting using a custom comparer in VB.NET.
- Explains the use of SortColumnDescriptor.Comparer to specify a custom comparer object.
- Provides steps for creating a custom comparer class and integrating it into the sorting process.

## Content

### Sorting Functions

The following method overloads are available for adding sort columns:

```vb
Overloads Public Function Add(propertyName As String) As Integer
Overloads Public Function Add(propertyName As String, dir As ListSortDirection) As Integer
Overloads Public Function Add(sdc As SortColumnDescriptor) As Integer
```

The second overload allows specifying the sort direction. The `SortColumnDescriptor.Comparer` property is an `IComparer` property that enables the use of a custom comparer object.

#### Custom Sorting Using IComparer

**Note:** We are going to use the third function in this section to perform custom sorting.

The following steps illustrate how to do custom sorting using the `IComparer` property:

1. Create a class that implements `IComparer`, which can accept values such as `ax`, where `x` is a digit used for comparison. This leads to numerical sorting, ignoring the leading character.

15. Add the following code immediately after the end of the `Class1` code:

### Custom Comparer Implementation

```csharp
public class AComparer : IComparer
{
    // Implementing IComparer to define the object comparisons.
    public int Compare(object x, object y)
    {
        if (x == null && y == null)
            return 0;
        else if (x == null)
            return -1;
        else if (y == null)
            return 1;
        else
        {
            int sx = 0;
            int sy = 0;
            try
            {
                // Ignoring the leading character to have numerical sorting.
                sx = int.Parse(x.ToString().Substring(1));
                // Additional code for comparing numerical values would follow here.
            }
            // Further implementation details are omitted for brevity.
        }
    }
}
```

## API Reference

The following sections detail how to use the `SortColumnDescriptor.Comparer` property to implement custom sorting:

### Methods

- **Add(sdc As SortColumnDescriptor) As Integer:** Adds a column descriptor with a custom comparer for sorting.

## Code Examples

The provided code snippet demonstrates the creation of a custom comparer class that ignores the leading character for numerical sorting.

### Import and Using Statements

Ensure that the following namespaces are included for the code to work seamlessly in your project:

```csharp
using System;
using System.Collections;
```

### Additional Information

For further details on implementing custom sorting in Syncfusion WinForms, refer to the official documentation or contact Syncfusion support.

## Cross References

- See also: [Syncfusion WinForms Documentation](https://www.syncfusion.com/documentation/windows-forms/)

### Page-level Navigation/TOC

- [Section 1](#essentials): Essential Grouping
- [Section 2](#customsorting): Custom Sorting Using IComparer
- [Section 3](#apireference): API Reference
- [Section 4](#codeexamples): Code Examples

<!-- tags: [Syncfusion WinForms, Custom Sorting, IComparer, SortColumnDescriptor, Numerical Sorting] keywords: [custom sorting, comparer, numerical, leading character,ignore] -->
```