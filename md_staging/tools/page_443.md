```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_443.jpeg
document_name: tools
page_number: 443
page_id: tools#page_443
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:13:25Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

This section deals with replacing MonthCalendarAdv 'Go to Today' ContextMenu with a Custom Context Menu. At run-time, you can right click any calendar date and go to the today date using 'Go to Today' ContextMenu.

![Figure 243: 'Go to Today' Context Menu](https://user-images.githubusercontent.com/115620278/244689249-7a86e528-ff5b-4f7d-ba1b-ebaff2461d5f.png)

### Overview
- Explains how to replace the default 'Go to Today' ContextMenu in MonthCalendarAdv with a custom menu.
- Instructions for creating a custom MonthCalendarAdv by deriving from the existing one and overriding the necessary methods.

### Content

This is the default context menu. To replace this with a custom context menu, you need to derive a Custom MonthCalendarAdv from the existing one and override the InitializeGrid so that the GetInternalGridControl method can be used to access the ContextMenu and replace it with a custom contextMenu.

It can be done programmatically using the below code snippet.

```csharp
[C#]

// Declaring and Initializing the calendar, Context menu and menu item
private CustomMonthCalendarAdv monthCalendarAdv1;
private System.Windows.Forms.MenuItem menuItem1;
private System.Windows.Forms.ContextMenu contextMenuStrip1;

this.contextMenuStrip1 = new System.Windows.Forms.ContextMenu();
this.menuItem1 = new System.Windows.Forms.MenuItem();
this.monthCalendarAdv1 = new
MonthCalendar.Form1.CustomMonthCalendarAdv();

this.contextMenuStrip1.MenuItems.AddRange(new
System.Windows.Forms.MenuItem[] { this.menuItem1 });
this.menuItem1.Text = "Go To Tomorrow";
this.menuItem1.Click += new System.EventHandler(this.menuItem1_Click);

// Override the internal grid context menu using the custom context menu
private void Form1_Load_1(object sender, EventArgs e)
```

### API Reference (if applicable)
- **Namespace**: System.Windows.Forms
- **Class**: ContextMenu, MenuItem
- **Methods**: AddRange, Click event handling

### Code Examples (multi-language supported)
- The provided code snippet shows how to create a custom context menu for MonthCalendarAdv, including menu items and event handlers.

### Cross References
- Refer to MonthCalendarAdv documentation for detailed information on initialization and customization.

<!-- tags: [WinForms, MonthCalendarAdv, ContextMenu, CustomMenu, Tooltips, Windows Forms] keywords: [MonthCalendarAdv, 'Go to Today', ContextMenu, CustomMenu, programming, customizing] -->
```