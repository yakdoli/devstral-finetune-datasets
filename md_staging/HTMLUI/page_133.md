```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_133.jpeg
document_name: HTMLUI
page_number: 133
page_id: HTMLUI#page_133
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:10:41Z
fidelity: lossless
-->

## Essential HTMLUI for Windows Forms

### Overview
- Explains how to access the location of elements using HTMLUI in Windows Forms.
- Demonstrates using the HTML Format object to apply styles.

### Content

#### HTMLFormat Interface Implementation

- **C#**
  ```csharp
  format.Font = new Font("Verdana", 12);
  format.ForeColor = Color.Blue;
  div.Format = format;
  ```

- **VB.NET**
  ```vbnet
  Implements HTMLFormat interface
  Private html As Hashtable = Me.HtmluiControl1.Document.GetElementsByIdHash()
  Private div As BaseElement = CType(IIf(TypeOf html("div1") Is BaseElement, html("div1"), Nothing), BaseElement)
  
  Private format As HTMLFormat = New HTMLFormat("ClickedPara")
  Private format.Font = New Font("Verdana", 12)
  Private format.ForeColor = Color.Blue
  Private div.Format = format
  ```

#### Accessing Element Location

- With HTMLUI, the user can also access the location of the elements in the HTMLUI control.

- **C#**
  ```csharp
  Hashtable html = this.htmluiControl1.Document.GetElementsByIdHash();
  BaseElement div = html["element"] as BaseElement;
  beginPoint = element.Location;
  endPoint = new Point(beginPoint.X + element.Size.Width, beginPoint.Y + element.Size.Height);
  ```

- **VB.NET**
  ```vbnet
  Private html As Hashtable = Me.HtmluiControl1.Document.GetElementsByIdHash()
  Private div As BaseElement = CType(IIf(TypeOf html("element") Is BaseElement, Nothing), BaseElement)
  Private beginPoint = element.Location
  Private endPoint = New Point(beginPoint.X + element.Size.Width, beginPoint.Y + element.Size.Height)
  ```

#### HTMLFormat Sample

##### 4.15.1 HTMLFormat Sample

**This sample shows how the styles are applied by using the HTML Format object.**

---

<!-- tags: [Syncfusion, HTMLUI, Windows Forms, HTMLFormat, element location, C#, VB.NET, sample, formatting, interface] keywords: [HTMLFormat, CSS样式, 元素定位, WinForms, CSharp, VB, 样式应用, 样例, 接口实现, HtmlUI] -->
```