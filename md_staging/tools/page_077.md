```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_077.jpeg
document_name: tools
page_number: 077
page_id: tools#page_077
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:20:09Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

1. In the properties window, select the **Items** property. The **BarItem Collection Editor** will be opened. Click **Add**, to add the required number of Items.

   ![Figure 25: BarItem Collection Editor opened on clicking the Items property in the Properties Grid of PopupMenu Control](https://user-images.githubusercontent.com/123456789/123456789.png)

   **Figure 25: BarItem Collection Editor opened on clicking the Items property in the Properties Grid of PopupMenu Control**

---

### Associate the PopupMenu with the CommandBar

3. Associate the **PopupMenu** control with the **CommandBar** using the **PopupMenu** property of the **CommandBar**.

   This can be done through code as follows.

   ```csharp
   private Syncfusion.Windows.Forms.Tools.CommandBarController commandBarController1;
   private Syncfusion.Windows.Forms.Tools.CommandBar commandBar1;
   private Syncfusion.Windows.Forms.Tools.XPMenus.PopupMenu popupMenu1;
   ```

## API Reference

### Namespaces and Classes

- **Syncfusion.Windows.Forms.Tools.CommandBarController**
- **Syncfusion.Windows.Forms.Tools.CommandBar**
- **Syncfusion.Windows.Forms.Tools.XPMenus.PopupMenu**
```