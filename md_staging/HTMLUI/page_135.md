```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_135.jpeg
document_name: HTMLUI
page_number: 135
page_id: HTMLUI#page_135
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:10:23Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```csharp
private void htmluiControl_LoadFinished(object sender, System.EventArgs e)
{
    // Returns the html element by its ID, defined in HTML document.
    IHTMLElement p = this.htmluiControl.Document.GetElementById("p");

    // Replace the  HTML inner text of current element.
    p.InnerHTML = p.InnerHTML.Replace(DEF_TIME, DEF_IMG_TAG);
    this.htmluiControl.Refresh();
}
```

### [VB.NET]

```vbnet
Private Const DEF_IMG_TAG As String = "<img src='...\\clock.jpg'>"
Private Const DEF_TIME As String = "time"

Private Sub htmluiControl_LoadFinished(ByVal sender As Object, ByVal e As System.EventArgs)

	' Returns the html element by its ID, defined in HTML document.
	Dim p As IHTMLElement = Me.htmluiControl.Document.GetElementById("p")

	' Replace the  HTML inner text of current element
	p.InnerHTML = p.InnerHTML.Replace(DEF_TIME, DEF_IMG_TAG)
	Me.htmluiControl.Refresh()
End Sub
```

The following image shows the text element `Time` replaced by an image while displayed using HTMLUI.

---
<!-- tags: [HtmlUI, Windows Forms, Replacing Text, Image Display] keywords: [HtmlUI, Windows Forms, LoadFinished, getElementById, InnerHTML, Refresh, DEF_TIME, DEF_IMG_TAG, Image] -->
```