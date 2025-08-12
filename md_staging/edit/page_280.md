```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_280.jpeg
document_name: edit
page_number: 280
page_id: edit#page_280
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:42Z
fidelity: lossless
-->

# Frequently Asked Questions

This section illustrates the solutions for various task-based queries about Essential Edit. Following are FAQs for the Edit Control:

## How To Access the Text Associated With Individual Lines In the Selected Text Region Of the Edit Control

The below given code snippet illustrates how you can access the text associated with individual lines in the selected text region of the Edit Control.

```csharp
[C#]

string cleanedSQL = "";
if (this.editControl1.SelectedText != "")
{
    // Get the start and end points of the selection
    CoordinatePoint start = this.editControl1.Selection.Top;
    CoordinatePoint end = this.editControl1.Selection.Bottom;
    string lineText = "";
    
    for (int i = start.VirtualLine; i <= end.VirtualLine; i++)
    {
        // Get the line object
        ILexemLine lexemLine = this.editControl1.GetLine(i);
        
        // Get the tokens in each line object and append them to get the line text
        foreach (ILexem lexem in lexemLine.LineLexems)
        {
            lineText += lexem.Text;
        }
        
        // Store each of these line text
        cleanedSQL += lineText + "\n";
        lineText = "";
    }
}
```

```vb.net
[VB.NET]
```

## API Reference
- Namespace: Syncfusion.Windows.Forms
- Class: EditControl
- Members:
  - `Selection`: Represents the start and end points of the selected text.
  - `GetLine(int virtualLineIndex)`: Returns the line object at the specified virtual line index.
  - `LineLexems`: Tokenizes the text into lexemes for each line.

### Methods
- `SelectedText`: Gets the text associated with the selected region.
- `CleanedSQL`: Function to clean and concatenate text from selected lines based on tokens.

### Events
- None explicitly shown in this snippet.

## Code Examples

### C# Example
```csharp
string cleanedSQL = "";
if (this.editControl1.SelectedText != "")
{
    CoordinatePoint start = this.editControl1.Selection.Top;
    CoordinatePoint end = this.editControl1.Selection.Bottom;
    string lineText = "";
    
    for (int i = start.VirtualLine; i <= end.VirtualLine; i++)
    {
        ILexemLine lexemLine = this.editControl1.GetLine(i);
        
        foreach (ILexem lexem in lexemLine.LineLexems)
        {
            lineText += lexem.Text;
        }
        
        cleanedSQL += lineText + "\n";
        lineText = "";
    }
}
```

### VB.NET Example
```vb.net
Dim cleanedSQL As String = ""
If Me.editControl1.SelectedText <> "" Then
    Dim start As CoordinatePoint = Me.editControl1.Selection.Top
    Dim end As CoordinatePoint = Me.editControl1.Selection.Bottom
    Dim lineText As String = ""
    
    For i As Integer = start.VirtualLine To end.VirtualLine
        Dim lexemLine As ILexemLine = Me.editControl1.GetLine(i)
        
        For Each lexem As ILexem In lexemLine.LineLexems
            lineText += lexem.Text
        Next
        
        cleanedSQL += lineText & vbCrLf
        lineText = ""
    Next
End If
```

## See also
- Syncfusion.Windows.Forms.EditControl
- Selection Handling in EditControl

<!-- tags: [syncfusion-sdk, editcontrol, text-selection, line-text] keywords: [essential edit, selected text, individual lines, edit control, text access, cleaning text] -->
```