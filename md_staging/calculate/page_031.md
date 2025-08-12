```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: calculate
page_number: 031
page_id: calculate#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:10Z
fidelity: lossless
-->

# Essential Calculate

## Content

### Using the CalculateQuickBase Object

#### Step 6: Parse and Compute Calculations

[VB.NET]

```vb
' Create a new CalculateQuickBase. This object represents the CalculateEngine.
Dim cq As CalcQuickBase
cq = New CalcQuickBase()
```

Use the `ParseAndCompute` method to perform calculations by using the `CalculateEngine`.

[C#]

```csharp
// Perform calculations by using Essential Calculate.
string formula = "if(20>10,\"BIG\",\"Small\")";
string value = cq.ParseAndCompute(formula);
```

[VB.NET]

```vb
' Perform calculations by using Essential Calculate.
Dim formula As String = "if(20>10,\"BIG\",\"Small\")"
Dim value As String = cq.ParseAndCompute(formula)
```

#### Step 7: Modify Default Behavior of the CalculateEngine

You can also modify the default behavior of the `CalculateEngine` by using the `Engine` property.

### Example

The default format of appending quotation marks to the concatenated string can be eliminated by using the following code.

[C#]

```csharp
// Strings concatenated by using the ampersand operator will be returned without quotation marks.
cq.Engine.UseNoAmpersandQuotes = true;
```

[VB.NET]

```vb
' Strings concatenated by using the ampersand operator will be returned without quotation marks.
cq.Engine.UseNoAmpersandQuotes = True
```

---

> **Note:** Engine is a class that is defined as a "property" in Essential Calculate.

## API Reference

### Properties
- `UseNoAmpersandQuotes`: A Boolean property to control whether ampersand operator concatenation includes quotation marks.

### Methods
- `ParseAndCompute`: Parses and computes the given formula string using the `CalculateEngine`.

## Code Examples

### C#

```csharp
string formula = "if(20>10,\"BIG\",\"Small\")";
string value = cq.ParseAndCompute(formula);
cq.Engine.UseNoAmpersandQuotes = true;
```

### VB.NET

```vb
Dim formula As String = "if(20>10,\"BIG\",\"Small\")"
Dim value As String = cq.ParseAndCompute(formula)
cq.Engine.UseNoAmpersandQuotes = True
```

---

<!-- tags: [syncfusion, calculate, calculatequickbase, calculateengine, parseandcompute, enginroperty, usenoampersandquotes] keywords: [essential calculate, calculatequickbase, parseandcompute, default behavior, engine property, ampersand operator, quotation marks] -->
```