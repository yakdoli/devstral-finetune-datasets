```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_111.jpeg
document_name: calculate
page_number: 111
page_id: calculate#page_111
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:40Z
fidelity: lossless
-->

## Essential Calculate

The second step for adding your own formula is to register your method with the `CalcEngine` object. This is done with the `AddFunction` method. This method accepts the string that is used when you reference the function in a spreadsheet formula, and the second argument is a delegate for which you pass your method. The only requirement here is that the function name should start with an alpha character and should only contain alpha-numeric characters. Additionally, the string cannot be the name of any existing library function.

### Adding a Custom Function

```csharp
[C#]

// Add formula name Mymin to the Library.
this.engine.AddFunction("Mymin", new LibraryFunction(ComputeMymin));
```

```vb
[VB]

' Add formula name Mymin to the Library.
Me.engine.AddFunction("Mymin", AddressOf ComputeMymin)
```

By convention, within the Essential Calculate library, the C# implementation method for each of the library functions that are shipped with the word "Compute" is named and followed by the name of the library function. The above code confirms to this convention, with the function name being 'Mymin' and the method name being 'ComputeMymin'. Our library functions are public members of the `CalcEngine` class, so that you can access them directly if it serves your purpose. Additionally, if you own the source code version, you can see implementation details that may be of use to you if you try to implement many custom library methods on your own.

### Note
Once this is done, you can use your custom method in the same manner as the default library functions.

### 4.5.2 Remove and Replace Function

This section discusses the Remove and Replace Function available for the `CalcEngine`.

#### Remove Function

Removing unused functions from the Function Library reduces the memory usage and speeds up parsing as well. Also, if you are only using a selected few Library functions, you may want to remove the unused ones. This can be done using the methods given below.

- To remove all functions, you can clear the hash table that holds them by using the `engine.LibraryFunctions.Clear` method.

```csharp
[C#]
```

## API Reference

### Functions
- `AddFunction(string name, LibraryFunction method)`: Registers a custom function with the `CalcEngine`.
- `RemoveFunction(string name)`: Removes a specific function from the `CalcEngine`.
- `Clear()`: Clears all functions from the `CalcEngine`.

## Code Examples

### Adding a Custom Function in C#
```csharp
this.engine.AddFunction("Mymin", new LibraryFunction(ComputeMymin));
```

### Adding a Custom Function in VB
```vb
Me.engine.AddFunction("Mymin", AddressOf ComputeMymin)
```

### Removing All Functions
```csharp
engine.LibraryFunctions.Clear();
```

<!-- tags: [CalcEngine, AddFunction, RemoveFunction, LibraryFunctions, CustomFunction, MemoryUsage, Performance, Syncfusion Windows Forms] keywords: [Custom function, library function, memory usage, parsing speed, function removal, custom method, function registration] -->
```