```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_025.jpeg
document_name: HTMLUI
page_number: 025
page_id: HTMLUI#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:04:04Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Creating and displaying custom controls
- Utilizing Custom tags for embedding Windows Forms controls in HTML
- Displaying MaskedTextBox, MonthCalendar, and DataGrid in an HTML Table

## Content

### 3.2.2 Creating And Displaying Custom Controls

To create and display Custom Controls:

1. Add the **Custom** tags in the HTML document to display custom Windows Forms controls. In this case, a MaskedTextBox, MonthCalendar, and DataGrid will be displayed in each of the cells in the HTML Table.

```html
[HTML]

<HTML>
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
```html
<!-- tags: [HTMLUI, custom controls, maskedittextbox, monthcalendar, datagrid, windows forms, html table, control embedding] keywords: [custom controls, html embedding, windows forms, datagrid, maskedittextbox, monthcalendar] -->
```