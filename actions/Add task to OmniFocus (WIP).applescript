tell application "OmniFocus"
	activate
	tell front document
		set new_task to make new inbox task with properties {name:the clipboard}
		#open quick entry with inbox task new_task
	end tell
end tell