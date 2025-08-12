```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_291.jpeg
document_name: edit
page_number: 291
page_id: edit#page_291
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:11:20Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

The following code snippet illustrates how to get all the ConfigLexems in the contents of the Edit Control.

### Code Examples

#### C#
```csharp
private ArrayList GetLexems()
{
    ArrayList configLexemList = new ArrayList();
    for (int i = 1; i <= this.editControl1.PhysicalLineCount; i++)
    {
        ILexemLine line = this.editControl1.GetLine(i);
        foreach (ILexem lexem in line.LineLexems)
        {
            IConfigLexem configLexem = lexem.Config;
            configLexemList.Add(configLexem);
        }
    }
    return configLexemList;
}
```

#### VB.NET
```vb
Private Function GetLexems() As ArrayList
    Dim configLexemList As ArrayList = New ArrayList()
    Dim i As Integer
    For i = 1 To Me.editControl1.PhysicalLineCount Step i + 1
        Dim line As ILexemLine = Me.editControl1.GetLine(i)
        Dim lexem As ILexem
        For Each lexem In line.LineLexems
            Dim configLexem As IConfigLexem = lexem.Config
            configLexemList.Add(configLexem)
        Next
    Next
    Return configLexemList
End Function
```

### 5.1.2 How To Get the Tokens In Each Line Of the Edit Control

You can get the tokens present in a line of the Edit Control by getting hold of the `ILexemLine` object associated with that particular line, and then accessing its Lexems in the `LineLexems` collection. The following code snippet illustrates this.

## RAG Annotations

<!-- tags: [Syncfusion Winforms, ILexemLine, LineLexems, ArrayList, C#, VB.NET] keywords: [Edit Control, ConfigLexems, tokens, ILexem, IConfigLexem, ILexemLine, LineLexems, ArrayList, GetLexems, PhysicalLineCount, For Loop, Foreach Loop] -->

```