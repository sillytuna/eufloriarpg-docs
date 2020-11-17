
Entity Class
============



Namespace
    :dn:ns:`Clay.Game.Mod.Entities`

Assemblies
    * Clay.Game

----

.. contents::
   :local:



Inheritance Hierarchy
---------------------

* :dn:cls:`System.Object`
* :dn:cls:`Tuna.Mob`
* :dn:cls:`Clay.Game.Mod.Entities.Entity`




Syntax
------

.. code-block:: csharp

    public class Entity : Mob, IComparable, IAudioSourceInfo, ITargettable





.. dn:class:: Clay.Game.Mod.Entities.Entity
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.Entity


Constructors
------------

.. dn:class:: Clay.Game.Mod.Entities.Entity
    :noindex:
    :hidden:

    .. dn:constructor:: Clay.Game.Mod.Entities.Entity.Entity()




        .. code-block:: csharp

            public Entity()



Fields
------

.. dn:class:: Clay.Game.Mod.Entities.Entity
    :noindex:
    :hidden:

    .. dn:field:: Clay.Game.Mod.Entities.Entity.DAMAGE_FLASH_ALPHA



        :rtype: System.Single

        .. code-block:: csharp

            public const float DAMAGE_FLASH_ALPHA = 0.9F

    .. dn:field:: Clay.Game.Mod.Entities.Entity.DAMAGE_FLASH_DURATION



        :rtype: System.Single

        .. code-block:: csharp

            public const float DAMAGE_FLASH_DURATION = 0.3F

    .. dn:field:: Clay.Game.Mod.Entities.Entity.HARDPOINT_COUNT



        :rtype: System.Int32

        .. code-block:: csharp

            public const int HARDPOINT_COUNT = 7

    .. dn:field:: Clay.Game.Mod.Entities.Entity._canDie



        :rtype: System.Boolean

        .. code-block:: csharp

            protected bool _canDie

    .. dn:field:: Clay.Game.Mod.Entities.Entity._entityAvatar



        :rtype: Clay.Game.Components.EntityAvatar

        .. code-block:: csharp

            protected EntityAvatar _entityAvatar

    .. dn:field:: Clay.Game.Mod.Entities.Entity._entityWorldObject



        :rtype: Clay.Game.WorldObjectSystem.WorldObject

        .. code-block:: csharp

            protected WorldObject _entityWorldObject

    .. dn:field:: Clay.Game.Mod.Entities.Entity.mAttributes



        :rtype: Attributes

        .. code-block:: csharp

            protected Attributes mAttributes

    .. dn:field:: Clay.Game.Mod.Entities.Entity.mAutoSpawnedPosition



        :rtype: System.Boolean

        .. code-block:: csharp

            protected bool mAutoSpawnedPosition

    .. dn:field:: Clay.Game.Mod.Entities.Entity.mCustomisedSpawnAttributes



        :rtype: System.Boolean

        .. code-block:: csharp

            protected bool mCustomisedSpawnAttributes

    .. dn:field:: Clay.Game.Mod.Entities.Entity.mHomePosition



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            protected Vector2 mHomePosition

    .. dn:field:: Clay.Game.Mod.Entities.Entity.mLastPosition



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            protected Vector2 mLastPosition

    .. dn:field:: Clay.Game.Mod.Entities.Entity.mMaxSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public float mMaxSpeed

    .. dn:field:: Clay.Game.Mod.Entities.Entity.mOnUpdateHandlers



        :rtype: System.Collections.Generic.List<System.Collections.Generic.List`1>{Tuna.ScriptHandler<Tuna.ScriptHandler>}

        .. code-block:: csharp

            protected List<ScriptHandler> mOnUpdateHandlers

    .. dn:field:: Clay.Game.Mod.Entities.Entity.mPosition



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            protected Vector2 mPosition

    .. dn:field:: Clay.Game.Mod.Entities.Entity.mRotation



        :rtype: System.Single

        .. code-block:: csharp

            protected float mRotation

    .. dn:field:: Clay.Game.Mod.Entities.Entity.mVelocity



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            protected Vector2 mVelocity

    .. dn:field:: Clay.Game.Mod.Entities.Entity.sInvokeBuffer



        :rtype: System.Object<System.Object>[]

        .. code-block:: csharp

            protected static object[] sInvokeBuffer

    .. dn:field:: Clay.Game.Mod.Entities.Entity.sInvokeBuffer2



        :rtype: System.Object<System.Object>[]

        .. code-block:: csharp

            protected static object[] sInvokeBuffer2

    .. dn:field:: Clay.Game.Mod.Entities.Entity.sInvokeBuffer3



        :rtype: System.Object<System.Object>[]

        .. code-block:: csharp

            protected static object[] sInvokeBuffer3



Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.Entity
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.Entity.FollowTarget



        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity FollowTarget { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.MovementRestricted



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool MovementRestricted { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.PreferredAiAction



        :rtype: PreferredAiAction

        .. code-block:: csharp

            public PreferredAiAction PreferredAiAction { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.TargetablePosition



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public virtual Vector2 TargetablePosition { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.TargetableRect



        :rtype: System.Nullable<System.Nullable`1>{UnityEngine.Rect<UnityEngine.Rect>}

        .. code-block:: csharp

            public virtual Rect? TargetableRect { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._collisionRadius



        :rtype: System.Single

        .. code-block:: csharp

            public float _collisionRadius { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._contactDamageAmount

        
        Contact damage is applied once every update, and only when entities overlap and are on
        opposing Teams.




        :rtype: System.Single

        .. code-block:: csharp

            public float _contactDamageAmount { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._damagedFx



        :rtype: System.String

        .. code-block:: csharp

            public string _damagedFx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._deathSfx



        :rtype: System.String

        .. code-block:: csharp

            public string _deathSfx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._destroyedFx



        :rtype: System.String

        .. code-block:: csharp

            public string _destroyedFx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._detonator



        :rtype: Detonator

        .. code-block:: csharp

            public Detonator _detonator { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._entityFlags



        :rtype: Clay.Game.Mod.Entities.EntityFlags

        .. code-block:: csharp

            public EntityFlags _entityFlags { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._eufloripediaKey



        :rtype: System.String

        .. code-block:: csharp

            public string _eufloripediaKey { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._explosive



        :rtype: Explosive

        .. code-block:: csharp

            public Explosive _explosive { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._fieldOfView



        :rtype: System.Single

        .. code-block:: csharp

            public float _fieldOfView { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._freezeFx



        :rtype: System.String

        .. code-block:: csharp

            public string _freezeFx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._hardPoint1



        :rtype: HardPoint

        .. code-block:: csharp

            public HardPoint _hardPoint1 { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._hardPoint2



        :rtype: HardPoint

        .. code-block:: csharp

            public HardPoint _hardPoint2 { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._hardPoint3



        :rtype: HardPoint

        .. code-block:: csharp

            public HardPoint _hardPoint3 { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._hardPoint4



        :rtype: HardPoint

        .. code-block:: csharp

            public HardPoint _hardPoint4 { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._hardPoint5



        :rtype: HardPoint

        .. code-block:: csharp

            public HardPoint _hardPoint5 { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._hardPoint6



        :rtype: HardPoint

        .. code-block:: csharp

            public HardPoint _hardPoint6 { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._hardPoint7



        :rtype: HardPoint

        .. code-block:: csharp

            public HardPoint _hardPoint7 { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._healthPowerRule



        :rtype: Framework.Utils.PowerRule

        .. code-block:: csharp

            public PowerRule _healthPowerRule { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._healthRegenRate



        :rtype: System.Single

        .. code-block:: csharp

            public float _healthRegenRate { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._maxGroupSize



        :rtype: System.Int32

        .. code-block:: csharp

            public int _maxGroupSize { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._maxSpeedInterpolator



        :rtype: SpeedInterpolator

        .. code-block:: csharp

            public SpeedInterpolator _maxSpeedInterpolator { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._onActivateHandlers



        :rtype: System.String<System.String>[]

        .. code-block:: csharp

            public string[] _onActivateHandlers { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._onAnimateHandlers



        :rtype: System.String<System.String>[]

        .. code-block:: csharp

            public string[] _onAnimateHandlers { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._onCleanUpHandlers



        :rtype: System.String<System.String>[]

        .. code-block:: csharp

            public string[] _onCleanUpHandlers { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._onDeathHandlers



        :rtype: System.String<System.String>[]

        .. code-block:: csharp

            public string[] _onDeathHandlers { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._onUpdateHandlers



        :rtype: System.String<System.String>[]

        .. code-block:: csharp

            public string[] _onUpdateHandlers { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._scale



        :rtype: System.Single

        .. code-block:: csharp

            public float _scale { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._sicknessFx



        :rtype: System.String

        .. code-block:: csharp

            public string _sicknessFx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._speechBubblePreScaleRadius



        :rtype: System.Single

        .. code-block:: csharp

            public float _speechBubblePreScaleRadius { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._speedPowerRule



        :rtype: Framework.Utils.PowerRule

        .. code-block:: csharp

            public PowerRule _speedPowerRule { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._sprite



        :rtype: System.String

        .. code-block:: csharp

            public string _sprite { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._stasisFx



        :rtype: System.String

        .. code-block:: csharp

            public string _stasisFx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._stateMachine



        :rtype: System.String

        .. code-block:: csharp

            public string _stateMachine { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._targets



        :rtype: Targets

        .. code-block:: csharp

            public Targets _targets { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._terraformEnergyPowerRule



        :rtype: Framework.Utils.PowerRule

        .. code-block:: csharp

            public PowerRule _terraformEnergyPowerRule { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._thinkTimer



        :rtype: System.Single

        .. code-block:: csharp

            public float _thinkTimer { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._uiPreScaleRadius



        :rtype: System.Single

        .. code-block:: csharp

            public float _uiPreScaleRadius { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._useSpriteWithAvatar



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool _useSpriteWithAvatar { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._viewRangePowerRule



        :rtype: Framework.Utils.PowerRule

        .. code-block:: csharp

            public PowerRule _viewRangePowerRule { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._weakenedFx



        :rtype: System.String

        .. code-block:: csharp

            public string _weakenedFx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity._worldObjectAvatar



        :rtype: System.String

        .. code-block:: csharp

            public string _worldObjectAvatar { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.aiGroup



        :rtype: AIGroup

        .. code-block:: csharp

            public AIGroup aiGroup { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.alpha



        :rtype: System.Single

        .. code-block:: csharp

            public float alpha { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.attributeRecoveryRate



        :rtype: System.Single

        .. code-block:: csharp

            public static float attributeRecoveryRate { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.attributes



        :rtype: Attributes

        .. code-block:: csharp

            public Attributes attributes { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.audioPosition



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 audioPosition { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.audioRange



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public virtual Vector2 audioRange { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.autoSpawnedPosition



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool autoSpawnedPosition { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.beamParticleProbability



        :rtype: System.Int32

        .. code-block:: csharp

            public static int beamParticleProbability { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.boundingRegionDirty



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool boundingRegionDirty { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.canResurrect



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool canResurrect { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.canRotate



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool canRotate { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.clipRadius



        :rtype: System.Single

        .. code-block:: csharp

            public float clipRadius { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.clipRegion



        :rtype: Tuna.CenteredAxisAlignedBox

        .. code-block:: csharp

            public CenteredAxisAlignedBox clipRegion { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.collidedWithDoor



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool collidedWithDoor { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.collidedWithDoorInfo



        :rtype: Door

        .. code-block:: csharp

            public Door collidedWithDoorInfo { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.collidedWithScenery



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool collidedWithScenery { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.collidedWithSceneryInfo



        :rtype: DistanceFieldCollisionInfo

        .. code-block:: csharp

            public DistanceFieldCollisionInfo collidedWithSceneryInfo { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.collisionQuadTreeNode



        :rtype: QuadTreeNode

        .. code-block:: csharp

            public QuadTreeNode collisionQuadTreeNode { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.collisionRegion



        :rtype: Tuna.CenteredCircle

        .. code-block:: csharp

            public CenteredCircle collisionRegion { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.collisionResponseMinSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public static float collisionResponseMinSpeed { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.collisionResponseSpeedMultiplier



        :rtype: System.Single

        .. code-block:: csharp

            public static float collisionResponseSpeedMultiplier { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.colours



        :rtype: UnityEngine.Color<UnityEngine.Color>[]

        .. code-block:: csharp

            public Color[] colours { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.cosHalfFieldOfView



        :rtype: System.Single

        .. code-block:: csharp

            public float cosHalfFieldOfView { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.csdata



        :rtype: Clay.Game.ScriptedData

        .. code-block:: csharp

            public ScriptedData csdata { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.customisedAttributes



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool customisedAttributes { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.damageParticleCountMultiRange



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public static Vector2 damageParticleCountMultiRange { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.damageProportionForMaxParticles



        :rtype: System.Single

        .. code-block:: csharp

            public static float damageProportionForMaxParticles { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.data



        :rtype: MoonSharp.Interpreter.Table

        .. code-block:: csharp

            public Table data { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.doorCollisionsEnabled



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool doorCollisionsEnabled { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.editHelpers



        :rtype: System.Collections.Generic.Dictionary<System.Collections.Generic.Dictionary`2>{System.String<System.String>, EditHelper<EditHelper>}

        .. code-block:: csharp

            public Dictionary<string, EditHelper> editHelpers { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.entityRenderCount



        :rtype: System.Single

        .. code-block:: csharp

            public static float entityRenderCount { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.explodeOnDeath



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool explodeOnDeath { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.followingEntity



        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity followingEntity { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.hardPoints



        :rtype: HardPoint<HardPoint>[]

        .. code-block:: csharp

            public HardPoint[] hardPoints { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.hasFieldOfView



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool hasFieldOfView { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.hasHome



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool hasHome { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.health



        :rtype: System.Single

        .. code-block:: csharp

            public float health { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.healthRatio



        :rtype: System.Single

        .. code-block:: csharp

            public float healthRatio { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.homePosition



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 homePosition { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.inventoryManager



        :rtype: InventoryManager

        .. code-block:: csharp

            public InventoryManager inventoryManager { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isAlive



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isAlive { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isAttractor



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isAttractor { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isAudioAvailable



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isAudioAvailable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isAudioCustomRange



        :rtype: System.Boolean

        .. code-block:: csharp

            public virtual bool isAudioCustomRange { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isColonist



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isColonist { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isColonyAttackResponse



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isColonyAttackResponse { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isContactDamage



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isContactDamage { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isDamageable



        :rtype: System.Boolean

        .. code-block:: csharp

            public virtual bool isDamageable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isDamagedByExplosives



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isDamagedByExplosives { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isDamagedByFreeze



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isDamagedByFreeze { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isDamagedBySickness



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isDamagedBySickness { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isDamagedByStasis



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isDamagedByStasis { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isDamagedBySuppression



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isDamagedBySuppression { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isDamagedByWeapons



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isDamagedByWeapons { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isDead



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isDead { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isDecorativeEntity



        :rtype: System.Boolean

        .. code-block:: csharp

            public virtual bool isDecorativeEntity { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isDetonatorActive



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isDetonatorActive { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isEnergyDropper



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isEnergyDropper { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isEquipment



        :rtype: System.Boolean

        .. code-block:: csharp

            public virtual bool isEquipment { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isFlora



        :rtype: System.Boolean

        .. code-block:: csharp

            public virtual bool isFlora { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isFrozen



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isFrozen { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isInStasis



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isInStasis { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isInteractive



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isInteractive { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isInvulnerable



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isInvulnerable { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isMine



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isMine { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isMorphingAttributes



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isMorphingAttributes { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isPlayer



        :rtype: System.Boolean

        .. code-block:: csharp

            public virtual bool isPlayer { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isPreferredTarget



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isPreferredTarget { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isRepellant



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isRepellant { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isResurrected



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isResurrected { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isSick



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isSick { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isSpawnedByLevel



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isSpawnedByLevel { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isSplinePathFinished



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isSplinePathFinished { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isStateLocked



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isStateLocked { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isTargetable



        :rtype: System.Boolean

        .. code-block:: csharp

            public virtual bool isTargetable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isThinking



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isThinking { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.isThinkingFixedUpdate



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isThinkingFixedUpdate { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.lastPosition



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 lastPosition { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.maxHealth



        :rtype: System.Single

        .. code-block:: csharp

            public float maxHealth { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.maxSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public float maxSpeed { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.normalizedFreeze



        :rtype: System.Single

        .. code-block:: csharp

            public float normalizedFreeze { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.offScreenAITimerMultiplier



        :rtype: System.Single

        .. code-block:: csharp

            public static float offScreenAITimerMultiplier { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.otherRepawnParams



        :rtype: System.Collections.Generic.List<System.Collections.Generic.List`1>{System.String<System.String>}

        .. code-block:: csharp

            public List<string> otherRepawnParams { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.owner



        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity owner { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.palette



        :rtype: Tuna.Palette

        .. code-block:: csharp

            public Palette palette { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.parentColony



        :rtype: Colony

        .. code-block:: csharp

            public Colony parentColony { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.parentFlora



        :rtype: Clay.Game.Mod.Entities.Flora

        .. code-block:: csharp

            public Flora parentFlora { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.pitch



        :rtype: System.Single

        .. code-block:: csharp

            public virtual float pitch { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.position



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 position { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.prefersPlayerTarget



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool prefersPlayerTarget { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.px



        :rtype: System.Single

        .. code-block:: csharp

            public float px { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.py



        :rtype: System.Single

        .. code-block:: csharp

            public float py { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.quadTreeNode



        :rtype: QuadTreeNode

        .. code-block:: csharp

            public QuadTreeNode quadTreeNode { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.radarTarget



        :rtype: RadarTarget

        .. code-block:: csharp

            public RadarTarget radarTarget { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.radius



        :rtype: System.Single

        .. code-block:: csharp

            public float radius { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.requireDoorCollisionTest



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool requireDoorCollisionTest { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.requiresLineOfSight



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool requiresLineOfSight { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.respawnRule



        :rtype: Clay.Game.Mod.Entities.RespawnRules

        .. code-block:: csharp

            public RespawnRules respawnRule { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.rotation



        :rtype: System.Single

        .. code-block:: csharp

            public float rotation { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.scale



        :rtype: System.Single

        .. code-block:: csharp

            public float scale { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.sceneryCollisionsEnabled



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool sceneryCollisionsEnabled { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.seekFriendlyPlayer



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool seekFriendlyPlayer { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.seekTargets



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool seekTargets { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.sensibleAiPosition



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public virtual Vector2 sensibleAiPosition { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.sicknessRange



        :rtype: System.Single

        .. code-block:: csharp

            public static float sicknessRange { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.sicknessSpeedMultiplier



        :rtype: System.Single

        .. code-block:: csharp

            public static float sicknessSpeedMultiplier { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.spawnHash



        :rtype: System.String

        .. code-block:: csharp

            public string spawnHash { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.speechBubbleRadius



        :rtype: System.Single

        .. code-block:: csharp

            public float speechBubbleRadius { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.speed



        :rtype: System.Single

        .. code-block:: csharp

            public virtual float speed { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.splinePath



        :rtype: Clay.Game.SplinePath

        .. code-block:: csharp

            public SplinePath splinePath { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.splinePathLength



        :rtype: System.Single

        .. code-block:: csharp

            public float splinePathLength { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.splinePathNearestVertex



        :rtype: System.Int32

        .. code-block:: csharp

            public int splinePathNearestVertex { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.splinePathPosition



        :rtype: System.Single

        .. code-block:: csharp

            public float splinePathPosition { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.spriteDef



        :rtype: Tuna.SpriteDef

        .. code-block:: csharp

            public SpriteDef spriteDef { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.spriteInstance



        :rtype: Tuna.SpriteInstance

        .. code-block:: csharp

            public SpriteInstance spriteInstance { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.spriteInstanceDirty



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool spriteInstanceDirty { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.spriteName



        :rtype: System.String

        .. code-block:: csharp

            public string spriteName { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.stateMachine



        :rtype: AIStateMachine

        .. code-block:: csharp

            public AIStateMachine stateMachine { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.stateMachineData



        :rtype: AIStateMachineData

        .. code-block:: csharp

            public AIStateMachineData stateMachineData { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.stateName



        :rtype: System.String

        .. code-block:: csharp

            public string stateName { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.targetsEntities



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool targetsEntities { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.targetsFlora



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool targetsFlora { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.team



        :rtype: Team

        .. code-block:: csharp

            public Team team { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.teamName



        :rtype: System.String

        .. code-block:: csharp

            public string teamName { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.terraformEnergy



        :rtype: System.Int32

        .. code-block:: csharp

            public int terraformEnergy { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.terraformEnergyDropRange



        :rtype: System.Single

        .. code-block:: csharp

            public static float terraformEnergyDropRange { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.transform



        :rtype: UnityEngine.Transform

        .. code-block:: csharp

            protected Transform transform { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.uiRadius



        :rtype: System.Single

        .. code-block:: csharp

            public float uiRadius { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.useSpawnEntityCommand



        :rtype: System.Boolean

        .. code-block:: csharp

            public virtual bool useSpawnEntityCommand { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.velocity



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 velocity { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.viewRange



        :rtype: System.Single

        .. code-block:: csharp

            public float viewRange { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.visiblePitch



        :rtype: System.Single

        .. code-block:: csharp

            public virtual float visiblePitch { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.vx



        :rtype: System.Single

        .. code-block:: csharp

            public float vx { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.vy



        :rtype: System.Single

        .. code-block:: csharp

            public float vy { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.wasAttacked



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool wasAttacked { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.wasAttackedBy



        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity wasAttackedBy { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.wasOnScreen



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool wasOnScreen { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.wasSick



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool wasSick { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Entity.weapons



        :rtype: System.Collections.Generic.List<System.Collections.Generic.List`1>{Weapon<Weapon>}

        .. code-block:: csharp

            public List<Weapon> weapons { get; }



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.Entity
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.Entity.Activate(Attributes, UnityEngine.Vector2, System.Single, Colony, Team)



        :type attr: Attributes

        :type atPosition: UnityEngine.Vector2

        :type atAngle: System.Single

        :type colony: Colony

        :type newTeam: Team


        .. code-block:: csharp

            public virtual void Activate(Attributes attr, Vector2 atPosition, float atAngle, Colony colony, Team newTeam)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.Activate(UnityEngine.Vector2)



        :type atPosition: UnityEngine.Vector2


        .. code-block:: csharp

            public void Activate(Vector2 atPosition)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.Activate(UnityEngine.Vector2, Colony)



        :type atPosition: UnityEngine.Vector2

        :type colony: Colony


        .. code-block:: csharp

            public void Activate(Vector2 atPosition, Colony colony)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.AddOverlay(System.String, System.Int32)



        :type spriteName: System.String

        :type layerModifier: System.Int32

        :rtype: Overlay

        .. code-block:: csharp

            public Overlay AddOverlay(string spriteName, int layerModifier)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.AddWeapon(HardPoint)



        :type hardPoint: HardPoint

        :rtype: Weapon

        .. code-block:: csharp

            public Weapon AddWeapon(HardPoint hardPoint)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.AddWeapon(System.String, HardPoint)



        :type weaponType: System.String

        :type hardPoint: HardPoint

        :rtype: Weapon

        .. code-block:: csharp

            public virtual Weapon AddWeapon(string weaponType, HardPoint hardPoint)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.AddWeapon(System.String, System.String)



        :type weaponType: System.String

        :type hardPointName: System.String

        :rtype: Weapon

        .. code-block:: csharp

            public Weapon AddWeapon(string weaponType, string hardPointName)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.AddWeaponToIndex(System.String, System.Int32)



        :type weaponType: System.String

        :type index: System.Int32

        :rtype: Weapon

        .. code-block:: csharp

            public Weapon AddWeaponToIndex(string weaponType, int index)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.AttackedBy(Clay.Game.Mod.Entities.Entity)



        :type attacker: Clay.Game.Mod.Entities.Entity


        .. code-block:: csharp

            public void AttackedBy(Entity attacker)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.CallHandlers(System.String[])



        :type handlerNames: System.String<System.String>[]


        .. code-block:: csharp

            public void CallHandlers(string[] handlerNames)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.CallHandlers(System.String[], System.Object[])



        :type handlerNames: System.String<System.String>[]

        :type invokeBuffer: System.Object<System.Object>[]


        .. code-block:: csharp

            public void CallHandlers(string[] handlerNames, object[] invokeBuffer)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.CanAttack()



        :rtype: System.Boolean

        .. code-block:: csharp

            public virtual bool CanAttack()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.CleanUpLevel()




        .. code-block:: csharp

            public static void CleanUpLevel()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.CleanUpScripts()




        .. code-block:: csharp

            protected virtual void CleanUpScripts()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.ClearSpriteDef()




        .. code-block:: csharp

            public void ClearSpriteDef()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.CloneConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            public override void CloneConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.CommonCleanUp()




        .. code-block:: csharp

            protected virtual void CommonCleanUp()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.CreateInventoryManager()




        .. code-block:: csharp

            public void CreateInventoryManager()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.CreateInventoryManager(System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Int32)



        :type consumables: System.Int32

        :type accessories: System.Int32

        :type seeds: System.Int32

        :type seedUnits: System.Int32

        :type consumableUnits: System.Int32

        :type artifacts: System.Int32


        .. code-block:: csharp

            public void CreateInventoryManager(int consumables, int accessories, int seeds, int seedUnits, int consumableUnits, int artifacts)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.CreateRadarTarget(RadarTypes, System.String)



        :type radarType: RadarTypes

        :type textureID: System.String

        :rtype: RadarTarget

        .. code-block:: csharp

            public RadarTarget CreateRadarTarget(RadarTypes radarType = RadarTypes.None, string textureID = "")

    .. dn:method:: Clay.Game.Mod.Entities.Entity.CreateRenderList()




        .. code-block:: csharp

            public static void CreateRenderList()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.DamagedBy(Clay.Game.Mod.Entities.Entity, System.Single, Weapon, System.Boolean, System.Boolean)

        
        Call to inflict damage on this entity.




        :param attacker: The instigator of this damage
        :type attacker: Clay.Game.Mod.Entities.Entity

        :param damage: How much damage to apply
        :type damage: System.Single

        :param weapon: The weapon that belongs to the attacker dealing this damage.
        :type weapon: Weapon

        :param effectHandled: If you are performing manual Effects, you should pass true to this method
        :type effectHandled: System.Boolean

        :param fxHandled: If you are performing manual FX, you should pass true to this method
        :type fxHandled: System.Boolean

        :rtype: System.Boolean
        :return: True if this method inflicts damage, False otherwise

        .. code-block:: csharp

            public virtual bool DamagedBy(Entity attacker, float damage, Weapon weapon, bool effectHandled = false, bool fxHandled = false)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.Die(System.Boolean, System.Boolean, System.Boolean)



        :type exploded: System.Boolean

        :type trash: System.Boolean

        :type quietly: System.Boolean


        .. code-block:: csharp

            public virtual void Die(bool exploded = false, bool trash = true, bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.DieQuietly()




        .. code-block:: csharp

            public virtual void DieQuietly()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.DoPhysics(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public virtual void DoPhysics(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.DoorCollisionHandler(Door)



        :type door: Door


        .. code-block:: csharp

            public virtual void DoorCollisionHandler(Door door)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.DropDeathEnergy()




        .. code-block:: csharp

            protected void DropDeathEnergy()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.EarlyRender()




        .. code-block:: csharp

            public override void EarlyRender()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.EditorHealthChanged()




        .. code-block:: csharp

            public void EditorHealthChanged()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.EditorSpriteNameChanged()




        .. code-block:: csharp

            public void EditorSpriteNameChanged()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.EnterFreeze(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public void EnterFreeze(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.EnterSickness(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public void EnterSickness(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.EnterStasis(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public void EnterStasis(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.EntityFixedUpdate(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public virtual void EntityFixedUpdate(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.Explode()




        .. code-block:: csharp

            public virtual void Explode()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.ExplodeOnTarget(Clay.Game.Mod.Entities.Entity)



        :type entity: Clay.Game.Mod.Entities.Entity


        .. code-block:: csharp

            public void ExplodeOnTarget(Entity entity)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.ExplodeOnTargetBranch(FloraBranch, UnityEngine.Vector2, UnityEngine.Vector2)



        :type branch: FloraBranch

        :type hitPosition: UnityEngine.Vector2

        :type hitDirection: UnityEngine.Vector2


        .. code-block:: csharp

            public void ExplodeOnTargetBranch(FloraBranch branch, Vector2 hitPosition, Vector2 hitDirection)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.Find(System.String)



        :type name: System.String

        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public static Entity Find(string name)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindByInternalUID(System.Int32)



        :type uid: System.Int32

        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public static Entity FindByInternalUID(int uid)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindByUID(System.String)



        :type uid: System.String

        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public static Entity FindByUID(string uid)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindHardPoint(System.String)



        :type name: System.String

        :rtype: HardPoint

        .. code-block:: csharp

            public HardPoint FindHardPoint(string name)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindHardPointByIndex(System.Int32)



        :type index: System.Int32

        :rtype: HardPoint

        .. code-block:: csharp

            public HardPoint FindHardPointByIndex(int index)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindNearestEntity(UnityEngine.Vector3, System.Single, GameUtils.IsEntityTargetValidDelegate)



        :type searchPosition: UnityEngine.Vector3

        :type range: System.Single

        :type isEntityTargetValidCB: GameUtils.IsEntityTargetValidDelegate

        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity FindNearestEntity(Vector3 searchPosition, float range, GameUtils.IsEntityTargetValidDelegate isEntityTargetValidCB)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindNearestEntityAny(UnityEngine.Vector3, System.Single, GameUtils.IsEntityTargetValidDelegate)



        :type searchPosition: UnityEngine.Vector3

        :type range: System.Single

        :type isEntityTargetValidCB: GameUtils.IsEntityTargetValidDelegate

        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity FindNearestEntityAny(Vector3 searchPosition, float range, GameUtils.IsEntityTargetValidDelegate isEntityTargetValidCB)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindNearestTarget()



        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity FindNearestTarget()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindNearestTarget(System.Single)



        :type range: System.Single

        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity FindNearestTarget(float range)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindNearestTarget(System.Single, GameUtils.IsEntityTargetValidDelegate)



        :type range: System.Single

        :type isEntityTargetValidCB: GameUtils.IsEntityTargetValidDelegate

        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity FindNearestTarget(float range, GameUtils.IsEntityTargetValidDelegate isEntityTargetValidCB)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindNearestTarget(UnityEngine.Vector3, System.Single)



        :type searchPosition: UnityEngine.Vector3

        :type range: System.Single

        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity FindNearestTarget(Vector3 searchPosition, float range)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindNearestTarget(UnityEngine.Vector3, System.Single, GameUtils.IsEntityTargetValidDelegate)



        :type searchPosition: UnityEngine.Vector3

        :type range: System.Single

        :type isEntityTargetValidCB: GameUtils.IsEntityTargetValidDelegate

        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity FindNearestTarget(Vector3 searchPosition, float range, GameUtils.IsEntityTargetValidDelegate isEntityTargetValidCB)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindWeapon(System.String)



        :type type: System.String

        :rtype: Weapon

        .. code-block:: csharp

            public Weapon FindWeapon(string type)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindWeaponAtHardPoint(HardPoint)



        :type hardPoint: HardPoint

        :rtype: Weapon

        .. code-block:: csharp

            public Weapon FindWeaponAtHardPoint(HardPoint hardPoint)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindWeaponAtHardPoint(System.String)



        :type name: System.String

        :rtype: Weapon

        .. code-block:: csharp

            public Weapon FindWeaponAtHardPoint(string name)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FindWeaponAtHardPointIndex(System.Int32)



        :type index: System.Int32

        :rtype: Weapon

        .. code-block:: csharp

            public Weapon FindWeaponAtHardPointIndex(int index)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FixedUpdate(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void FixedUpdate(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FixedUpdateAllEntityPhysics(System.Single, System.Int32, System.Int32)



        :type time: System.Single

        :type thread: System.Int32

        :type threadCount: System.Int32


        .. code-block:: csharp

            public static void FixedUpdateAllEntityPhysics(float time, int thread, int threadCount)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FixedUpdatePhysics(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public void FixedUpdatePhysics(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FixedUpdateQuadTreeLocators()




        .. code-block:: csharp

            public static void FixedUpdateQuadTreeLocators()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FloraAttackedBy(Clay.Game.Mod.Entities.Entity)



        :type attacker: Clay.Game.Mod.Entities.Entity


        .. code-block:: csharp

            public void FloraAttackedBy(Entity attacker)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FollowEntity(Clay.Game.Mod.Entities.Entity)



        :type entity: Clay.Game.Mod.Entities.Entity


        .. code-block:: csharp

            public virtual void FollowEntity(Entity entity)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.FrozenBy(Clay.Game.Mod.Entities.Entity, System.Single)



        :type attacker: Clay.Game.Mod.Entities.Entity

        :type damage: System.Single


        .. code-block:: csharp

            public void FrozenBy(Entity attacker, float damage)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.GenerateAllCharacteristics()




        .. code-block:: csharp

            public void GenerateAllCharacteristics()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.GenerateCharacteristics()




        .. code-block:: csharp

            protected virtual void GenerateCharacteristics()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.GenerateDependantCharacteristics()




        .. code-block:: csharp

            protected virtual void GenerateDependantCharacteristics()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.GenerateWeaponCharacteristics()




        .. code-block:: csharp

            public void GenerateWeaponCharacteristics()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.GetCommandLine(System.Boolean)



        :type multiLine: System.Boolean

        :rtype: System.String

        .. code-block:: csharp

            public virtual string GetCommandLine(bool multiLine)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.GetRespawnString()



        :rtype: System.String

        .. code-block:: csharp

            public virtual string GetRespawnString()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.Heal()




        .. code-block:: csharp

            public void Heal()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.HomeDistanceSquared(UnityEngine.Vector2)



        :type sourcePosition: UnityEngine.Vector2

        :rtype: System.Single

        .. code-block:: csharp

            public float HomeDistanceSquared(Vector2 sourcePosition)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.InRange(Clay.Game.Mod.Entities.Entity)



        :type entity: Clay.Game.Mod.Entities.Entity

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool InRange(Entity entity)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.InRange(Clay.Game.Mod.Entities.Entity, System.Single)



        :type entity: Clay.Game.Mod.Entities.Entity

        :type range: System.Single

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool InRange(Entity entity, float range)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.InRange(System.Single, System.Single, System.Single)



        :type x: System.Single

        :type y: System.Single

        :type range: System.Single

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool InRange(float x, float y, float range)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.InRange(UnityEngine.Vector2, System.Single)



        :type position: UnityEngine.Vector2

        :type range: System.Single

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool InRange(Vector2 position, float range)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.InitialiseApp()




        .. code-block:: csharp

            public static void InitialiseApp()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.InitialiseAttributeMorphing(Attributes, System.Single)



        :type attr: Attributes

        :type rate: System.Single


        .. code-block:: csharp

            public void InitialiseAttributeMorphing(Attributes attr, float rate)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.InitialiseLevel()




        .. code-block:: csharp

            public static void InitialiseLevel()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.InitialiseScripts(System.Boolean)



        :type rebuild: System.Boolean


        .. code-block:: csharp

            protected virtual void InitialiseScripts(bool rebuild)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsContactDamageTargetValidCB(Clay.Game.Mod.Entities.Entity, UnityEngine.Vector2)



        :type target: Clay.Game.Mod.Entities.Entity

        :type sourcePosition: UnityEngine.Vector2

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsContactDamageTargetValidCB(Entity target, Vector2 sourcePosition)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsEntityVisible(Clay.Game.Mod.Entities.Entity)



        :type entity: Clay.Game.Mod.Entities.Entity

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsEntityVisible(Entity entity)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsFloraElementTargetValidCB(FloraElement, UnityEngine.Vector2, UnityEngine.Vector2, UnityEngine.Vector2, System.Single)



        :type target: FloraElement

        :type sourcePosition: UnityEngine.Vector2

        :type targetPosition: UnityEngine.Vector2

        :type dv: UnityEngine.Vector2

        :type targetDistanceSq: System.Single

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsFloraElementTargetValidCB(FloraElement target, Vector2 sourcePosition, Vector2 targetPosition, Vector2 dv, float targetDistanceSq)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsFloraTargetValidCB(Clay.Game.Mod.Entities.Flora)



        :type target: Clay.Game.Mod.Entities.Flora

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsFloraTargetValidCB(Flora target)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsFollowTargetValidCB(Clay.Game.Mod.Entities.Entity, UnityEngine.Vector2)



        :type target: Clay.Game.Mod.Entities.Entity

        :type sourcePosition: UnityEngine.Vector2

        :rtype: System.Boolean

        .. code-block:: csharp

            public virtual bool IsFollowTargetValidCB(Entity target, Vector2 sourcePosition)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsInFieldOfView(Clay.Game.Mod.Entities.Entity)



        :type entity: Clay.Game.Mod.Entities.Entity

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsInFieldOfView(Entity entity)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsInFieldOfView(System.Single, System.Single)



        :type x: System.Single

        :type y: System.Single

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsInFieldOfView(float x, float y)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsInFieldOfView(UnityEngine.Rect)



        :type bounds: UnityEngine.Rect

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsInFieldOfView(Rect bounds)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsInFieldOfView(UnityEngine.Vector2)



        :type targetPosition: UnityEngine.Vector2

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsInFieldOfView(Vector2 targetPosition)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsInFieldOfView(UnityEngine.Vector2, System.Single)



        :type dv: UnityEngine.Vector2

        :type targetDistanceSq: System.Single

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsInFieldOfView(Vector2 dv, float targetDistanceSq)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsInFieldOfViewIsInLineOfSight(System.Single, System.Single)



        :type x: System.Single

        :type y: System.Single

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsInFieldOfViewIsInLineOfSight(float x, float y)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsInFieldOfViewIsInLineOfSightIgnoreUnlockedDoors(System.Single, System.Single)



        :type x: System.Single

        :type y: System.Single

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsInFieldOfViewIsInLineOfSightIgnoreUnlockedDoors(float x, float y)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsInLineOfSight(Clay.Game.Mod.Entities.Entity)



        :type entity: Clay.Game.Mod.Entities.Entity

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsInLineOfSight(Entity entity)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsInLineOfSight(UnityEngine.Rect)



        :type bounds: UnityEngine.Rect

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsInLineOfSight(Rect bounds)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsInLineOfSight(UnityEngine.Vector2)



        :type targetPosition: UnityEngine.Vector2

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsInLineOfSight(Vector2 targetPosition)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsInLineOfSightIgnoreUnlockedDoors(UnityEngine.Vector2)



        :type targetPosition: UnityEngine.Vector2

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsInLineOfSightIgnoreUnlockedDoors(Vector2 targetPosition)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsOnScreen(System.Boolean)



        :type recalculate: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsOnScreen(bool recalculate = false)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsPlayerAction()



        :rtype: System.Boolean

        .. code-block:: csharp

            public virtual bool IsPlayerAction()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsSaveable()



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsSaveable()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IsSicknessTargetValidCB(Clay.Game.Mod.Entities.Entity, UnityEngine.Vector2)



        :type target: Clay.Game.Mod.Entities.Entity

        :type sourcePosition: UnityEngine.Vector2

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsSicknessTargetValidCB(Entity target, Vector2 sourcePosition)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.IssueCommand(Clay.Game.CommandTypes, UnityEngine.Vector2, System.Boolean)



        :type commandType: Clay.Game.CommandTypes

        :type fromPosition: UnityEngine.Vector2

        :type quietly: System.Boolean


        .. code-block:: csharp

            public void IssueCommand(CommandTypes commandType, Vector2 fromPosition, bool quietly)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.LogWeaponDebugInfo(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public void LogWeaponDebugInfo(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.ModifyHealth(System.Single)



        :type value: System.Single

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool ModifyHealth(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.MovePosition(System.Single, System.Single)



        :type x: System.Single

        :type y: System.Single


        .. code-block:: csharp

            public virtual void MovePosition(float x, float y)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.MovePosition(UnityEngine.Vector2)



        :type value: UnityEngine.Vector2


        .. code-block:: csharp

            public virtual void MovePosition(Vector2 value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.MutateAttribute(System.Single, System.Single, System.Single, System.Single)



        :type value: System.Single

        :type modifier: System.Single

        :type min: System.Single

        :type max: System.Single

        :rtype: System.Single

        .. code-block:: csharp

            public float MutateAttribute(float value, float modifier, float min = 0.2F, float max = 1F)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.OnEntityDiedOrTrashedListener(System.String, System.Object, System.Object, System.Object)



        :type ev: System.String

        :type sender: System.Object

        :type param1: System.Object

        :type param2: System.Object


        .. code-block:: csharp

            protected virtual void OnEntityDiedOrTrashedListener(string ev, object sender, object param1, object param2)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.OutOfHealth()




        .. code-block:: csharp

            public virtual void OutOfHealth()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.ParentAwakened()




        .. code-block:: csharp

            public virtual void ParentAwakened()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.ParentColonised()




        .. code-block:: csharp

            public virtual void ParentColonised()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.ParentFloraDied(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public virtual void ParentFloraDied(bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.PingFollowVisual()




        .. code-block:: csharp

            public void PingFollowVisual()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.PlayOrRetrySfx(System.String)



        :type sfxName: System.String

        :rtype: Tuna.SoundVoice

        .. code-block:: csharp

            public SoundVoice PlayOrRetrySfx(string sfxName)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.PlaySfx(System.String)



        :type sfxName: System.String

        :rtype: Tuna.SoundVoice

        .. code-block:: csharp

            public SoundVoice PlaySfx(string sfxName)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.ProcessSprites()




        .. code-block:: csharp

            public void ProcessSprites()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.Prototyped()




        .. code-block:: csharp

            public override void Prototyped()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.ReadAIStateConfig(AIState)



        :type state: AIState


        .. code-block:: csharp

            public virtual void ReadAIStateConfig(AIState state)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.ReadProperty(System.Object, System.Reflection.PropertyInfo, Tuna.Setting)



        :type o: System.Object

        :type property: System.Reflection.PropertyInfo

        :type setting: Tuna.Setting

        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool ReadProperty(object o, PropertyInfo property, Setting setting)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.ReadUndefinedSetting(System.Object, Tuna.Setting)



        :type o: System.Object

        :type setting: Tuna.Setting

        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool ReadUndefinedSetting(object o, Setting setting)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RebuildAIScripts()




        .. code-block:: csharp

            public void RebuildAIScripts()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RebuildAIStateMachine()




        .. code-block:: csharp

            public void RebuildAIStateMachine()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RebuildAttributes()




        .. code-block:: csharp

            public void RebuildAttributes()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RebuildPrototype()




        .. code-block:: csharp

            public override void RebuildPrototype()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RebuildSprite()




        .. code-block:: csharp

            public void RebuildSprite()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RecalculateExtents()




        .. code-block:: csharp

            protected virtual void RecalculateExtents()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RecalculateSpriteExtents()




        .. code-block:: csharp

            public void RecalculateSpriteExtents()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RecycleConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            protected override void RecycleConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RemoveOverlay(Overlay)



        :type overlay: Overlay


        .. code-block:: csharp

            public void RemoveOverlay(Overlay overlay)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RemoveOverlay(System.String)



        :type spriteName: System.String


        .. code-block:: csharp

            public void RemoveOverlay(string spriteName)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RemoveRadarTarget()




        .. code-block:: csharp

            public void RemoveRadarTarget()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RemoveSplinePath()




        .. code-block:: csharp

            public void RemoveSplinePath()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RemoveWeapon(System.String)



        :type weaponType: System.String


        .. code-block:: csharp

            public void RemoveWeapon(string weaponType)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RemoveWeapon(Weapon)



        :type weapon: Weapon


        .. code-block:: csharp

            public void RemoveWeapon(Weapon weapon)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RemoveWeaponAtHardPoint(HardPoint)



        :type hardPoint: HardPoint


        .. code-block:: csharp

            public void RemoveWeaponAtHardPoint(HardPoint hardPoint)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RemoveWeaponAtHardPoint(System.String)



        :type hardPointName: System.String


        .. code-block:: csharp

            public void RemoveWeaponAtHardPoint(string hardPointName)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RemoveWeaponAtHardPoint(System.String, HardPoint)



        :type weaponType: System.String

        :type hardPoint: HardPoint


        .. code-block:: csharp

            public void RemoveWeaponAtHardPoint(string weaponType, HardPoint hardPoint)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RemoveWeaponAtHardPoint(System.String, System.String)



        :type weaponType: System.String

        :type hardPointName: System.String


        .. code-block:: csharp

            public void RemoveWeaponAtHardPoint(string weaponType, string hardPointName)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RemoveWeaponAtHardPointIndex(System.Int32)



        :type index: System.Int32


        .. code-block:: csharp

            public void RemoveWeaponAtHardPointIndex(int index)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RemoveWeaponAtHardPointIndex(System.String, System.Int32)



        :type weaponType: System.String

        :type index: System.Int32


        .. code-block:: csharp

            public void RemoveWeaponAtHardPointIndex(string weaponType, int index)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.Render()




        .. code-block:: csharp

            public override void Render()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RenderDebug()




        .. code-block:: csharp

            public override void RenderDebug()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RenderDebugStatString()




        .. code-block:: csharp

            protected void RenderDebugStatString()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RenderDebugWeapons()




        .. code-block:: csharp

            public void RenderDebugWeapons()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RenderLeaf(FloraLeaf, System.Single, System.Single)



        :type leaf: FloraLeaf

        :type alpha: System.Single

        :type size: System.Single

        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 RenderLeaf(FloraLeaf leaf, float alpha, float size)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.RenderWeapons()




        .. code-block:: csharp

            public void RenderWeapons()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.ResetPalette()




        .. code-block:: csharp

            public void ResetPalette()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.Resurrect()




        .. code-block:: csharp

            public virtual void Resurrect()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SceneryCollisionHandler(DistanceFieldCollisionInfo)



        :type info: DistanceFieldCollisionInfo


        .. code-block:: csharp

            public virtual void SceneryCollisionHandler(DistanceFieldCollisionInfo info)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetAIGroup(AIGroup)



        :type value: AIGroup


        .. code-block:: csharp

            public virtual void SetAIGroup(AIGroup value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetAIStateMachineState(System.String)



        :type state: System.String


        .. code-block:: csharp

            public void SetAIStateMachineState(string state)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetAction(PreferredAiAction, UnityEngine.Vector2, System.Boolean, Clay.Game.Mod.Entities.Entity)



        :type action: PreferredAiAction

        :type fromPosition: UnityEngine.Vector2

        :type quietly: System.Boolean

        :type target: Clay.Game.Mod.Entities.Entity


        .. code-block:: csharp

            public void SetAction(PreferredAiAction action, Vector2 fromPosition, bool quietly, Entity target = null)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetAttributes(Attributes)



        :type attr: Attributes


        .. code-block:: csharp

            public void SetAttributes(Attributes attr)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetAttributes(System.Single, System.Single, System.Single)



        :type energy: System.Single

        :type strength: System.Single

        :type speed: System.Single


        .. code-block:: csharp

            public void SetAttributes(float energy, float strength, float speed)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetColony(Colony)



        :type colony: Colony


        .. code-block:: csharp

            public void SetColony(Colony colony)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetColony(System.String)



        :type colonyName: System.String


        .. code-block:: csharp

            public void SetColony(string colonyName)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetFieldOfView(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void SetFieldOfView(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetHealth(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void SetHealth(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetHealthRegenRate(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void SetHealthRegenRate(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetNameAndUID(System.String, System.String, System.String[])



        :type name: System.String

        :type uid: System.String

        :type parameters: System.String<System.String>[]


        .. code-block:: csharp

            public void SetNameAndUID(string name, string uid, string[] parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetOwner(Clay.Game.Mod.Entities.Entity)



        :type newOwner: Clay.Game.Mod.Entities.Entity


        .. code-block:: csharp

            public virtual void SetOwner(Entity newOwner)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetPalette(System.String)



        :type paletteName: System.String


        .. code-block:: csharp

            public void SetPalette(string paletteName)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetPalette(Tuna.Palette)



        :type palette: Tuna.Palette


        .. code-block:: csharp

            public void SetPalette(Palette palette)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetParentColony(Colony)



        :type value: Colony


        .. code-block:: csharp

            public virtual void SetParentColony(Colony value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetParentFlora(Clay.Game.Mod.Entities.Flora)



        :type value: Clay.Game.Mod.Entities.Flora


        .. code-block:: csharp

            public virtual void SetParentFlora(Flora value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetPitch(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public virtual void SetPitch(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetPlayerAction(System.Boolean)



        :type isPlayerAction: System.Boolean


        .. code-block:: csharp

            public virtual void SetPlayerAction(bool isPlayerAction)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetPosition(System.Single, System.Single)



        :type x: System.Single

        :type y: System.Single


        .. code-block:: csharp

            public virtual void SetPosition(float x, float y)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetPosition(UnityEngine.Vector2)



        :type value: UnityEngine.Vector2


        .. code-block:: csharp

            public virtual void SetPosition(Vector2 value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetRotation(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public virtual void SetRotation(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetScale(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void SetScale(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetSpeechBubbleRadius(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void SetSpeechBubbleRadius(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetSplinePath(Clay.Game.SplinePath)



        :type path: Clay.Game.SplinePath


        .. code-block:: csharp

            public void SetSplinePath(SplinePath path)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetSplinePath(System.String)



        :type name: System.String


        .. code-block:: csharp

            public void SetSplinePath(string name)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetSpriteDef(System.String)



        :type spriteName: System.String


        .. code-block:: csharp

            public void SetSpriteDef(string spriteName)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetSpriteDefDelayed(System.String)



        :type spriteName: System.String


        .. code-block:: csharp

            public void SetSpriteDefDelayed(string spriteName)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetTeam(System.String)



        :type teamName: System.String


        .. code-block:: csharp

            public void SetTeam(string teamName)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetTeam(Team)



        :type team: Team


        .. code-block:: csharp

            public void SetTeam(Team team)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetUIRadius(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void SetUIRadius(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetVelocity(System.Single, System.Single)



        :type x: System.Single

        :type y: System.Single


        .. code-block:: csharp

            public virtual void SetVelocity(float x, float y)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetVelocity(UnityEngine.Vector2)



        :type value: UnityEngine.Vector2


        .. code-block:: csharp

            public virtual void SetVelocity(Vector2 value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetViewRange(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void SetViewRange(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetVisiblePitch(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public virtual void SetVisiblePitch(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SetVisiblePitchForcefully(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void SetVisiblePitchForcefully(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SpawnEntity(System.String[], System.Boolean)



        :type parameters: System.String<System.String>[]

        :type internalCall: System.Boolean

        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public static Entity SpawnEntity(string[] parameters, bool internalCall = false)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SpawnEntityLua(System.String)



        :type parameters: System.String

        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public static Entity SpawnEntityLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.Spawned()




        .. code-block:: csharp

            public override void Spawned()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SpreadSickness(Clay.Game.Mod.Entities.Entity)



        :type entity: Clay.Game.Mod.Entities.Entity


        .. code-block:: csharp

            public void SpreadSickness(Entity entity)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.StartAIStateMachine()




        .. code-block:: csharp

            public void StartAIStateMachine()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.StatRecord(System.String)



        :type s: System.String


        .. code-block:: csharp

            public void StatRecord(string s)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.StatRecord(System.String, System.Object[])



        :type format: System.String

        :type args: System.Object<System.Object>[]


        .. code-block:: csharp

            public void StatRecord(string format, params object[] args)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.StatRecordLine()




        .. code-block:: csharp

            public void StatRecordLine()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.StatRecordLine(System.String)



        :type s: System.String


        .. code-block:: csharp

            public void StatRecordLine(string s)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.StatRecordLine(System.String, System.Object[])



        :type format: System.String

        :type args: System.Object<System.Object>[]


        .. code-block:: csharp

            public void StatRecordLine(string format, params object[] args)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.StatsClear()




        .. code-block:: csharp

            public void StatsClear()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.StatsGetString()



        :rtype: System.String

        .. code-block:: csharp

            public string StatsGetString()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.StopSfx(System.String)



        :type sfxName: System.String


        .. code-block:: csharp

            public void StopSfx(string sfxName)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.SuppressedBy(Clay.Game.Mod.Entities.Entity, System.Single, System.Boolean, System.Boolean)



        :type attacker: Clay.Game.Mod.Entities.Entity

        :type time: System.Single

        :type effectHandled: System.Boolean

        :type fxHandled: System.Boolean


        .. code-block:: csharp

            public virtual void SuppressedBy(Entity attacker, float time, bool effectHandled = false, bool fxHandled = false)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.ThreadedUpdateQuadTree()




        .. code-block:: csharp

            public void ThreadedUpdateQuadTree()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.TimedDeath(System.Single)



        :type delay: System.Single


        .. code-block:: csharp

            public void TimedDeath(float delay)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.Trashed()




        .. code-block:: csharp

            public override void Trashed()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.TryAttack(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public virtual void TryAttack(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.Update(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void Update(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.UpdatePersistentEffects(System.Single, System.Boolean)



        :type time: System.Single

        :type fx: System.Boolean


        .. code-block:: csharp

            public virtual void UpdatePersistentEffects(float time, bool fx)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.UpdateQuadTree()




        .. code-block:: csharp

            public void UpdateQuadTree()

    .. dn:method:: Clay.Game.Mod.Entities.Entity.ValidateSpawn(System.String[], System.String, Colony, Team, System.Boolean, ref System.String, Clay.Game.Mod.Entities.RespawnRules)



        :type parameters: System.String<System.String>[]

        :type type: System.String

        :type colony: Colony

        :type team: Team

        :type colonyPosition: System.Boolean

        :type spawnHash: System.String

        :type respawnRule: Clay.Game.Mod.Entities.RespawnRules

        :rtype: System.Boolean

        .. code-block:: csharp

            public static bool ValidateSpawn(string[] parameters, string type, Colony colony, Team team, bool colonyPosition, ref string spawnHash, RespawnRules respawnRule)

    .. dn:method:: Clay.Game.Mod.Entities.Entity.WeakenedBy(Clay.Game.Mod.Entities.Entity, System.Single, Weapon, System.Boolean, System.Boolean)



        :type attacker: Clay.Game.Mod.Entities.Entity

        :type amount: System.Single

        :type weapon: Weapon

        :type effectHandled: System.Boolean

        :type fxHandled: System.Boolean


        .. code-block:: csharp

            public virtual void WeakenedBy(Entity attacker, float amount, Weapon weapon, bool effectHandled = false, bool fxHandled = false)



