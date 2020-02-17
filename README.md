# adventure
An adventure game written in python

## Requirements
* python-3.7.4
(Install Requirements: `pip install -r requirements.txt`)

* pygame==1.9.6
* PyTMX==3.21.7
* six==1.14.0

## Optional Requirements
* Tiled 1.3.2
* paint.net 4.2.9

## Todo
- [x] scale sprite sheet image to 32 x 32 instead of 16 x 16
- [x] change player width/height to 32
- [ ] fix color key issues on player sprite sheet (edges blurred when resized)
- [ ] make main overworld (largest map)
- [ ] come up with dungeons
- [ ] scene management (start screen, game screen, pause screen, inventory)
- [ ] dungeon fog (ex: dark caves)
- [ ] add inventory items (ex: torch, raft)
- [ ] inventory item torch lights up caves, removes fog
- [ ] inventory item raft allows player to travel over water
- [ ] tileset for caves
- [ ] tileset for dungeons