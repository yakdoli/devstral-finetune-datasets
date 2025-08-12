```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_098.jpeg
document_name: HTMLUI
page_number: 098
page_id: HTMLUI#page_098
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:08:57Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

By default, this sample can be found under the following location:

```
C:\Documents and Settings\username\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\HTMLUI.Windows\Samples\2.0\HTML Tags\HTMLTags
```

## 4.7 Custom Controls

The Custom Controls are not standard HTML elements but user-defined controls that are created for improving the application's richness and productivity.

The **Custom** tag is used to include the custom controls in an HTML document. The custom tag comes with two attributes: **assembly** and **class**.

- The **assembly** attribute refers to the namespace where the control is located.
- The **class** attribute represents the control.

An HTML document containing custom controls is shown below.

```html
[HTML]

<html>
<body>
	<div>
		CheckBoxAdv: <CUSTOM class="Syncfusion.Windows.Forms.Tools.CheckBoxAdv" assembly="Syncfusion.tools.windows"></CUSTOM>
	</div>
	<div>
		NumericUpDown: <CUSTOM class="NumericUpDown" assembly="System.Windows.Forms"></CUSTOM>
	</div>
</body>
</html>
```

The custom controls defined in the HTML document are interfaced with their equivalent Windows Forms control with the help of the **PreRenderDocument** event. The PreRenderDocument event occurs at a time when the HTML document is being loaded into the HTMLUI control, but the elements are not yet positioned.

The HTML elements are loaded into an hash table with an equivalent ID as their key. An equivalent Base class object, here **BaseElement** class, is defined to link the HTML elements stored in the hash table with the help of the key associated with the element. The BaseElement is the Base class for all HTML elements. All HTML tag elements inherit this class.

The **CustomControlBase** implements the base functionality of the Windows Forms control on the HTML tag element.

```csharp
[C#]
```

## Summary

## Copyright
© 2013 Syncfusion. All rights reserved.
<!-- tags: [Syncfusion, HTMLUI, Custom Controls, Windows Forms, PreRenderDocument, BaseElement, CustomControlBase] keywords: [custom controls, HTMLUI, user-defined controls, assembly namespace, class attribute, PreRenderDocument event, BaseElement class, CustomControlBase, Windows Forms, HTML tags, HTMLUI control, hash table, ID, events, HTML elements] -->
```