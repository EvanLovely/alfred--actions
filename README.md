# Alfred Actions

> It's like iOS Drafts for Mac

This allows you to create text (from about a half dozen ways), copy it, then be presented with a list of Actions that do things to the copied text. That list is just a folder of scripts, and is easy to add to and alter. Some of the things that can be done after Actioning some text are:

- Send text to new note (Evernote, nvAlt, and Mac Notes support)
- Create new email (Apple Mail or Gmail)
- Append text to bottom of file (great for running lists)
- Post to Twitter, Facebook, or LinkedIn
- Send new iMessage
- Shorten URL
- Create new task in OmniFocus or Reminders (and optionally add due date)
- Augment text:
    - Replace spaces with underscores
    - Capitalize/lower case

# Install Instructions

- [Download](https://github.com/EvanLovely/alfred--actions/blob/master/Alfred%20Workflow/Actions.alfredworkflow?raw=true) the Alfred Worfklow (requires paid [PowerPack](http://www.alfredapp.com/powerpack/) to install).
- Create a folder at: `~/Dropbox/utilities/clipboard-actions/` – This can be changed; see below.
- [Download all the Actions](https://github.com/EvanLovely/clipboard-actions/archive/master.zip) and place them in the directory from the previous step.
    - *Optional* – Selectively download some of the scripts from my [clipboard actions repo](https://github.com/EvanLovely/clipboard-actions)  
    - *Optional* – For the command-line savvy, I'd recommend just cloning that repo in a sub-folder, then you can have your own and an updatable folder from this one.

# Useage Instructions

## Basic

- Invoke Alfred, type `action ` and then a chunk of text you want to "action" and hit enter.
    - You hold Option and hit enter to edit that text in Sublime Text if you want. Save and close that file for it to be passed to the next step.
- You'll see a list of things that can be done with that text (from the actions directory we set up). Select or filter the list and hit enter. Hit Ctrl+Enter to paste immediately after.
    - You can optionally edit your action text (clipboard contents) or create new action text after selecting an action, by hitting Cmd+Enter for 1 line editing or Option+Enter to edit in Sublime Text.

## With pre-copied text

- After copying text, invoke Alfred and type `clipactions` to select actions for it. 
- *Optionally* assign a hotkey for it (it's the slot that feeds into `clipactions`)

![Hotkey for clipactions](https://raw.githubusercontent.com/EvanLovely/alfred--actions/master/readme-assets/hotkey_for_clipactions.png)

## With selected text

- Assign a hotkey to the top Hotkey slot first
- Select text anywhere, hit that Hotkey, and then select your action.

![Hotkey for selected text](https://raw.githubusercontent.com/EvanLovely/alfred--actions/master/readme-assets/hotkey_for_text_selection.png)

## Passing in the contents of a text file

- Select a file using Alfred's File Window, then select it's File Actions (right arrow)
- Select "Action Contents of File"
- Select the Action to fire off

# Change Action Scripts Folder Location

You can *optionally* set your folder where the workflow will look for scripts/actions to execute. This is set to `~/Dropbox/utilities/clipboard-actions/` by default. You can changed it by double-clicking the Alfred Workflow object shown below:

![Change Folder](https://raw.githubusercontent.com/EvanLovely/alfred--actions/master/readme-assets/how_to_change_default_folder.png)
