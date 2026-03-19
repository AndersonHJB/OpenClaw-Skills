# mac-browser-automation

## Description
A physical, hardware-level browser automation skill for macOS. Use this skill when normal browser automation (JS `click()`, `insertText`, or DOM manipulation) fails due to strict anti-bot measures, Vue/React synthetic event requirements (like `isTrusted: true`), or deeply nested Shadow DOMs (e.g., Bilibili comments, Waline).

## Trigger
Use when the user asks to operate the browser, comment on a stubborn website (like Bilibili), fill forms, or explicitly permits "physical mouse/keyboard operations".

## Methodology: "The Physical Override"

When a website blocks script-based clicks/inputs, we bypass the DOM entirely by calculating the exact screen pixels and using `peekaboo` and AppleScript to perform real hardware events.

### Step 1: Calculate Absolute Screen Coordinates
Use AppleScript to run JS in the active tab. Find the element (piercing through `.shadowRoot` if necessary), get its `getBoundingClientRect()`, and add the browser window's offset.

```javascript
// AppleScript + JS Example to get X,Y coordinates
osascript -e 'tell application "Google Chrome" to execute front window'\''s active tab javascript "
    // 1. Find the element (e.g., inside shadow DOM)
    var btn = document.querySelector(\"bili-comments\").shadowRoot.querySelector(\"bili-comment-box\").shadowRoot.querySelectorAll(\"button\")[1];
    
    // 2. Get relative rect
    var rect = btn.getBoundingClientRect();
    
    // 3. Calculate absolute macOS screen coordinates
    var winX = window.screenX;
    var winY = window.screenY + (window.outerHeight - window.innerHeight);
    
    // 4. Return formatted X,Y
    Math.round(rect.x + rect.width/2 + winX) + \",\" + Math.round(rect.y + rect.height/2 + winY);
"'
```

### Step 2: Physical Mouse Click
Extract the `X,Y` from the previous step and use `peekaboo` to click it. This click is registered by the OS as a real human click (`isTrusted: true`).

```bash
/opt/homebrew/bin/peekaboo click --coords X,Y
```

### Step 3: Physical Keyboard Typing (Paste)
To bypass Vue/React input detection, do not set `.value` or `.textContent`. Instead, focus the input (via click or `editor.focus()`) and simulate a real `Cmd+V` paste via macOS System Events.

```applescript
tell application "System Events"
    set the clipboard to "你的评论内容"
    delay 0.5
    keystroke "v" using {command down}
    delay 0.5
    keystroke return -- Optional: press enter to submit
end tell
```

## Important Rules
1. **Always Ensure Chrome is Active:** Run `tell application "Google Chrome" to activate` before physical interactions.
2. **Handle Shadow DOM:** Many modern sites (Bilibili, etc.) hide their inputs inside `<custom-element>.shadowRoot`. You must traverse each shadow boundary manually in your JS query.
3. **Delay is Crucial:** Always add small delays (`sleep 1` or AppleScript `delay 1`) between focusing, pasting, and clicking to allow the UI/network to catch up.
