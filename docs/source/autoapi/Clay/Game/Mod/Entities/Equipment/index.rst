
Equipment Class
===============



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




Syntax
------

.. code-block:: csharp

    public class Equipment : Vehicle, IComparable, IAudioSourceInfo, ITargettable, IPathFindingAgent





.. dn:class:: Clay.Game.Mod.Entities.Equipment
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.Equipment


Constructors
------------

.. dn:class:: Clay.Game.Mod.Entities.Equipment
    :noindex:
    :hidden:

    .. dn:constructor:: Clay.Game.Mod.Entities.Equipment.Equipment()




        .. code-block:: csharp

            public Equipment()



Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.Equipment
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.Equipment._activatedSfx



        :rtype: System.String

        .. code-block:: csharp

            public string _activatedSfx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment._cantCollectSfx



        :rtype: System.String

        .. code-block:: csharp

            public string _cantCollectSfx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment._cantCollectShake



        :rtype: System.Single

        .. code-block:: csharp

            public float _cantCollectShake { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment._capturedSfx



        :rtype: System.String

        .. code-block:: csharp

            public string _capturedSfx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment._collectedSfx



        :rtype: System.String

        .. code-block:: csharp

            public string _collectedSfx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment._deactivatedSfx



        :rtype: System.String

        .. code-block:: csharp

            public string _deactivatedSfx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.canPlayUncollectableEffects



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool canPlayUncollectableEffects { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.hudIcon



        :rtype: Clay.Game.HudEquipmentMeter

        .. code-block:: csharp

            public HudEquipmentMeter hudIcon { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.inventoryItem



        :rtype: InventoryItem

        .. code-block:: csharp

            public InventoryItem inventoryItem { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.isActivated



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isActivated { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.isCaptured



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isCaptured { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.isCollectable



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isCollectable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.isCollected



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isCollected { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.isCollecting



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isCollecting { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.isEquipment



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isEquipment { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.isEquipped



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isEquipped { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.isFree



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isFree { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.shakeCooldownTimer



        :rtype: System.Single

        .. code-block:: csharp

            public float shakeCooldownTimer { set; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.spawnHeader



        :rtype: System.String

        .. code-block:: csharp

            public virtual string spawnHeader { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.state



        :rtype: Clay.Game.Mod.Entities.EquipmentStates

        .. code-block:: csharp

            public EquipmentStates state { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.stateManager



        :rtype: Tuna.MobStateManager

        .. code-block:: csharp

            public MobStateManager stateManager { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.throwSpeedRange



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public static Vector2 throwSpeedRange { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.uncollectableAlpha



        :rtype: System.Single

        .. code-block:: csharp

            public static float uncollectableAlpha { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Equipment.uncollectableTimer



        :rtype: System.Single

        .. code-block:: csharp

            public static float uncollectableTimer { get; set; }



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.Equipment
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.Activate(Attributes, UnityEngine.Vector2, System.Single, Colony, Team)



        :type attr: Attributes

        :type atPosition: UnityEngine.Vector2

        :type atAngle: System.Single

        :type colony: Colony

        :type newTeam: Team


        .. code-block:: csharp

            public override void Activate(Attributes attr, Vector2 atPosition, float atAngle, Colony colony, Team newTeam)

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.CloneConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            public override void CloneConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.Deactivate()



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool Deactivate()

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.Deactivate(System.Boolean)



        :type quietly: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public virtual bool Deactivate(bool quietly)

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.DeactivateQuietly()



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool DeactivateQuietly()

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.Die(System.Boolean, System.Boolean, System.Boolean)



        :type exploded: System.Boolean

        :type trash: System.Boolean

        :type quietly: System.Boolean


        .. code-block:: csharp

            public override void Die(bool exploded = false, bool trash = true, bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.EntityFixedUpdate(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void EntityFixedUpdate(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.GetCommandLine(System.Boolean)



        :type multiLine: System.Boolean

        :rtype: System.String

        .. code-block:: csharp

            public override string GetCommandLine(bool multiLine)

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.GetRespawnString()



        :rtype: System.String

        .. code-block:: csharp

            public override string GetRespawnString()

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.InitialiseLevel()




        .. code-block:: csharp

            public static void InitialiseLevel()

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.SetOwner(Clay.Game.Mod.Entities.Entity)



        :type newOwner: Clay.Game.Mod.Entities.Entity


        .. code-block:: csharp

            public override void SetOwner(Entity newOwner)

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.SetState(Clay.Game.Mod.Entities.EquipmentStates)



        :type nextState: Clay.Game.Mod.Entities.EquipmentStates


        .. code-block:: csharp

            public void SetState(EquipmentStates nextState)

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.SetState(Clay.Game.Mod.Entities.EquipmentStates, System.Boolean)



        :type nextState: Clay.Game.Mod.Entities.EquipmentStates

        :type quietly: System.Boolean


        .. code-block:: csharp

            public void SetState(EquipmentStates nextState, bool quietly)

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.Shake()




        .. code-block:: csharp

            public void Shake()

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.SpawnEquipment(System.String, System.String[])



        :type spawnHeader: System.String

        :type parameters: System.String<System.String>[]

        :rtype: Clay.Game.Mod.Entities.Equipment

        .. code-block:: csharp

            public static Equipment SpawnEquipment(string spawnHeader, string[] parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.StateChangeCB()




        .. code-block:: csharp

            public void StateChangeCB()

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.Throw()




        .. code-block:: csharp

            public void Throw()

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.Throw(System.Single, System.Single)



        :type angle: System.Single

        :type speedMultiplier: System.Single


        .. code-block:: csharp

            public void Throw(float angle, float speedMultiplier = 1F)

    .. dn:method:: Clay.Game.Mod.Entities.Equipment.Trashed()




        .. code-block:: csharp

            public override void Trashed()



