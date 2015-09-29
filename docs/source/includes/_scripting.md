# Scripting

## Introduction

Scripting is implemented using the [Lua](http://www.lua.org/manual/5.1/) scripting language.

As well as Lua's [standard libries](http://www.lua.org/manual/5.1/manual.html#5),many additional functions and classes included to allow significant customisation of the game.

It's also possible to access many of [Mono's standard libraries](https://goo.gl/wHKMaJ) and [Unity's libraries](http://docs.unity3d.com/ScriptReference/).

<aside class="success">
Lua is integrated with uLua/LuaInterface, an implementation of Lua 5.1.4.
</aside>

<aside class="warning">
Unity 5 will require another Lua plug-in, curently planned to be MoonSharp.
This has a few difference from regular Lua.
</aside>


## Data types

```lua
local value = 1
local value = 25.0
local value = false
local value = "Hello world"
```

Lua and C# data types are converted as best as possible. Lua numbers convert to ints or floats, and so on.
C# classes objects are also accessible from Lua and described later.

<aside class="blue">
Take care to precede Lua variable definitions with local unless you really want them to be globally accessible!
</aside>

## Debugging

```lua
print("Hello World")
```

Use Lua's print functionality to log to the console. [See examples](http://www.lua.org/pil/2.4.html).


## Accessing C# Classes and Structs

>Import a class from the game.

```lua
Action = luanet.import_type("Action")
```

>Import a class from the standard libraries.

```lua
List = luanet.import_type("System.Collections.Generic.List")
```

>Import a class from UnityEngine.

```lua
Application = luanet.import_type("UnityEngine.Application")
```

Several C# classes and structs are exposed to Lua and can be used directly by using their name.

`<luaclassname> = luanet.import_type("[<namespace>.]<classname>)`

`<luastructname> = luanet.import_type("[<namespace>.]<structname>)`

>Load a custom assembly.

```lua
luanet.load_assembly("CustomAssembly")
```

Where a class is not accessible from Lua, it can be imported with luanet's load_assembly command. If the class is held in a different assembly,
that must be referenced first, and loaded if not already loaded

<aside class="warning">
Future versions of the game will not allow custom class or assembly imports for security reasons.
</aside>


## Instantiate a C# Object

>Instantiate a struct then change it by using a new struct.

```lua
local position = new Vector2(5, 25)
print(position.x + "," + position.y)
position = new Vector2(position.x + 10, position.y)
```

Although it's easy to instantiate a C# object, it incures a significant overhead. It should be done as rarely as possible.
Several functions have been provided specifically to help avoid Vector2 and Color structures being required from Lua.

Instantiate an object as follows:

`value = new <class>(...)`

`value = new <struct>(...)`

<aside class="warning">
Structs cannot have their fields set independently, so they must always be set with a new struct.
This has a significant overhead and should be avoided where possible.
</aside>


## Accessing C# Properties

>Access the name property of an entity.

```lua
local name = entity.name
```

Accessing object properties is done using Lua table accessors, so can use simple dot notation.

`value = <object>.<property>`

If a property is used more than once, it should be cached in a local variable.


## Accessing C# Methods

>Access an instance's function.

```lua
local isOnScreen = entity.IsOnScreen()
```

Accessing an instance's functions has a different notation from properties; a colon must be used.

`value = <instance>:<function>(...)`

>Access a static class function.

```lua
local isOnScreen = Level.Reset()
```

However, accessing a static class function must use a dot, just like properties.

`value = <class>:<function>(...)`

<aside class="notice">
Properties start with a lowercase letter, functions start with a capital letter.
</aside>


### Pass by Reference

>Pass by 'ref' reference

```lua
-- C# function is: public void TryGet(string key, ref Setting setting)
local setting = null
setting = App.settingManager.Get("Player.acceleration", setting)
```

>Pass by 'out' reference

```lua
-- C# function is: public bool TryGet(string key, out Setting setting)
local result, setting = TryGet("Player.speed")
```

C# allows arguments to be passed by reference.

Where an argument is specified as **ref**, it means it must be initialised before being passed in and Lua will return an updated value in the return values.

Where an argument is specified as **out**, it should not be passed at all but is treated as an extra return value.

`value1, value2 = function(...)`

<aside class="notice">
Lua allows multiple return values by separating them with a comma.
</aside>


## Accessing C# Enums

>Use an enum.

```lua
local layer = ArtifactDef.Types.Shield
```

Enums are referenced using dot notation:

`value = [<Class>.]<Enum>.<Value>`

>Import new enums.

```lua
ArtifactDef_Types = luanet.import_type("ArtifactDef+Types")
RuntimePlatform = luanet.import_type("UnityEngine.RuntimePlatform")
```

If an enum isn't defined in lua, import it with:

`<luaenumname> = luanet.import_type("[<namespace>.][<class>+]<enumname>)`

<aside class="notice">
The module is followed by '.' but the class is followed by '+'.
</aside>

>StringToEnum example.

```lua
local artifactType = "Shield"
local value = StringToEnum("ArtifaceDef+Types", artifactType)
```

Where an enum has to come from a string, such as in a config or an external file, use StringToEnum in [Additional Functions](#additional-utility-functions).

`StringToEnum("[<class>+]<type>", <string>)`


>StringToEnum example.

```lua
local path = "PlayerManager.Paths.None"
local pathAsString = StringToEnum(path)
```

StringToEnum does the opposite.

`StringToEnum(<value>)`


## Manager Classes

>Access an object manager.

```lua
local terraformEnergy = App.terraformEnergyManager.AddEnergy(...)
```

Most objects in the game are handled by associated managers, such as the MobManager for objects, or the ExplosionManager for explosions. Managers are instances rather than static classes, and are accessed through the App static class as follows:

`App.<managerName>:<function>(...)`

<aside class="notice">
Manager instances always start with a lowercase letter, as with all properties.
</aside>


## Additional Utility Functions

### StringToEnum

>StringToEnum example.

```lua
local artifactType = "Shield"
local value = StringToEnum("ArtifaceDef+Types", artifactType)
```

Where an enum has to come from a string, such as in a config or an external file, use StringToEnum.

`StringToEnum("[<class>+]<type>", <string>)`

### math.randomf(f)

> Get a random int between 0 and 3 (exclusive) using lua's internal function.

```lua
local value = math.random(4)
```

> Get a random float between 0 and 10 (inclusive) using math.randomf.

```lua
local value = math.randomf(10.0)
```

Supplements Lua's math.random functions with a method to get a float between two values, inclusive.

Parameters | Type | Description
--------- | ------- | -----------
f | float | Maximum number to return

**Returns:**
Random value between 0 and f inclusive


## Supported Classes

Class| Namespace | Type
---------|---------| ---------
List | System| class&lt;generic&gt;
Dictionary | System| class&lt;generic&gt;
| |
Application | UnityEngine| class
AudioClip | UnityEngine| class
AudioListener | UnityEngine| class
Camera | UnityEngine| class
Color | UnityEngine| **struct**
Component | UnityEngine| class
Debug | UnityEngine| class
Display | UnityEngine| class
GameObject | UnityEngine| class
Graphics | UnityEngine| class
HandHeld | UnityEngine| class
Input | UnityEngine| class
Mathf | UnityEngine| class
Matrix4x4 | UnityEngine| class
Microphone | UnityEngine| class
MonoBehaviour | UnityEngine| class
QualitySettings | UnityEngine| class
Quaternion | UnityEngine| class
Screen | UnityEngine| class
Social | UnityEngine| class
SystemInfo | UnityEngine| class
Texture2D | UnityEngine| class
Time | UnityEngine| class
Touch | UnityEngine| class
Transform | UnityEngine| class
Vector2 | UnityEngine| **struct**
Vector3 | UnityEngine| **struct**
Vector4 | UnityEngine| **struct**
ReInput | Rewired| class
| |
ScriptManager | Tuna| class
SettingManager | Tuna| class
Setting | Tuna | class
| |
Action | | class
ActionManager | | class
Artifact | | class
ArtifactDef | | class
ArtifactManager | | class
Attributes | | **struct**
Colony | | class
DataCan | | class
DistanceField | | class
DistanceFieldCollisionInfo | | class
DistanceFieldAvoidanceInfo | | class
Door | | class
DoorDef | | class
DoorManager | | class
Drawing | | class
Entity_Overlay | (Entity)| class
Equipment | | class
Explosive | | class
Flora | | class
FloraDef | | class
FloraManager | | class
GrassDef | | class
GrassManager | | class
Key | | class
LaserMine | | class
Level | | class
LevelManager | | class
MapEffectManager | | class
Overlay | | class
Pickup | | class
PickupDef | | class
PickupManager | | class
PlayerManager | | class
PlayerShip | | class
RadarTarget | | class
RadarTargetManager | | class
Seedling | | class
SoloShip | | class
SoundEvent | | class
SpriteInstance | | class
SpriteDef | | class
SpriteManager | | class
Team | | class
Vehicle | | class
Turret | | class
Vortex | | class

## Supported Enums


### DifficultyModes
- Casual
- Normal
- PermaDeath


### PlayerPaths

- Balanced
- MostlyStrength
- MostlySpeed
- MostlyEnergy
- FavourStrengthSpeed
- FavourStrengthEnergy
- FavourSpeedEnergy


### Equipment States
- Uninitialised
- Free
- Captured
- Collecting
- Collected
- Equipped
- Activated


### InventoryCategories
- Artifact
- Consumable
- Accessory
- Key


### PickupTypes
- Health
- Invulnerability
- Invisibility
- Weapon
- Ammo
- Bomb
- StasisBomb
- SpeedBoost
- HealthRegenRate
- ArtifactSlot
- PickupSlot
- Radar
- Custom


### PickupCategories
- Consumable
- Instant
- Accessory


### ArtifactTypes
- Defender
- Shield
- Companion
- Health
- Decoy
- Beacon
- Avoid
- Fungus
- Bomb
- StasisBomb
- PacifierBomb
- LaserMine
- Invisibility
- Custom


<aside class="warning">TODO: Add a lot more!</aside>

