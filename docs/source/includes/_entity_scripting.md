# Entity Scripting

## Lua callbacks

>Set a lua callback in MobDefs.

```
Set onActivateLuaHandler				ExampleActivateLuaHandler
```

Lua can receive callbacks allowing entities to be almost entirely controlled from script. These are initialised in MobDefs.

<aside class="notice">
More callbacks will be added in future.
</aside>

### onActivateLuaHandler(entity)

Perform any initialisation in onActivateLuaHandler.

The AI state machine has not been loaded at this point, and some of the entity specific settings
may not be ready, possibly including position, so this should be limited to setting custom data.

Other initialisation could be part of FixedUpdate. When entity.isStarted == false, it's the very first time FixedUpdate has been run.


### onFixedUpdateLuaHandler(entity, time)

Fixed updates are called very 1/60th of a second. Multiple fixed updates can occur between rendering frames.

Use this for game logic.

<aside class="notice">
The first time FixedUpdate runs, entity.isStarted == false.
</aside>


### onUpdateLuaHandler(entity, time)

Updates are called between every rendering frame, after any fixed updates.

Use this for animation or input system functions.

<aside class="warning">
Unity's input system refreshes between each update, not the fixed update.
</aside>


### onDeathLuaHandler(entity&#91;, bool noFX&#93;)

The entity has died. The noFX flag requests no visual or audio fx.

This should be used for any death related actions, such as loot drops or spawning new enemies.


### onTrashLuaHandler(entity)

The entity is being trashed.

This should be used to do any clean up required, such as releasing any particular resources or clearing any references.


## Custom Properties

>Add a frequency property to an entity

```
entity.data.frequency = 5
```

Custom properties can be stored in the data property, which is a Lua table:

`entity.data.<name> = <value>`

Accessing entity.data is a little slow so cache the data reference if using multiple times per frame:

`local data = entity.data`


## References to Other Entities

>How to find and use an entity reference by id.

```
enemy = Entity.Find(entity.data.enemyUID)

if enemy ~= nil then
    -- Do something
else
    -- Zero the uid
    entity.data.enemyUID = 0
end
```

>Find an entity by name.

```
Entity.Find(entity.data.enemyName)
```

It's often useful to store some kind of reference to an entity. However, **do not ever store an actual reference to an entity, only store the entity.uid.**
Use the following functions to find the entity, and check for nil to be sure the entity still exists:

`Entity.Find(<uid>)`

This can be used but is slower:

`Entity.Find(<name>)`

Entities will be returned if dead, but not if trashed. Most entities trash themselves on death unless they have a death sequence or are the player.

<aside class="warning">
Do not ever store a reference to an entity.
</aside>

<aside class="success">
The uid is never 0 so this can be used safely to indicate no entity.
</aside>


## Spawning Entities

> Create a projectile from an entity which we know is a turret.

```
projectile = App.mobManager:Create(entity.ammunition)
projectile:Activate(entity.attributes, entity.position, entity.parentColony, entity.team)
projectile:SetPitch(math.PI)
```

Although there are commands to spawn entities, it's possible to create them using the internal functions.

Two steps are required: Create and Activate. Create spawns the basic entity but entity specific settings are uninitialised and should not be used.
Normally Activate will be called immediately afterwards. With the resultant entity, it's possible to then further customise it.

### App.mobManager.Create(type)

Creates the new entity.

Parameters | Type | Description
---------- | ---- | -----------
type | string | The MobDef to create.

**Returns:** The created entity or nil if there was an error.

### entity.Activate(...)

Creates the new entity.

Parameters | Type | Description
---------- | ---- | -----------
attributes | Attributes |
position | Vector2
parentColony | Colony
team | Team

<aside class="notice">
Some entities have their own Activate method. This will be documented with the entity class documentation.
</aside>


## World Collisions

