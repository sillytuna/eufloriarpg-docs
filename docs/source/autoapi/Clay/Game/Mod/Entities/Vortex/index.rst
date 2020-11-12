
Vortex Class
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
* :dn:cls:`Clay.Game.Mod.Entities.Vortex`




Syntax
------

.. code-block:: csharp

    public class Vortex : Entity, IComparable, IAudioSourceInfo, ITargettable





.. dn:class:: Clay.Game.Mod.Entities.Vortex
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.Vortex


Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.Vortex
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.CanPlayerUse



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool CanPlayerUse { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.IsLocked



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsLocked { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.NavigableByLevel



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool NavigableByLevel { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.PressureLevel



        :rtype: System.Int32

        .. code-block:: csharp

            public int PressureLevel { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.SpinSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public float SpinSpeed { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.VortexIsUnlocked



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool VortexIsUnlocked { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex._machineSprite



        :rtype: System.String

        .. code-block:: csharp

            public string _machineSprite { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex._vortexFlags



        :rtype: Clay.Game.Mod.Entities.VortexFlags

        .. code-block:: csharp

            public VortexFlags _vortexFlags { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex._vortexLoop



        :rtype: System.String

        .. code-block:: csharp

            public string _vortexLoop { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.activationRange



        :rtype: System.Single

        .. code-block:: csharp

            public static float activationRange { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.attractStrength



        :rtype: System.Single

        .. code-block:: csharp

            public static float attractStrength { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.attractStrengthAngularMultiplier



        :rtype: System.Single

        .. code-block:: csharp

            public static float attractStrengthAngularMultiplier { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.colourCycleTimer



        :rtype: System.Single

        .. code-block:: csharp

            public static float colourCycleTimer { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.dataCanColor



        :rtype: DataCanColor

        .. code-block:: csharp

            public DataCanColor dataCanColor { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.fallRange



        :rtype: System.Single

        .. code-block:: csharp

            public static float fallRange { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.fallScale



        :rtype: System.Single

        .. code-block:: csharp

            public static float fallScale { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.fallTimer



        :rtype: System.Single

        .. code-block:: csharp

            public static float fallTimer { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.isActivated



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isActivated { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.isClockwise



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isClockwise { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.isColourCycling



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isColourCycling { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.isFullSpeed



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isFullSpeed { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.isOneShot



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isOneShot { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.isOutgoing



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isOutgoing { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.isSpecialVortex



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isSpecialVortex { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.isTargetable



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isTargetable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.isTranscendenceEnergy



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isTranscendenceEnergy { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.isTranscendenceOut



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isTranscendenceOut { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.isTranscendenceSpeed



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isTranscendenceSpeed { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.isTranscendenceStrength



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isTranscendenceStrength { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.overridePressure



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool overridePressure { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.spinAccelerationMultiplier



        :rtype: System.Single

        .. code-block:: csharp

            public static float spinAccelerationMultiplier { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.spinDecelerationMultiplier



        :rtype: System.Single

        .. code-block:: csharp

            public static float spinDecelerationMultiplier { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.spinLayerMultiplier



        :rtype: System.Single

        .. code-block:: csharp

            public static float spinLayerMultiplier { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.spinLayers



        :rtype: System.Int32

        .. code-block:: csharp

            public static int spinLayers { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.spinPower



        :rtype: System.Single

        .. code-block:: csharp

            public float spinPower { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.spinSpeedActive



        :rtype: System.Single

        .. code-block:: csharp

            public static float spinSpeedActive { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.spinSpeedInactive



        :rtype: System.Single

        .. code-block:: csharp

            public static float spinSpeedInactive { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.spinSpeedInactiveSpecial



        :rtype: System.Single

        .. code-block:: csharp

            public static float spinSpeedInactiveSpecial { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.travelDown



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool travelDown { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.travelHub



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool travelHub { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.travelSideways



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool travelSideways { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.travelUp



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool travelUp { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.useSpawnEntityCommand



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool useSpawnEntityCommand { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vortex.usesDataCanColor



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool usesDataCanColor { get; }



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.Vortex
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.Activate(Attributes, UnityEngine.Vector2, System.Single, Colony, Team)



        :type attr: Attributes

        :type atPosition: UnityEngine.Vector2

        :type atAngle: System.Single

        :type colony: Colony

        :type newTeam: Team


        .. code-block:: csharp

            public override void Activate(Attributes attr, Vector2 atPosition, float atAngle, Colony colony, Team newTeam)

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.ActivateVortex()




        .. code-block:: csharp

            public void ActivateVortex()

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.CloneConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            public override void CloneConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.DeactivateVortex()




        .. code-block:: csharp

            public void DeactivateVortex()

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.DisableUntilOutOfRange()




        .. code-block:: csharp

            public void DisableUntilOutOfRange()

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.EntityFixedUpdate(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void EntityFixedUpdate(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.GetCommandLine(System.Boolean)



        :type multiLine: System.Boolean

        :rtype: System.String

        .. code-block:: csharp

            public override string GetCommandLine(bool multiLine)

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.GetNearbyVortex(UnityEngine.Vector2)



        :type position: UnityEngine.Vector2

        :rtype: Clay.Game.Mod.Entities.Vortex

        .. code-block:: csharp

            public static Vortex GetNearbyVortex(Vector2 position)

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.GetRespawnString()



        :rtype: System.String

        .. code-block:: csharp

            public override string GetRespawnString()

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.GetVortexProgressRoot(System.String)



        :type levelName: System.String

        :rtype: Tuna.Setting

        .. code-block:: csharp

            public static Setting GetVortexProgressRoot(string levelName = null)

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.InitialiseApp()




        .. code-block:: csharp

            public static void InitialiseApp()

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.InitialiseLevel()




        .. code-block:: csharp

            public static void InitialiseLevel()

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.IsVortexLocked(System.String, System.String)



        :type levelname: System.String

        :type vortexname: System.String

        :rtype: System.Boolean

        .. code-block:: csharp

            public static bool IsVortexLocked(string levelname, string vortexname)

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.Jump(Clay.Game.Mod.Entities.Vortex)



        :type vortex: Clay.Game.Mod.Entities.Vortex


        .. code-block:: csharp

            public static void Jump(Vortex vortex)

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.ParentColonised()




        .. code-block:: csharp

            public override void ParentColonised()

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.PlayerEscaping()




        .. code-block:: csharp

            public void PlayerEscaping()

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.PlayerJumped()




        .. code-block:: csharp

            public void PlayerJumped()

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.Rebuild()




        .. code-block:: csharp

            public static void Rebuild()

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.SetAsOutgoing()




        .. code-block:: csharp

            public void SetAsOutgoing()

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.SpawnVortex(System.String[])



        :type parameters: System.String<System.String>[]

        :rtype: Clay.Game.Mod.Entities.Vortex

        .. code-block:: csharp

            public static Vortex SpawnVortex(string[] parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.SpawnVortexLua(System.String)



        :type parameters: System.String

        :rtype: Clay.Game.Mod.Entities.Vortex

        .. code-block:: csharp

            public static Vortex SpawnVortexLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.Trashed()




        .. code-block:: csharp

            public override void Trashed()

    .. dn:method:: Clay.Game.Mod.Entities.Vortex.Update(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void Update(float time)



