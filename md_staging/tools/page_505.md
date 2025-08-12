```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_505.jpeg
document_name: tools
page_number: 505
page_id: tools#page_505
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:16:37Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### 3.5.3.2.5.5 How to close the DateTimePickerAdv's Drop-Down by hitting ENTER key or ESC key

If you want to close the DateTimePickerAdv's drop-down when you hit the ENTER key or the ESC key, you need to set `DateTimePickerAdv.WantEnterKey` property to `false`.

| Property             | Description                                      |
|----------------------|--------------------------------------------------|
| WantEnterKey         | True – Drop-down is not closed when hitting the Enter key or Esc key<br>False – Drop-down will get closed when hitting the Enter key or Esc key |

```csharp
this.dateTimePickerAdv1.Calendar.WantEnterKey = false;
```

```vb
Me.dateTimePickerAdv1.Calendar.WantEnterKey = False
```

### 3.5.4 ColorUI Controls

The following advanced ColorUI Controls are discussed below.

#### 3.5.4.1 ColorUIControl

The Essential Tools ColorUIControl allows .NET developers to provide a standard user interface which is similar to the Visual Studio .NET color picker drop-down for selecting colors in their Windows Forms applications. The ColorUIControl implements a palette type visual interface comprising the System, Standard, Custom, and UserColor color groups. The control can be used either as a regular control that is hosted within a parent container or as a drop-down. Refer **ColorPickerButton** to use ColorUIControl as drop down.

 <!-- tags: [product, module, control, api, version?] keywords: [DateTimePickerAdv, WantEnterKey, ColorUIControl, ColorUI, ColorPickerButton, Windows Forms, drop-down, ENTER key, ESC key, System, Standard, Custom, UserColor, control] -->
```