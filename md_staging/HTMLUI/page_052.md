```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_052.jpeg
document_name: HTMLUI
page_number: 052
page_id: HTMLUI#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:05:44Z
fidelity: lossless
-->

## Content

### 4.3.1 HTMLUI Control Events Sample

This sample illustrates the different events executed by the HTMLUI control.

```csharp
MessageBox.Show("Title Changed");
}
```

#### [VB.NET]

```vb
' Event is raised after the Title property of the HTMLUI control is changed.
Me.HtmlUICtl.TitleChanged += New
Syncfusion.Windows.Forms.HTMLOI.ValueChangedEventHandler(Me.htmluiControl_TitleChanged)

Private Sub htmluiControl_TitleChanged(ByVal sender As Object, ByVal e As
ValueChangedEventArgs)
    MessageBox.Show("Title Changed")
End Sub
```

#### Figure: HTMLUIControlEvents Sample

The following figure depicts the various events executed by the HTMLUI control.

![HTMLUI Control Events Sample](https://i.imgur.com/XY5D03q.png)

**Figure 24: HTMLUIControlEvents Sample**

### Additional Notes
- The events listed in the screenshot include `LoadStarted`, `LoadFinished`, `LoadError`, `PreRenderDocument`, `TitleChanged`, and `ShowTitleChanged`.
- Buttons for `Load Document`, `Change Title`, and `Clear` are present for user interaction.

## Cross References
- For more details on event handling in HTMLUI, refer to the previous sections on Events in the documentation.

<!-- tags: [HTMLUI, events, VB.NET, Syncfusion] keywords: [HTMLUI control, events, LoadStarted, LoadFinished, LoadError, PreRenderDocument, TitleChanged, ShowTitleChanged] -->
```