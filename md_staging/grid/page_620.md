```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_620.jpeg
document_name: grid
page_number: 620
page_id: grid#page_620
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:28:33Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates a class for managing data with properties like `Index`, `Name`, `SomeValue`, and `OtherValue`.
- Provides a basic implementation of property getters and setters for encapsulation.

## Content

This section defines a class with the following fields and properties:

```csharp
string name;
double someValue;
double otherValue;

public int Index
{
    get
    {
        return index;
    }
    set
    {
        index = value;
    }
}
public string Name
{
    get
    {
        return name;
    }
    set
    {
        name = value;
    }
}
public double SomeValue
{
    get
    {
        return someValue;
    }
    set
    {
        someValue = value;
    }
}
public double OtherValue
{
    get
    {
        return otherValue;
    }
    set
    {
        otherValue = value;
    }
}
```

### Description

This class encapsulates data using private fields and public properties with getters and setters. It allows controlled access to the fields, ensuring data integrity and encapsulation.

---

## API Reference

### Class Members

#### Fields
- `name`: A `string` field for storing the name.
- `someValue`: A `double` field for storing a numerical value.
- `otherValue`: A `double` field for storing another numerical value.

#### Properties
- **Index**
  - **Get**: Returns the value of the `index` field.
  - **Set**: Assigns a new value to the `index` field.
- **Name**
  - **Get**: Returns the value of the `name` field.
  - **Set**: Assigns a new value to the `name` field.
- **SomeValue**
  - **Get**: Returns the value of the `someValue` field.
  - **Set**: Assigns a new value to the `someValue` field.
- **OtherValue**
  - **Get**: Returns the value of the `otherValue` field.
  - **Set**: Assigns a new value to the `otherValue` field.

---

## Code Examples

### Example Usage

```csharp
using System;

class Program
{
    static void Main()
    {
        // Create an instance of the class
        var data = new MyClass();

        // Set values
        data.Index = 1;
        data.Name = "Sample Data";
        data.SomeValue = 10.5;
        data.OtherValue = 20.3;

        // Access values
        Console.WriteLine("Index: " + data.Index);
        Console.WriteLine("Name: " + data.Name);
        Console.WriteLine("SomeValue: " + data.SomeValue);
        Console.WriteLine("OtherValue: " + data.OtherValue);
    }
}

class MyClass
{
    string name;
    double someValue;
    double otherValue;

    public int Index
    {
        get
        {
            return index;
        }
        set
        {
            index = value;
        }
    }
    public string Name
    {
        get
        {
            return name;
        }
        set
        {
            name = value;
        }
    }
    public double SomeValue
    {
        get
        {
            return someValue;
        }
        set
        {
            someValue = value;
        }
    }
    public double OtherValue
    {
        get
        {
            return otherValue;
        }
        set
        {
            otherValue = value;
        }
    }
}
```

This example demonstrates how to create an instance of the class, set its properties, and access the stored data.

---

## Cross References

- For more information on data binding, see the Grid control documentation.
- Refer to the Syncfusion WinForms SDK for additional examples and tutorials.

---

<!-- tags: [syncfusion, winforms, data management, encapsulation, properties, getters, setters] keywords: [Essential Grid, data class, property, getter, setter, field, encapsulation, string, double, index, name, numeric value] -->
```