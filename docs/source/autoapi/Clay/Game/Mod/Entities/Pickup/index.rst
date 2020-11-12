
Pickup Class
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
* :dn:cls:`Clay.Game.Mod.Entities.Vehicle`
* :dn:cls:`Clay.Game.Mod.Entities.Equipment`
* :dn:cls:`Clay.Game.Mod.Entities.Pickup`




Syntax
------

.. code-block:: csharp

    public class Pickup : Equipment, IComparable, IAudioSourceInfo, ITargettable, IPathFindingAgent, IProjectileCompatibleEntity





.. dn:class:: Clay.Game.Mod.Entities.Pickup
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.Pickup


Constructors
------------

.. dn:class:: Clay.Game.Mod.Entities.Pickup
    :noindex:
    :hidden:

    .. dn:constructor:: Clay.Game.Mod.Entities.Pickup.Pickup()




        .. code-block:: csharp

            public Pickup()



Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.Pickup
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.Pickup.IsNoseProjectile



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsNoseProjectile { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup.NonProjectileVariant



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool NonProjectileVariant { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup.ProjectileToCreate



        :rtype: System.String

        .. code-block:: csharp

            public string ProjectileToCreate { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup._pickupType



        :rtype: System.String

        .. code-block:: csharp

            public string _pickupType { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup._projectile



        :rtype: System.String

        .. code-block:: csharp

            public string _projectile { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup._projectileWorldObject



        :rtype: System.String

        .. code-block:: csharp

            public string _projectileWorldObject { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup.completeRatio



        :rtype: System.Single

        .. code-block:: csharp

            public float completeRatio { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup.delayTime



        :rtype: System.Single

        .. code-block:: csharp

            public float delayTime { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup.delayedRatio



        :rtype: System.Single

        .. code-block:: csharp

            public float delayedRatio { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup.effectTime



        :rtype: System.Single

        .. code-block:: csharp

            public float effectTime { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup.isDelayed



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isDelayed { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup.isTargetable



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isTargetable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup.isWeaponSwapping



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isWeaponSwapping { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup.miscTime



        :rtype: System.Single

        .. code-block:: csharp

            public float miscTime { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup.pickupDef



        :rtype: PickupDef

        .. code-block:: csharp

            public PickupDef pickupDef { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup.spawnHeader



        :rtype: System.String

        .. code-block:: csharp

            public override string spawnHeader { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pickup.useSpawnEntityCommand



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool useSpawnEntityCommand { get; }



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.Pickup
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.Pickup.Activate(Attributes, UnityEngine.Vector2, System.Single, Colony, Team)



        :type attr: Attributes

        :type atPosition: UnityEngine.Vector2

        :type atAngle: System.Single

        :type colony: Colony

        :type newTeam: Team


        .. code-block:: csharp

            public override void Activate(Attributes attr, Vector2 atPosition, float atAngle, Colony colony, Team newTeam)

    .. dn:method:: Clay.Game.Mod.Entities.Pickup.CloneConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            public override void CloneConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.Pickup.Deactivate(System.Boolean)



        :type quietly: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool Deactivate(bool quietly)

    .. dn:method:: Clay.Game.Mod.Entities.Pickup.EntityFixedUpdate(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void EntityFixedUpdate(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Pickup.InitialiseApp()




        .. code-block:: csharp

            public static void InitialiseApp()

    .. dn:method:: Clay.Game.Mod.Entities.Pickup.InitialiseLevel()




        .. code-block:: csharp

            public static void InitialiseLevel()

    .. dn:method:: Clay.Game.Mod.Entities.Pickup.PrototypeInitialiseDef()




        .. code-block:: csharp

            public void PrototypeInitialiseDef()

    .. dn:method:: Clay.Game.Mod.Entities.Pickup.Render()




        .. code-block:: csharp

            public override void Render()

    .. dn:method:: Clay.Game.Mod.Entities.Pickup.SpawnPickup(System.String[])



        :type parameters: System.String<System.String>[]

        :rtype: Clay.Game.Mod.Entities.Pickup

        .. code-block:: csharp

            public static Pickup SpawnPickup(string[] parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Pickup.SpawnPickupLua(System.String)



        :type parameters: System.String

        :rtype: Clay.Game.Mod.Entities.Pickup

        .. code-block:: csharp

            public static Pickup SpawnPickupLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Pickup.SpawnRandom(UnityEngine.Vector2)



        :type position: UnityEngine.Vector2

        :rtype: Clay.Game.Mod.Entities.Pickup

        .. code-block:: csharp

            public static Pickup SpawnRandom(Vector2 position)

    .. dn:method:: Clay.Game.Mod.Entities.Pickup.Trashed()




        .. code-block:: csharp

            public override void Trashed()

    .. dn:method:: Clay.Game.Mod.Entities.Pickup.Update(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void Update(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Pickup.UpgradeWeapon(Clay.Game.Mod.Entities.Entity, PickupDef, Weapon, HardPoint)



        :type owner: Clay.Game.Mod.Entities.Entity

        :type pickupDef: PickupDef

        :type weapon: Weapon

        :type hp: HardPoint

        :rtype: Weapon

        .. code-block:: csharp

            public static Weapon UpgradeWeapon(Entity owner, PickupDef pickupDef, Weapon weapon, HardPoint hp)



Fields
------

.. dn:class:: Clay.Game.Mod.Entities.Pickup
    :noindex:
    :hidden:

    .. dn:field:: Clay.Game.Mod.Entities.Pickup.projectile



        :rtype: PickupProjectile

        .. code-block:: csharp

            public PickupProjectile projectile



