```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: HTMLUI
page_number: 064
page_id: HTMLUI#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:06:28Z
fidelity: lossless
-->

## Essential HTMLUI for Windows Forms

### Example Code: Retrieving Bitmap and Dimensions of IMG Element

#### C#

```csharp
// Gets the bitmap of the image that represents IMG element.
Hashtable hmlelements = 
    this.htmluiControl.Document.GetElementsByIdHash();
IMAGEElementImpl img = hmlelements["img"] as IMAGEElementImpl;

// Gets the width and height of the image.
this.label1.Text = "\nIMG(Image)" + img.Image.PhysicalDimension.ToString();
```

#### VB.NET

```vb
' Gets the bitmap of the image that represents IMG element.
Private hmlelements As Hashtable =
    Me.htmluiControl.Document.GetElementsByIdHash()
Private img As IMAGEElementImpl = CType(IIf(TypeOf hmlelements("img") Is
    IMAGEElementImpl, hmlelements("img"), Nothing), IMAGEElementImpl)
Me.label1.Text = Constants.vbLf & "IMG(Image)" &
    Me.img.Image.PhysicalDimension.ToString()
```

### 4.5.18 INPUT Element

#### Overview
The `INPUT` element is used for getting input from the user. It can be a text box, a button, or a check box, which is determined by the `type` attribute of the `<input>` tag in the HTML document. The `INPUTElementImpl` class is used in determining the methods and properties for this element.

#### Properties
- **UserControl**: Gets / sets the user control instance for the particular input element declared by the user.

#### Example Code: Setting the User Control Instance for an Input Element

##### C#

```csharp
// Sets the user control instance for the particular input element declared by the user.
Hashtable hmlelements =
    this.htmluiControl.Document.GetElementsByIdHash();
INPUTElementImpl txt = hmlelements["txt"] as INPUTElementImpl;
this.txt.UserControl.CustomControl.Text = "This is a textBox";
```

##### VB.NET

```vb
' User control property sets the user control instance for the particular
' input element declared by the user.
Private hmlelements As Hashtable =
    Me.HtmluiControl.Document.GetElementsByIdHash()
```

<!-- tags: [Syncfusion Winforms, HTMLUI, INPUT Element, IMAGE Element, UserControl] keywords: [HTMLUI, Windows Forms, INPUT, IMAGE, UserControl, GetElementsByIdHash, PhysicalDimension, String] -->
```