# Amnesia-io

[Amnesia.io](https://amnesia.io) integration for [Sublime Text 3](https://www.sublimetext.com/).

This package allows you to share code via amnesia.io directly
from the editor, and copies a share link to your clipboard.

Amnesia.io is an ephemeral code sharing service with nice collaboration and privacy
features. Read more about it at https://amnesia.io.

Also available for [Atom](https://github.com/nathamanath/amnesia-atom)

## Usage

### Installation

* Get from [Package Control](https://packagecontrol.io/packages/AmnesiaIO)
* Or copy into a folder in your Packages directory (under `Preferences -> Browse Packages...`)

### Functionality

The `amnesia` command by default will share the current selection, or if none and multiple cursors, the active lines, or if one cursor, the entire current file.

You can choose what to share with the following args:

* `file` - Share the content of the entire current buffer.
* `selection` - Share the current highlighted selection.
* `line` - Share the current line.

Default key mappings are as follows:

|                            | Windows          | Linux            | OSX             |
|----------------------------|------------------|------------------|-----------------|
| Share Selection/Lines/File | ctrl-alt-shift-a | ctrl-alt-shift-a | cmd-alt-shift-a |
| Share File                 | ctrl-alt-shift-f | ctrl-alt-shift-f | cmd-alt-shift-f |
| Share Selection            | ctrl-alt-shift-s | ctrl-alt-shift-s | cmd-alt-shift-s |
| Share Line                 | ctrl-alt-shift-l | ctrl-alt-shift-l | cmd-alt-shift-l |

To edit go to `Preferences -> Package Settings -> AmnesiaIO` and copy a command from Key Bindings - Default to Key Bindings - User to overwrite it.

### Configuration

#### Settings

Available settings and their default values are shown below.

```yaml
      # How long amnesia.io will hold on to your code snippets in seconds
      ttl: 6000,

      # Syntax highlighting format which will be used if it cannot be discerned
      # from your file name
      defaultFormat: "bash"
```
## Development

To edit, clone into your packages directory and edit `AmnesiaIO.py`:

```bash
  git clone https://github.com/jolyongray/amnesia-sublime
  cd amnesia-atom
```
