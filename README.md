# ![Sortify](https://craiy.net/resources/sortify.png) Sortify - A file and directory sorting script
Sortify is a simple script to keep the computer organized. It uses customizable json config files to sort the files by the users wishes and writes a log file to keep track of them.

## Usage
Sortify can be used via the command line. Simply run `python sortify <name-of-config> <log>`
- The `<name-of-config>` parameter will tell the program which config to use. Configs must be placed in the config folder of the program and the parameter does NOT need the file extension. The parameter is optional and is normally set to "default".
- The `<log>` parameter defines whether to write a log file `1 = true`, `0 = false`. This parameter is optional and will be 1 by default 

If the target path already exists, the script will rename it by the windows standard i.e. New File (2), New File (3)...

## Configuration
### Basics
The config file is based on a list of objects which contain to attributes at the top layer
- `match` is an object which defines the matching rules
- `dest` will set the destination path for the matches items. Additionally the match string can contain the placeholder {user} which will be replaces by the current user path

### Matching files
The match object currently supports 4 types of parameters. Each of these is optional and can also be used together to match only items which apply to multiple parameters
- `ext` is used to match files by extension, which is the most common use case. Simply set a list of file extensions (without the .) to match them. (Only applies to files)
- `regex` takes in a regular expression string to match a filename. This can be used in multiple different scenarios to define specific filename types to be matched
- `type` is used to define whether to match a directory `"dir"` or a file `"file"`
- `contains` is used to take a recursive look into a directories content. From here on it uses a default `match` object. (Only applies to directories)

### Example
Matching a range of different image files
```json
[
    {
        "match": {
            "ext": ["bmp", "dds", "gif", "heic", "jpg", "jpeg", "png", "pspimage", "tga", "thm", "tif", "tiff", "yuv", "webp"]
        },
        "dest": "{user}\\Images"
    }
]
```
Matching all files and directories which start with "abc"
```json
[
    {
        "match": {
            "regex": "abc"
        },
        "dest": "{user}\\Documents"
    }
]
```
Matching all directories containing .py files
```json
[
    {
        "match": {
            "type": "dir",
            "contains": {
               "ext": ["py"]
            }
        },
        "dest": "{user}\\Documents\\Workspace"
    }
]
```
