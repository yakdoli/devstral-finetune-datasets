```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_023.jpeg
document_name: grouping
page_number: 023
page_id: grouping#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:56Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Creating a new console project.
- Defining a custom object class and integrating it into the generated code.
- Sample code for the custom object class with properties and constructor.

## Content

### Creating a New Console Project

Figure 11 illustrates the process of creating a new console project in Visual Studio.

```plaintext
Name:          GroupingSample
Location:      C:\A_SyncWork\incident
```

#### Step 1: Create a Custom Object Class
Create a custom object class and add it to the 'Class1' file generated in the first step. Name the class 'MyObject', and define it with the following properties:

- Four string properties named A, B, C, and D.
- A constructor that accepts an integer argument.

**Note:** The B property is designed to hold digits and will be used later for summarizing data.

#### Sample Code for the Custom Object Class

```csharp
using System;

namespace GroupingSample
{
    class Class1
    {
        [STAThread]
        static void Main(string[] args)
        {
        }
    }

    public class MyObject
    {
        // Properties and constructor to be defined here
    }
}
```

### Explanation of the Code
The provided code snippet includes the basic structure for the console application and the starting point for defining the `MyObject` class. The `MyObject` class will include the required properties and a constructor as specified.

## API Reference

### Class `MyObject`
- **Properties**:
  - `A` (string)
  - `B` (string)
  - `C` (string)
  - `D` (string)
- **Constructor**:
  - Accepts an integer argument for initialization.

## Code Examples

### Full Sample Code
```csharp
using System;

namespace GroupingSample
{
    class Class1
    {
        [STAThread]
        static void Main(string[] args)
        {
            // Example usage of MyObject
            MyObject obj = new MyObject(123);
            Console.WriteLine(obj.A);
            Console.WriteLine(obj.B);
            Console.WriteLine(obj.C);
            Console.WriteLine(obj.D);
        }
    }

    public class MyObject
    {
        public string A { get; set; }
        public string B { get; set; }
        public string C { get; set; }
        public string D { get; set; }

        public MyObject(int value)
        {
            A = "InitialA";
            B = value.ToString(); // B holds digits
            C = "InitialC";
            D = "InitialD";
        }
    }
}
```

## Cross References
- Refer to the generated 'Class1' file for further implementation details.
- Ensure the custom object class integrates seamlessly with the existing application logic.

<!-- tags: [Syncfusion, WinForms, data grouping, console application, custom object class] keywords: [GroupingSample, MyObject, Class1, properties, constructor, data summarization, digits] -->
```