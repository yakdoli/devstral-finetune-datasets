```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_177.jpeg
document_name: HTMLUI
page_number: 177
page_id: HTMLUI#page_177
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:13:27Z
fidelity: lossless
-->

## Essential HTMLUI for Windows Forms

```csharp
IHTMLElement image = Global.Document.GetElementByUserId("img");
image.Click += new EventHandler(image_Click);
IHTMLElement[] elem = this.htmluiControl.Document.GetElementsByName("td");

public void image_Click(object sender, EventArgs e)
{
    string visibleString = "";
    htmluiControl.BeginUpdate();
    if (this.bDescriptionHidden == false)
        visibleString = "false";
    else
        visibleString = "true";
    this.bDescriptionHidden = !this.bDescriptionHidden;
    foreach (IHTMLElement description in elem)
    {
        if (description.ID == "tdpopup")
            description.Attributes["xVisible"].Value = visibleString;
    }
    htmluiControl.EndUpdate();
    this.htmluiControl.Refresh();
}
```

### [VB.NET]

```vb
Private image As IHTMLElement = Global.Document.GetElementByUserId("img")
Private image.Click += New EventHandler(image_Click)
Private elem As IHTMLElement() = Me.htmluiControl.Document.GetElementsByName("td")

Public Sub image_Click(ByVal sender As Object, ByVal e As EventArgs)
    Dim visibleString As String = ""
    htmluiControl.BeginUpdate()
    If Me.bDescriptionHidden = False Then
        visibleString = "false"
    Else
        visibleString = "true"
    End If
    Me.bDescriptionHidden = Not Me.bDescriptionHidden
    For Each description As IHTMLElement In elem
        If description.ID = "tdpopup" Then
            description.Attributes("xVisible").Value = visibleString
        End If
    Next description
    htmluiControl.EndUpdate()
    Me.htmluiControl.Refresh()
End Sub
```

```html
<!-- tags: [product, windows.forms, htmlui, event_handling, xvisible, properties] keywords: [page_177, image_click, htmlui_control, event_handler, xvisible, description_hidden, begin_update, end_update, refresh] -->
```