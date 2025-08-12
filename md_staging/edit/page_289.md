```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_289.jpeg
document_name: edit
page_number: 289
page_id: edit#page_289
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:11:49Z
fidelity: lossless
-->

## Overview
- This section explains how to format keywords in the contents of the Edit Control using configuration settings.
- It demonstrates handling the `ConfigurationChanged` event and the `OnCustomDraw` event to perform string manipulations on tokens of the "Format" keyword.

## Content

### 5.9 How To Format Keywords In the Contents Of the Edit Control Using Configuration Settings

Handle the `ConfigurationChanged` event of the Edit Control and get all the tokens of the "Format" keyword. Then, handle the `OnCustomDraw` event of each of these tokens and perform string manipulation operations. The following code snippet illustrates this.

#### Code Examples
- **C#**

```csharp
private void editControl_ConfigurationChanged(object sender, System.EventArgs e)
{
    foreach ( FormatManager lang in editControl.Languages )
    {
        Format format = lang[FormatType.KeyWord] as Format;
        if( format != null )
        {
            format.OnCustomDraw += new
            CustomSnippetDrawEventHandler(format_OnCustomDraw);
        }
    }
}

private void format_OnCustomDraw(object sender, CustomSnippetDrawEventArgs e)
{
    string text = e.Text;
    text = text.ToLower();
    text = text[0].ToString().ToUpper() + text.Substring( 1, text.Length - 1 );
    e.Text = text;
}
```

- **VB.NET**

```vb
Private Sub editControl_ConfigurationChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles EditControl.ConfigurationChanged
    Dim lang As FormatManager
    For Each lang In editControl.Languages
        Dim format As Format = lang(FormatType.KeyWord)
        If Not (format Is Nothing) Then
            AddHandler format.OnCustomDraw, AddressOf format_OnCustomDraw
        End If
    Next
End Sub

Private Sub format_OnCustomDraw(ByVal sender As Object, ByVal e As CustomSnippetDrawEventArgs)
    Dim text As String = e.Text
    text = text.ToLower()
    text = text(0).ToString().ToUpper() + text.Substring(1, text.Length - 1)
    e.Text = text
End Sub
```

## API Reference
- **Events:**
  - `ConfigurationChanged`: Triggered when the configuration of the Edit Control changes.
  - `OnCustomDraw`: Triggered to customize the drawing of specific tokens.

- **Classes/Methods:**
  - `FormatManager`: Manages formatting settings for different types.
  - `Format`: Represents a specific format type.
  - `CustomSnippetDrawEventArgs`: Contains the text to be formatted.
  - `CustomSnippetDrawEventHandler`: Event handler for custom drawing of formatted text.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Edit Control, Formatted Text, Keywords, Configuration settings, OnCustomDraw, FormatManager, CustomSnippetDraw] keywords: [ConfigurationChanged, Keywords, Tokens, OnCustomDraw, Formatting, CustomDrawing, String Manipulation, C#, VB.NET, Edit Control] -->
```