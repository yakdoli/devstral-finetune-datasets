```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_138.jpeg
document_name: HTMLUI
page_number: 138
page_id: HTMLUI#page_138
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:11:23Z
fidelity: lossless
-->

### Essential HTMLUI for Windows Forms

```csharp
private Bitmap CreateBitmap()
{
    FormatManager manager = new FormatManager(htmluiControl1);
    InputHTML doc = new InputHTML(@"C:\MyProjects\HTML.htm", manager);
    doc.ClientSize = new Size(550, 200);
    htmluiControl1.PrepareDocument(doc);
    return LoadFinished(doc);
}

private Bitmap LoadFinished(InputHTML document)
{
    Bitmap bmp = new Bitmap(450, 500);
    Graphics g = Graphics.FromImage(bmp);
    PaintEventArgs args = new PaintEventArgs(g, new Rectangle(0, 0, 450, 500));
    Point startPoint = new Point(-document.Margins.Right, -document.Margins.Top);
    Size oldSize = document.ClientSize;
    document.ClientSize = document.RenderRoot.Size;
    document.Draw(args, startPoint);
    g.Dispose();
    document.ClientSize = oldSize;
    return bmp;
}
```

### [VB.NET]

```vb
Private Sub button1_Click(ByVal sender As Object, ByVal e As System.EventArgs)
    Dim bmp As Bitmap = CreateBitmap()
    bmp.Save("C:\Muprojects\Bitmap.bmp")
    bmp.Dispose()
End Sub

Private Function CreateBitmap() As Bitmap
    Dim manager As FormatManager = New FormatManager(htmluiControl1)
    Dim doc As InputHTML = New InputHTML("C:\MyProjects\HTML.htm", manager)
    doc.ClientSize = New Size(550, 200)
    htmluiControl1.PrepareDocument(doc)
    Return LoadFinished(doc)
End Function

Private Function LoadFinished(ByVal document As InputHTML) As Bitmap
    Dim bmp As Bitmap = New Bitmap(450, 500)
    Dim g As Graphics = Graphics.FromImage(bmp)
    Dim args As PaintEventArgs = New PaintEventArgs(g, New Rectangle(0, 0, 450, 500))
    Dim startPoint As Point = New Point(-document.Margins.Right, -document.Margins.Top)
    Dim oldSize As Size = document.ClientSize
    document.ClientSize = document.RenderRoot.Size
    document.Draw(args, startPoint)
    g.Dispose()
End Function
```

<!-- tags: [Syncfusion Winforms, HTMLUI] keywords: [HTMLUI, Windows Forms, Bitmap, Graphics, PaintEventArgs, FormatManager, InputHTML, Document Rendering, Code Examples] -->
```