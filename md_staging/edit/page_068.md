```html
<!--  
source: image  
domain: syncfusion-sdk  
task: pdf-ocr-to-markdown  
language: en  
source_filename: page_068.jpeg  
document_name: edit  
page_number: 068  
page_id: edit#page_068  
product: Syncfusion Winforms  
version: 11.4.0.26  
timestamp: 2025-08-09T04:58:08Z  
fidelity: lossless  
-->  

## Essential Edit for Windows Forms  

### Underlining Options  

|  |  |
| --- | --- |
|  | UnderLineStyle.Dot, UnderLineStyle.Dash, UnderLineStyle.Wave, and UnderLineStyle.DashDot. |
| UnderlineWeight | UnderlineWeight.Thick(default) and UnderlineWeight.Double. |

### Underlining Selected Text  

Underlining can be set and removed for selected text by using the below given methods.  

#### Underlining Methods  

| Edit Control Method | Description |
| --- | --- |
| SetUnderline | Sets underlining of the specified text region. |
| RemoveUnderLine | Removes underlining in the specified region. |

#### Example Code  

```csharp
[C#]

this.editControl1.SetUnderline(this.editControl1.Selection.Top, 
this.editControl1.Selection.Bottom, format);
this.editControl1.RemoveUnderline(this.editControl1.Selection.Top, 
this.editControl1.Selection.Bottom);
```

```vbnet
[VB.NET]

Me.editControl1.SetUnderline(Me.editControl1.Selection.Top, 
Me.editControl1.Selection.Bottom, format)
Me.editControl1.RemoveUnderline(Me.editControl1.Selection.Top, 
Me.editControl1.Selection.Bottom)
```

### Underlining using Configuration File  

You can also set the underlining from the configuration file, as shown in the below example.  

#### Configuration Example  

```xml
[XML]

<format name="Comment" Font="Courier New, 10pt, style=Bold" FontColor="Green" 
LineColor="Red" Weight="Thick" Underline="DashDot" />
```  

<!-- tags: [Syncfusion Winforms, edit, underlining, configuration file, version 11.4.0.26] keywords: [underlining, selected text, set underline, remove underline, configuration file, text formatting, underlinestyle, underlineweight, edit control method, linecolor, weight, font] -->
``` 
