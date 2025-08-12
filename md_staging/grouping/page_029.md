```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_029.jpeg
document_name: grouping
page_number: 029
page_id: grouping#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:34Z
fidelity: lossless
-->

# Essential Grouping

## Overview

- Demonstrates how to iterate through a `Records` collection and display output in the Console.
- Explains the concept of interacting with the operating system using the Console interface.
- Provides C# and VB.NET examples for accessing data directly from the Engine.

## Content

### Iterating through the Records Collection

Add the following code to the main function. This code will iterate through the `Records` collection and will display the output in the Console.

#### Console Interface Note

> **Note:**  
> Console is a text-only user interface that allows the user to interact with the operating system or text-based application by entering the text through the keyboard and reading the text output from the computer screen.

#### C# Example

```csharp
// Access the data directly from the Engine.
foreach (Record rec in groupingEngine.Table.Records)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}

// Pause
Console.ReadLine();
```

#### VB.NET Example

```vb.net
' Access the data directly from the Engine.
Dim rec As Record
For Each rec In groupingEngine.Table.Records
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec

' Pause
Console.ReadLine()
```

### Explanation

- **Accessing Data:**  
  The code demonstrates how to access data directly from the `groupingEngine.Table.Records` collection. Each record is processed using a loop, and its data is retrieved using the `GetData()` method.
  
- **Type Casting:**  
  The data retrieved from each record is cast to the `MyObject` type using `as` in C# and `CType` in VB.NET. The code checks if the cast was successful (`obj != null` in C# and `Not obj Is Nothing` in VB.NET) before displaying the object.

- **Pause Option:**  
  The `Console.ReadLine()` method is used to pause the program, allowing the user to see the output in the Console before the program terminates.

### Key Steps

1. **Iterate through Records:**  
   Use a `foreach` loop in C# or a `For Each` loop in VB.NET to iterate through the `Records` collection.

2. **Retrieve Data:**  
   Call the `GetData()` method on each record to retrieve its data and cast it to the appropriate type.

3. **Check for Null:**  
   Ensure that the retrieved object is not `null` before attempting to display it in the Console.

4. **Display Output:**  
   Use `Console.WriteLine()` to display the retrieved data in the Console.

5. **Pause Program:**  
   Use `Console.ReadLine()` to pause the program, allowing the user to view the output.

## API Reference

### Methods

- `GetData()`  
  Retrieves the data associated with a record.
- `Console.WriteLine()`  
  Displays the specified data in the Console.
- `Console.ReadLine()`  
  Waits for the user to press a key before continuing.

## Code Examples

### C# Example

```csharp
// Access the data directly from the Engine.
foreach (Record rec in groupingEngine.Table.Records)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}

// Pause
Console.ReadLine();
```

### VB.NET Example

```vb.net
' Access the data directly from the Engine.
Dim rec As Record
For Each rec In groupingEngine.Table.Records
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec

' Pause
Console.ReadLine()
```

## RAG Annotations

<!-- tags: [product: Syncfusion Winforms, version: 11.4.0.26] keywords: [Essential Grouping, Records collection, Console interface, C# example, VB.NET example, GetData(), Console.WriteLine(), Console.ReadLine()] -->
```