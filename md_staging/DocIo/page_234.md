```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_234.jpeg
document_name: DocIo
page_number: 234
page_id: DocIo#page_234
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:43:02Z
fidelity: lossless
-->

# Essential DocIO

```vb
paragraph = section.AddParagraph()
paragraph.AppendText("First bulleted ( level 0 )")
paragraph.ListFormat.ApplyDefBulletStyle()

paragraph = section.AddParagraph()
paragraph.AppendText("Level 1")
paragraph.ListFormat.ContinueListNumbering()
paragraph.ListFormat.IncreaseIndentLevel()

paragraph = section.AddParagraph()
paragraph.AppendText("Level 0")
paragraph.ListFormat.ContinueListNumbering()
paragraph.ListFormat.DecreaseIndentLevel()

section.AddParagraph()
section.AddParagraph()

'Write mixed bulleted and numbered list
Dim myStyle As ListStyle = doc.AddListStyle(ListType.Numbered, "UserStyle")
Dim listLevel1 As WListLevel = myStyle.Levels(0)
listLevel1.FollowCharacter = FollowCharacterType.Tab
listLevel1.TextPosition = 80f
listLevel1.NumberAlignment = ListNumberAlignment.Right
listLevel1.TabSpaceAfter = 40f
listLevel1.StartAt = 3
listLevel1.NumberPrefix = "(("
listLevel1.NumberSufix = "**"

paragraph = section.AddParagraph()
paragraph.AppendText("First numbered")
paragraph.ListFormat.ApplyStyle("UserStyle")

paragraph = section.AddParagraph()
Dim bulletStyle As ListStyle = doc.AddListStyle(ListType.Bulleted, "UserStyle1")
Dim level As WListLevel = bulletStyle.Levels(0)
level.NumberPosition = 30f
level.TabSpaceAfter = 15f
level.FollowCharacter = FollowCharacterType.Tab

paragraph.AppendText("First bullet")
paragraph.ListFormat.ApplyStyle("UserStyle1")

paragraph = section.AddParagraph()
paragraph.AppendText("Bulleted level 1")
paragraph.ListFormat.ContinueListNumbering()
```

**Copyright © 2013 Syncfusion. All rights reserved.**  
**Page 234 |**

<!-- tags: [product, module, control, api, version?]
keywords: [DocIO, WinForms, ListStyle, Bulleted, Numbered, Syncfusion.Windows.Forms, version] -->
```