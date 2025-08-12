```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_281.jpeg
document_name: edit
page_number: 281
page_id: edit#page_281
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:11:22Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

```vb
Dim cleanedSQL As String = ""
If Me.editControl1.SelectedText <> "" Then
    ' Get the start and end points of the selection
    Dim start As CoordinatePoint = Me.editControl1.Selection.Top
    Dim end As CoordinatePoint = Me.editControl1.Selection.Bottom
    Dim lineText As String = ""
    Dim i As Integer
    For i = start.VirtualLine To i <= end.VirtualLine
        ' Get the line object
        Dim lexemLine As ILexemLine = Me.editControl1.GetLine(i)

        ' Get the tokens in each line object and append them to get the line text
        Dim lexem As ILexem
        For Each lexem In lexemLine.LineLexems
            lineText += lexem.Text
        Next

        ' Store each of these line text
        cleanedSQL += lineText + "\n"
        lineText = ""
    Next
End If
```

## 5.2 How To Change the Lexems Dynamically

You can change the lexems dynamically by adding / removing the lexems by using the `Lexem.Add` and `Lexem.Remove` methods.

### C#

```csharp
//Removing Lexems from the language
this.editControl1.Language.Lexems.Remove(objconfigLex);

//Changing the lexems
objconfigLex = new ConfigLexem(this.TextBox1.Text, "", FormatType.Custom, false);
objconfigLex.IndentationGuideline = true;
objconfigLex.FormatName = "HighLight";

//Add it to the current language's Lexems collection
this.editControl1.Language.Lexems.Add(objconfigLex);
```

<!-- tags: [Syncfusion Winforms, Lexems, Dynamic Lexem Management, C#, VB.NET] keywords: [Dynamic Lexem Management, Adding Lexems, Removing Lexems, ConfigLexem, editControl, TextHighlight, FormatType.Custom] -->
```