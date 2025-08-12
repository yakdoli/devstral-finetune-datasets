```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_160.jpeg
document_name: DocIo
page_number: 160
page_id: DocIo#page_160
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:56Z
fidelity: lossless
-->

## Working with Variables

This section describes how to add, modify, and retrieve variables in a Word document using Syncfusion's DocIO library in both C# and VB.NET.

### Example: Managing Document Variables

#### C# Code Example

```csharp
WordDocument doc = new WordDocument();
doc.Open("Sample.doc");
DocVariables v = document1.Variables;

// Add a variable
v.Add("var1", "Author Name");

// Add / modify variables:
v["var2"] = "change name";

Console.WriteLine("Number of Variables:" + document1.Variables.Count.ToString());
Console.WriteLine("Variable Name:" + document1.Variables.GetNameByIndex(0));
Console.WriteLine("Variable Value:" + document1.Variables.GetValueByIndex(0));

doc.Save("SampleModified.doc");
```

#### VB.NET Code Example

```vbnet
Dim doc As WordDocument = New WordDocument()
doc.Open("Sample.doc")
Dim v As DocVariables = document1.Variables

' Add a variable
v.Add("var1", "Author Name")

' Add / modify variables:
v("var2") = "change name"

Console.WriteLine("Number of Variables:" + document1.Variables.Count.ToString())
Console.WriteLine("Variable Name:" + document1.Variables.GetNameByIndex(0))
Console.WriteLine("Variable Value:" + document1.Variables.GetValueByIndex(0))

doc.Save("SampleModified.doc")
```

---

### Explanation

1. **Opening a Document**:
   - The `WordDocument` class is used to open an existing Word document named `Sample.doc`.

2. **Accessing Variables**:
   - The `document1.Variables` property is accessed to get the `DocVariables` instance, which allows managing variables in the document.

3. **Adding Variables**:
   - The `Add` method is used to insert a new variable with the key `var1` and the value `Author Name`.

4. **Modifying Variables**:
   - Variables can be added or modified using the indexer notation. Here, `var2` is either added or updated to the value `"change name"`.

5. **Retrieving Variables**:
   - The count of variables in the document is printed using `document1.Variables.Count`.
   - The name of the variable at the specified index (0 in this case) is retrieved using `GetNameByIndex(0)`.
   - The corresponding value of the variable at index 0 is retrieved using `GetValueByIndex(0)`.

6. **Saving the Modified Document**:
   - The modified document is saved as `SampleModified.doc`.

---

### Notes

- Ensure that the `WordDocument` and `DocVariables` classes are properly imported and that the necessary assemblies are referenced.
- The `DocVariables` feature is useful for managing structured data within Word documents programmatically.

---

<!-- tags: [docio, word document, variables, csharp, vb.net, syncfusion winforms, version 11.4.0.26] keywords: [word variables, document management, csharp example, vb.net example, docio library, syncfusion, word document manipulation] -->
```