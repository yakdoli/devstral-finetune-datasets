```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_071.jpeg
document_name: calculate
page_number: 071
page_id: calculate#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:44Z
fidelity: lossless
-->

# Essential Calculate

```csharp
this.textBoxC.Leave += new EventHandler(textBoxC_Leave);
this.textBoxD.Leave += new EventHandler(textBoxD_Leave);

// 7) Allow the CalcQuickBase sheet to create dependency lists.
// Necessary for auto-calculations.
this.calculator.RefreshAllCalculations();

// 8) Raised when a variable value is calculated.
private void calculator_ValueSet(object sender, QuicKeyValueSetEventArgs e)
{
    switch (e.Key)
    {
        case "A":
            this.textBoxA.Text = this.calculator[e.Key].ToString();
            break;
        case "B":
            this.textBoxB.Text = this.calculator[e.Key].ToString();
            break;
        case "C":
            this.textBoxC.Text = this.calculator[e.Key].ToString();
            break;
        case "D":
            this.textBoxD.Text = this.calculator[e.Key].ToString();
            break;
        default:
            break;
    }
}

// 9) Handles the changing of the text in the text box so the CalQuick object
// can be updated as the text changes.
private void textBoxA_Leave(object sender, EventArgs e)
{
    if (this.textBoxA.Modified)
    {
        calculator["A"] = this.textBoxA.Text;
        this.textBoxA.Modified = false;
    }
}
// ..... same for textBoxB_Leave, textBoxC_Leave, textBoxD_Leave
```

### [VB]

```vb
Private calculator As CalcQuickBase = Nothing

Private Sub Form_Load(sender As Object, e As System.EventArgs)
    ' 1) Instantiate a CalcQuickBase object.
    calculator = New CalcQuickBase()
End Sub
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

<!-- tags: [Syncfusion Winforms, CalcQuickBase, EventHandler, Form Load, Auto-calculations, Text Box] keywords: [calculator, dependency lists, events, auto-calculations, text box events, text box leave event] -->
```