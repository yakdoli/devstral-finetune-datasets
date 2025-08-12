```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_248.jpeg
document_name: calculate
page_number: 248
page_id: calculate#page_248
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:14:50Z
fidelity: lossless
-->

# Essential Calculate

```csharp
engine.CalculatingSuspended = True

' Makes multiple updates to this.data somehow...
' Turn on calculations.
engine.CalculatingSuspended = False
```

## 5.3 Common

This section deals with the tasks and solutions that apply to both CalcQuick and CalcEngine.

### 5.3.1 How to Use a Comma as a Decimal Separator in Formula?

Local settings may require the use of a different decimal separator than the period character that Essential Calculate uses by default. For example, many Local settings use a comma as the decimal separator.

To manage this problem, Essential Calculate exposes two static (Shared in VB.NET) members, which you can set to specify the character that is recognized as the decimal separator and the character that is recognized as the list separator. The default values of these members are a period and a comma, respectively. You can set these static members at any point in your code before you use any Essential Calculate objects.

#### Code Example

```csharp
[C#]
public string Form_Load(object sender, EventArgs e)
{
    // Comma
    CalcEngine.ParseDecimalSeparator = ',';

    // Semicolon
    CalcEngine.ParseArgumentSeparator = ';';

    // .... More code
}
```

```vb
[VB]
```

## API Reference

## Code Examples

## Page-level Navigation/TOC

## Cross References

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```