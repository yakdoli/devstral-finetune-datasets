```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_154.jpeg
document_name: DocIo
page_number: 154
page_id: DocIo#page_154
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:33Z
fidelity: lossless
-->

### Essential DocIO

```plaintext
break;
}
}
}
```

#### [VB.NET]

**Example 1**

```vb
Dim doc As IWordDocument = New WordDocument(True)
Dim par As IWParagraph = doc.LastParagraph

' Append text form field to the paragraph.
Dim textFormField As WTextFormField = par.AppendTextFormField("Hello")
textFormField.TextFormat = TextFormat.Uppercase
textFormField.Enabled = False
textFormField.Help = "Help2"
textFormField.StatusBarHelp = "Help1"
textFormField.MacroOnStart = "Test1"
textFormField.CalculateOnExit = True
```

**Example 2**

```vb
' In this sample we modify all text form field in document.
For Each sec As WSection In doc.Sections
    For Each body As WTextBody In sec.ChildEntities

        ' Every WTextBody object has a collection of form fields.
        For Each ffield As WFormField In body.FormFields
            Select Case ffield.FormFieldType
                Case FormFieldType.TextInput
                    Dim textField As WTextFormField = CType(ffield, WTextFormField)
                    textField.Type = TextFormFieldType.DateText

                    ' Setting of default text of form field.
                    textField.DefaultText = "01/01/2007"
                    textField.StringFormat = "MM/dd/YYYY"

                    ' Setting character format of field (not text of form field).
                    ' This formatting you can see, when you press Alt+F9 on
                    ' document, which has form field.
                    textField.CharacterFormat.FontName = "Comic Sans MS"
                    textField.CharacterFormat.Shadow = True
            End Select
        Next
    Next
Next
```

## API Reference (if applicable)

### Code Examples

```vb
' Example 1: Append a text form field to the paragraph.
Dim doc As IWordDocument = New WordDocument(True)
Dim par As IWParagraph = doc.LastParagraph

Dim textFormField As WTextFormField = par.AppendTextFormField("Hello")
textFormField.TextFormat = TextFormat.Uppercase
textFormField.Enabled = False
textFormField.Help = "Help2"
textFormField.StatusBarHelp = "Help1"
textFormField.MacroOnStart = "Test1"
textFormField.CalculateOnExit = True

' Example 2: Modify all text form fields in the document.
For Each sec As WSection In doc.Sections
    For Each body As WTextBody In sec.ChildEntities
        For Each ffield As WFormField In body.FormFields
            Select Case ffield.FormFieldType
                Case FormFieldType.TextInput
                    Dim textField As WTextFormField = CType(ffield, WTextFormField)
                    textField.Type = TextFormFieldType.DateText
                    textField.DefaultText = "01/01/2007"
                    textField.StringFormat = "MM/dd/YYYY"
                    textField.CharacterFormat.FontName = "Comic Sans MS"
                    textField.CharacterFormat.Shadow = True
            End Select
        Next
    Next
Next
```

<!-- tags: [Syncfusion, DocIO, Form Fields, VB.NET, WordDocument] keywords: [text form field, document manipulation, document formatting, form fields, VB.NET, Syncfusion DocIO, WordDocument, IWordDocument, IWParagraph, WFormFields, WTextFormField, default text, form field type, character format, shadow effect, (Comic Sans MS)] -->
```