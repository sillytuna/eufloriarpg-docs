# Entity Reference

Entities are managed through a combination of internal code and external scripting,. The internal code handles core management, such as health and movement.
Scripting can be used to create custom entities, AI and animation.

## Mobs, Entities and Vehicles

The core game objects are Mobs, managed by the MobManager, and the Entity class inherits from the Mob class.
Entities are the most common game elements that will be interacted with. The core game objects derive from Entity either directly or indirectly.

The Vehicle class the parent of any entity which uses the behaviour system or has more complex movement controls.

<aside class="notice">
All mobs can be configured in Settings/MobDefs.cfg.
</aside>


## Mobs

Property | Type | RW | Description
-------- | ---- | --- | -----------
type | string | r
uid | int | r | Guaranteed to be unique.
name | string | rw
autoNamed | bool | r | The mob was given an automatic name: &lt;type&gt;_&lt;uid&gt;.
isActive | bool | rw | A mob can be made temporarily inactive in which case it won't be updated etc.
isStarted | bool | rw | At least one fixed update or update has run.
isRecyclable | bool | rw | Mob is suitable for recycling.
isTrashed | bool | r | Mob has been trashed. Some mobs may be in the active mob list but no longer active or about to be trashed at the end of the frame. They should be ignored.
isRecycled | bool | r | Mob has been recycled.
isRenderable | bool | rw | Mob can be rendered.
isDebugRenderable | bool | rw | Mob can be debug rendered.


