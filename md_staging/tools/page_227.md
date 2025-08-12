```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_227.jpeg
document_name: tools
page_number: 227
page_id: tools#page_227
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:47:58Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
-探讨了Docking 窗口的 DragAllow 事件触发条件及其使用方法。
- 描述了 DragAllow 事件的数据属性及其用途。
- 提供了 C# 示例代码，展示了如何处理 DragAllow 事件的逻辑。

## Content

### 3.4.3.8.7.1 DragAllow Event

#### 描述
The DragAllow event is triggered when a docking window is about to be dragged. Whenever the user wants to dock a control, he will try to drag the control, to dock it to a particular target. This event will be raised, when this dragging process starts.

#### Event Data

DragAllowEventHandler receives an argument of type DragAllowEventArgs containing data related to this event. The following DragAllowEventArgs properties provides information specific to this event.

| Members | Description |
|---------|-------------|
| Cancel | This property gets / sets the value indicating whether the event should be canceled. |
| Control | The control that is about to be dragged. |

#### 示例代码 (C#)

```csharp
[C#]

// The DragAllow event occurs when a docking window is about to be dragged.
private void dockingManager1_DragAllow(object sender, Syncfusion.Windows.Forms.Tools.DragAllowEventArgs arg)
{
    Console.WriteLine("DragAllow Event has been triggered");
    //arg.Control property gives the reference to be dragged.
    if(arg.Control==this.panell)
    {
        //arg.Cancel is the property used to cancel the drag operation when it's in true state.
        arg.Cancel=true;
    }
}
```

## API Reference

- **DragAllowEventArgs**: 
  - **Cancel**: A property to get or set the value indicating whether the event should be canceled.
  - **Control**: A property that provides the reference to the control that is about to be dragged.

---

<!-- tags: [product, winforms, event, dragallow, eventargs, control, cancel, dockmanager] keywords: [syncfusion, drag, allow, event, window, docking, control, c#, code] -->
```