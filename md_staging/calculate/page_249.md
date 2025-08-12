```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_249.jpeg
document_name: calculate
page_number: 249
page_id: calculate#page_249
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:27Z
fidelity: lossless
-->

## Essential Calculate

```vb
Public Sub Form_Load(sender As Object, ByVal e As EventArgs)
    // Comma
    CalcEngine.ParseDecimalSeparator = ","

    // Semicolon
    CalcEngine.ParseArgumentSeparator = ";"

    '...... More code
End Sub
```

### How to generate error messages or exceptions while performing String-related calculations?

#### Overview
- Discusses generating error messages or exceptions during string-related calculations.
- Focuses on the `TreatStringAsZero` property to handle string multiplication operations.

#### Content

##### 5.3.2 How to generate error messages or exceptions while performing String-related calculations?

Normally, the `CalcEngine` will not display an invalid error message or exception while performing mathematical operations with string or text. To generate an invalid error message or exception, the **TreatStringAsZero** property must be set to **false**.

For example, if a string is multiplied with a number (for example, `"text" * 10`), the calculated result will be zero. But, if the `TreatStringAsZero` property is set to **false**, the `#VALUE!` exception will be generated.

##### Code Examples

1. **C#**
    ```csharp
    this.engine.TreatStringsAsZero = false;
    ```

2. **VB**
    ```vb
    Me.engine.TreatStringsAsZero = False
    ```

<!-- tags: [syncfusion, winforms, calcengine, string-related calculations, error messages, exceptions, TreatStringAsZero] keywords: [string multiplication, error handling, C#, VB, #VALUE!] -->
```