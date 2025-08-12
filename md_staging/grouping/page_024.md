```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: grouping
page_number: 024
page_id: grouping#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:03Z
fidelity: lossless
-->

## Example: Essential Grouping in a WinForms Application

### Overview
- Demonstrates the implementation of grouping in a WinForms application.
- Shows how to create a class `MyObject` with properties for grouping and displaying data.
- Includes a constructor that initializes the object with a numerical parameter.
- Provides public string properties `A`, `B`, `C`, and `D` for accessing grouped data.
- Overrides the `ToString` method for custom string representation.

### Code Example

#### C#

```csharp
{
    private string aValue;
    private string bValue;
    private string cValue;
    private string dValue;

    public MyObject(int i)
    {
        aValue = string.Format("a{0}", i);

        // Use digit only.
        bValue = string.Format("{0}", i);
        cValue = string.Format("c{0}", i % 3);
        dValue = string.Format("d{0}", i % 2);
    }

    public string A
    {
        get { return aValue; }
        set { aValue = value; }
    }

    public string B
    {
        get { return bValue; }
        set { bValue = value; }
    }

    public string C
    {
        get { return cValue; }
        set { cValue = value; }
    }

    public string D
    {
        get { return dValue; }
        set { dValue = value; }
    }

    public override string ToString()
    {
        return A + "\t" + B + "\t" + C + "\t" + D;
    }
}
```

#### VB.NET

```vb
Module Module1
```

### Explanation
- **Constructor**: The `MyObject` constructor initializes the private fields `aValue`, `bValue`, `cValue`, and `dValue` based on the input integer `i`. The `string.Format` method is used to create formatted strings.
- **Properties**: The `A`, `B`, `C`, and `D` properties provide access to the private fields, allowing both retrieval and modification of the values.
- **ToString Method**: Overrides the default `ToString` method to return a tab-separated string representation of the object's values.

#### Notes:
- The use of the modulus operator (`%`) in the calculations for `cValue` and `dValue` suggests a cyclic behavior based on the input `i`.
- The `ToString` method formats the output in a tabular form, making it suitable for display in a grid or table.

### API Reference

#### Class
- **MyObject**
  - **Constructor**: `MyObject(int i)`
    - Initializes the object with a numerical parameter `i`.
  - **Properties**:
    - `A`: A string property representing the first group.
    - `B`: A string property representing the second group.
    - `C`: A string property representing the third group.
    - `D`: A string property representing the fourth group.
  - **Method**:
    - `ToString()`: Overrides the default implementation to provide a custom string representation of the object.

### RAG Annotations
<!-- tags: [Syncfusion Winforms, grouping, MyObject, C#, VB.NET, property, ToString] keywords: [grouping, WinForms, object initialization, property accessor, tab-separated string, override, modulus, tabular display] -->
```