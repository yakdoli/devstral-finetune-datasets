```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: HTMLUI
page_number: 051
page_id: HTMLUI#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:05:29Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

- newValue-Indicates the current value of the ShowTitle property
- oldValue-Indicates the old value of the ShowTitle property

### [C#]

```csharp
// Event that is raised after the ShowTitle property of the HTMLUI control is changed.
this.htmluiControl.ShowTitleChanged += new
Syncfusion.Windows.Forms.HTMLUI.ValueChangedEventHandler(this.htmluiControl_ShowTitleChanged);

private void htmluiControl_ShowTitleChanged(object sender, ValueChangedEventArgs e)
{
    MessageBox.Show("ShowTitle Changed");
}
```

### [VB.NET]

```vb
' Event that is raised after the ShowTitle property of the HTMLUI control is changed.
Me.htmluiControl.ShowTitleChanged += New
Syncfusion.Windows.Forms.HTMLUI.ValueChangedEventHandler(Me.htmluiControl_ShowTitleChanged)

Private Sub htmluiControl_ShowTitleChanged(ByVal sender As Object, ByVal e As ValueChangedEventArgs)
    MessageBox.Show("ShowTitle Changed")
End Sub
```

## TitleChanged Event

The TitleChanged event is raised after the Title property of the HTMLUI control is changed. The Title value can be set explicitly by the user or it can be extracted from the title tag of the HTML document that is to be loaded into the HTMLUI control.

The event handler receives its data from the ValueChangedEventArgs. The following properties are associated with the TitleChanged event handling.

- newValue: Gets the new value for the Title
- oldValue: Gets the old value that has been changed

### [C#]

```csharp
// Event is raised after the Title property of the HTMLUI control is changed.
this.htmluiControl.TitleChanged += new
Syncfusion.Windows.Forms.HTMLUI.ValueChangedEventHandler(this.htmluiControl_TitleChanged);

private void htmluiControl_TitleChanged(object sender, ValueChangedEventArgs e)
{
```

<!-- tags: [Syncfusion Winforms, HTMLUI, Event Handling, Window Forms, Value Changed, TitleChanged, ShowTitle, Property Change] keywords: [newValue, oldValue, HTMLUI control, ShowTitle property, ValueChangedEventArgs, property handling, event, Syncfusion] -->
```