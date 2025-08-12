```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_808.jpeg
document_name: grid
page_number: 808
page_id: grid#page_808
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:44Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### USState Class

#### Overview
The `USState` class represents a U.S. state with properties for both the state's code and name. The class is structured to be browsable and includes an override for the `ToString` method.

```csharp
public USState(string key, string name)
{
    this._code = key;
    this._name = name;
}

[Browsable(true)]
public string Key
{
    get
    {
        return _code;
    }
    set
    {
        _code = value;
    }
}

[Browsable(true)]
public string Name
{
    get
    {
        return _name;
    }
    set
    {
        _name = value;
    }
}

public override string ToString()
{
    return this._name + "(" + this._code + ")";
}
```

### USStatesCollection Class (VB.NET)

#### Overview
The `USStatesCollection` class is a serializable collection class that manages a list of `USState` objects. This class provides a structured way to handle and store U.S. state information.

```vb.net
' US States Collection.
<Serializable()>
Public Class USStatesCollection
    Inherits CollectionBase
    ...
End Class
```

## Code Examples

#### C# Example

```csharp
using System;
using System.Collections.Generic;

public class USState
{
    private string _code;
    private string _name;

    public USState(string key, string name)
    {
        this._code = key;
        this._name = name;
    }

    [System.ComponentModel.Browsable(true)]
    public string Key
    {
        get
        {
            return _code;
        }
        set
        {
            _code = value;
        }
    }

    [System.ComponentModel.Browsable(true)]
    public string Name
    {
        get
        {
            return _name;
        }
        set
        {
            _name = value;
        }
    }

    public override string ToString()
    {
        return this._name + "(" + this._code + ")";
    }
}
```

#### VB.NET Example

```vb.net
Imports System
Imports System.Collections

<Serializable()>
Public Class USStatesCollection
    Inherits CollectionBase
    ' Methods and properties related to the collection would be added here.
    ...
End Class
```

## API Reference

### USState Class

#### Properties
- **Key**: 
  - Type: `string`
  - Getter: Returns the state's code.
  - Setter: Sets the state's code.
- **Name**: 
  - Type: `string`
  - Getter: Returns the state's name.
  - Setter: Sets the state's name.

#### Methods
- **ToString**: 
  - Returns: A `string` formatted as `"Name (Code)"`.

### USStatesCollection Class

#### Attributes
- **Serializable**:
  - Marks the class as serializable.

#### Inheritance
- Inherits from `CollectionBase`.

## Cross References

See also:
- [Serialization in .NET](#serialization-in-.net)
- [Working with Collections](#working-with-collections)

<!-- tags: [winforms, grid, usstate, usstatescollection, serialization, collection] keywords: [usstate, name, key, tostring, serializable, collectionbase] -->
```