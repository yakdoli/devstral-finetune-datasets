```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_678.jpeg
document_name: grid
page_number: 678
page_id: grid#page_678
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:33:55Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Demonstrates the use of a C# class that manages category data.
- Includes getter and setter methods for properties related to `cat_Id`, `cat_Name`, and `desc`.

## Content

### Class Implementation

#### C#

```csharp
this.cat_Id = cat_Id;
this.cat_Name = cat_Name;
this.desc = desc;

private string cat_Name;
public string CategoryName
{
    get
    {
        return this.cat_Name;
    }
    set
    {
        this.cat_Name = value;
    }
}

private string desc;
public string Description
{
    get
    {
        return this.desc;
    }
    set
    {
        this.desc = value;
    }
}

private string cat_Id;
public string CategoryID
{
    get
    {
        return this.cat_Id;
    }
    set
    {
        this.cat_Id = value;
    }
}
```

#### VB.NET

```vb
Public Class Data
```

## API Reference

### Properties

#### `CategoryName`

- Getter: Returns the value of `cat_Name`.
- Setter: Assigns a value to `cat_Name`.

#### `Description`

- Getter: Returns the value of `desc`.
- Setter: Assigns a value to `desc`.

#### `CategoryID`

- Getter: Returns the value of `cat_Id`.
- Setter: Assigns a value to `cat_Id`.

## Code Examples

#### C#

```csharp
public void UpdateCategoryDetails(string newName, string newDescription)
{
    this.CategoryName = newName;
    this.Description = newDescription;
}

public string GetCategoryInfo()
{
    return $"Category ID: {this.CategoryID}, Name: {this.CategoryName}, Description: {this.Description}";
}
```

#### VB.NET

```vb
Public Sub UpdateCategoryDetails(ByVal newName As String, ByVal newDescription As String)
    Me.CategoryName = newName
    Me.Description = newDescription
End Sub

Public Function GetCategoryInfo() As String
    Return $"Category ID: {Me.CategoryID}, Name: {Me.CategoryName}, Description: {Me.Description}"
End Function
```

## Cross References

- Related pages or sections on grid functionality, data management, and property bindings within the Syncfusion documentation.

<!-- tags: [essential grid, windows forms, category data, properties, getters, setters, csharp, vb.net] keywords: [cat_Id, cat_Name, desc, CategoryName, Description, CategoryID, data management, getter, setter, property binding] -->
```