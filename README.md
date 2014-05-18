alfred--actions
===============

> It's like Drafts for Mac

# Install Instructions

- [Download](https://github.com/EvanLovely/alfred--actions/blob/master/Alfred%20Workflow/Actions.alfredworkflow?raw=true) the Alfred Worfklow (requires paid [PowerPack](http://www.alfredapp.com/powerpack/) to install).
- *Optionally* set your folder where the workflow will look for scripts/actions to execute. This is set to `~/Dropbox/utilities/clipboard-actions/` by default. You can changed it by double-clicking the Alfred Workflow object shown below:

![Change Folder](https://raw.githubusercontent.com/EvanLovely/alfred--actions/master/readme-assets/how_to_change_default_folder.png)

- Download any of the scripts from my [clipboard actions repo](https://github.com/EvanLovely/clipboard-actions) place them in the directory from the previous step. All of them can be easily grabbed by [here](https://github.com/EvanLovely/clipboard-actions/archive/master.zip). For the command-line savvy, I'd recommend just cloning that repo in a sub-folder, then you can have your own and and updatable folder from this one.

# Useage Instructions

## Basic

- Invoke Alfred, type `action ` and then a chunk of text you want to "action" and hit enter.
- You'll see a list of things that can be done with that text (from the actions directory we set up). Select or filter the list and hit enter. Hit Cmd+Enter to paste immediately after.

## With pre-copied text

- After copying text, invoke Alfred and type `clipactions` to select actions for it. 
- *Optionally* assign a hotkey for it (it's the slot that feeds into `clipactions`)

![Hotkey for clipactions](https://raw.githubusercontent.com/EvanLovely/alfred--actions/master/readme-assets/hotkey_for_clipactions.png)

## With selected text

- Assign a hotkey to the top Hotkey slot first
- Select text anywhere, hit that Hotkey, and then select your action.

![Hotkey for selected text](https://raw.githubusercontent.com/EvanLovely/alfred--actions/master/readme-assets/hotkey_for_text_selection.png)
