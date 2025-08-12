```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_084.jpeg
document_name: HTMLUI
page_number: 084
page_id: HTMLUI#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:43Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\listItem\ol.html");
```

```vb.net
Me.htmluiControl.LoadHTML(@"C:\MyProjects\listItem\ol.html")
```

## 4.6.19 OPTION - Option Tag

The **Option** tag is used to include items to the drop-down list. The option tag is the child of the select tag. The option tag in HTMLUI supports the **selected** attribute. This attribute specifies the control that the specified option item is to be selected at startup.

### Example

```html
<!-- File Location and Name:  C:\MyProjects\select\option.html -->
<html>
 <body>
  <p>Dear Customer, please choose your option among our following products.</p>
  <select>
   <option>Essential Tools</option>
   <option>Essential Chart</option>
   <option selected="selected">Essential HTMLUI</option>

   <!-- HTMLUI also supports this format, <option selected>Essential HTMLUI</option> -->
  </select>
 </body>
</html>
```

```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\select\option.html");
```

```vb.net
Me.htmluiControl.LoadHTML(@"C:\MyProjects\select\option.html")
```

## 4.6.20 P - Paragraph Tag

## Footer
© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [Syncfusion Winforms, HTMLUI, Option Tag, drop-down list, selected attribute] keywords: [option tag, select tag, dropdown list, selected, HTMLUI, C#, VB.NET, paragraph tag] -->
```