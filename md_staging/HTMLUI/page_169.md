```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_169.jpeg
document_name: HTMLUI
page_number: 169
page_id: HTMLUI#page_169
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:12:57Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```html
<HEAD>
<TITLE>HTMLUI CUSTOM CONTROLS</TITLE>
<style>
.tttDisplay { text-decoration: none; color: #ffffff; font-family: Tahoma; font-size: 34pt; font-weight: bold; line-height: 30px; padding-left: 2px; }
</style>
</HEAD>
<BODY>

<TABLE id="CustomControls" cellSpacing="0" cellPadding="0" width="100%" bgColor="silver" border="1" height="100%" align="center">
<TR>
<TD class="tttDisplay" height="33%" width="100%" id="cctd1" vAlign="center">
<maskededittextbox id="maskedEditTextBox1" height="20" width="136"></maskededittextbox>
</TD>
</TR>

<TR>
<TD class="tttDisplay" height="33%" width="100%" id="cctd2" vAlign="center">
<monthcalendar id="monthCalendar1" width="199" height="155"></monthcalendar>
</TD>
</TR>

<TR>
<TD class="tttDisplay" height="33%" width="100%" id="cctd3" vAlign="center">
<datagrid id="dataGrid1" width="304" height="144"></datagrid>
</TD>
</TR>
</TABLE>
</BODY>
</HTML>
```

## The CustomControlBase Implementation

The `CustomControlBase` implements the base functionality of the Windows forms control on the HTML `TAG` element and loads the custom controls with its respective functionalities into the HTMLUI.

### C#
```csharp
// Event Handler Declaration.
this.htmluiControl.PreRenderDocument += new Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentEventHandler(this.htmluiControl_PreRenderDocument);
```

## Footnotes
- **Page Number**: 169
- **Copyright**: © 2013 Syncfusion. All rights reserved.

<!-- tags: [Syncfusion, Winforms, HTMLUI, CustomControlBase, PreRenderDocument, Windows Forms] keywords: [CustomControlBase, Windows forms control, HTMLUI, PreRenderDocumentEventHandler, event handler, functionality loading, custom controls, Syncfusion Winforms] -->
```