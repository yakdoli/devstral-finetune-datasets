```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_071.jpeg
document_name: tools
page_number: 071
page_id: tools#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:18:32Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

![Figure 19: CommandBar and Buttons in the Designer](https://i.imgur.com/bTwkc9D.png)

Figure 19: CommandBar and Buttons in the Designer

### Adjusting Docking State for CommandBar

1. **Specify the Docking State:**
   - Use the following steps to specify the docking state of the `CommandBar` based on the button click event.

2. **Code Snippet for C#:**

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    Button btn = sender as Button;
    // Dock to the Top
    if (btn == this.top)
        this.commandBar1.DockState = CommandBarDockState.Top;
    // Dock to the Bottom
    if (btn == this.bottom)
        this.commandBar1.DockState = CommandBarDockState.Bottom;
    // Dock to the Right
    if (btn == this.right)
        this.commandBar1.DockState = CommandBarDockState.Right;
    // Dock to the Left
    if (btn == this.left)
        this.commandBar1.DockState = CommandBarDockState.Left;
    // Dock as Floating
    if (btn == this.float_btn)
        this.commandBar1.DockState = CommandBarDockState.Float;
}
```

3. **Code Snippet for VB.NET:**
   - The VB.NET equivalent code will follow similar logic but with slight syntactical differences, which can be provided upon request.

<!-- tags: [Windows Forms, CommandBar, DockingState, C#] keywords: [CommandBar, DockState, Windows Forms, Adjusting Dock State, C# Sample] -->
```