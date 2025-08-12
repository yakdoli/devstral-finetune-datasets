```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_088.jpeg
document_name: edit
page_number: 088
page_id: edit#page_088
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:59:13Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

```csharp
customBookmark.UseInBookmarkSearch = True

' Removes the bookmark of the current line.
Dim customBookmark As ICustomBookmark = 
Me.editControl.RemoveCustomBookmark(Me.editControl.CurrentLine, 
BookmarkPaintEventHandler(CustomBookmarkPainter))
```

### Setting Tooltips for Bookmarks

Tooltips can be set for bookmarks and customized by using the below given properties.

| Edit Control Property            | Description                                              |
|----------------------------------|----------------------------------------------------------|
| ShowBookmarkTooltip             | Specifies whether the tooltip of the bookmark is shown. |
| BookmarkTooltipBackgroundBrush  | Gets / sets brush for bookmark tooltip background.      |
| BookmarkTooltipBorderColor      | Specifies the color of the bookmark tooltip form border. |

```csharp
// Shows the tooltip of the bookmark.
this.editControl.ShowBookmarkTooltip = true;

// Gets or sets brush for bookmark tooltip background.
this.editControl.BookmarkTooltipBackgroundBrush = new
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.PatternStyle.Percent05, 
System.Drawing.SystemColors.WindowText, System.Drawing.Color.Gold);

// Specify the color of the bookmark tooltip form border.
this.editControl.BookmarkTooltipBorderColor = 
System.Drawing.Color.Crimson;
```

```vb
' Shows the tooltip of the bookmark.
Me.editControl.ShowBookmarkTooltip = True

' Gets or sets brush for bookmark tooltip background.
Me.editControl.BookmarkTooltipBackgroundBrush = New
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.PatternStyle.Percent05, 
System.Drawing.SystemColors.WindowText, System.Drawing.Color.Gold)

' Specify the color of the bookmark tooltip form border.
Me.editControl.BookmarkTooltipBorderColor =
```
```html
<!-- tags: [Syncfusion Winforms, Edit Control, Bookmarks, Tooltips, Properties] keywords: [ShowBookmarkTooltip, BookmarkTooltipBackgroundBrush, BookmarkTooltipBorderColor, CustomBookmarkPainter] -->
```
```