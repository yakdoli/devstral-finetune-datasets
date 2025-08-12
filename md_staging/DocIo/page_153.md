```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_153.jpeg
document_name: DocIo
page_number: 153
page_id: DocIo#page_153
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:54Z
fidelity: lossless
-->

# Essential DocIO

```csharp
textField.StatusBarHelp = "Help1";
textField.MacroOnStart = "Test1";
textField.CalculateOnExit = true;
```

## Example 2

```csharp
// In this sample we modify all text form field in document.
foreach (WSection sec in doc.Sections)
{
    foreach (WTextBody body in sec.ChildEntities)
    {
        // Every WTextBody object has a collection of form fields.
        foreach (WFormField ffield in body.FormFields)
        {
            switch (ffield.FormFieldType)
            {
                case FormFieldType.TextInput:
                    WTextFormField textField = (WTextFormField)ffield;
                    textField.Type = Text FieldType.DateText;

                    // Setting of default text of form field.
                    textField.DefaultText = "01/01/2007";
                    textField.StringFormat = "MM/dd/yyyy ";

                    // Setting character format of field (not text of form field).
                    // This formatting you can see, when you press Alt+F9 on
                    // document, which has form field.
                    textField.CharacterFormat.FontName = "Comic Sans MS";
                    textField.CharacterFormat.Shadow = true;
                    textField.CharacterFormat.FontSize = 20f;

                    // Setting text of text form field and it's character format.
                    // If textField.TextRange.Text value is not equal to
                    // string.Empty, form field's text will be textField.TextRange.Text, in
                    // other case textField.DefaultText.
                    if (textField.TextRange.Text != string.Empty)
                    {
                        textField.TextRange.Text = "";
                    }

                    textField.TextRange.CharacterFormat.FontName = "Comic Sans MS";
                    textField.TextRange.CharacterFormat.Shadow = true;
                    textField.TextRange.CharacterFormat.FontSize = 20f;
                    textField.TextRange.CharacterFormat.TextColor = Color.Blue;
                    break;

                default:
            }
        }
    }
}
```
```html

<!-- tags: [Essential DocIO, WSection, WTextBody, WFormField, FormFieldType, WTextFormField, DateText, DefaultText, StringFormat, CharacterFormat, FontName, Shadow, FontSize, TextRange, TextColor] keywords: [text form field, document sections, child entities, form fields, field format, default text, character format, font properties, text field text, text formatting, date field, DocIO, Syncfusion Winforms] -->
```