The collision system runs as long as the object has a velocity and the relevant [collision flags](#entity-physicals) are set.
Entities are stopped from moving through scenery or doors but the actual reaction is entity specific. Vehicles
react by bouncing, as does the player, other items may simply stop.

Entities have two flags to signify collisions:

Property | Type | RW | Description
-------- | ---- | --- | -----------
collidedWithScenery | bool | r | Collided with the level map (distance field). **collidedWithSceneryInfo** contains the relevant details. This is described futher below.
collidedWithDoor | bool | r | Collided with a door. **collidedWithDoorInfo** contains the Door itself.

> Get the door direction.

```
normalisedDirection = door.ClosedSegment.Direction
```

> Find which side of the door an entity is.

```
if (App.doorManager:RightSide(door, entity.position)) then ...
```

If a door was collided with, it may be useful to get the door direction and to find which side of the door the entity is.
It's then possible to move perpendicular to the door direction (for example).

If it would be useful to have a few tenths of a second to deal with the collision, such as to engage in avoidance procedures, this call starts a small and somewhat randomised timer accordingly:

`entity.SetAvoidanceMode()`

Check if in avoidance mode with:

`entity.isInAvoidanceMode`

<aside class="notice">
AvoidanceMode is simply a flag managed by a preset timer.
</aside>


## World Collision Methods

> Look ahead of the entity and get the collision information.

```
local info, reflectedPosition = Level.distanceField:CollideVector(entity.position, entity.position + moveVector)

if info ~= nil then
    -- Collision handling
end
```

It may be useful to actually run collision methods manually. The CollideVector method is accurate and uses bilinear interpolation.

`Level.distanceField:CollideVector(start, end, out reflectedPosition[, length])`

Parameters | Type | Description
---------- | ---- | -----------
start | Vector2 | Start position.
end | Vector2 | End position.
result | Vector2 | Resulting position based on the angle of incidence.
length | float | Pass the length parameter if (end - start).magnitude is know, else it will be calculated.

**Returns:** A DistanceFieldCollisionInfo structure or nil if there was no collision.

<aside class="notice">
Notice that 'reflectedPosition' is an out parameter so is passed by an out reference. See the example.
</aside>

### DistanceFieldCollisionInfo

Property | Type | RW | Description
-------- | ---- | --- | -----------
intersection | Vector2 | rw|  The actual point of intersection with the solid area of the distance field.
gradientAngle | float | rw | The gradient angle of the intersection (radians).
reflectionAngle | float | rw | The angle of reflection (radians).


## World Avoidance Methods

Collision methods have a high processing overhead, but avoidance methods provide various ways to look into the distance field.


### Distance Field Value

The simplest methods get the distance field value. The distance field has a value 0-255, where 128 is the border between outside and inside the scenery.
The raw values in the field tend to be multiples of 4 and are never 128. Values of 116+ or 140- may benefit from bilinear interpolated field values, depending what the requirement is.
All raw values should be treated as very approximate but they are very fast to obtain.

`Level.distanceField:GetPoint(position)`

`Level.distanceField:GetBilinearPoint(position)`


### Distance Field Gradient

`Level.distanceField:GetGradient(position)`

**Returns:** The gradient as a normalized Vector2.


### GetAvoidanceVector(start, end, avoidanceArea)

Parameters | Type | Description
---------- | ---- | -----------
start | Vector2 | Start position.
end | Vector2 | End position.
avoidanceArea | float | How far from the border region needs to be avoided. This is in distance field units, so a value of 8 would consider 120 (128-8) as the start of the avoidance area.

**Returns:** A DistanceFieldAvoidanceInfo structure or nil if there was no avoidance needed.

### DistanceFieldAvoidanceInfo

Property | Type | RW | Description
-------- | ---- | --- | -----------
strength | float | rw | The strength of the avoidance needed, 0-1 (linearly interpolated).
avoidanceAngle | float | rw | The avoidance angle (radians).
collision | bool | rw | true if there was a collision with a solid area (128+).


## World Line of Sight Methods

It can be useful to test for line of sight. This accounts for raw distance field values and doors.

The following two functions require both points to be on the map:

```local result = Level.distanceField:LineOfSight(start, length, angle)```

```local result = Level.distanceField:LineOfSight(start, end)```

**Returns:** true if there is line of sight.

The following two functions ignores if the start point is in a solid area and also clips against the map edges:

```local result = Level.distanceField:LineOfSightClipped(start, length, angle)```

```local result = Level.distanceField:LineOfSightClipped(start, end)```

**Returns:** true if there is line of sight.

The following function returns the interception point, again only using raw distance field values rather than bilinear interpolation so it's quite approximate.

local result, intercept = Level.distanceField:Intercept(start, end)

**Returns:** true if there is an intercept point.

Parameters | Type | Description
---------- | ---- | -----------
start | Vector2 | Start position.
end | Vector2 | End position.
length | float | Given with angle as an alternative to the end point.
angle | float | Angle (Radians). Given with length as an alternative to the end point.


## Animation

Although there is no animation system, SpriteInstance objects can be controlled by code to do procedural or other animation.
This should be done in the onFixedUpdateLuaHandler.

SpriteInstances are a processed version of SpriteDefs, as defined in the SpriteDefs configuration file.
They have all the layers and elements that are enabled at that point, but they have processed the element settings into something closer to a rendering primitive.
Primitives are created at render time, however, so the instance is still in a form where it can be animated in interesting ways.


### Step 1 - SpriteDef Layers and Elements

> ParameciumMine example.

```
local spriteDef = entity.spriteDef

local elementUpper = spriteDef:GetIndexedLayerElement(0, 0)
local elementLower = spriteDef:GetIndexedLayerElement(0, 1)
```

> ParameciumMine example 2 - slower but can be a useful technique.

```
local layer = entity.spriteDef.layers[0]
local elementUpper = layer.elements[0]
local elementLower = layer.elements[1]

local radiusUpper = elementUpper.baseWidth / 2
local lengthUpper = elementUpper.baseLength

local radiusLower = elementLower.baseWidth / 2
local lengthLower = elementLower.baseLength
```

It's usually important to have reference to the original SpriteDef and the SpriteInstance, and get the matching layers and elements of each.

`local layer = entity.spriteDef:GetLayer("<layer>")`

`local element = entity.spriteDef:GetElement(layer, "<element>")`

Or in one call:

`local element = entity.spriteDef:GetLayerElement("<layer>", "<element>")`

There is a **faster** approach. We can also work in the same order that the SpriteDef was defined, assuming the layer and element order and accessing them as arrays:

`layer = entity.spriteDef.layers[<index>]`

`element = layer.elements[<index>]`

Or in one call:

`element = entity.spriteDef:GetIndexedLayerElement(4, 0)`

Changing the original SpriteDef would change it for all objects using that SpriteDef, and only if they were all told to update their SpriteInstance.

If the SpriteDef itself is changed, to tell all related objects to update as soon as possible, for each one:

`entity.spriteInstanceDirty = true`

Or to update immediately:

`entity.ProcessSprites()`

If only the current sprite needs to change and the only way to do the animation is by animating the SpriteDef:

- Change the SpriteDef
- Use a custom property on the entity to track the change
- Call entity.ProcessSprites()
- Revert the SpriteDef to its original form


### Step 2 - SpriteDef Layers and Elements

> ParameciumMine example.

```
local spriteInstance = entity.spriteInstance

local rawElementUpper = spriteInstance:GetIndexedRawLayerElement(0, 0)
local rawElementLower = spriteInstance:GetIndexedRawLayerElement(0, 1)
local rawElementLight = spriteInstance:GetIndexedRawLayerElement(1, 0)
```

> ParameciumMine example 2 - slower but can be a useful technique.

```
local rawLayer = entity.spriteInstance.rawLayers[0]
local rawElementUpper = rawLayer.rawElements[0]
local rawElementLower = rawLayer.rawElements[1]
local lightLayer = entity.spriteInstance.rawLayers[1]
local lightElement = lightLayer.rawElements[0]
```

In most circumstances it's only the SpriteDef that should be changed.
Layers and elements are accessed in a similar fashion to with SpriteDefs, but note that these a given a raw label to differentiate them.

`local rawLayer = entity.spriteInstance:GetRawLayer("<layer>")`

`local rawElement = entity.spriteInstance:GetRawElement(rawLayer, "<element>")`

Or in one call:

`local rawElement = entity.spriteInstance:GetRawLayerElement("<layer>", "<element>")`

There is a faster approach. We can also work in the same order that the SpriteDef was defined, assuming the layer and element order and accessing them as arrays:

`rawLayer = entity.spriteInstance.rawLayers[<index>]`

`rawElement = rawLayer.rawElements[<index>]`

Or in one call:

`rawElement = entity.spriteInstance:GetIndexedRawLayerElement(<index>, <index>)`

<aside class="warning">
If any layers or elements are disabled, then the SpriteInstance will be in a different order to the SpriteDef.
</aside>


### Step 3 - Animate!

> ParameciumMine example.

```
local data = entity.data

-- Get the current point in the animation
local animationLength = data.animationLength
local time = App.game.LevelTime + data.animationOffset
local t = time - (math.floor(time / animationLength) * animationLength)

-- Sine pulse
local minScale = 1

local scale = math.sin((t * math.pi * 2)/animationLength)
local finalScale = (minScale ) + (scale * 0.2)

rawElementUpper:SetRadius(radiusUpper * finalScale)
rawElementUpper:SetLength(lengthUpper * finalScale)
rawElementLight:SetOffset(scale)

finalScale = (minScale) + (-scale * .2)
rawElementLower:SetRadius(radiusLower * finalScale)
rawElementLower:SetLength(lengthLower * finalScale)
rawElementLight:SetRadius(radiusUpper * (1 + (math.abs(scale))))
rawElementLight:SetLength(radiusUpper * (4.5 - (0.5 * math.abs(scale))))
```

SpriteDef properties are accessed using the same names as in the SpriteDef file.

Changing SpriteInstance or SpriteDef's properties directly can be slow, particularly with Vector2 and Color, as can accessing a colour's individual components.
Use the Set methods where possible.

The following SpriteInstance properties can be changed. Note that the actual effect does depend somewhat on the actual element being rendered.

Property | Type | Description
-------- | ---- | -----------
hotspot | Vector2 |
radius | float |
length | float |
angle | float |
angle2 | float | Used by Nose elements.
colour1 | Color |
colour2 | Color |
offset | float |
extension | float | Used by ExtendedLine elements.


Method | Parameters | Description
--------- | ------- | -----------
SetHotspot | float x, float y |
SetRadius | float |
SetLength | float |
SetAngle | float |
SetAngle2 | float |
SetColour1 | float r, float g, float b |
SetColour2 | float r, float g, float b |
SetColourAlpha | float |
SetOffset | float |
SetExtension | float |


### Step 4

If the size expands to substantially different than the original sprite, clipping will be affected. This can be rectified by calling:

`entity:RecalculateExtents()`

<aside class="notice">
This should only be used if clipping problems are apparent.
</aside>


## Misc Actions

### Dropping Energy

>Drop 5 units of energy in 15 energy balls within a 10 unit radius of the current entity.

```
App.terraformEnergyManager:AddEnergySpread(entity.position, 5, 15, 10.0)
```

To drop energy without relying on the regular energy drop:

`App.terraformEnergyManager:AddEnergySpread(position, amount, numParticles, radius[,timeOut])`

For a single ball of energy:

`App.terraformEnergyManager:AddEnergy(position, amount[,time out])`

Parameters | Type | Description
---------- | ---- | -----------
position | Vector2 | Location of energy drop.
amount | int | Amount of energy to drop.
numParticles | int | Number of particles to distribute energy within.
radius | float | Radius of energy drop area.
timeOut | float | How long before the energy times out. If no time out is provided, a random time will be used based on the life configs in GameDefaults:GameConfig.TerraformEnergyManager