Method | Parameters | Description
--------- | ------- | -----------
IsType | type&#91;,bool inherited&#93; | Test if mob is an instance of type, or inherits from a type. **Returns:** true if mob is an instance of type.
GetUserConfig | key | Gets a user config setting. See [Entity Configs](#entity-configs). **Returns:** Setting object or nil if key not found.
Trash | | Trash a mob with no idea fx, stats etc. Don't use the object at all after it's trashed.

<aside class="warning">
Do not ever use a Trashed object. If in an update for the entity and you call its trashed method, return immediately afterwards. The isTrashed flag is set when the mob is trashed.
</aside>


## Entity Configs

>Access an entity's config setting.

```
local value = entity.speciesID
```

The MobDefs [Configuration](#configuration) file is used to initialise entities. These configs can be accessed from an entity just like any other property.

<aside class="notice">
These items should be considered read only.
</aside>

### Custom Config Settings

>Access a custom item from an entity's config.

```
-- In MobDefs:
-- 	Set frequency				120

local value = entity.userConfigs.frequency.asInt
```

Custom entries can be added to entities in MobDefs by simply adding them as any other config setting. Since they are not declared within the source code, they are added instead as a Setting to a Dictionary in the entity, called userConfigs. A Setting is a class storing custom data.

From lua, they can be accessed as follows:

`<entity>.userConfigs.<key>`

It's also possible to use a function which returns nil if the key doesn't exist:

`setting = entity.GetUserConfig(key)`

When you come to use it, you need to tell the Setting what kind of data it is. There are the following options:

- asInt
- asFloat
- asBool
- asString
- asVector2
- asVector3
- asVector4
- asColor
- asIntArray
- asFloatArray
- asStringArray

>Print a Setting's path or key.

```
print(entity.userConfigs.frequency.path)
print(entity.userConfigs.frequency.key)
```

If it’s useful, you can also print out the full path to the setting, or just the name (key) itself, using the path or key properties.


## Entity Physicals

Property | Type | RW | Description
-------- | ---- | --- | -----------
position | Vector2 | r |
lastPosition | Vector2 | r |
velocity | Vector2 | r |
rotation | float | r | Radians
scale | float | r |
radius | float | r | Accounts for scale
pitch | float | r | Angle of movement and should match Velocity normally (may be entity dependent)
visiblePitch | float | r | Visible angle which will often match pitch and will almost always match rotation (entity dependent)
maxSpeed | float | r |
speed | float | r | Vehicles only. If not available, can be calculated from from the velocity magnitude (velocity.magnitude)
fieldOfViewRadians | float | r
cosHalfFieldOfView | float | r
sceneryCollisionsEnabled | bool | rw
collidedWithScenery | bool | r
collidedWithSceneryInfo | DistanceFieldCollisionInfo | r
collidedWithDoor | bool | r
collidedWithDoorInfo | Door | r


Method | Parameters | Description
--------- | ------- | -----------
SetPosition | float x, float, y | Sets position and lastPosition to the arguments.
MovePosition | float x, float, y | Sets position, and sets lastPosition to the old position value.
SetVelocity | float x, float, y |
SetPitch | float  |  Radians. May change rotation.
SetVisiblePitch | float | Radians. May change rotation.
SetRotation | float | Radians. Use only if Pitch and VisiblePitch cannot be used as object can't officially rotate
SetScale | float
SetRadius | float
SetFieldOfView | float  | Degres.
IsOnScreen | &#91;bool retest&#93; | This is usually baed on rendering, so sometimes a test needs to be requested to prevent a faulty cached value being used. Note that this test is not very accurate and errs on the side of caution for clipping purposes. **Returns:** true if the sprite is on screen.


## Entity Attributes and Relationships

>Add a frequency property to the entity in Lua

```
entity.data.frequency = 5
```

Property | Type | RW | Description
-------- | ---- | --- | -----------
label | string | rw | The label is the name of the item as used in-game. A random name is created using the label generator if none is provided.
attributes | float energy, float strength, float speed | r | Core attributes such as speed, strength, and energy. They are not clamped but should normally be 0-1. Higher numbers can give interesting visuals and most calculations using these attributes will clamp the input to 0-1 anyway.
team | Team | r | Can print team.name, check team.isPlayer or check team.isGrey
teamColours | Color[] | r | The team colour array.
parentFlora | Flora | r | The parent flora, if any.
parentColony | Colony | r | The parent colony, if any.
aiGroup | AIGroup | r | The parent group, if any (for AI travelling in groups).
isAlive | bool | r
isDead | bool | r
isInStasis | bool | r
isPacified | bool | r
isThinking | bool | r
isPlayer | bool | r
isFlora | bool | r
isEquipment | bool | r
isTargetable | bool | r | Entity is a legitimate attack target.
isDamageable | bool | r | Entity can be damaged it attacked.
data | bool | r | Lua can use the data property to store additional properties. This can be any Lua datatype. **This is automatically cleared when the mob is trashed.**


Method | Parameters | Description
--------- | ------- | -----------
SetAttributes | Attributes |
UpdateCharacteristics | | Updates any characteristics which depend on attributes.
SetTeam | Team |
SetTeam | team name |
SetParentColony | Colony |
SetParentFlora | Flora |
SetAIGroup | AIGroup |
PowerRule | float attribute, Vector2 minMax, float rule | Static function which calculates a characteristic based on a power rule. c = min + (max - min) * pow(attr, rule). The attribute is clamped 0-1. **Returns:** float result

## Entity Visuals

Entities are normally rendered using sprites.
A **SpriteDef** is the original definition and a **SpriteInstance** is a processed version of the SpriteDef.
and is what is actually rendered on screen. Animation works through procedural modification of the SpriteInstance.

Property | Type | RW | Description
-------- | ---- | --- | -----------
spriteDef | SpriteDef | r
spriteInstance | SpriteInstance | r
spriteInstanceDirty | bool | w | Set to true if the sprite has been changed and the sprite instance needs processing.
alphaTransparency | float | rw | Set the sprite alpha. This is multiplied on top of the sprite colour.
boundingRegionDirty | bool | w | Set to true if something about the sprite size has changed manually, i.e. not using a regular function since these do this already.


Method | Parameters | Description
--------- | ------- | -----------
SetSpriteDef | sprite name | Switches to using a new SpriteDef and immediately processes the SpriteInstance.
ProcessSprites | | Rarely, it may be required to reprocess an entity's sprites manually but this shouldn't be used unless it specifically solves a problem.
AddOverlay | sprite name, int layerModifier | Overlay a sprite, using the layer modifier to have it go in front or beind the main sprite. Multiple overlays can be used.
RemoveOverlay | sprite name |
RemoveOverlay | Overlay |

### Overlays

Overlay is a simple class which manages entity overlays.
In Lua this is tagged Entity_Overlay since it's a subclass of Entity.

Property | Type | RW | Description
-------- | ---- | --- | -----------
name | string | r
spriteDef | SpriteDef | r
spriteInstance | SpriteInstance | r
layerModifier | int | r


## Entity Health and Damage

Property | Type | RW | Description
-------- | ---- | --- | -----------
health | float | r
maxHealth | float | r
healthRatio | float | r | This is simply health / maxHealth
wasAttacked | bool | r | true if attacked since the last fixed update.
wasAttackedBy | Entity | r | The attacker if attacked since the last fixed update.


Method | Parameters | Description
--------- | ------- | -----------
ModifyHealth | amount&#91;, bool fx&#93; | Increase or reduce health, with or without a visual effect if increasing health. The entity will die if health reaches zero. **Returns:** true if died
SetHealth | value | Set the health to a precise value
Heal | | Fully heal entity
Explode | |
ExplodeStasis | float time | Explodes and puts area it affects into stasis
ExplodePacifier | float time, float ratio | Explodes and pacifies area such that entities attack is affected by ratio.
DieQuietly | | Die without any fx.
Die | &#91;bool noFX&#93; | If true is passed, there will be no visual or audio effect associated with the death.


## Entity Attacks

Property | Type | RW | Description
-------- | ---- | --- | -----------
attackRange | float | rw
timeBeforeAttack | float | rw
attackDamage | float | r
attackFieldOfViewRadians | float | r
cosHalfAttackFieldOfView | float | r
targetEntity | Entity | r | Some entities have a target used for movement or attacking.


Method | Parameters | Description
--------- | ------- | -----------
SetAttackFiendOfView | float | Degrees.

<aside class="warning">
The attack support functions need some minor reworking to make suitable for Lua.
</aside>


## Entity Sound FX

Method | Parameters | Description
--------- | ------- | -----------
PlaySfx | sfx name&#91;,float volume, float pan&#93;  | Play sound with volume (0-1) and pan (0-1).
PlayPositionalSfx | sfx name | Play sound and set volume and pan automatically.

<aside class="warning">
The audio API will be updated to deal with looping sounds.
</aside>


## Vehicles

The main additions to Vehicles are improved movement configuration and code, and the support for the behaviour system.
Behaviours allow targets, flocking, and flowfields to be used as inputs to aid in deciding where to move towards.

Property | Type | RW | Description
-------- | ---- | --- | -----------
speed | float | r | The current speed.
behavioursEnabled | bool | rw | Toggle to enable or disable behaviours.
isInAvoidanceMode | bool | r | true if a vehicle is trying to avoid scenery or a door, i.e. when there was a collision within the recent past (approx 0.35-0.65s). It's intended to allow ai code to have a chance to get away from the problem.


Method | Parameters | Description
--------- | ------- | -----------
SetBehaviour | Behaviour
SetTargetBehaviour | Behaviour
SetAvoidanceMode | | Puts the vehicle into avoidance mode. Internally this actually just sets a timer and relevant flag.



