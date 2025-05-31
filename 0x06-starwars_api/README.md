# Star Wars Characters API Script

This project contains a script that prints all characters of a Star Wars movie using the Star Wars API.

## Usage

```
./0-starwars_characters.js <Movie ID>
```

- The first positional argument is the Movie ID (e.g., 3 for "Return of the Jedi").
- The script prints one character name per line in the order provided by the API.

## Requirements
- Node.js 10.x
- The `request` module (install globally with `npm install request --global`)
- The script must be executable (`chmod +x 0-starwars_characters.js`)

## Example
```
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
...
```

## Installation

Install Node.js 10.x:
```
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Install the required modules:
```
sudo npm install semistandard --global
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```
