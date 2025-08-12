```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_113.jpeg
document_name: tools
page_number: 113
page_id: tools#page_113
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:29:31Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Code Example

```csharp
Syncfusion.Windows.Forms.Tools.CommandBarDockState.Float
{
    Size szmaxwrap = new Size(40, 67);
    Size szminwrap = new Size(72, 23);
    this.DoToolBarWrapping(this.tbAlign, szmaxwrap, szminwrap, arg);
}

else if ((this.commandBarAlign.DockState == 
Syncfusion.Windows.Forms.Tools.CommandBarDockState.Left) || 
(this.commandBarAlign.DockState == 
Syncfusion.Windows.Forms.Tools.CommandBarDockState.Right))
{
    Size szmaxwrap = new Size(24, 67);
    arg.ClientSize = szmaxwrap;
}
}

private void DoToolBarWrapping(ToolBar toolbar, Size szmaxwrap, Size szminwrap, Syncfusion.Windows.Forms.Tools.CommandBarWrappingEventArgs arg)
{
    Size szcurrent = arg.ClientSize;
    Size sztemp = toolbar.Size;

    int nbtncount = toolbar.Buttons.Count;
    Size szbtn = toolbar.ButtonSize;

    if ((arg.CommandBarResizeType == 
Syncfusion.Windows.Forms.Tools.CommandBarResizeType.Right) || 
(arg.CommandBarResizeType == 
Syncfusion.Windows.Forms.Tools.CommandBarResizeType.Left))
    {
        int nfactor = (int)Math.Ceiling((float)szminwrap.Width /
(float)szcurrent.Width);
        float ffactor = (float)szminwrap.Width / 
(float)szcurrent.Width;

        if (szcurrent.Width < szmaxwrap.Width)
        {
            arg.ClientSize = szmaxwrap;
        }
        else if ((nfactor > 1) && (nfactor == ffactor))
        {
            int nnewwidth = (int)Math.Ceiling((float)nbtncount / (float)nfactor) *
szbtn.Width;

            Size sznew = Size.Empty;
            if (nnewwidth > szmaxwrap.Width)
            {
```

## Page-level Navigation/TOC (if applicable)

- **Essential Tools for Windows Forms**

## Cross References

See also:
- [Other relevant section headings or API references if present on the page]

<!-- tags: [Syncfusion, WinForms, CommandBar, DockState, Tools] keywords: [resize, buttons, client size, toolbar wrapping, syncfusion windows forms] -->
``` 
