
PlayerShip Class
================



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
* :dn:cls:`Clay.Game.Mod.Entities.PlayerShip`




Syntax
------

.. code-block:: csharp

    public class PlayerShip : Vehicle, IComparable, IAudioSourceInfo, ITargettable, IPathFindingAgent, IWindEffector





.. dn:class:: Clay.Game.Mod.Entities.PlayerShip
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.PlayerShip


Constructors
------------

.. dn:class:: Clay.Game.Mod.Entities.PlayerShip
    :noindex:
    :hidden:

    .. dn:constructor:: Clay.Game.Mod.Entities.PlayerShip.PlayerShip()




        .. code-block:: csharp

            public PlayerShip()



Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.PlayerShip
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.AutomaticTouchControl



        :rtype: System.Boolean

        .. code-block:: csharp

            [UsedImplicitly]
            [ConsoleCommand]
            public bool AutomaticTouchControl { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.Followers



        :rtype: System.Collections.Generic.IEnumerable<System.Collections.Generic.IEnumerable`1>{Clay.Game.Mod.Entities.Entity<Clay.Game.Mod.Entities.Entity>}

        .. code-block:: csharp

            public IEnumerable<Entity> Followers { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.ForceAttackingRestricted



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool ForceAttackingRestricted { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.ForceMovementRestricted



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool ForceMovementRestricted { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.SendModeDisabled



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool SendModeDisabled { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.SendModeMouseHold



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool SendModeMouseHold { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.SendModeSnappedObject



        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity SendModeSnappedObject { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.SendModeTargetPosition



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 SendModeTargetPosition { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.SpriteDefName



        :rtype: System.String

        .. code-block:: csharp

            public string SpriteDefName { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.WindActive



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool WindActive { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.WindForce



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 WindForce { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.WindPosition



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 WindPosition { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.WindRadius



        :rtype: System.Single

        .. code-block:: csharp

            public float WindRadius { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip._accelerationSpeedAttackMultiplier



        :rtype: System.Single

        .. code-block:: csharp

            public float _accelerationSpeedAttackMultiplier { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip._accelerationSpeedMultiplier



        :rtype: System.Single

        .. code-block:: csharp

            public float _accelerationSpeedMultiplier { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip._autoFollowCommandIssueRange



        :rtype: System.Single

        .. code-block:: csharp

            public float _autoFollowCommandIssueRange { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip._commandIssueRange



        :rtype: System.Single

        .. code-block:: csharp

            public float _commandIssueRange { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip._dragAttackMultiplier



        :rtype: System.Single

        .. code-block:: csharp

            public float _dragAttackMultiplier { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip._dragEnergyMultiplier



        :rtype: System.Single

        .. code-block:: csharp

            public float _dragEnergyMultiplier { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip._levelUpExplosive



        :rtype: Explosive

        .. code-block:: csharp

            public Explosive _levelUpExplosive { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip._pitchSpeedAttackMultiplier



        :rtype: System.Single

        .. code-block:: csharp

            public float _pitchSpeedAttackMultiplier { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip._pitchSpeedBase



        :rtype: System.Single

        .. code-block:: csharp

            public float _pitchSpeedBase { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip._pitchSpeedMultiplier



        :rtype: System.Single

        .. code-block:: csharp

            public float _pitchSpeedMultiplier { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip._playerHealthWarningSound



        :rtype: System.String

        .. code-block:: csharp

            public string _playerHealthWarningSound { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip._sendModeCommandIssueRange



        :rtype: System.Single

        .. code-block:: csharp

            public float _sendModeCommandIssueRange { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip._thrustFx



        :rtype: System.String

        .. code-block:: csharp

            public string _thrustFx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.cameraPan



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 cameraPan { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.cameraShouldZoomOut



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool cameraShouldZoomOut { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.energyCollectionRange



        :rtype: System.Single

        .. code-block:: csharp

            public float energyCollectionRange { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.firedTime



        :rtype: System.Single

        .. code-block:: csharp

            public float firedTime { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.firingCharge



        :rtype: System.Single

        .. code-block:: csharp

            public float firingCharge { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.inAttackMode



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool inAttackMode { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.isDamageable



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isDamageable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.isLevellingUp



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isLevellingUp { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.isMutating



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isMutating { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.isNoseAttachmentFiring



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isNoseAttachmentFiring { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.isPlayer



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isPlayer { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.isPrimaryAttacking



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isPrimaryAttacking { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.isRespawned



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isRespawned { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.isSecondaryAttacking



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isSecondaryAttacking { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.isTargetable



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isTargetable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.nearestArtifactTree



        :rtype: Clay.Game.Mod.Entities.Flora

        .. code-block:: csharp

            public Flora nearestArtifactTree { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.nearestCollectionTree



        :rtype: Clay.Game.Mod.Entities.Flora

        .. code-block:: csharp

            public Flora nearestCollectionTree { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.nearestRelayTree



        :rtype: Clay.Game.Mod.Entities.Flora

        .. code-block:: csharp

            public Flora nearestRelayTree { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.nearestVortex



        :rtype: Clay.Game.Mod.Entities.Vortex

        .. code-block:: csharp

            public Vortex nearestVortex { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.noseAttachmentProjectile



        :rtype: NoseProjectile

        .. code-block:: csharp

            public NoseProjectile noseAttachmentProjectile { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.primaryFiredTime



        :rtype: System.Single

        .. code-block:: csharp

            public float primaryFiredTime { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.secondaryFiredTime



        :rtype: System.Single

        .. code-block:: csharp

            public float secondaryFiredTime { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.statMeterCount



        :rtype: System.Int32

        .. code-block:: csharp

            public int statMeterCount { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.state



        :rtype: Clay.Game.Mod.Entities.PlayerShipStates

        .. code-block:: csharp

            public PlayerShipStates state { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.stateManager



        :rtype: Tuna.MobStateManager

        .. code-block:: csharp

            public MobStateManager stateManager { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.thrustImpulse



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 thrustImpulse { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.useSpawnEntityCommand



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool useSpawnEntityCommand { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.wasPrimaryAttacking



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool wasPrimaryAttacking { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.wasSecondaryAttacking



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool wasSecondaryAttacking { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.zoomCameraPosition



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 zoomCameraPosition { get; }

    .. dn:property:: Clay.Game.Mod.Entities.PlayerShip.zoomPanPosition



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 zoomPanPosition { get; }



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.PlayerShip
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.Activate(Attributes, UnityEngine.Vector2, System.Single, Colony, Team)



        :type attr: Attributes

        :type atPosition: UnityEngine.Vector2

        :type atAngle: System.Single

        :type colony: Colony

        :type newTeam: Team


        .. code-block:: csharp

            public override void Activate(Attributes attr, Vector2 atPosition, float atAngle, Colony colony, Team newTeam)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.AddWeapon(System.String, HardPoint)



        :type weaponType: System.String

        :type hardPoint: HardPoint

        :rtype: Weapon

        .. code-block:: csharp

            public override Weapon AddWeapon(string weaponType, HardPoint hardPoint)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.CloneConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            public override void CloneConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.CollectEnergy(System.Int32)



        :type value: System.Int32


        .. code-block:: csharp

            public void CollectEnergy(int value)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.CommonCleanUp()




        .. code-block:: csharp

            protected override void CommonCleanUp()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.DamagedBy(Clay.Game.Mod.Entities.Entity, System.Single, Weapon, System.Boolean, System.Boolean)



        :type other: Clay.Game.Mod.Entities.Entity

        :type damage: System.Single

        :type weapon: Weapon

        :type effectHandled: System.Boolean

        :type fxHandled: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool DamagedBy(Entity other, float damage, Weapon weapon, bool effectHandled = false, bool fxHandled = false)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.DebugRespawn(UnityEngine.Vector2)



        :type position: UnityEngine.Vector2


        .. code-block:: csharp

            public void DebugRespawn(Vector2 position)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.Destroyed()




        .. code-block:: csharp

            public override void Destroyed()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.Die(System.Boolean, System.Boolean, System.Boolean)



        :type exploded: System.Boolean

        :type trash: System.Boolean

        :type quietly: System.Boolean


        .. code-block:: csharp

            public override void Die(bool exploded = false, bool trash = true, bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.DisableSendMode()




        .. code-block:: csharp

            public void DisableSendMode()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.DoorCollisionHandler(Door)



        :type door: Door


        .. code-block:: csharp

            public override void DoorCollisionHandler(Door door)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.EntityFixedUpdate(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void EntityFixedUpdate(float time)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.EquipPrimaryWeapon()




        .. code-block:: csharp

            public void EquipPrimaryWeapon()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.GenerateCharacteristics()




        .. code-block:: csharp

            protected override void GenerateCharacteristics()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.GenerateDependantCharacteristics()




        .. code-block:: csharp

            protected override void GenerateDependantCharacteristics()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.GetCommandLine(System.Boolean)



        :type multiLine: System.Boolean

        :rtype: System.String

        .. code-block:: csharp

            public override string GetCommandLine(bool multiLine)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.GetFlightMode()



        :rtype: Clay.Game.Mod.Entities.FlightMode

        .. code-block:: csharp

            public FlightMode GetFlightMode()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.GetNearbySendPoints(System.Collections.Generic.List<Clay.Game.Mod.Entities.Entity>, System.Single)



        :type sendPoints: System.Collections.Generic.List<System.Collections.Generic.List`1>{Clay.Game.Mod.Entities.Entity<Clay.Game.Mod.Entities.Entity>}

        :type range: System.Single


        .. code-block:: csharp

            public void GetNearbySendPoints(List<Entity> sendPoints = null, float range = -1F)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.GrowthPathInitialised(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void GrowthPathInitialised(bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.InVortexEnterState(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void InVortexEnterState(bool quietly)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.InVortexExitState(System.Enum, System.Boolean)



        :type nextState: System.Enum

        :type quietly: System.Boolean


        .. code-block:: csharp

            public void InVortexExitState(Enum nextState, bool quietly)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.InVortexUpdateState(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public void InVortexUpdateState(float time)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.IsValidEntityForSendCommand(Clay.Game.Mod.Entities.Entity)



        :type entity: Clay.Game.Mod.Entities.Entity

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsValidEntityForSendCommand(Entity entity)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.IssueAutoAiCommand(Clay.Game.CommandTypes)



        :type newCommand: Clay.Game.CommandTypes


        .. code-block:: csharp

            public void IssueAutoAiCommand(CommandTypes newCommand)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.IssueNewAiCommand(Clay.Game.CommandTypes, System.Boolean, System.Collections.Generic.IEnumerable<Clay.Game.Mod.Entities.Entity>)



        :type newCommand: Clay.Game.CommandTypes

        :type manuallyTriggered: System.Boolean

        :type commandEntities: System.Collections.Generic.IEnumerable<System.Collections.Generic.IEnumerable`1>{Clay.Game.Mod.Entities.Entity<Clay.Game.Mod.Entities.Entity>}


        .. code-block:: csharp

            public void IssueNewAiCommand(CommandTypes newCommand, bool manuallyTriggered, IEnumerable<Entity> commandEntities = null)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.IssueSendAiCommand(System.Collections.Generic.IEnumerable<Clay.Game.Mod.Entities.Entity>, Clay.Game.Mod.Entities.Entity)



        :type commandEntities: System.Collections.Generic.IEnumerable<System.Collections.Generic.IEnumerable`1>{Clay.Game.Mod.Entities.Entity<Clay.Game.Mod.Entities.Entity>}

        :type sendPoint: Clay.Game.Mod.Entities.Entity


        .. code-block:: csharp

            public void IssueSendAiCommand(IEnumerable<Entity> commandEntities, Entity sendPoint)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.IssueSendModeFollowCommand()




        .. code-block:: csharp

            public void IssueSendModeFollowCommand()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.KillPlayer()




        .. code-block:: csharp

            public void KillPlayer()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.LevelUp(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void LevelUp(bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.LoadNoseAttachment(Clay.Game.Game.Entities.IProjectileCompatibleEntity)



        :type projectileBaseEntity: Clay.Game.Game.Entities.IProjectileCompatibleEntity


        .. code-block:: csharp

            public void LoadNoseAttachment(IProjectileCompatibleEntity projectileBaseEntity)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.Mutate(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void Mutate(bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.NormalUpdateState(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public void NormalUpdateState(float time)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.OnEntityDiedOrTrashedListener(System.String, System.Object, System.Object, System.Object)



        :type ev: System.String

        :type sender: System.Object

        :type param1: System.Object

        :type param2: System.Object


        .. code-block:: csharp

            protected override void OnEntityDiedOrTrashedListener(string ev, object sender, object param1, object param2)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.OutVortexEnterState(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void OutVortexEnterState(bool quietly)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.OutVortexExitState(System.Enum, System.Boolean)



        :type nextState: System.Enum

        :type quietly: System.Boolean


        .. code-block:: csharp

            public void OutVortexExitState(Enum nextState, bool quietly)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.OutVortexUpdateState(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public void OutVortexUpdateState(float time)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.RebuildPrototype()




        .. code-block:: csharp

            public override void RebuildPrototype()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.RecycleConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            protected override void RecycleConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.RemoveNoseAttachment()




        .. code-block:: csharp

            public void RemoveNoseAttachment()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.Render()




        .. code-block:: csharp

            public override void Render()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.RenderDebug()




        .. code-block:: csharp

            public override void RenderDebug()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.ResetCameraPan()




        .. code-block:: csharp

            public void ResetCameraPan()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.ResetNearRelayTree()




        .. code-block:: csharp

            public void ResetNearRelayTree()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.SceneryCollisionHandler(DistanceFieldCollisionInfo)



        :type info: DistanceFieldCollisionInfo


        .. code-block:: csharp

            public override void SceneryCollisionHandler(DistanceFieldCollisionInfo info)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.SetNearestArtifactTree(Clay.Game.Mod.Entities.Flora)



        :type flora: Clay.Game.Mod.Entities.Flora


        .. code-block:: csharp

            public void SetNearestArtifactTree(Flora flora)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.SetNearestCollectionTree(Clay.Game.Mod.Entities.Flora)



        :type flora: Clay.Game.Mod.Entities.Flora


        .. code-block:: csharp

            public void SetNearestCollectionTree(Flora flora)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.SetNearestRelayTree(Clay.Game.Mod.Entities.Flora)



        :type flora: Clay.Game.Mod.Entities.Flora


        .. code-block:: csharp

            public void SetNearestRelayTree(Flora flora)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.SetNearestVortex(Clay.Game.Mod.Entities.Vortex)



        :type vortex: Clay.Game.Mod.Entities.Vortex


        .. code-block:: csharp

            public void SetNearestVortex(Vortex vortex)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.SetPlayerHealthToWarningLevel()




        .. code-block:: csharp

            public void SetPlayerHealthToWarningLevel()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.SetRespawnFlag(System.Boolean)



        :type value: System.Boolean


        .. code-block:: csharp

            public void SetRespawnFlag(bool value)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.SetState(Clay.Game.Mod.Entities.PlayerShipStates)



        :type nextState: Clay.Game.Mod.Entities.PlayerShipStates


        .. code-block:: csharp

            public void SetState(PlayerShipStates nextState)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.SetState(Clay.Game.Mod.Entities.PlayerShipStates, System.Boolean)



        :type nextState: Clay.Game.Mod.Entities.PlayerShipStates

        :type quietly: System.Boolean


        .. code-block:: csharp

            public void SetState(PlayerShipStates nextState, bool quietly)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.SuppressedBy(Clay.Game.Mod.Entities.Entity, System.Single, System.Boolean, System.Boolean)



        :type other: Clay.Game.Mod.Entities.Entity

        :type time: System.Single

        :type effectHandled: System.Boolean

        :type fxHandled: System.Boolean


        .. code-block:: csharp

            public override void SuppressedBy(Entity other, float time, bool effectHandled = false, bool fxHandled = false)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.TeleportPlayer(System.Int32, System.Int32)



        :type x: System.Int32

        :type y: System.Int32


        .. code-block:: csharp

            public void TeleportPlayer(int x, int y)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.TeleportPlayerLua(System.String)



        :type parameters: System.String


        .. code-block:: csharp

            public void TeleportPlayerLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.ToggleFlightMode()




        .. code-block:: csharp

            public void ToggleFlightMode()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.TogglePrimaryAttacking()




        .. code-block:: csharp

            public void TogglePrimaryAttacking()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.ToggleSendModeMouseHold()




        .. code-block:: csharp

            public void ToggleSendModeMouseHold()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.TryAttack(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void TryAttack(float time)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.TryNoseAttachmentFiring()




        .. code-block:: csharp

            public void TryNoseAttachmentFiring()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.Update(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void Update(float time)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.UpdateCollectedEnergy(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public void UpdateCollectedEnergy(float time)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.UpdateFiringCharge(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public void UpdateFiringCharge(float time)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.UpdateHealth(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public void UpdateHealth(float time)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.UpdateNearbyEntities()




        .. code-block:: csharp

            public void UpdateNearbyEntities()

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.UpdateNoseAttachment(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public void UpdateNoseAttachment(float time)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.UpdateVelocity(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public void UpdateVelocity(float time)

    .. dn:method:: Clay.Game.Mod.Entities.PlayerShip.WeakenedBy(Clay.Game.Mod.Entities.Entity, System.Single, Weapon, System.Boolean, System.Boolean)



        :type other: Clay.Game.Mod.Entities.Entity

        :type amount: System.Single

        :type weapon: Weapon

        :type effectHandled: System.Boolean

        :type fxHandled: System.Boolean


        .. code-block:: csharp

            public override void WeakenedBy(Entity other, float amount, Weapon weapon, bool effectHandled = false, bool fxHandled = false)



